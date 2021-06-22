from psycopg2._psycopg import cursor

from connection_utils import connection
from flask import Flask, render_template, request, jsonify
from werkzeug.utils import redirect

from daos.account_dao_postgres import AccountDaoPostgres
from entities.account import Account
from entities.my_reimbursements import MyReimbursement
from entities.reimbursement_chart_info import ReimbursementChartInfo
from exceptions.not_found_exception import ResourceNotFoundError
from services.account_services_impl import AccountServiceImpl

app = Flask(__name__)

account_dao = AccountDaoPostgres()
account_service = AccountServiceImpl(account_dao)  # Dependency injection!


@app.route('/')
def hello():
    return "<h3> Hello Welcome to the employee site. This site handles all reimbursement transactions</h3>"


@app.route('/home')
def home():
    return render_template('base.html')


#
# @app.route('/logout')
# def logout():
#     return render_template("logout.html")


@app.route('/api/register', methods=['POST'])
def create_account_api():
    body = request.json
    name = body.get('name')
    email = body.get('email')
    accountType = body.get('accountType')
    password1 = body.get('password1')
    password2 = body.get('password2')
    balance = body.get('balance')

    msg = ''
    if len(email) < 4:
        msg = 'Email must be greater than 4 characters.'
    elif len(name) < 2:
        msg = 'First name must be greater than 1 characters.'
    elif password1 != password2:
        msg = 'Passwords don\'t match.'
    elif len(password1) < 7:
        msg = 'Password must be at least 7 characters.'

    if len(msg) > 0:
        return msg, 400

    account = Account(0, name, email, password1, accountType, balance)
    account = account_service.create_account(account)  # save to database

    return jsonify(account.as_json_dict()), 201


@app.route('/api/reimbursement', methods=['POST'])
def create_reimbursement_api():
    body = request.json

    account_id = body.get('accountId')
    transferAmount = body.get('transferAmount')

    msg = ''
    if int(account_id) < 0:
        msg = 'Invalid account id'
    elif int(transferAmount) < 1:
        msg = 'Transfer Amount should be at least 1'

    if len(msg) > 0:
        return msg, 400

    re = MyReimbursement(0, account_id, transferAmount)
    # saving to db
    reimbursement = account_service.create_reimbursement(re)
    if reimbursement is None:
        return 'Reimbursement not created', 503

    return jsonify(reimbursement.as_json_dict()), 201


@app.route('/api/reimbursement/status/<status>', methods=['GET'])
def get_all_reimbursements_api(status: str):
    if status not in ['Waiting', 'Approved', 'Denied']:
        return 'Status should be from [\'Waiting\', \'Approved\', \'Denied\']', 400

    reimbursementList: list = account_service.get_all_reimbursements(status, '')
    if reimbursementList is None:
        return 'reimbursementList not found', 503

    json_accounts = [a.as_json_dict() for a in reimbursementList]
    return jsonify(json_accounts), 200


@app.route('/api/reimbursement/<id>', methods=['GET'])
def get_reimbursement_api(id: str):
    if int(id) < 0:
        return 'Invalid id', 400

    reimbursement = account_service.get_reimbursement(id)
    if reimbursement is None:
        return 'reimbursement not found', 503

    return jsonify(reimbursement.as_json_dict()), 200


@app.route('/api/reimbursement/id/<id>/newStatus/<status>', methods=['PUT'])
def update_reimbursement_api(id: str, status: str):
    msg = ''
    if len(id) < 0:
        msg = 'Invalid reimbursement id'
    elif status not in ['Approved', 'Denied']:
        return 'Status should be from [\'Approved\', \'Denied\']', 400

    if len(msg) > 0:
        return msg, 400

    reimbursement: MyReimbursement = account_service.get_reimbursement(id)
    if reimbursement is None:
        return 'reimbursement not found', 400

    if reimbursement.status in ['Approved', 'Denied']:
        return 'Already decided', 400

    reimbursement.status = status

    email = reimbursement.email
    acc: Account = account_service.find_account(email)
    if acc is None:
        return "Acc not found", 400
    a: int = acc.balance
    b: int = int(reimbursement.transferAmount)
    c: int = a + b
    acc.balance = c
    account_service.update_account(acc)

    # Saving to database
    reimbursement = account_service.update_reimbursement(reimbursement)
    if reimbursement is None:
        return 'Reimbursement not updated', 503

    return jsonify(reimbursement.as_json_dict()), 200


