from app import app
from flask import render_template, jsonify, request, redirect, url_for
import json

@app.route('/')
def index():
    return render_template('index.html', n=['0','0'])

@app.route('/add', methods=['POST'])
def add():
    try:
        r = float(request.form['num1']) + float(request.form['num2'])
        return jsonify({
            'n1': request.form['num1'],
            'n2': request.form['num2'],
            'result': r
        })
    except ValueError:
        return jsonify({
            'n1': request.form['num1'],
            'n2': request.form['num2'],
            'error': 'Both Fields Must Have Valid Numbers'
        })

@app.route('/subtract', methods=['POST'])
def subtract():
    try:
        r = float(request.form['num1']) - float(request.form['num2'])
        return jsonify({
            'n1': request.form['num1'],
            'n2': request.form['num2'],
            'result': r
        })
    except ValueError:
        return jsonify({
            'n1': request.form['num1'],
            'n2': request.form['num2'],
            'error': 'Both Fields Must Have Valid Numbers'
        })

@app.route('/divide', methods=['POST'])
def divide():
    try:
        r = float(request.form['num1']) / float(request.form['num2'])
        return jsonify({
            'n1': request.form['num1'],
            'n2': request.form['num2'],
            'result': r
        })
    except ZeroDivisionError:
        return jsonify({
            'n1': request.form['num1'],
            'n2': request.form['num2'],
            'error': 'ERROR: Divide by Zero'
        })
    except ValueError:
        return jsonify({
            'n1': request.form['num1'],
            'n2': request.form['num2'],
            'error': 'Both Fields Must Have Valid Numbers'
        })

@app.route('/multiply', methods=['POST'])
def multiply():
    try:
        r = float(request.form['num1']) * float(request.form['num2'])
        return jsonify({
            'n1': request.form['num1'],
            'n2': request.form['num2'],
            'result': r
        })
    except ValueError:
        return jsonify({
            'n1': request.form['num1'],
            'n2': request.form['num2'],
            'error': 'Both Fields Must Have Valid Numbers'
        })