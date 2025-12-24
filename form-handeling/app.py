from flask import Flask, render_template, request 

app= Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        data = request.form
        return render_template('data.html', data = data)
    return render_template('index.html')




if __name__ == '__main__':
    app.run(debug=True)