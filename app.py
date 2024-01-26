from flask import Flask 

app = Flask(__name__)

@app.route('/')
def main():
    return "Har doimgdek, 'Hello World'!"

@app.route("/users")
def users():
    return "Shomurodov Mirjaxon 2003."

if __name__=="__main__":
    app.run(debug=True,port=8000)