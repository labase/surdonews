# -*- coding: utf-8 -*-
from jqueryui import jq
from browser import document, html
from superpython.peixes.main import Sala, Labirinto, Cena, INVENTARIO

STYLE = dict(position="absolute", width=300, left=0, top=0, background="white")
STYLE["min-height"] = "300px"
# 29.09
IMAGEM = "http://images.akamai.steamusercontent.com/ugc/577886316482675420/F077A67B1EC421E7980FEDA9C89CE4CA2180A8B0/"


class Peixes:
    Setor = None

    def __init__(self):
        pass

    def monta(self):
        NONE = [None] * 4
        imn = "http://www.riodasostras.rj.gov.br/img/n273.jpg"
        iml = "http://www.cpt.com.br/imagens/cursos-profissionalizantes/cabecalho/operador-de-telemarketing.jpg"
        ims = "http://s2.glbimg.com/vSsk3wIWZbcNx584AksmPAjZnFI=/620x465/s.glbimg.com/jo/g1/f/original/2015/02/03/pombo-arquivo_pessoal.jpg"
        imo = "http://www.ff.ul.pt/wp-content/uploads/2013/05/auditorio.jpg"
        irl = "http://observatoriofeminino.blog.br/wp-content/uploads/2013/10/Rua_Vinicius_de_Moraes_-_Ipanema_-_Rio_de_Janeiro.jpg"
        iro = "http://static1.squarespace.com/static/517e9335e4b0847823500845/t/5236fdd9e4b05de551a592e9/1379335642541/rua-francisco-otaviano.jpg?format=750w"
        iro = "https://upload.wikimedia.org/wikipedia/commons/4/49/Metro_Rio_01_2013_5419.JPG"
        irn = "https://encrypted-tbn3.gstatic.com/images?q=tbn:ANd9GcTvXYdmpQr7QIcfcrj4ANLTkASP7CPg3g5L-_-ReSKq10vEJQCX"
        irs = "https://inbustransportonibus.files.wordpress.com/2013/01/dscn2792.jpg"
        isn = "http://caxias.ma.gov.br/uploads/images/sa%C3%BAde/ubs_cohab_interno.jpg"
        isl = "http://www.guiasaoroque.com.br/useruploads/images/marco_2010/sjn_160310.jpg"
        iso = "http://www.portaldecampomaior.com.br/novo/wp-content/uploads/2012/06/DSC_00082.jpg"
        iss = "http://1.bp.blogspot.com/-mhLXXZWJy_o/VHZCx8jS6PI/AAAAAAAAE04/ctFquFHyGjc/s1600/_BEA4382.JPG"
        escritorio1 = "http://www.solinemoveis.com.br/wp-content/themes/soline/images/pp-moveis-para-escritorio-1.jpg"
        escritorio2 = "http://static.wixstatic.com/media/55942c_5c76a65d3ec1446f98a2785cd7113126.jpg"
        escritorio3 = "http://img.edilportale.com/products/prodotti-57140-rele634f624-76c4-4c2a-a631-d80a7d28c93e.jpg"
        escritorio4 = "https://encrypted-tbn3.gstatic.com/images?q=tbn:ANd9GcQ2juSbPu4_SHT77NGzzf3uFw98WjjeixANDTFfPhvEgRiTzuZ2"
        cofre = "http://www.supracil.com.br/fotos/04c007dbd5.jpg"

        sala_norte = Sala([isn, isl, iss, iso], NONE)
        sala_leste = Sala([salac, sala, escriv, salab], NONE)
        sala_sul = Sala([irn, irl, irs, iro], NONE)
        sala_oeste = Sala([salaa, salab, salac, sala], NONE)
        salas = [sala_norte.norte, sala_leste.leste, sala_sul.sul, sala_oeste.oeste]
        sala_centro = Sala([imn, iml, ims, imo], salas)
        labirinto = Peixes.Setor = Labirinto([
            sala_centro, sala_norte, sala_leste, sala_sul, sala_oeste])

        labirinto.norte.leste.meio = Cena(img=leitor)

        labirinto.sul.sul.meio = Cena(vai=self.ajuda)
        labirinto.leste.sul.meio = Cena(vai=self.pega_relat)

        return labirinto

    def nao_monta(self):
        pass

    def vai(self):
        labirinto = self.monta()
        self.monta = self.nao_monta
        labirinto.centro.norte.vai()
        return labirinto

    def pega_autoriza(self):
        autoriza = "http://www.ufjf.br/sri-sou-servidor-ufjf/files/2014/04/Very-Basic-Document-icon.jpg"
        flag = None

        def clicou(_):
            input("“Os postos de saúde funcionam de segunda a sexta-feira, das 8h às 17h./"
                  "No próximo sábado, dia 9, as unidades de vacinação também ficarão abertas, no mesmo horário, por conta do Dia Nacional de Mobilização conta a Gripe”")

        if not "relat" in INVENTARIO.inventario:
            input("Você pegou a autorização.")
            INVENTARIO.bota("relat", relat, clicou)
        else:
            input("Procure a autoriação no cofre")

    def ajuda(self):
        hint = "http://icons.iconarchive.com/icons/oxygen-icons.org/oxygen/256/Actions-help-hint-icon.png"
        flag = None

        def clicou(_):
            # caso aconteça flag
            input("Você precisa ir na sala à leste do atendimento.")

        if not "card" in INVENTARIO.inventario:
            input("Meu relatorio está na sala à leste do atendimento.")
            INVENTARIO.bota("hint", hint, clicou)
        else:
            input("Achou a autorização?")


INSTANCIA = None


def Peixes():
    def cria_peixes():
        global INSTANCIA
        INSTANCIA = Peixes()

    if not INSTANCIA:
        cria_peixes()
    return INSTANCIA


if __name__ == "__main__":
    lab = Peixes()
    print(INSTANCIA)
    INVENTARIO.inicia()
    lab.vai()
    # lab.centro.norte.vai()
    # lab.sul.oeste.meio = metro.centro.norte
