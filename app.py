from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Configure SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///contact.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define a model for Contact data
class Contact(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(100), nullable=True)
    message = db.Column(db.Text, nullable=False)

# Create the database
with app.app_context():
    db.create_all()

# Define a route to handle form submissions
@app.route('/submit', methods=['POST'])
def submit_contact():
    data = request.json  # Receive JSON data from the frontend
    first_name = data.get('first_name')
    last_name = data.get('last_name')
    email = data.get('email')
    message = data.get('message')

    # Validate required fields
    if not first_name or not last_name or not message:
        return jsonify({'error': 'First name, last name, and message are required'}), 400

    # Save data to the database
    new_contact = Contact(first_name=first_name, last_name=last_name, email=email, message=message)
    db.session.add(new_contact)
    db.session.commit()

    return jsonify({'message': 'Contact information saved successfully'}), 200

if __name__ == '__main__':
    app.run(debug=True)
