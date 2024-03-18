
from flask import Flask, render_template, request, jsonify
import re

app = Flask(__name__)

####################################################################


@app.route('/')
def home():
    return render_template('home.html')

@app.route('/result', methods=['POST'])
def result():
    test_string = request.form['test_string']
    regex_pattern = request.form['regex_pattern']

    matches = find_matches(test_string, regex_pattern)

    return jsonify({'matches': matches})

def find_matches(test_string, regex_pattern):
    matches = re.findall(regex_pattern, test_string)
    return matches


@app.route('/email', methods = ["POST"])
def email_check():
    return render_template("email_check.html")


#################################################################


if __name__ == "__main__":
    app.run(debug=True)