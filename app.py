import MySQLdb.cursors
from flask import Flask, render_template, request ,session
from flask_mysqldb import MySQL
from datetime import date
from jira import JIRA

app = Flask(__name__, template_folder='templates')

app.config['MYSQL_HOST'] = "db"
app.config['MYSQL_USER'] = "mysql_user"
app.config['MYSQL_PASSWORD'] = "######"
app.config['MYSQL_DB'] = "alnafi"

mysql = MySQL(app)
app.secret_key='########'

@app.route("/")
def sample():
    if 'loggedin' in session:
        return render_template('index.html',username=session['username'])
    return render_template('login_page.html')

@app.route("/trainee")
def trainer():
    return render_template('demo.html')

@app.route("/trainer_create", methods=['POST', 'GET'])
def trainer_create():
    if request.method == "POST":
        fname = request.form.get('fname')
        lname = request.form.get('lname')
        desig = request.form.get('desig')
        passwd = request.form.get('passwd')
        cdate = date.today()

        sql = "INSERT INTO trainer_detail (fname, lname, desig, passwd, datetime) VALUES (%s, %s, %s, %s, %s)"
        values = (fname, lname, desig, passwd, cdate)

        with mysql.connection.cursor() as cursor:
            cursor.execute(sql, values)
            mysql.connection.commit()

        return "Trainer created successfully"

@app.route("/trainer_data", methods=['POST', 'GET'])
def trainee_data():
    sql = "SELECT * FROM trainer_detail"
    with mysql.connection.cursor() as cursor:
        cursor.execute(sql)
        row = cursor.fetchall()
    return render_template("data.html", output_data=row)


@app.route("/jira")
def jira():
    return render_template('JIRA_TICKET_CREATION.html')
@app.route("/jira_create",methods=['POST','GET'])
def jira_create():
    if request.method == "POST":
        Project = request.form.get('project')
        Issuetype = request.form.get('issuetype')
        Reporter = request.form.get('reporter')
        Summary = request.form.get('summary')
        Description = request.form.get('desc')
        user = "abdullahkhanhr01@gmail.com"
        apikey = "##############"
        server = "https://haservice.atlassian.net/"
        jira = JIRA(server, basic_auth=(user, apikey))
        jira.create_issue(project=Project,issuetype=Issuetype,summary=Summary,description=Description,reporter={'accountId':Reporter})
        return render_template("JIRA_TICKET_CREATION.html")
@app.route("/login_page")
def login_page():
    return render_template('login_page.html')
@app.route("/login",methods=['POST','GET'])
def login():
    msg = ''
    if request.method == "POST":
        Username = request.form.get('username')
        Password = request.form.get('password')
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute("SELECT * FROM users WHERE username=%s AND password=%s",(Username,Password))
        account = cursor.fetchone()
        if account:
            session['loggedin'] = True
            session['id']=account['id']
            session['username']=account['username']
            return render_template("index.html",username=session['username'])
        else:
            msg = "Incorect username/password"
    return render_template('login_page.html',msg=msg)
@app.route("/logout")
def logout():
    session.pop('loggedin',None)
    session.pop('id', None)
    session.pop('username', None)
    return render_template('login_page.html')
@app.route("/course")
def courses():
    return render_template('course.html')
if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=9000)