#    View routes
@app.route('/register', methods=['GET', 'POST'])
def create_account():
    if request.method == 'GET':
        return render_template("register.html", boolean=True)

    body = request.form
    name = body['name']
    email = body['email']
    accountType = 'Employee'  # body['accountType']
    password1 = body['password1']
    password2 = body['password2']
    balance = 0  # body['balance']

    msg = ''
    if len(email) < 4:
        msg = 'Email must be greater than 4 characters.'
    elif len(name) < 2:
        msg = 'First name must be greater than 1 characters.'
    elif password1 != password2:
        msg = 'Passwords don\'t match.'
    elif len(password1) < 7:
        msg = 'Password must be at least 7 characters.'

    if len(msg) > 0:
        return msg, 400

    account = Account(0, name, email, password1, accountType, balance)
    account = account_service.create_account(account)  # saving to database

    return redirect("/employee")


@app.route('/login', methods=['GET', 'POST'])
def login():
    print('Reaching /login')

    if request.method == 'GET':
        return render_template("user_logins.html", boolean=True)

    # trying to handle the login and verify, if error send error message else show welcome page

    body = request.form
    print(body)

    email = body.get('email')
    password = body.get('password')

    msg = ''
    if len(email) < 4:
        msg = 'Email must be greater than 4 characters.'
    elif len(password) < 7:
        msg = 'Password must be at least 7 characters.'

    if len(msg) > 0:
        return msg, 400

    # check database for user
    account = account_service.find_account(email)
    print(account)

    if account is None:
        return 'Account not found', 404

    print(account.password, password)

    if account.password != password:
        return 'Invalid email / password', 403

    if account.accountType == 'Employee':
        return redirect("/employee/" + email)
    #  manager
    return redirect("/manager")


@app.route('/employee/<email>', methods=['GET', 'POST'])
def create_reimbursement(email: str):
    if request.method == 'GET':
        reimbursementList: list = account_service.get_all_reimbursements('Waiting', email)
        return render_template('createReim.html', reimbursementList=reimbursementList)

    body = request.form
    email = body['email']
    transferAmount = body['transferAmount']
    reason = body['reason']

    msg = ''
    if len(email) < 4:
        msg = 'Invalid account email'
    elif int(transferAmount) < 1:
        msg = 'Transfer Amount should be at least 1'
    elif len(reason) < 5:
        msg = 'Reason should be at least 5'

    if len(msg) > 0:
        return msg, 400

    account: Account = account_service.find_account(email)
    if account is None:
        return 'Account not found', 404
    re = MyReimbursement(0, email, int(transferAmount), reason)
    reimbursement = account_service.create_reimbursement(re)
    if reimbursement is None:
        return 'Reimbursement not created', 503

    return redirect('/employee/' + email)


@app.route('/manager')
def managerHome():
    reimbursementList: list = account_service.get_all_reimbursements('Waiting', '')
    if reimbursementList is None:
        return render_template('ManagerHome.html')

    return render_template('ManagerHome.html', reimbursementList=reimbursementList)


@app.route("/reimbursementsList")
def reimbursements():
    sql = """select * from my_reimbursement"""
    cursor = connection.cursor()
    cursor.execute(sql)
    connection.commit()
    records = cursor.fetchall()
    reimbursements = [MyReimbursement(*record) for record in records]
    if len(reimbursements) == 0:
        raise ResourceNotFoundError("No reimbursement records found")
    else:
        return render_template("display.html", reimbursements=reimbursements)


@app.route('/statistics', methods=['GET', 'POST'])
def statistics():
    sql = """select * from my_reimbursement"""
    cursor = connection.cursor()
    cursor.execute(sql)
    connection.commit()
    records = cursor.fetchall()
    reimbursements = [MyReimbursement(*record) for record in records]
    if len(reimbursements) == 0:
        raise ResourceNotFoundError("No reimbursement records found")
    else:
        return render_template("statistics.html", reimbursements=reimbursements)


@app.route('/chart-statistics', methods=['GET'])
def chartStatistics():
    sql = """select status, SUM(transfer_amount) as amount from my_reimbursement group by status"""
    cursor = connection.cursor()
    cursor.execute(sql)
    connection.commit()
    records = cursor.fetchall()
    reimbursements = [ReimbursementChartInfo(*record) for record in records]
    if len(reimbursements) == 0:
        raise ResourceNotFoundError("No records found")
    else:
        return jsonify(records)


@app.route("/report")
def reimbursements_report():
    report = account_service.get_report_reimbursement()
    return jsonify(report)


if __name__ == '__main__':
    app.run(debug=True)
