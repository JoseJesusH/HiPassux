# PASSUX

## Descripción

Esta es una aplicación web desarrollada con Flask, utilizando un enfoque de **Domain-Driven Design (DDD)** y **Model-View-Controller (MVC)**. La aplicación está configurada para trabajar con una base de datos MySQL utilizando `PyMySQL` y `Flask-Migrate` para manejar las migraciones.

## Estructura del Proyecto
    ```
    my_flask_app/
    │
    ├── app/
    │   ├── __init__.py
    │   ├── controllers/
    │   │   ├── __init__.py
    │   │   ├── user_controller.py  # Controladores para rutas web
    │   │   └── ... (otros controladores)
    │   ├── api/
    │   │   ├── __init__.py
    │   │   ├── user_api.py  # Controladores para rutas API
    │   │   └── ... (otros controladores de API)
    │   ├── domain/
    │   │   ├── __init__.py
    │   │   ├── entities/
    │   │   │   ├── __init__.py
    │   │   │   ├── user.py
    │   │   │   └── ... (otras entidades)
    │   │   ├── repositories/
    │   │   │   ├── __init__.py
    │   │   │   ├── user_repository.py
    │   │   │   └── ... (otros repositorios)
    │   │   ├── services/
    │   │   │   ├── __init__.py
    │   │   │   ├── user_service.py
    │   │   │   └── ... (otros servicios)
    │   ├── templates/
    │   │   ├── base.html
    │   │   ├── index.html
    │   │   └── ... (otras plantillas)
    │   ├── static/
    │   │   ├── css/
    │   │   │   └── ... (archivos CSS)
    │   │   ├── js/
    │   │   │   └── ... (archivos JavaScript)
    │   │   └── img/
    │   │       └── ... (imágenes)
    │   ├── viewmodels/
    │   │   ├── __init__.py
    │   │   ├── user_viewmodel.py
    │   │   └── ... (otros viewmodels)
    │   ├── config.py
    │   ├── routes.py
    │   ├── extensions.py
    │   ├── api_routes.py  # Definición de rutas API
    │
    ├── tests/
    │   ├── __init__.py
    │   ├── test_user.py
    │   ├── test_user_api.py  # Pruebas para la API
    │   └── ... (otros tests)
    │
    ├── migrations/
    │   └── ... (archivos de migración)
    │
    ├── venv/
    │   └── ... (entorno virtual)
    │
    ├── .env
    ├── .gitignore
    ├── requirements.txt
    ├── run.py
    └── README.md
    ```


## Instalación

1. **Clona el repositorio**:

    ```bash
    git clone <url-del-repositorio>
    ```

2. **Crea y activa un entorno virtual**:

    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

3. **Instala las dependencias**:

    ```bash
    pip install -r requirements.txt
    ```

4. **Configura las variables de entorno**:

    Crea un archivo `.env` en la raíz del proyecto con el siguiente contenido:

    ```plaintext
    DATABASE_URL=mysql+pymysql://root:PASSWORD@localhost/DATABASENAME!
    ```

5. **Inicializa la base de datos**:
    Necesario haber creado la DATABASE, las relaciones se crean por medio de estos comandos!

    ```bash
    flask db init
    flask db migrate -m "Initial migration."
    flask db upgrade
    ```

## Uso

1. **Ejecuta la aplicación**:

    ```bash
    flask run
    ```

2. **Exporta la aplicación Flask (si es necesario)**:

    ```bash
    export FLASK_APP=run.py
    ```

## Estructura del Código

- **`app/controllers/`**: Controladores que manejan la lógica de las rutas.
- **`app/domain/`**: Dominio de la aplicación, incluyendo entidades, repositorios y servicios.
- **`app/templates/`**: Plantillas HTML para renderizar vistas.
- **`app/static/`**: Archivos estáticos como CSS, JavaScript e imágenes.
- **`app/viewmodels/`**: ViewModels para la lógica de presentación.
- **`tests/`**: Pruebas unitarias y de integración.
- **`migrations/`**: Archivos de migración de la base de datos.

## Contribuciones

Las contribuciones son bienvenidas. Por favor, sigue los siguientes pasos para contribuir:

