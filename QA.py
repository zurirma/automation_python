import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time
from pageCategorias import PageCategorias
from pageResults import PageResults
class buscar_prods (unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome('/home/zurima/Documents/personales/QA_Automation/mercadolibre_python/chromedriver.exe')
        self.driver.implicitly_wait(5)
        self.driver.get('http://mercadolibre.com.ar')
        self.driver.maximize_window()
        self.pageCategorias = PageCategorias(self.driver)
        self.pageResults = PageResults(self.driver)

    def test_buscar_climatizacion(self):

        self.pageCategorias.seleccionarClimatizacion()


        self.assertEqual(self.pageResults.recuperar_titulo_subcategoria(),"Climatización")
        self.assertTrue('resultados' in self.pageResults.recuperar_cantidad_subcategoria())

    def test_buscar_cuarto_del_bebe(self):
        self.pageCategorias.seleccionarCuartoDeBebe()

        self.assertEqual(self.pageResults.recuperar_titulo_subcategoria(), "Cuarto del Bebé")
        self.assertTrue('resultados' in self.pageResults.recuperar_cantidad_subcategoria())


    def test_buscar_perfumes(self):
        self.pageCategorias.seleccionarPerfumesDeMujer()

        self.assertEqual(self.pageResults.recuperar_titulo_subcategoria(), "Perfumes de Mujer Nuevo")
        self.assertTrue('resultados' in self.pageResults.recuperar_cantidad_subcategoria())


    def test_buscar_celulares(self):
        self.pageCategorias.seleccionarCelularesYSmartphones()

        self.assertEqual(self.pageResults.recuperar_titulo_subcategoria(), "Celulares y Smartphones")
        self.assertTrue('resultados' in self.pageResults.recuperar_cantidad_subcategoria())

    def test_buscar_industria_textil(self):
        self.pageCategorias.seleccionarIndustriaTextil()

        self.assertEqual(self.pageResults.recuperar_titulo_subcategoria(), "Industria Textil")
        self.assertTrue('resultados' in self.pageResults.recuperar_cantidad_subcategoria())


    def tearDown(self):
        self.driver.close()
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()

