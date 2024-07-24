from flask import Blueprint, render_template, request , redirect, url_for
from app.domain.services.user_service import UserService
from datetime import datetime

bp = Blueprint('user', __name__)

@bp.route('/users', methods=['GET'])
def get_users():
    """
    Retrieve and display all users.
    
    This route handles GET requests to retrieve all users from the database
    and renders them in the 'users.html' template.
    
    :return: Rendered template with list of users.
    """
    users = UserService.get_all_users()
    return render_template('users.html', users=users)

@bp.route('/register', methods=['GET', 'POST'])
def register():
    """
    Handle user registration form.
    
    This route handles both GET and POST requests. For GET requests, it displays
    the registration form. For POST requests, it processes the form data and creates
    a new user in the database.
    
    :return: Redirect to user list on success, or re-render registration form with an error message on failure.
    """
    if request.method == 'POST':
        try:
            username = request.form['username']
            first_name = request.form['first_name']
            last_name = request.form['last_name']
            birth_date = datetime.strptime(request.form['birth_date'], '%Y-%m-%d')
            phone_number = request.form.get('phone_number')
            gender = request.form.get('gender')
            email = request.form['email']
            password = request.form['password']

            UserService.create_user(
                username=username,
                first_name=first_name,
                last_name=last_name,
                birth_date=birth_date,
                phone_number=phone_number,
                gender=gender,
                email=email,
                password=password
            )

            return redirect(url_for('user.get_users'))  # Redirige después de crear el usuario

        except Exception as e:
            return render_template('register.html', error=f'Ocurrió un error: {e}')
    
    # Si es GET, simplemente muestra el formulario
    return render_template('register.html')