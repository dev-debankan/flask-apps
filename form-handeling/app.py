from flask import Flask, render_template, request 

app= Flask(__name__)

@app.route('/', methods=['GET', 'POST'])

def index():
    name=None
    age=None
    phone=None
    email=None
    if request.method == 'POST':
        name = request.form.get('name')
        age = request.form.get('age')
        phone = request.form.get('phone')
        email = request.form.get('email')
        # details = name + " " + age + " " + phone + " " + email
    return render_template('index.html', name=name, age=age, phone=phone, email=email)




if __name__ == '__main__':
    app.run(debug=True)