from flask import Flask

app = Flask('__name__')

# Home
@app.route('/')
def index():
    return '<center><h1>Bienbenido</h1></center>'

# Nombre y Edad
@app.route('/<name>')
@app.route('/<name>/<edad>')
def user(name = None, edad = None):
    if edad == None:
        return f'<center><h1>Tu nombre es: {name}</h1></center>'
    else:
        return f'<center><h1>Tu nombre es: {name}, y tu edad: {edad}</h1></center>'

# Calculadora

# suma
@app.route('/suma/<int:num1>,<int:num2>')
@app.route('/suma/<int:num1>,<int:num2>,<int:num3>')
def suma(num1, num2, num3=None):
    if num3 is None:
        resultado = num1 + num2
        return f'<center><h1>{num1} + {num2} = {resultado}</h1></center>'
    else:
        resultado = num1 + num2 + num3
        return f'<center><h1>{num1} + {num2} + {num3} = {resultado}</h1></center>'

# resta
@app.route('/resta/<int:num1>,<int:num2>')
@app.route('/resta/<int:num1>,<int:num2>,<int:num3>')
def resta(num1, num2, num3=None):
    if num3 is None:
        resultado = num1 - num2
        return f'<center><h1>{num1} - {num2} = {resultado}</h1></center>'
    else:
        resultado = num1 - num2 - num3
        return f'<center><h1>{num1} - {num2} - {num3} = {resultado}</h1></center>'

# multiplicacion
@app.route('/multiplicacion/<int:num1>,<int:num2>')
@app.route('/multiplicacion/<int:num1>,<int:num2>,<int:num3>')
def multiplicacion(num1, num2, num3=None):
    if num3 is None:
        resultado = num1 * num2
        return f'<center><h1>{num1} * {num2} = {resultado}</h1></center>'
    else:
        resultado = num1 * num2 * num3
        return f'<center><h1>{num1} * {num2} * {num3} = {resultado}</h1></center>'

# division
@app.route('/division/<int:num1>,<int:num2>')
@app.route('/division/<int:num1>,<int:num2>,<int:num3>')
def division(num1, num2, num3=None):
    if num3 is None:
        resultado = num1 / num2
        return f'<center><h1>{num1} / {num2} = {resultado}</h1></center>'
    else:
        resultado = num1 / num2 / num3
        return f'<center><h1>{num1} / {num2} / {num3} = {resultado}</h1></center>'

# potencia
@app.routr('potencia/<int:num1>,<int:num2>')
def potencia(num1,num2):
    resultado = num1 ** num2
    return f'<center><h1>{num1} ** {num2} = {resultado}</h1></center>'

if __name__ == "__main__":
    app.run()