import unittest
import sys
import os

# Agregar la ruta de la carpeta `app` al sistema
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app import app  # Importar la aplicación Flask

class TestApp(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_home_status_code(self):
        """Verifica que la página principal devuelve un código HTTP 200"""
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)

    def test_home_content(self):
        """Verifica que el contenido de la página principal contiene palabras clave"""
        response = self.app.get('/')
        self.assertIn(b'Noticias DevSecOps', response.data)  # Texto clave del header
        self.assertIn(b'Welcome to DevSecOps CVSS Evaluation', response.data)  # Texto dentro del HTML

if __name__ == "__main__":
    unittest.main()
