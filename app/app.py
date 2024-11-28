from flask import Flask, render_template

app = Flask(__name__)
app.config['ENV'] = 'development'  # Asegurar entorno de desarrollo
app.config['DEBUG'] = True  # Activar depuración

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
