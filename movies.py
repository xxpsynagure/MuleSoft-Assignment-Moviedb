from flask import (
    Flask,
    json,
    render_template,
    request,
    redirect
)
from flask_mysqldb import MySQL

app = Flask(__name__)
app.secret_key = "hello"

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'dbadmin'
app.config['MYSQL_PASSWORD'] = 'helloworld'
app.config['MYSQL_DB'] = 'Movies'
 
mysql = MySQL(app)

@app.route("/", methods = ["POST","GET"])
def home():
    try:
        cur= mysql.connection.cursor()
        try:
            sql = "SELECT MovieName, MaleLead, Femalelead, YearOfRelease, Director FROM MovDetails WHERE Ratings = 5;"
            cur.execute(sql)
        except(IntegrityError,OperationalError) as e:
            print(e)
        data = cur.fetchall()
        print(data)
    except DatabaseError or DataError as e:
        print(e)
    return render_template("index.html", movies = data, head = "My 5 Rated Movies")


@app.route("/search", methods = ["POST","GET"])
def search():
    if request.method == 'POST':
        data = ''
        try:
            cur= mysql.connection.cursor()
            try:
                sql = "SELECT MovieName, MaleLead, Femalelead, YearOfRelease, Director FROM MovDetails WHERE %s = '%s';" % (request.form.get('movval'),request.form.get('movip'))
                print(sql)
                cur.execute(sql)
            except(IntegrityError,OperationalError) as e:
                print(e)
            data = cur.fetchall()
            print(data)

        except DatabaseError or DataError as e:
            print(e)
        if(data == ()):
            return render_template("index.html", movies = data, head='Oops! We have different taste')
        else:
            return render_template("index.html", movies = data, head='Our Movie Match')

@app.route("/admin", methods = ["GET","POST"])
def admin():
    try:
        cur= mysql.connection.cursor()
        try:
            sql = "SELECT MovieName, MaleLead, Femalelead, YearOfRelease, Director FROM MovDetails WHERE Ratings = 5;"
            cur.execute(sql)
        except(IntegrityError,OperationalError) as e:
            print(e)
        data = cur.fetchall()
        print(data)
    except DatabaseError or DataError as e:
        print(e)
    return render_template("admin.html")

@app.route("/adminfill", methods = ["GET","POST"])
def adminfill():
    if(request.method =='POST'):
        params = (request.form.get('movie'),
        request.form.get('actor'),
        request.form.get('actress'),
        request.form.get('yor'),
        request.form.get('director'),
        request.form.get('rating')
        )
        try:
            cur= mysql.connection.cursor()
            try:
                sql = " INSERT INTO MovDetails (MovieName, MaleLead, FemaleLead, YearOfRelease, Director, Ratings) values( '%s','%s','%s','%s','%s',%s);" % params
                print(sql)
                cur.execute(sql)
                
            except(IntegrityError,OperationalError) as e:
                print(e)
            
        except DatabaseError or DataError as e:
            print(e)
    return render_template("admin.html")
            

if(__name__ == "__main__"):
    app.run(debug = True)