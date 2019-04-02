from flask import Flask, request
app = Flask(__name__)
app.config['DEBUG'] = True 

form = """str.format

<!DOCTYPE html>

<html>
    <head>
        <style>
            form{{
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }}
            textarea{{
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }}
         </style>
    </head>
    <body>
        <form>
        <input type="text" name="rot" value=0>
        <textarea name="text">{0}</textarea>
        <input type="submit" value="Submit">
        </form>
    </body>
</html>
"""
@app.route("/")
def index():
    return form.format("")

from caesar import rotate_string

@app.route("/", methods=['POST']) 
def encrypt():

    rot = request.form["rot"] 
    text = request.form["text"]
    return form.format("rot", "text")
    


app.run()
