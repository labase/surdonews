from browser import document, htm
from jqueryui import jq

STYLE = dict(position="absolute", width=300, left=0, top=0,
             background="white")
STYLE["min-height"] = "300px"
IMAGEM = "http://s16.postimg.org/k81hwi2n9/Desert.jpg"


class Labirinto:
    def __init__(self, salas):
        self.salas = salas
        self.centro, self.norte, self.leste, self.sul, self.oeste = self.salas
        for indice, sala in enumerate(self.salas[1:]):
            self.centro.cenas[indice].meio = sala.cenas[indice]
            sala.cenas[(indice + 2) % 4].meio = self.centro.cenas[indice]


class Sala:
    def __init__(self, imagensnlso, saidasnlso):
        self.cenas = []
        for img in imagensnlso:
            self.cenas.append(CenaFrente(img))
        self.norte, self.leste, self.sul, self.oeste = self.cenas
        for cena, saida in enumerate(saidasnlso):
            self.cenas[cena].meio = saida
        for esquerda in range(4):
            cena_a_direita = (esquerda + 1) % 4
            self.cenas[esquerda].direita = self.cenas[cena_a_direita]
            self.cenas[cena_a_direita].esquerda = self.cenas[esquerda]


class CenaFrente:
    def __init__(self, img=IMAGEM, esquerda=None, direita=None, meio=None):
        self.img, self.esquerda, self.direita = img, esquerda, direita
        self.meio = meio

    def vai(self):
        def vai_direita(_=0):
            divdir.style.opacity = 0.8
            if self.direita:
                self.direita.vai()

        def vai_esquerda(_=0):
            divesq.style.opacity = 0.8
            if self.esquerda:
                self.esquerda.vai()

        def vai_meio(_=0):
            divmeio.style.opacity = 0.8
            if self.meio:
                self.meio.vai()

        tela = document["pydiv"]
        tela.html = ""
        self.cena = cena = html.IMG(src=self.img, width=300, style=STYLE)

        divesq = html.DIV(style=STYLE)
        divesq.style.width = 100
        divesq.style.opacity = 0.3
        divesq.onclick = vai_esquerda

        divmeio = html.DIV(style=STYLE)
        divmeio.style.width = 100
        divmeio.style.opacity = 0.2
        divmeio.onclick = vai_meio
        divmeio.style.left = 100

        divdir = html.DIV(style=STYLE)
        divdir.style.opacity = 0.1
        divdir.style.width = 100
        divdir.onclick = vai_direita
        divdir.style.left = 200

        tela <= cena
        tela <= divesq
        tela <= divmeio
        tela <= divdir
        return self


