from flask import *
from pymongo.mongo_client import *
from flask_session import *
from pymongo import *
url = "mongodb+srv://naup96321:aaa@naup.xsauomk.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(url)

app = Flask(__name__)
app.config['SECRET_KEY'] = 'naup'
app.config['SESSION_TYPE'] = 'filesystem'
Session(app)


@app.route("/")
def home():
    return render_template("home.html")



if __name__ == "__main__":
    app.run(debug=True)
