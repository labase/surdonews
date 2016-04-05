# -*- coding: utf-8 -*-
from browser import document, html
from superpython.virgem.main import Sala, Labirinto, Cena, INVENTARIO


class Cancer:
    SETOR = None

    def __init__(self):
        input("""Você chegou na clínica médica. 
        Você deve conseguir informações sobre quem tem
        autorização para tomar a vacina.""")

    def monta(self):
        NONE = [None] * 4

        icafe = "http://joiabergamo.com.br/wp-content/oqey_gallery/galleries/com-clinica-medica2/galimg/1img_0033.jpg"
        iquarto = "http://www.faculdadedosaber.com.br/tim.php?src=datafiles/conteudo/30/chamada.jpg&w=350&a=c"
        ipiscina = "http://www.portaldapiscina.com.br/wp-content/uploads/2012/07/piscina-agua-turva.jpg"
        icamelo = "https://upload.wikimedia.org/wikipedia/commons/a/a0/Desert_road_camel-other.jpg"
        ifloresta = "http://www.fundospaisagens.com/Imagens/floresta-no-outono.jpg"
        ifloresta2 = "http://cantimdanoticia.files.wordpress.com/2008/02/floresta.jpg"
        ihotel = "http://www.faculdadedosaber.com.br/tim.php?src=datafiles/conteudo/30/chamada.jpg&w=350&a=c"
        ipredio = "http://www.hirschclinica.com.br/wp-content/uploads/2013/01/Clinica-odontologica-01.jpg"  # 2
        imar = "http://joiabergamo.com.br/wp-content/oqey_gallery/galleries/com-clinica-medica2/galimg/1img_0033.jpg"  # 1
        ipraia = "http://www.osmais.com/wallpapers/201212/praia-barco-wallpaper.jpg"
        itop = "https://upload.wikimedia.org/wikipedia/commons/c/c3/Montanhas_Idaho_Springs,_CO.jpg"
        imonte = "http://lavanderiafontes.com.br/wp-content/uploads/2013/12/sof%C3%A1-de-couro-4.jpg"
        iareia = "http://noticias.gospelmais.com.br/files/2015/08/deserto.jpg"
        ideserto = "http://www.uberabasaude.com.br/wp-content/uploads/2011/08/739994.jpg"
        icidade = "http://www.3f.com.br/blog/wp-content/uploads/2015/02/porta1.jpg"  # 3
        irua = "http://www.insed.com.br/wp-content/uploads/2015/04/INSED-Jovem-M%C3%A9dico.jpg"  # 4

        sala_norte = Sala([ipraia, icamelo, ideserto, iareia], NONE)  # praia
        sala_leste = Sala([imonte, ifloresta2, itop, ifloresta], NONE)  # topo do monte

        sala_sul = Sala([imar, ipredio, icidade, irua], NONE)  # deserto

        sala_oeste = Sala([ihotel, icafe, ipiscina, icafe], NONE)  # mangue
        salas = [sala_norte.norte, sala_leste.leste, sala_sul.sul, sala_oeste.oeste]
        # sala_centro = Sala([ipraia,imonte,ideserto,imangue], salas)
        sala_centro = Sala([imar, imonte, imar, ihotel], salas)

        labirinto = Cancer.SETOR = Labirinto([
            sala_centro, sala_norte, sala_leste, sala_sul, sala_oeste])

        from superpython.leao.main import leao
        from superpython.sargitario.main import sagitario
        labirinto.sul.leste.meio = leao()
        # print("in sagitario")
        labirinto.sul.sul.meio = sagitario()
        labirinto.norte.leste.meio = Cena(vai=self.pega_card)

        return labirinto

    def nao_monta(self):
        pass

    def vai(self):
        labirinto = self.monta()
        self.monta = self.nao_monta
        labirinto.centro.sul.vai()
        return labirinto

    def pega_card(self):
        riocard = "https://www.cartaoriocard.com.br/rcc/static/img/personal-1.png"

        def clicou(_):
            input("você não está num meio de transporte")

        input("você pega o seu rio card")
        INVENTARIO.bota("card",
                        riocard, clicou)


INSTANCIA = None


def cancer():
    def cria_cancer():
        global INSTANCIA
        INSTANCIA = Cancer()

    if not INSTANCIA:
        cria_cancer()
    return INSTANCIA


if __name__ == "__main__":
    lab = cancer()
    print (INSTANCIA)
    lab.vai()
