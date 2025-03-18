from flask import Flask, render_template, request
import qrcode

app = Flask(__name__)



# The Main Route
@app.route('/')
def home():
    return render_template('index.html')



#   Inserting The Link Function
@app.route('/', methods=['POST'])
def generateQR():
    data = request.form.get('link')
    img = qrcode.make(data)






if  __name__ == '__main__':
    app.run(debug=True)





