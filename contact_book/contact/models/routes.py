from flask import render_template, request, url_for, redirect
from contact import app, db
#from contact import Contact
from .contact import Contact




@app.route('/')
def home():
    contacts = Contact.query.all()
    return render_template('home.html', contacts=contacts)


@app.route('/add', methods=['GET', 'POST'])
def add_contact():
    if request.method == 'POST':
        # Get form data
        name = request.form.get('name')
        phone_number = request.form.get('phone_number')
        email = request.form.get('email')
        address = request.form.get('address')

        # Create new contact
        contact = Contact(name=name, phone_number=phone_number, email=email, address=address)

        # Add contact to database
        db.session.add(contact)
        db.session.commit()

        # Redirect to home page
        return redirect(url_for('home'))

    return render_template('add_contact.html')


@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit_contact(id):
    contact = Contact.query.get(id)
    if request.method == 'POST':
        # Update contact details
        contact.name = request.form.get('name')
        contact.phone_number = request.form.get('phone_number')
        contact.email = request.form.get('email')
        contact.address = request.form.get('address')

        # Commit the changes
        db.session.commit()

        return redirect(url_for('home'))

    return render_template('edit_contact.html', contact=contact)

@app.route('/delete/<int:id>', methods=['POST'])
def delete_contact(id):
    contact = Contact.query.get(id)
    db.session.delete(contact)
    db.session.commit()

    return redirect(url_for('home'))