1. Haz un fork del repositorio.
2. Crea una nueva rama (`git checkout -b feature/nueva-caracteristica`).
3. Realiza tus cambios y haz commit (`git commit -am 'Añadida nueva característica'`).
4. Empuja tus cambios (`git push origin feature/nueva-caracteristica`).
5. Abre un Pull Request.

## Licencia

Este proyecto está licenciado bajo la [Licencia MIT](LICENSE).

## Clear Comments
Before:
# This function does something
def do_something():
    pass
After:
def initialize_database_connection():
    """
    Initialize the connection to the database using environment variables.
    """
    pass
# Improved Function Names
Before:def get_users():
    pass
After:
def retrieve_all_users():
    """
    Retrieve all users from the database.
    """
    pass

## Principios SOLID Aplicados

En este proyecto, hemos aplicado varios principios SOLID para garantizar un diseño modular y mantenible:

1. **Principio de Responsabilidad Única (SRP)**:
   - **Controladores**: `user_controller.py` maneja solo las rutas relacionadas con usuarios, mientras que cada función en el controlador gestiona una responsabilidad específica (por ejemplo, `get_users` recupera usuarios, `register` maneja el registro de usuarios).
   - **Servicios**: `user_service.py` contiene la lógica de negocio relacionada con usuarios, separándola de la lógica de enrutamiento del controlador.

2. **Principio de Abierto/Cerrado (OCP)**:
   - **Servicios Extensibles**: Al colocar la lógica de negocio en `UserService`, puedes extender el servicio para manejar funcionalidades adicionales sin modificar el código existente. Por ejemplo, podrías agregar nuevos métodos a `UserService` para operaciones adicionales de usuario.
   - **Patrón Repositorio**: El patrón `UserRepository` permite extender o reemplazar el acceso a datos subyacente sin modificar el código del servicio o del controlador.

3. **Principio de Sustitución de Liskov (LSP)**:
   - **Herencia y Sustituibilidad**: El principio LSP se respeta siempre que cualquier subclase de la entidad `User` pueda ser utilizada en lugar de la entidad base `User` sin alterar la corrección de la aplicación. Si agregas diferentes tipos de usuarios o implementas diferentes repositorios, la aplicación debe seguir funcionando correctamente con estas variaciones.

4. **Principio de Segregación de Interfaces (ISP)**:
   - **Interfaces Granulares**: Las interfaces `UserRepository` y `UserService` están diseñadas para manejar responsabilidades específicas. Al usar estas interfaces enfocadas, la aplicación evita forzar a cualquier componente a depender de interfaces que no utiliza. Por ejemplo, la interfaz del repositorio puede incluir solo métodos relacionados con el acceso a datos de usuario.

5. **Principio de Inversión de Dependencias (DIP)**:
   - **Inyección de Dependencias**: Aunque no se muestra explícitamente en el código proporcionado, adherirse al DIP implica diseñar tus clases para que dependan de abstracciones en lugar de implementaciones concretas. Por ejemplo, `UserService` debería depender de una interfaz abstracta de repositorio en lugar de una implementación específica de `UserRepository`. Esto permite una prueba más fácil y flexibilidad al intercambiar implementacionecs.

Estos principios ayudan a hacer que el código sea más modular, mantenible y flexible.

# Refactored Code with SOLID Principles Applied
1. User Retrieval Service:
# app/domain/services/user_retrieval_service.py
from app.domain.repositories.user_repository import UserRepository

class UserRetrievalService:
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    def get_all_users(self):
        return self.user_repository.get_all_users()

2. User Creation Service:
# app/domain/services/user_creation_service.py
from app.domain.repositories.user_repository import UserRepository
from app.domain.entities.user import User

class UserCreationService:
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    def create_user(self, username, first_name, last_name, birth_date, phone_number, gender, email, password):
        new_user = User(
            username=username,
            first_name=first_name,
            last_name=last_name,
            birth_date=birth_date,
            phone_number=phone_number,
            gender=gender,
            email=email,
            password=password
        )
        self.user_repository.add_user(new_user)

3. Updated User Controller:

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