class Libra:
    SETOR = None

    def __init__(self):
        pass

    def monta(self):
        NONE = [None] * 4
        imn = "http://www.hportugues.com.br/maternidade/uti-neo/UTINeonatalmaternidade.JPG/@@images/image/preview"  # norte"https://blog.getkisi.com/wp-content/uploads/2015/03/interesting-office-designs-white.jpg"
        iml = "http://www.cisbaf.org.br/newsletter/julagoset2013/images/fotos/19.1.jpg"  # leste"https://encrypted-tbn2.gstatic.com/images?q=tbn:ANd9GcROPPwsHkrj0ifm7Du22pFldDkI8SO9I4ei64mU_cMZ_VhnR5lg"
        ims = "http://i0.statig.com.br/bancodeimagens/2j/rt/qu/2jrtqupcugmkd23702yrbk3jp.jpg"  # sul"https://www.trilux.com/fileadmin/Content/DE/Images/Anwendungen/Office/ATHENIK_Office_Slider.jpg"
        imo = "http://www.hospitalsalvalus.com.br/maternidade/images/06_l.jpg"  # oeste"http://www.ealuxe.com/wp-content/uploads/2015/03/Most-Expensive-Office-Spaces-in-the-World-Top-10-Image-Source-kardorff.de_.jpg"
        irl = "https://upload.wikimedia.org/wikipedia/commons/7/79/Rua_Haddock_Lobo.JPG"
        iro = "http://www.netinforma.com/admin/noticias/images/3f729953f4a1122967fd6683543d0c33.jpg"  # oeste"http://eucurtopocos.com.br/administracao/imagens/FOTO_TEXTO/rua_rio_de_janeiro_pocos_de_caldas.jpg"
        iro = "http://www.netinforma.com/admin/noticias/images/3f729953f4a1122967fd6683543d0c33.jpg"  # oeste"https://encrypted-tbn2.gstatic.com/images?q=tbn:ANd9GcRKuZiT0kWJG_YfAo5z3NloeyY_d_VmPEc8qSy_DEHWj3u-krI8Dg"
        irn = "http://s14.postimg.org/ddl03ajoh/image.jpg"
        irs = "https://encrypted-tbn3.gstatic.com/images?q=tbn:ANd9GcTgKATTzedxRNtpXRyjuVqKUwMHv5EzODgghddlD8dHpRb7roW14Q"

        imar = "http://s21.postimg.org/x2vqvlr3b/La_Mar.jpg"
        ipraia = "http://msalx.viajeaqui.abril.com.br/2012/09/21/1743/6IivB/praia.jpg?1348260191"

        itop = "http://www.madrecor.com.br/site/wp-content/uploads/2014/04/DSC06013site.jpg"  # "http://www.acf-fr.org/i/07-12-06_mountain-top-4.jpg"#diretorcentro
        imonte = "https://pensesobre.files.wordpress.com/2012/02/vazio.jpg"  # "https://lh4.googleusercontent.com/_wIBnV-jS0pk/TaWP5uBgrfI/AAAAAAAACHQ/1Ge1OPTckW0/montanha-huayna-picchu..jpg"

        iareia = "https://pensesobre.files.wordpress.com/2012/02/vazio.jpg"  # "http://s10.postimg.org/5pipdjp2x/singing_sand.jpg"
        ideserto = "https://pensesobre.files.wordpress.com/2012/02/vazio.jpg"  # "http://s16.postimg.org/k81hwi2n9/Desert.jpg"

        ipantano = "https://pensesobre.files.wordpress.com/2012/02/vazio.jpg"  # "http://s8.postimg.org/gu0olg8ol/prd_022431.jpg"
        imangue = "https://pensesobre.files.wordpress.com/2012/02/vazio.jpg"
        sala_norte = Sala([imar, imar, ipraia, imar], NONE)  # mar
        sala_leste = Sala([itop, itop, itop, imonte], NONE)  # topo do monte
        sala_sul = Sala([irn, irl, irs, iro], NONE)  # sala maternidae principal
        sala_oeste = Sala([ipantano, imangue, ipantano, ipantano], NONE)  # mangue
        salas = [sala_norte.norte, sala_leste.leste, sala_sul.sul, sala_oeste.oeste]
        sala_centro = Sala([ipraia, imonte, ideserto, imangue], salas)
        sala_centro = Sala([imn, iml, ims, imo], salas)
        labirinto = Labirinto([
            sala_centro, sala_norte, sala_leste, sala_sul, sala_oeste])

        class Taxi:
            def vai(self):
                from superpython.libra.main import libra
                libra().centro.norte.vai()

        class Onibus:
            def vai(self):
                from superpython.leao.main import leao
                leao().centro.norte.vai()

        labirinto.sul.leste.meio = Taxi()
        labirinto.sul.sul.meio = Onibus()
        return labirinto

    def nao_monta(self):
        pass

    def vai(self):
        labirinto = self.monta()
        self.monta = self.nao_monta
        labirinto.centro.sul.vai()
        return labirinto


INSTANCIA = None


def libra():
    def cria_libra():
        global INSTANCIA
        INSTANCIA = Libra()

    if not INSTANCIA:
        cria_libra()
    return INSTANCIA


if __name__ == "__main__":
    lab = libra()
    print(INSTANCIA)
    lab.vai()

