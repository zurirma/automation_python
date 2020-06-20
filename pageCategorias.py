class PageCategorias():
    def __init__(self, driver):

        self.menu = 'Categorías'
        self.logo = "//a[@class='nav-menu-categories-link']"
        self.categoria_hogar = '//a[@data-order="1"]'
        self.categoria_juguetes = '//a[@data-order="3"]'
        self.categoria_belleza = "//a[contains(text(),'Belleza y Cuidado Personal')]"
        self.categoria_tecnologia = "//a[contains(text(),'Tecnología')]"
        self.categoria_herramientas = '//a[@data-order="2"]'
        self.subcategoria_clima = 'Climatización'
        self.subcategoria_cuarto_bebe = 'Cuarto del Bebé'
        self.subcategoria_perfumes_mujer = "//div[2]//div[1]//section[2]//div[1]//a[1]"
        self.subcategoria_celulares = 'Celulares y Smartphones'
        self.subcategoria_textil = 'Industria Textil'
        self.driver = driver


    def seleccionarClimatizacion(self):
        self.driver.find_element_by_link_text(self.menu).click()
        self.driver.find_element_by_xpath(self.categoria_hogar).click()
        self.driver.find_element_by_link_text(self.subcategoria_clima).click()

    def seleccionarCuartoDeBebe(self):
        self.driver.find_element_by_link_text(self.menu).click()
        self.driver.find_element_by_xpath(self.categoria_juguetes).click()
        self.driver.find_element_by_link_text(self.subcategoria_cuarto_bebe).click()

    def seleccionarPerfumesDeMujer(self):
        self.driver.find_element_by_link_text(self.menu).click()
        self.driver.find_element_by_xpath(self.categoria_belleza).click()
        self.driver.find_element_by_xpath(self.subcategoria_perfumes_mujer).click()

    def seleccionarCelularesYSmartphones(self):
        self.driver.find_element_by_link_text(self.menu).click()
        self.driver.find_element_by_xpath(self.categoria_tecnologia).click()
        self.driver.find_element_by_link_text(self.subcategoria_celulares).click()

    def seleccionarIndustriaTextil(self):
        self.driver.find_element_by_link_text(self.menu).click()
        self.driver.find_element_by_xpath(self.categoria_herramientas).click()
        self.driver.find_element_by_link_text(self.subcategoria_textil).click()



