from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tourism.db'  # SQLite database
db = SQLAlchemy(app)

class Tourism(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    destination = db.Column(db.String(100), nullable=False)
    date = db.Column(db.Date, nullable=False)
    duration = db.Column(db.Integer, nullable=False)
    people = db.Column(db.Integer, nullable=False)
    budget = db.Column(db.Integer, nullable=False)

@app.route('/seventh', methods=['GET', 'POST'])
def seventh_pg():
    if request.method == 'POST':
        destination = request.form['destination']
        date = request.form['date']
        duration = request.form['duration']
        people = request.form['people']
        budget = request.form['budget']
        
        tourism = Tourism(destination=destination, date=date, duration=duration, people=people, budget=budget)
        db.session.add(tourism)
        db.session.commit()
        return 'Tourism details submitted successfully!'
    return render_template('form.html')

@app.route('/tourism-details')
def tourism_details():
    tourism_data = Tourism.query.all()
    return render_template('tourism_details.html', data=tourism_data)

if __name__ == "__main__":
    db.create_all()  # Create tables based on defined models
    app.run(debug=True, port=8000)
