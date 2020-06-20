class PageResults:

    def __init__(self, driver):
        self.titulo_categoria = "//h1[@class='breadcrumb__title']"
        self.cantidad_resultados = "//div[contains(@class,'quantity-results')]"
        self.driver = driver


    def recuperar_titulo_subcategoria(self):
        return self.driver.find_element_by_xpath(self.titulo_categoria).text

    def recuperar_cantidad_subcategoria(self):
        return self.driver.find_element_by_xpath(self.cantidad_resultados).text




