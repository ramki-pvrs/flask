"""App entry point."""
from app_modules import create_app

application = create_app()

if __name__ == "__main__":
    #application.run(port=8000, debug=True)
    #application.run(port=8000, debug=True)
    application.debug=True
    application.run()
