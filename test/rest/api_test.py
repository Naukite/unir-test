import http.client
import os
import unittest
from urllib.request import urlopen
import urllib 

import pytest

BASE_URL = os.environ.get("BASE_URL")
DEFAULT_TIMEOUT = 2  # in secs


@pytest.mark.api
class TestApi(unittest.TestCase):
    def setUp(self):
        self.assertIsNotNone(BASE_URL, "URL no configurada")
        self.assertTrue(len(BASE_URL) > 8, "URL no configurada")

    def test_api_add(self):
        url = f"{BASE_URL}/calc/add/2/2"
        response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(
            response.status, http.client.OK, f"Error en la petición API a {url}"
        )

    #se añade prueba para comprobar la resta
    def test_api_substract(self):
        url = f"{BASE_URL}/calc/substract/2/2"
        response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(
            response.status, http.client.OK, f"Error en la petición API a {url}"
        )        

    #se añade prueba para comprobar la división
    def test_api_divide(self):
        url = f"{BASE_URL}/calc/divide/2/2"
        response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(
            response.status, http.client.OK, f"Error en la petición API a {url}"
        )                

    #se añade prueba para comprobar la potencia
    def test_api_power(self):
        url = f"{BASE_URL}/calc/power/2/2"
        response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(
            response.status, http.client.OK, f"Error en la petición API a {url}"
        )                        

    #se añade prueba para comprobar la raíz cuadrada
    def test_api_sqrt(self):
        url = f"{BASE_URL}/calc/sqrt/4"
        response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(
            response.status, http.client.OK, f"Error en la petición API a {url}"
        )                                

    #se añade prueba para comprobar el log10
    def test_api_log10(self):
        url = f"{BASE_URL}/calc/log10/10"
        response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(
            response.status, http.client.OK, f"Error en la petición API a {url}"
        )                                   
        
    #se añade prueba para comprobar que se devuelve status code 400 al dividir por cero
    def test_api_dividebyzero(self):
        url = f"{BASE_URL}/calc/divide/10/0"
        response = {}
        try: 
            response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        except urllib.error.HTTPError as ex:
            self.assertEqual(ex.code, 400)     
        return False
    
    #se añade prueba para comprobar que se devuelve status code 400 al hacer raíz cuadrada de número negativo
    def test_api_sqrtnegative(self):
        url = f"{BASE_URL}/calc/sqrt/-1"
        response = {}
        try: 
            response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        except urllib.error.HTTPError as ex:
            self.assertEqual(ex.code, 400)     
        return False
    
    #se añade prueba para comprobar que se devuelve status code 400 al hacer log10 de cero 
    def test_api_log10zero(self):
        url = f"{BASE_URL}/calc/log10/0"
        response = {}
        try: 
            response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        except urllib.error.HTTPError as ex:
            self.assertEqual(ex.code, 400)     
        return False    
    
    #se añade prueba para comprobar que se devuelve status code 400 al hacer log10 de un número negativo 
    def test_api_log10negative(self):
        url = f"{BASE_URL}/calc/log10/-1"
        response = {}
        try: 
            response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        except urllib.error.HTTPError as ex:
            self.assertEqual(ex.code, 400)     
        return False        
        
                                        
