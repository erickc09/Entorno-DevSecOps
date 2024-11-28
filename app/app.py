from flask import Flask, render_template

# Crear instancia de Flask
app = Flask(__name__)

# Configuración del entorno
app.config['ENV'] = 'development'
app.config['DEBUG'] = True

@app.route('/')
def home():
    return render_template('index.html')

# Hacer que el objeto `app` esté disponible para pruebas
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
