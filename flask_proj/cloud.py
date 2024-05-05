import MySQLdb
from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__, static_url_path='/static')
app.secret_key = 'your_secret_key'  # Change this to a random secret key
app.config['MYSQL_HOST'] = 'mysql'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'password'
app.config['MYSQL_DB'] = 'cloud_project'

def get_students():
    try:
        conn = MySQLdb.connect(host=app.config['MYSQL_HOST'],
                               user=app.config['MYSQL_USER'],
                               password=app.config['MYSQL_PASSWORD'],
                               db=app.config['MYSQL_DB'])
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM students")
        students = cursor.fetchall()
        return students
    except MySQLdb.Error as e:
        print("Error fetching data from MySQL:", e)
        return []

    finally:
        if 'cursor' in locals() and cursor:
            cursor.close()
        if 'conn' in locals() and conn:
            conn.close()

@app.route("/")
def index():
    return render_template("homepage.html")

@app.route("/login", methods=["POST"])
def login():
    id = request.form['id']
    password = request.form['password']
    if id == '11111' and password == '12345':
        session['logged_in'] = True
        return redirect(url_for('home'))  # Redirect to data page on successful login
    else:
        return "Invalid credentials. Please try again."

@app.route("/logout")
def logout():
    session.pop('logged_in', None)
    return redirect(url_for('index'))

@app.route("/home")
def home():
    if 'logged_in' in session:
        students = get_students()
        return render_template("data.html", students=students)
    else:
        return redirect(url_for('index'))

if __name__ == "__main__":
    app.run(host='0.0.0.0',debug=True)
