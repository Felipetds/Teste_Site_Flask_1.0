from flask import Flask, render_template, request, flash, redirect
import requests

app = Flask(__name__)

app.config['SECRET_KEY']="teste"

@app.route("/", methods=['GET', 'POST'])
def teste():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)