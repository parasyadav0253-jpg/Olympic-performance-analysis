from flask import Flask, render_template

app = Flask(_name_)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/sheet1')
def sheet1():
    return render_template('sheet1.html', title="Medals by Country")

@app.route('/sheet2')
def sheet2():
    return render_template('sheet2.html', title="Medals Trend")

@app.route('/sheet3')
def sheet3():
    return render_template('sheet3.html', title="Investment vs Medals")

@app.route('/sheet4')
def sheet4():
    return render_template('sheet4.html', title="Medals by Region")

@app.route('/sheet5')
def sheet5():
    return render_template('sheet5.html', title="Avg Medals by Sport Category")

@app.route('/dashboard1')
def dashboard1():
    return render_template('dashboard1.html', title="Dashboard 1")

@app.route('/dashboard2')
def dashboard2():
    return render_template('dashboard2.html', title="Dashboard 2")

@app.route('/story')
def story():
    return render_template('story.html', title="Story View")

if _name_ == '_main_':
    app.run(debug=True)