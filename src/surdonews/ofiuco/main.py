# -*- coding: utf-8 -*-
from browser import document, html, alert
from superpython.virgem.main import Sala, Labirinto, Cena, INVENTARIO
from superpython.virgem.main import Droppable


class Card(Cena, Droppable):
    passou = False
    metro = None

    def __init__(self, img, esquerda):
        self.pega = Cena(vai=self.pega_card)
        Cena.__init__(self, img=img, esquerda=esquerda)
        Droppable.__init__(self, self.divmeio, "card", self.passa_card)

    def vai_meio(self, _=0):
        if self.passou:
            alert("Você precisa encostar o passe no leitor")
        else:
            alert("Você está sem o passe, volte para buscar")

    def passa_card(self, _=0, __=0):
        if Card.passou:
            alert("Você segue para o seu destino")
        else:
            alert("Você está sem o passe, volte para buscar")

    def pega_card(self):
        riocard = "https://www.cartaoriocard.com.br/rcc/static/img/personal-1.png"
        Card.passou = True
        flag = None

        def clicou(_):
            # hipótese de flag
            if INVENTARIO.cena == self or INVENTARIO.cena == self.metro:
                alert("Você precisa encostar o passe no leitor")
            else:
                alert("Você não está num meio de transporte.")

        if not "card" in INVENTARIO.inventario:
            alert("Você pega o seu RioCard")
            INVENTARIO.bota("card", riocard, clicou)
        else:
            alert("A gaveta está vazia")


class Metro(Card):
    def __init__(self, img, esquerda):
        Card.metro = self
        Cena.__init__(self, img=img, esquerda=esquerda)
        Droppable.__init__(self, self.divmeio, "card", self.passa_card)

    def passa_card(self, _=0, __=0):
        if Card.passou:
            alert("Você pega o metro e segue para o seu destino")
        else:
            alert("Você está sem o passe do metro, volte para buscar")


class Ofiuco:
    SETOR = None

    def __init__(self):
        pass

    def monta(self):
        NONE = [None] * 4
        imn = "https://blog.getkisi.com/wp-content/uploads/2015/03/interesting-office-designs-white.jpg"
        iml = "https://encrypted-tbn2.gstatic.com/images?q=tbn:ANd9GcROPPwsHkrj0ifm7Du22pFldDkI8SO9I4ei64mU_cMZ_VhnR5lg"
        ims = "https://www.trilux.com/fileadmin/Content/DE/Images/Anwendungen/Office/ATHENIK_Office_Slider.jpg"
        imo = "http://www.ealuxe.com/wp-content/uploads/2015/03/Most-Expensive-Office-Spaces-in-the-World-Top-10-Image-Source-kardorff.de_.jpg"
        irl = "https://upload.wikimedia.org/wikipedia/commons/7/79/Rua_Haddock_Lobo.JPG"
        iro = "http://eucurtopocos.com.br/administracao/imagens/FOTO_TEXTO/rua_rio_de_janeiro_pocos_de_caldas.jpg"
        iro = "https://encrypted-tbn2.gstatic.com/images?q=tbn:ANd9GcRKuZiT0kWJG_YfAo5z3NloeyY_d_VmPEc8qSy_DEHWj3u-krI8Dg"
        irn = "http://s14.postimg.org/ddl03ajoh/image.jpg"
        irs = "https://encrypted-tbn3.gstatic.com/images?q=tbn:ANd9GcTgKATTzedxRNtpXRyjuVqKUwMHv5EzODgghddlD8dHpRb7roW14Q"
        isn = "http://engage.synecoretech.com/Portals/141995/images/my-office-wall.png"
        isl = "http://engage.synecoretech.com/Portals/141995/images/my-office-wall.png"
        iso = "http://engage.synecoretech.com/Portals/141995/images/my-office-wall.png"
        iss = "https://encrypted-tbn2.gstatic.com/images?q=tbn:ANd9GcQ4xlWEsKlnNhlXe0T86uJrplHLzjSrj3cq90EfLlfwY4v6lcDU"
        desk = "http://cdn.decoist.com/wp-content/uploads/2012/08/white-lacquer-desk.jpg"
        drawer = "https://www.nystorefixture.com/images/Bisley-large/NoteDropInPentray2.jpg"
        leitor = "http://netdiario.com.br/wp-content/uploads/2015/08/zseguranca_onibus3-AO.jpg"
        roleta = "http://netdiario.com.br/wp-content/uploads/2012/12/z1biometria2-AOaa.jpg"
        metro = "http://super.abril.com.br/blogs/planeta/files/2011/05/catraca-metro-Super-650px1.jpg"
        sala_norte = Sala([isn, desk, iss, iso], NONE)  # Escritorio com mesa
        sala_leste = Sala([isn, isl, iss, iso], NONE)  # Sala vazia
        sala_sul = Sala([irn, irl, irs, iro], NONE)  # Escolher transporte
        sala_oeste = Sala([isn, isl, iss, iso], NONE)  # Sala Vazia
        salas = [sala_norte.norte, sala_leste.leste, sala_sul.sul, sala_oeste.oeste]
        sala_centro = Sala([imn, iml, ims, imo], salas)
        labirinto = Ofiuco.SETOR = Labirinto([
            sala_centro, sala_norte, sala_leste, sala_sul, sala_oeste])
        # from superpython.leao.main import leao
        # from superpython.sargitario.main import sagitario

        # labirinto.sul.leste.meio = leao()
        # Criar cena interior do ônibus
        # labirinto.sul.sul.meio = sagitario()
        card = Card(leitor, labirinto.sul.norte)
        labirinto.sul.sul.meio = card
        labirinto.sul.oeste.meio = Metro(metro, labirinto.sul.leste)
        # Criar um jeito de colocar uma Flag para mudar uso do cartão nessa cena
        labirinto.norte.leste.meio = card.pega  # Cena(vai=self.pega_card)
        return labirinto

    def nao_monta(self):
        pass

    def vai(self):
        labirinto = self.monta()
        self.monta = self.nao_monta
        labirinto.centro.norte.vai()
        return labirinto


INSTANCIA = None


def ofiuco():
    def cria_ofiuco():
        global INSTANCIA
        INSTANCIA = Ofiuco()

    if not INSTANCIA:
        cria_ofiuco()
    return INSTANCIA


if __name__ == "__main__":
    lab = ofiuco()
    print(INSTANCIA)
    INVENTARIO.inicia()
    lab.vai()
    # lab.centro.norte.vai()
    # lab.sul.oeste.meio = metro.centro.norte