"""
from superpython.virgem.main import Sala, Labirinto, Cena,INVENTARIO
from superpython.virgem.main import Droppable

class Card(Cena, Droppable):
    passou = False
    metro = None

    def __init__(self, img, esquerda):
        self.pega = Cena(vai=self.pega_card)
        Cena.__init__(self, img=img, esquerda=esquerda)
        Droppable.__init__(self, self.divmeio,"card", self.passa_card)

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
            #hipótese de flag
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
        Droppable.__init__(self, self.divmeio,"card", self.passa_card)

    def passa_card(self, _=0, __=0):
        if Card.passou:
            alert("Você pega o metro e segue para o seu destino")
        else:
            alert("Você está sem o passe do metro, volte para buscar")

class Libra:
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
        sala_norte = Sala([isn,desk,iss,iso], NONE) #Maternidade
        sala_leste = Sala([isn,isl,iss,iso], NONE) #Sala vazia
        sala_sul = Sala([irn, irl, irs, iro], NONE) #Escolher transporte
        sala_oeste = Sala([isn,isl,iss,iso], NONE) #Sala Vazia
        salas = [sala_norte.norte, sala_leste.leste, sala_sul.sul, sala_oeste.oeste]
        sala_centro = Sala([imn, iml, ims,imo], salas)
        labirinto = Libra.SETOR = Labirinto([
            sala_centro, sala_norte, sala_leste, sala_sul, sala_oeste])
        #from superpython.leao.main import leao
        #from superpython.sargitario.main import sagitario

        #labirinto.sul.leste.meio = leao()
        #Criar cena interior do ônibus
        #labirinto.sul.sul.meio = sagitario()
        card = Card(leitor, labirinto.sul.norte)
        labirinto.sul.sul.meio = card
        labirinto.sul.oeste.meio = Metro(metro, labirinto.sul.leste)
        #Criar um jeito de colocar uma Flag para mudar uso do cartão nessa cena
        labirinto.norte.leste.meio = card.pega  # Cena(vai=self.pega_card)
        return labirinto

    def nao_monta(self):
        pass

    def vai(self):
        labirinto  = self.monta()
        self.monta = self.nao_monta
        labirinto.centro.norte.vai()
        return labirinto

INSTANCIA = None

def libra():
    def cria_libra():
        global INSTANCIA
        INSTANCIA = Libra()
    if not INSTANCIA:
        cria_libra()
    return INSTANCIA

if __name__ == "__main__":
    lab = libra()
    print(INSTANCIA)
    INVENTARIO.inicia()
    lab.vai()
class Maquina:
    def __init__(self):
        tela = document["pydiv"]
        tela.html = ""
        self.cena = cena = html.IMG(src=IMAGEM, width=300, style=STYLE)
        def clicou(_=0):
            self.inicio()
        cena.onclick = clicou
        tela <= cena

    def inicio(self):
        input("pre lavagem")
        self.era_inicio, self.inicio = self.inicio, self.lavagem

    def lavagem(self):
        input("lavagem")
        self.inicio = self.enxague

    def enxague(self):
        input("enxague")
        self.inicio = self.centrifuga

    def centrifuga(self):
        input("centrifuga")
        self.inicio = self.fim

    def fim(self):
        input("estado final")
        self.inicio = self.era_inicio

def _():
    NONE = [None] * 4
    imn = "http://www.hportugues.com.br/maternidade/uti-neo/UTINeonatalmaternidade.JPG/@@images/image/preview"#norte"https://blog.getkisi.com/wp-content/uploads/2015/03/interesting-office-designs-white.jpg"
    iml = "http://www.cisbaf.org.br/newsletter/julagoset2013/images/fotos/19.1.jpg"#oeste"https://encrypted-tbn2.gstatic.com/images?q=tbn:ANd9GcROPPwsHkrj0ifm7Du22pFldDkI8SO9I4ei64mU_cMZ_VhnR5lg"
    ims = "http://i0.statig.com.br/bancodeimagens/2j/rt/qu/2jrtqupcugmkd23702yrbk3jp.jpg"#sul"https://www.trilux.com/fileadmin/Content/DE/Images/Anwendungen/Office/ATHENIK_Office_Slider.jpg"
    imo = "http://www.hospitalsalvalus.com.br/maternidade/images/06_l.jpg"#leste"http://www.ealuxe.com/wp-content/uploads/2015/03/Most-Expensive-Office-Spaces-in-the-World-Top-10-Image-Source-kardorff.de_.jpg"
    irl = "https://upload.wikimedia.org/wikipedia/commons/7/79/Rua_Haddock_Lobo.JPG"
    iro = "http://www.netinforma.com/admin/noticias/images/3f729953f4a1122967fd6683543d0c33.jpg"#oeste"http://eucurtopocos.com.br/administracao/imagens/FOTO_TEXTO/rua_rio_de_janeiro_pocos_de_caldas.jpg"
    iro = "http://www.netinforma.com/admin/noticias/images/3f729953f4a1122967fd6683543d0c33.jpg"#oeste"https://encrypted-tbn2.gstatic.com/images?q=tbn:ANd9GcRKuZiT0kWJG_YfAo5z3NloeyY_d_VmPEc8qSy_DEHWj3u-krI8Dg"
    irn = "http://s14.postimg.org/ddl03ajoh/image.jpg"
    irs = "https://encrypted-tbn3.gstatic.com/images?q=tbn:ANd9GcTgKATTzedxRNtpXRyjuVqKUwMHv5EzODgghddlD8dHpRb7roW14Q"

    imar = "http://s21.postimg.org/x2vqvlr3b/La_Mar.jpg"
    ipraia="http://msalx.viajeaqui.abril.com.br/2012/09/21/1743/6IivB/praia.jpg?1348260191"

    itop = "http://www.acf-fr.org/i/07-12-06_mountain-top-4.jpg"
    imonte="https://lh4.googleusercontent.com/_wIBnV-jS0pk/TaWP5uBgrfI/AAAAAAAACHQ/1Ge1OPTckW0/montanha-huayna-picchu..jpg"

    iareia="http://s10.postimg.org/5pipdjp2x/singing_sand.jpg"
    ideserto="http://s16.postimg.org/k81hwi2n9/Desert.jpg"

    ipantano="http://s8.postimg.org/gu0olg8ol/prd_022431.jpg"
    imangue="http://s4.postimg.org/ez3co2sm5/Culbin_Salt_Marsh_geograph_org_uk_185128.jpg"
    sala_norte = Sala([imar,imar,ipraia,imar], NONE) #mar
    sala_leste = Sala([itop,itop,itop,imonte], NONE) #topo do monte
    sala_sul = Sala([irn, irl, irs, iro], NONE) #deserto
    sala_oeste = Sala([ipantano,imangue,ipantano,ipantano], NONE) #mangue
    salas = [sala_norte.norte, sala_leste.leste, sala_sul.sul, sala_oeste.oeste]
    #sala_centro = Sala([ipraia,imonte,ideserto,imangue], salas)
    sala_centro = Sala([imn, iml, ims,imo], salas)
    labirinto = Labirinto([
        sala_centro, sala_norte, sala_leste, sala_sul, sala_oeste])
    sala_centro.norte.vai()
    sala_norte.sul.meio = sala_centro.sul
    sala_leste.oeste.meio = sala_centro.oeste
    sala_sul.norte.meio = sala_centro.norte
    sala_oeste.leste.meio = sala_centro.leste

class Sala:
    def __init__(self, imagensnlso, saidasnlso):
        self.cenas = [CenaFrente(img) for img in imagensnlso]
        self.norte, self.leste, self.sul, self.oeste = self.cenas
        for cena, saida in enumerate(saidasnlso):
            self.cenas[cena].meio = saida
        for esquerda in range(4):
            cena_a_direita = (esquerda + 1) % 4
            self.cenas[esquerda].direita = self.cenas[cena_a_direita]
            self.cenas[cena_a_direita].esquerda = self.cenas[esquerda]


STYLE = dict(position ="absolute", width = 300, left=0, top=0, background="white")
STYLE["min-height"]="300px"
IMAGEM = "http://www.susanasteil.com.br/wp-content/uploads/2012/09/mar.jpg"
class Sala:
    def __init__(self, imangensnlso, saidanlso):
        self.cenas = [CenaFrente(img) for img in imangensnlso]
        self.norte, self.lest, self.sul, sel,oeste = self.cenas
        for cena, saida in enumerate(saidanlso):
            self.cena.meio = saida
        for esquerda in range(4):
            cena_a_direita = esquerda % 4
            self.cena[esquerda].direita = self.cena[cena_a_direita]
            self.cena[cena_a_direita].esquerda = self.cena[esquerda]

class Labirinto:
    def __init__(self, imagensnlso, saidasnlso):
        self.salas = salas
        self.centro, self.norte, self.leste, self.sul, self.oeste = self.salas
        for indice, saida in enumerate(self.salas[1:]):
            self.centro.cenas[indice].meio = sala.cenas[indice]
            sala.cenas[(indice+2)%4].meio = self.centro




class CenaFrente:

    def __init__(self, img=IMAGEM, esquerda=None, direita=None, meio=None):
        self.img, self.esquerda, self.direita = img, esquerda, direita
        self.meio = meio

    def vai(self):
        def vai_direita(_=0):
            divdir.style.opacity = 0.8
            if self.direita:
                self.direita.vai()
        def vai_esquerda(_=0):
            divesq.style.opacity = 0.8
            if self.esquerda:
                self.esquerda.vai()
        def vai_meio(_=0):
            divmeio.style.opacity = 0.8
            if self.meio:
                self.meio.vai()
        tela = document["pydiv"]
        tela.html = ""
        self.cena = cena = html.IMG(src=self.img, width=300, style=STYLE)
        divesq = html.DIV(style=STYLE)
        divesq.style.width = 100
        divesq.style.opacity = 0.3
        divesq.onclick = vai_esquerda
        divmeio = html.DIV(style=STYLE)
        divmeio.style.width = 100
        divmeio.style.opacity = 0.2
        divmeio.onclick = vai_meio
        divmeio.style.left = 100
        divdir = html.DIV(style=STYLE)
        divdir.style.opacity = 0.1
        divdir.style.width = 100
        divdir.onclick = vai_direita
        divdir.style.left = 200
        tela <= cena
        tela <= divesq
        tela <= divmeio
        tela <= divdir
        return self

    def libra():
        NONE = [None] * 4
        imn = "http://www.decorandoimoveis.com/wp-content/gallery/sala-de-estar-simples-e-bonita/sala-de-estar-simples-e-bonita-1.jpg"
        iml = "http://cdn.limaonagua.com.br/wp-content/uploads/2014/08/sala-luxuosa-01.jpg"
        ims = "http://www.nossaweb.org/img/fotos/fotos%20de%20salas%20de%20tv%202.jpg"
        imo = "http://www.unimed.coop.br/portal/conteudo/materias/1340131044405hospital-maternidade.jpg"
        iro = "https://acidadecomoeuquero.files.wordpress.com/2011/03/rua_amauri.jpg"
        irl = "http://www.guia-se.com.br/painel/upload/fotos-clientes/7913/26103/varal%20giratorio.jpg"
        irn = "http://diariodorio.com/wp-content/uploads/2009/02/torredoriosulporalexandremicaelo.jpg"
        irs = "http://www.mylifevans.com.br/include/img/layout/locacao-de-onibus-em-sp.jpg"
        imar = "http://wallpaper.ultradownloads.com.br/277950_Papel-de-Parede-Estudio-de-Musica_1440x900.jpg"#som"http://s21.postimg.org/x2vqvlr3b/La_Mar.jpg"
        ipraia="http://img.ibxk.com.br/materias/3632/11553.jpg?w=1040"#teclado"http://msalx.viajeaqui.abril.com.br/2012/09/21/1743/6IivB/praia.jpg?1348260191"
        itop = "http://i.ytimg.com/vi/iYycdYZnXUI/maxresdefault.jpg"#bateria"http://www.acf-fr.org/i/07-12-06_mountain-top-4.jpg"
        imonte="http://images.comunidades.net/est/estudiodegravacaorj/nes.jpg"#guitar"https://lh4.googleusercontent.com/_wIBnV-jS0pk/TaWP5uBgrfI/AAAAAAAACHQ/1Ge1OPTckW0/montanha-huayna-picchu..jpg"
        iareia="http://img.olx.com.br/images/53/531506038999878.jpg"#caixasom"http://s10.postimg.org/5pipdjp2x/singing_sand.jpg"
        ideserto="http://www.sompurorj.com.br/imagens/microfone-estudio.jpg"#microfone"http://s16.postimg.org/k81hwi2n9/Desert.jpg"
        ipantano="http://spc.fotolog.com/photo/28/16/69/eternalcrossing/1267756962049_f.jpg"#espelho"http://s8.postimg.org/gu0olg8ol/prd_022431.jpg"
        imangue="http://www.audiorebel.com.br/imgs/home-foto-estudio.jpg"#entrada"http://s4.postimg.org/ez3co2sm5/Culbin_Salt_Marsh_geograph_org_uk_185128.jpg"

        sala_norte = Sala([imar,imar,ipraia,imar], NONE) #mar
        sala_leste = Sala([itop,itop,itop,imonte], NONE) #topo do monte
        sala_sul = Sala([inr. irl, irs, iro], NONE) #deserto
        sala_oeste = Sala([ipantano,imangue,ipantano,ipantano], NONE)
        #sala_centro = Sala([ipraia,imonte,ideserto,imangue], salas)
        sala_centro = Sala([imn, iml, ims, imo], salas)
        labirinto = Labirinto([
            sala_centro, sala_norte, sala_leste, sala_sul, sala_oeste])
        return labirinto


    def __init__(self, img=IMAGEM, esquerda=None, direita=None, meio=None):
        self.img, self.esquerda, self.direita, self.meio = img, esquerda, direita, self.meio = meio

    def vai(self):
        def vai_direita(_=0):
            divdir.style.opacity = 0.8
            if self.direita:
                self.direita.vai()

        def vai_esquerda(_=0):
            divesq.style.opacity=0.8
            if self.esquerda:
                self.esquerda.vai()

        def vai_meio(_=0):
            divmeio.style.opacity=0.8
            if self.meio:
                self.meio.vai()

        tela = document["pydiv"]
        tela.html = ""
        cena = html.IMG(src=self.img, width=300, style=STYLE)

        divdir = html.DIV(style = STYLE)
        divdir.style.opacity = 0.1
        divdir.onclick = vai_direita
        divdir.style.width = 100
        divdir.style.left = 200

        divesq = html.DIV(style = STYLE)
        divesq.style.width = 100
        divesq.style.opacity = 0.5
        divesq.onclick =vai_esquerda

        divmeio = html.DIV(style = STYLE)
        divmeio.style.width = 100
        divmeio.style.opacity = 0.3
        divmeio.style.left = 100
        divmeio.onclick =vai_meio

        tela <= cena
        tela <= divesq
        tela <= divdir
        tela <= divmeio
        return self


if __name__ == "__main__":
    lab = ofiuco()
    lab.centro.norte.vai()



def _():

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

    imar = "http://s21.postimg.org/x2vqvlr3b/La_Mar.jpg"
    ipraia="http://msalx.viajeaqui.abril.com.br/2012/09/21/1743/6IivB/praia.jpg?1348260191"

    itop = "http://www.acf-fr.org/i/07-12-06_mountain-top-4.jpg"
    imonte="https://lh4.googleusercontent.com/_wIBnV-jS0pk/TaWP5uBgrfI/AAAAAAAACHQ/1Ge1OPTckW0/montanha-huayna-picchu..jpg"

    iareia="http://s10.postimg.org/5pipdjp2x/singing_sand.jpg"
    ideserto="http://s16.postimg.org/k81hwi2n9/Desert.jpg"

    ipantano="http://s8.postimg.org/gu0olg8ol/prd_022431.jpg"
    imangue="http://s4.postimg.org/ez3co2sm5/Culbin_Salt_Marsh_geograph_org_uk_185128.jpg"
    sala_norte = Sala([imar,imar,ipraia,imar], NONE) #mar
    sala_leste = Sala([itop,itop,itop,imonte], NONE) #topo do monte
    sala_sul = Sala([irn, irl, irs, iro], NONE) #deserto
    sala_oeste = Sala([ipantano,imangue,ipantano,ipantano], NONE) #mangue
    salas = [sala_norte.norte, sala_leste.leste, sala_sul.sul, sala_oeste.oeste]
    #sala_centro = Sala([ipraia,imonte,ideserto,imangue], salas)
    sala_centro = Sala([imn, iml, ims,imo], salas)
    labirinto = Labirinto([
        sala_centro, sala_norte, sala_leste, sala_sul, sala_oeste])
    sala_centro.norte.vai()
    sala_norte.sul.meio = sala_centro.sul
    sala_leste.oeste.meio = sala_centro.oeste
    sala_sul.norte.meio = sala_centro.norte
    sala_oeste.leste.meio = sala_centro.leste


    ime = "http://www.fundospaisagens.com/1024x768/por-do-sol-romantico.jpg"
    imd = "http://amulherequemanda.sapo.pt/wp-content/uploads/2014/05/praia-paradisiaca.jpg"
    imm = "http://www2.mapfre.com.br/documents/10379/20599/img_floresta.jpg/09b57e22-9be8-42ec-ae5b-50e2739db043?t=1366044839000"

    NONE = [None] * 4
    imn = "http://www.decorandoimoveis.com/wp-content/gallery/sala-de-estar-simples-e-bonita/sala-de-estar-simples-e-bonita-1.jpg"
    iml = "http://cdn.limaonagua.com.br/wp-content/uploads/2014/08/sala-luxuosa-01.jpg"
    ims = "http://www.nossaweb.org/img/fotos/fotos%20de%20salas%20de%20tv%202.jpg"
    imo = "http://www.unimed.coop.br/portal/conteudo/materias/1340131044405hospital-maternidade.jpg"
    iro = "https://acidadecomoeuquero.files.wordpress.com/2011/03/rua_amauri.jpg"
    irl = "http://www.guia-se.com.br/painel/upload/fotos-clientes/7913/26103/varal%20giratorio.jpg"
    irn = "http://diariodorio.com/wp-content/uploads/2009/02/torredoriosulporalexandremicaelo.jpg"
    irs = "http://www.mylifevans.com.br/include/img/layout/locacao-de-onibus-em-sp.jpg"

    imar = "http://wallpaper.ultradownloads.com.br/277950_Papel-de-Parede-Estudio-de-Musica_1440x900.jpg"#som"http://s21.postimg.org/x2vqvlr3b/La_Mar.jpg"
    ipraia="http://img.ibxk.com.br/materias/3632/11553.jpg?w=1040"#teclado"http://msalx.viajeaqui.abril.com.br/2012/09/21/1743/6IivB/praia.jpg?1348260191"
    itop = "http://i.ytimg.com/vi/iYycdYZnXUI/maxresdefault.jpg"#bateria"http://www.acf-fr.org/i/07-12-06_mountain-top-4.jpg"
    imonte="http://images.comunidades.net/est/estudiodegravacaorj/nes.jpg"#guitar"https://lh4.googleusercontent.com/_wIBnV-jS0pk/TaWP5uBgrfI/AAAAAAAACHQ/1Ge1OPTckW0/montanha-huayna-picchu..jpg"
    iareia="http://img.olx.com.br/images/53/531506038999878.jpg"#caixasom"http://s10.postimg.org/5pipdjp2x/singing_sand.jpg"
    ideserto="http://www.sompurorj.com.br/imagens/microfone-estudio.jpg"#microfone"http://s16.postimg.org/k81hwi2n9/Desert.jpg"
    ipantano="http://spc.fotolog.com/photo/28/16/69/eternalcrossing/1267756962049_f.jpg"#espelho"http://s8.postimg.org/gu0olg8ol/prd_022431.jpg"
    imangue="http://www.audiorebel.com.br/imgs/home-foto-estudio.jpg"#entrada"http://s4.postimg.org/ez3co2sm5/Culbin_Salt_Marsh_geograph_org_uk_185128.jpg"

    sala_norte = Sala([imar,imar,ipraia,imar], NONE) #mar
    sala_leste = Sala([itop,itop,itop,imonte], NONE) #topo do monte
    sala_sul = Sala([irn.irl,irs,iro], NONE) #deserto
    sala_oeste = Sala([ipantano,imangue,ipantano,ipantano], NONE)
    salas = [sala_norte.norte, sala_leste.leste, sala_sul.sul, sala_oeste.oeste]
    #sala_centro = Sala([ipraia,imonte,ideserto,imangue], salas)
    sala_centro = Sala([imn, iml, ims, imo], salas)
    labirinto = Labirinto([
        sala_centro, sala_norte, sala_leste, sala_sul, sala_oeste])
    salas = [sala_norte.norte, sala_leste.leste, sala_sul.sul, sala_oeste.oeste]
    sala_centro.norte.vai()
    sala_norte.sul.meio = sala_centro.sul
    sala_leste.oeste.meio = sala_centro.oeste
    sala_sul.norte.meio = sala_centro.norte
    sala_oeste.leste.meio = sala_centro.leste


    praia.direita = mar
    praia.esquerda = sol
    praia.meio = floresta

    sol.esquerda = praia
    sol.direita = floresta
    sol.meio = mar

    floresta.direita = sol
    floresta.esquerda = praia
    floresta.meio = mar



class Cenaprincipal:
    def __init__(self):
        tela = document["pydiv"]
        tela.html = ""
        cenadiv = html.DIV()
        cenaimg = html.IMG(src = "http://tse2.mm.bing.net/th?id=JN.mL2JMVeyNhjkLB4Ml9eA2Q&pid=15.1&P=0&w=300&h=300", width= 300)
        tela <= cenadiv
        cenadiv <= cenaimg
        dialogdiv = html.DIV("O QUE FAZER AGORA?", id = "dialogdiv")
        cenadiv <= dialogdiv
        jp["dialogdiv"].dialog()

class Folha:
    def __init__(self, texto, html, tela, left):
        style = dict (position = "absolute", width=80, heigt=80, left=left, top=10,
        background = "yellow")
        fid = "folha%d" % left
        self.folha = html.DIV(texto, Id = fid, style=style, draggable = True)
        tela <= self.folha
        self.folha.ondragstart = self.drag_start
        self.folha.onmouseover = self.mouse_over

    def mouse_over(self, ev):
        ev.target.style.cursor = "point"

    def drag_start(self, ev):
        ev.data["text"]=ev.target.id
        ev.data.effectAllowed = "move"

class Suporte:
    def __init__(self, bloco, html, tela, left, certa):
        style = dict(position="absolute", width=80, heigt=80, left=left, top=110,
        background = "gray")
        self.folha = html.DIV(".......... ..........", style=style)
        self.left = left
        self.certa = certa
        tela <= self.folha
        self.folha.ondragover = self.drag_over
        self.folha.ondrop = self.drop
        self.bloco = bloco

    def drag_over(self, ev):
        ev.data.dropEffect = 'move'
        ev.preventDefault()

    def drop(self, ev):

        ev.preventDefault()
        src_id = ev.data['text']
        elt = document[src_id]
        elt.style.left = self.left
        elt.style.top = 100
        elt.draggable = False # don't drag any more
        elt.style.cursor = "auto"
        certa = True

        if src_id != self.certa:
            elt.style.background="red"
            certa = False
        self.bloco.conta_peça(certa)


class Bloco:
    def __init__(self):
        ordem = "10 410 310 210 110".split()
        texto = ""\
        "Não era uma vez\n"\
        "era sempre\n"\
        "sempre que\n"\
        "todo dia\n"\
        "era quase sempre\n"\
        "".split("\n")
        tela = document["pydiv"]
        tela.html = ""
        self.pecas_colocadas = []
        print(list(enumerate(ordem)))
        for pos, fl in enumerate(ordem):
            Suporte(self, html, tela, pos*100+10, "folha"+fl)
        for pos, tx in enumerate(texto):
            Folha(tx, html, tela, pos*100+10)

    def começo_de_novo(self):
        Bloco()

    def conta_peça(self, valor_peça):
        self.pecas_colocadas += [valor_peça]
        if len(self.pecas_colocadas) == 5:
            if all(self.pecas_colocadas):
                input("o texto está certo ")
                self.começo_de_novo()
            else:
                vai = input("tentar de novo?")
                if vai in "sim":
                    self.começo_de_novo()


def libra():
    Bloco()
    #Cenaprincipal()


if "men" in __name__:
    libra()
"""
