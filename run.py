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
@app.route('/calculadora')
def calculadora():
    return '<center><h1>Calculadora</h1></center>'

# Calculadora de 2 numeros
@app.route('/calculadora/<Signo>/<int:num1>/<int:num2>')
def calculadora1(signo, num1, num2):
    if signo == 'suma':
        result = num1 + num2
        return f'<center><h1>{num1} + {num2} = {num1 + num2}</h1></center>'
    elif signo == 'resta':
        result = num1 - num2
        return f'<center><h1>{num1} - {num2} = {num1 - num2}</h1></center>'
    elif signo == 'multiplicacion':
        result = num1 * num2
        return f'<center><h1>{num1} x {num2} = {num1 * num2}</h1></center>'
    elif signo == 'division':
        result = num1 / num2
        return f'<center><h1>{num1} ÷ {num2} = {num1 / num2}</h1></center>'
    elif signo == "potencia":
        result = num1 ** num2
        return f'<center><h1>{num1} ^ {num2} = {result}</h1></center>'
    else:
        return f'<center><h1>ERROR</h1></center>'

# Calculadora de 3 numeros
@app.route('/calculadora/<signo>/<int:num1>/<int:num2>/<int:num3>')
def calculadora2(signo, num1, num2, num3 = None):
    if signo == 'suma':
        result = num1 + num2 + num3
        return f'<center><h1>{num1} + {num2} + {num3} = {result}</h1></center>'
    elif signo == 'resta':
        result = num1 - num2 - num3
        return f'<center><h1>{num1} - {num2} - {num3} = {result}</h1></center>'
    else:
        return f'<center><h1>ERROR</h1></center>'

if __name__ == "__main__":
    app.run()