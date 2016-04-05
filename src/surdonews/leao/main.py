from jqueryui import jq
from browser import document, html
from superpython.virgem.main import Sala, Labirinto, Cena, INVENTARIO  # importando do virgem

STYLE = dict(position="absolute", width=300, left=0, top=0, background="blue")  # mudar cor do background lá embaixo
STYLE["min-height"] = "300px"
IMAGEM = "http://s16.postimg.org/k81hwi2n9/Desert.jpg"


class Leao:
    SETOR = None

    def __init__(self):
        pass

    def monta(self):
        NONE = [None] * 4
        imn = "https://upload.wikimedia.org/wikipedia/commons/1/1e/Est%C3%BAdio_-_TV_Cultura_Montenegro.jpg"
        iml = "http://mochilaotrips.com/wp-content/uploads/2013/03/IMG_1447.jpg"
        ims = "https://upload.wikimedia.org/wikipedia/commons/0/01/Morro_de_Castelo_Branco,_aspectos_1,_Castelo_Branco,_concelho_da_Horta,_ilha_do_Faial,_A%C3%A7ores,_Portugal.JPG"
        imo = "http://www.unicos.cc/wp-content/uploads/2014/12/jornalismo-1-951x476.jpg"
        irl = "http://www.vipcomm.com.br/site/upload/sbHulk_GN_150614026.jpg"
        iro = "https://blogpontodeonibus.files.wordpress.com/2013/02/photodownload-php.jpg"
        iro = "http://imagens.canaltech.com.br/38560.54878-Tirar-fotos.jpg"
        irn = "http://7diasverdes.com.br/wp-content/uploads/2013/07/Bicicleta-de-passeio.jpg"
        irs = "http://www.boulevardshopping.com.br/novo/wp-content/uploads/2012/02/Mcdonalds.jpg"
        isn = "http://www.comercialvidoto.com.br/site/wgc_media/photos/Banco-pe-de-Ferro-Tamandua.png"
        isl = "http://andif.com.br/imagens/noticias/Banco_Santander_mjg.jpg"
        iso = "http://imguol.com/2013/01/08/fiat-mille-economy-1357657820399_956x500.jpg"
        iss = "http://images.forwallpaper.com/files/images/a/a809/a809de18/32241/notepad.jpg"
        desk = "https://blogpontodeonibus.files.wordpress.com/2012/07/expresso_brasileirold_chassiscania_1.jpg"
        drawer = "http://s.glbimg.com/og/rg/f/original/2010/07/09/tiago606.jpg"
        imageM = ""

        sala_norte = Sala([isn, desk, iss, iso], NONE)  # mar
        sala_leste = Sala([isn, isl, iss, iso], NONE)  # mar
        sala_sul = Sala([irn, irl, irs, iro], NONE)  # deserto
        sala_oeste = Sala([isn, isl, iss, iso], NONE)  # mar
        salas = [sala_norte.norte, sala_leste.leste, sala_sul.sul, sala_oeste.oeste]
        sala_centro = Sala([imn, iml, ims, imo], salas)
        labirinto = Leao.SETOR = Labirinto([
            sala_centro, sala_norte, sala_leste, sala_sul, sala_oeste])

        labirinto.norte.leste.meio = Cena(img=imageM)

        labirinto.sul.sul.meio = Cena(vai=self.help)  # mudado
        labirinto.leste.sul.meio = Cena(vai=self.pega_invent)  # mudado
        labirinto = Cena(vai=self.objetivo)  # mudado

        return labirinto

    def nao_monta(self):
        pass

    def vai(self):
        labirinto = self.monta()
        self.monta = self.nao_monta
        labirinto.centro.norte.vai()
        return labirinto

    """def pega_card(self):
        riocard = "https://www.cartaoriocard.com.br/rcc/static/img/personal-1.png" #link da imagem
        flag = None
        def clicou(_):
            #hipótese de flag
            input("Você não está num meio de transporte.")
        if not "card" in INVENTARIO.inventario: #Se o Rio Card não estiver no inventário significa que ele pegou
            input("Você pegou o RioCard.")
            INVENTARIO.bota("card", riocard, clicou)
        else:
            input("Atenção: o inventário está vazio!")"""

    def pega_invent(self):
        riocard = "https://www.cartaoriocard.com.br/rcc/static/img/personal-1.png"  # link da imagem
        flag = None

        def clicou(_):
            # hipótese de flag
            input("Você não está num meio de transporte.")

        if not "card" in INVENTARIO.inventario:  # Se o Rio Card não estiver no inventário significa que ele pegou
            input("Você pegou o RioCard.")
            INVENTARIO.bota("card", riocard, clicou)
        else:
            input("Atenção: o inventário está vazio!")

    def help(self):
        ajuda = "http://icons.iconarchive.com/icons/oxygen-icons.org/oxygen/256/Actions-help-hint-icon.png"
        flag = None

        def clicou(_):
            # caso aconteça flag
            input("Você precisa ir na sala à leste do atendimento.")

        if not "ajuda" in INVENTARIO.inventario:
            input("Você quer saber sobre o meu relátorio sobre a gripe? Ele na escrivaninha na sala lesta à recepção.")
            INVENTARIO.bota("ajuda", ajuda, clicou)
        else:
            input("Achou o relatorio? Procurou na sala certa?")

    """
    def objetivo(self):
        ajuda = "http://www.iconsdownload.net/icons/256/11335-target-icon.png"
        flag = None
        def clicou(_):
            input("Objetivo do programa: Você é um repórter e precisa achar o relatório com o resumo de todas as matérias que você vai conquistar nos diversos lugares do labirinto.")
        """


INSTANCIA = None


def leao():
    def cria_leao():
        global INSTANCIA
        INSTANCIA = Leao()

    if not INSTANCIA:
        cria_leao()
    return INSTANCIA


if __name__ == "__main__":
    change_bg = "Para qual cor você quer mudar o plano de fundo? azul/branco"
    escolha = input(change_bg)
    if escolha == "azul":
        background = "blue"

    lab = leao()
    print(INSTANCIA)
    INVENTARIO.inicia()
    lab.vai()

    # lab.centro.norte.vai()
    # lab.sul.oeste.meio = metro.centro.norte
