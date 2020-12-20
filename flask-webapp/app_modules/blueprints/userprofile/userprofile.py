"""Routes for logged-in userprofile."""
from faker import Faker
from flask import Blueprint, render_template

fake = Faker()

# Blueprint Configuration
userprofile_bp = Blueprint(
    "userprofile_bp", __name__, template_folder="templates", static_folder="static"
)


@userprofile_bp.route("/userprofile", methods=["GET"])
def user_profile():
    """Logged-in user userprofile page."""
    user = fake.simple_profile()
    job = fake.job()
    return render_template(
        "userprofile.jinja2",
        title="User Profile",
        template="userprofile-template",
        user=user,
        job=job,
    )
