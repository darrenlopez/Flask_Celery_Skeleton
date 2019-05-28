import pandas
import settings
import sentry_sdk
from exchange import tasks
from flask import Flask, render_template

sentry_sdk.init(settings.SENTRY_API_KEY)

app = Flask(__name__)

@app.route("/")
def hello():
    try:
        return "Hello World"  
    except Exception as e:
        sentry_sdk.capture_exception(e)
        return str(e)

if __name__ == "__main__":
    app.run(debug=True, host= '0.0.0.0')