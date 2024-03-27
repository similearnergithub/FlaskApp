from flask import Flask, render_template
app=Flask(__name__)

app = Flask(__name__, static_url_path='/static', static_folder='static')

@app.route('/')
def hello_world():
    return render_template('index1.html')

@app.route('/first')
def first_pg():
    return render_template('index.html')

@app.route('/second')
def second_pg():
    return render_template('home2.html')

@app.route('/third')
def third_pg():
    return render_template('contact.html')

@app.route('/fourth')
def fourth_pg():
    return render_template('projects.html')

@app.route('/fifth')
def fifth_pg():
    return render_template('resume.html')

@app.route('/sixth')
def sixth_pg():
    return render_template('aboutme.html')

@app.route('/seventh')
def seventh_pg():
    return render_template('form.html')

@app.route('/eighth')
def eight_pg():
    return render_template('tourism_details.html')


if __name__ == "__main__":
    app.run(debug=True, port=8000) 

