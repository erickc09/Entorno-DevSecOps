import unittest
import sys
import os
from bs4 import BeautifulSoup  # Importar BeautifulSoup para analizar HTML

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
        """Verifica que el contenido visible de la página principal contiene palabras clave"""
        response = self.app.get('/')
        soup = BeautifulSoup(response.data, 'html.parser')
        visible_text = soup.get_text()

        # Registrar HTML completo si falla
        try:
            self.assertIn('Noticias DevSecOps', visible_text)  # Título principal
            self.assertIn('El lugar para estar al día en seguridad y desarrollo', visible_text)  # Subtítulo
        except AssertionError as e:
            print("\nHTML devuelto por Flask:\n", soup.prettify())
            raise e

if __name__ == "__main__":
    unittest.main()
