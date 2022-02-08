from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from fncs.gerador import GeradorCodBarras



class MainWindow(BoxLayout):

    def gerar(self):
        obj = GeradorCodBarras()
        obj.entry_codproduto = self.ids.entrada_id.text
        self.ids.res_codbarras.text = str(obj.entry_codproduto)

    def limpar(self):
        self.ids.entrada_id.text = ""
        self.ids.res_codbarras.text = "CODIGO DE BARRAS"



class GeradorUI(App):
    title = 'PROGRAMA GERADOR CÓDIGO DE BARRAS EAN-13 NOS PRODUTOS PESO'
    def build(self):
        self.__version__ = '1.0.0'
        return MainWindow()

