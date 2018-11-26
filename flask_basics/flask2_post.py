from flask import Flask, request

app = Flask(__name__)

@app.route('/url_name', methods = ['POST'])
def add():
    a = request.form["a"]  # request through post parameter with form
    b = request.form["b"]
    return str(int(a) + int(b))

if __name__ == '__main__':
    app.run(port=7000)

# use post requests when the user should not see params in url - more secure
# in postman make new request, for example in default collection
# add url and switch to POST left of url
# go to body, form-data
# and add your parameters



# http://127.0.0.1:5000/?a=2&b=3
