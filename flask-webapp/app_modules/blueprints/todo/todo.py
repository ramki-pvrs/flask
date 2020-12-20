from flask import Blueprint
from flask import current_app as app

#Blueprint Configuration

todo_bp = Blueprint(
        'todo_bp', __name__,
        template_folder='templates'
        static_folder='static'
)
