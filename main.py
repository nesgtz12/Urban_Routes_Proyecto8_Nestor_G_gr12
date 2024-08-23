from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
import data
from urban_routes_page import UrbanRoutesPage
from helpers import retrieve_phone_code

class TestUrbanRoutes:

    driver = None

    @classmethod
    def setup_class(cls):
        chrome_options = ChromeOptions()
        chrome_options.set_capability('goog:loggingPrefs', {'performance': 'ALL'})
        cls.driver = webdriver.Chrome(options=chrome_options)
        cls.driver.maximize_window()
        cls.driver.delete_all_cookies()

    def test_set_route(self):
        self.driver.get(data.urban_routes_url)
        routes_page = UrbanRoutesPage(self.driver)
        address_from = data.address_from
        address_to = data.address_to
        routes_page.set_route(address_from, address_to)
        assert routes_page.get_from() == address_from
        assert routes_page.get_to() == address_to

    def test_texto_tarifa_comfort(self):
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.set_click_boton_pedir_un_taxi()
        assert routes_page.get_boton_comfort()

    def test_agregar_numero_de_telefono(self):
        routes_page = UrbanRoutesPage(self.driver)
        numero = data.phone_number
        routes_page.set_proceso_numero_de_telefono_ingresar(numero)
        codigo = retrieve_phone_code(self.driver)  # Llamar a la función directamente
        routes_page.set_codigo_numero_telefono(codigo)
        assert routes_page.get_numero_telefono() == numero

    def test_agregar_una_tarjeta_de_credito(self):
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.set_clicks_metodo_pago_agregar_tarjeta()
        numero_De_Tarjeta = data.card_number
        numero_Code = data.card_code
        routes_page.set_rellenar_campos_tarjeta_y_codigo(numero_De_Tarjeta, numero_Code)
        assert routes_page.get_obtener_campo_tarjeta() == numero_De_Tarjeta
        assert routes_page.get_obtener_campo_codigo() == numero_Code
        routes_page.set_clicks_perder_enfoque_agregar_tarjeta_cerrar_ventana()
        assert routes_page.get_obtener_metodo_de_pago() == 'Tarjeta'

    def test_agregar_comentario_al_conductor(self):
        routes_page = UrbanRoutesPage(self.driver)
        comentario = data.message_for_driver
        routes_page.set_agregar_comentario(comentario)
        assert routes_page.get_comprobar_comentario() == comentario

    def test_seleccionar_manta_y_pañuelos(self):
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.set_click_manta_y_pañuelos()
        assert routes_page.get_saber_si_slider_esta_seleccionado() == True

    def test_agregar_2_helados(self):
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.set_agregar_helado()
        assert routes_page.get_cantidad_de_helados() == '2'  # Agregar paréntesis para llamar al método

    def test_ventana_emergente(self):
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.set_click_pedir_taxi()
        assert routes_page.get_comprobar_ventana_emergente_si() == 'Buscar automóvil'

    def test_ventana_opcional(self):
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.set_tiempo()
        assert 'El conductor llegará en' in routes_page.get_comprobar_informacion_de_conductor()

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()
