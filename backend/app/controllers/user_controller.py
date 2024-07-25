# app/controllers/user_controller.py
from flask import Blueprint, render_template, request, redirect, url_for
from app.domain.services.user_creation_service import UserCreationService
from app.domain.services.user_retrieval_service import UserRetrievalService
from app.domain.repositories.user_repository import UserRepository
from datetime import datetime

bp = Blueprint('user', __name__)

user_repository = UserRepository()
user_retrieval_service = UserRetrievalService(user_repository)
user_creation_service = UserCreationService(user_repository)

@bp.route('/users', methods=['GET'])
def get_users():
    users = user_retrieval_service.get_all_users()
    return render_template('users.html', users=users)

@bp.route('/register', methods=['GET', 'POST'])
def register():
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

            user_creation_service.create_user(
                username=username,
                first_name=first_name,
                last_name=last_name,
                birth_date=birth_date,
                phone_number=phone_number,
                gender=gender,
                email=email,
                password=password
            )

            return redirect(url_for('user.get_users'))

        except Exception as e:
            return render_template('register.html', error=f'Ocurrió un error: {e}')
    
    return render_template('register.html')
