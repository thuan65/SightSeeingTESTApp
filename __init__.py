from flask import Flask
from flask_migrate import Migrate
from extensions import init_extensions

from Login.login import login_bp
from add_favorites.routes import favorite_bp

def create_app(config_class="config.Config"):
    app = Flask(__name__)
    app.config.from_object(config_class)
    
    # app.config['SECRET_KEY'] = 'mysecretkey'
    # app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///FlaskDataBase.db'
    # app.config['UPLOAD_FOLDER'] = 'static/uploads'
    # app.config['JSON_AS_ASCII'] = False
    
    # app.config.from_object(config_class)

    # Khởi tạo extensions
    init_extensions(app)

    app.register_blueprint(login_bp)
    app.register_blueprint(favorite_bp)

    # ---------------------------------------------------------
    # KẾT NỐI DB ẢNH VÀ REGISTER BLUEPRINT
    #  ---------------------------------------------------------


    return app
