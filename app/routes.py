from app import app
from flask import render_template, request, redirect, url_for
import json

@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    try:
        if request.method == 'POST':
            num = [request.form.get('num1'), request.form.get('num2')]
            if float(num[0]) and float(num[1]):
                pass
            for op in ['Add', 'Subtract', 'Divide', 'Multiply']:
                if request.form.get(op):
                    return redirect(url_for(op.lower(), numbers=json.dumps(num)))
        elif request.method == 'GET':
            return render_template('index.html', n=['0','0'])
    except ValueError:
        return render_template('index.html', error='ERROR : Both entries must be numbered', n=['0','0'])

@app.route('/add', methods=['GET'])
def add():
    numbers = json.loads(request.args.get('numbers'))
    x = float(numbers[0]) + float(numbers[1])
    result = 'The result of {0} + {1} is {2}'.format(numbers[0], numbers[1], x)    
    return render_template('index.html', result=result, n=numbers)

@app.route('/subtract', methods=['GET'])
def subtract():
    numbers = json.loads(request.args.get('numbers'))
    x = float(numbers[0]) - float(numbers[1])    
    result = 'The result of {0} - {1} is {2}'.format(numbers[0], numbers[1], x)    
    return render_template('index.html', result=result, n=numbers)

@app.route('/divide', methods=['GET'])
def divide():
    try:
        numbers = json.loads(request.args.get('numbers'))
        x = float(numbers[0]) / float(numbers[1])
        result = 'The result of {0} / {1} is {2}'.format(numbers[0], numbers[1], x)
        return render_template('index.html', result=result, n=numbers)
    except ZeroDivisionError:
        return render_template('index.html', error='ERROR: Divide by Zero', n=numbers)

@app.route('/multiply', methods=['GET'])
def multiply():
    numbers = json.loads(request.args.get('numbers'))
    x = float(numbers[0]) * float(numbers[1])
    result = 'The result of {0} * {1} is {2}'.format(numbers[0], numbers[1], x)    
    return render_template('index.html', result=result, n=numbers)
