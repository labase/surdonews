# -*- coding: utf-8 -*-
from jqueryui import jq
from browser import document, html
from superpython.virgem.main import Sala, Labirinto, Cena, INVENTARIO

STYLE = dict(position="absolute", width=300, left=0, top=0, background="white")
STYLE["min-height"] = "300px"
# 29.09
IMAGEM = "http://images.akamai.steamusercontent.com/ugc/577886316482675420/F077A67B1EC421E7980FEDA9C89CE4CA2180A8B0/"


class Sagitario:
    Setor = None

    def __init__(self):
        pass

    def monta(self):
        NONE = [None] * 4
        imn = "http://www.segurancamonitoramento.org/wp-content/uploads/2013/05/seguranca-portaria-condominios.jpg"  # atendimento
        iml = "https://upload.wikimedia.org/wikipedia/commons/0/0d/Sala_de_aula_CB_Unicamp.jpg"  # office 2
        ims = "https://c1.staticflickr.com/9/8493/8405249485_373350aca6.jpg"  # corredor
        imo = "http://www.ff.ul.pt/wp-content/uploads/2013/05/auditorio.jpg"  # office 3
        irl = "http://www.franca.sp.gov.br/portal/images/phocagallery/galeria-educacao/uab/img_uab01.jpg"  # rua 1
        iro = "http://blog.fct.unesp.br/blog/wp-content/uploads/2014/10/yu1.jpg"  # rua 2
        iro = "http://revistasuacasa.arq.br/sc/wp-content/uploads/2013/08/520a6d4dc2959.jpeg"  # estação metro
        irn = "http://www.descubraja.com/wp-content/uploads/2013/12/imagens-de-porta-de-madeira-branca.jpg"  # rua 3
        irs = "http://www.utfpr.edu.br/pontagrossa/estrutura-universitaria/diretorias/dirgrad/daens/coordenacoes/cafis/fotos/sala-dos-professores/image_preview"  # bus
        isn = "https://upload.wikimedia.org/wikipedia/commons/7/79/Rua_Haddock_Lobo.JPG"  # 1
        isl = "http://www.acessibilidadenapratica.com.br/wp-content/uploads/2011/12/DSCN3362.jpg"  # 2
        iso = "https://upload.wikimedia.org/wikipedia/commons/4/49/Metro_Rio_01_2013_5419.JPG"  # 3
        iss = "http://www.ebc.com.br/sites/_portalebc2014/files/styles/full_colunm/public/atoms_image/ifcs_ufrj_060109_wikimapa_0.jpg?itok=tUTsWT4v"
        leitor = "http://netdiario.com.br/wp-content/uploads/2015/08/zseguranca_onibus3-AO.jpg"
        sala = "http://cse.ufsc.br/files/2011/04/10.jpg"
        salaa = "http://www.digitalw.com.br/fotos/lousa-digital-smart-600-1.jpg"
        salac = "http://www.eteabs.com.br/tpl/img/portfolio/full/sala-aula.jpg"
        salab = "http://vitoriaempreendimentos.com.br/wp-content/uploads/2011/03/947_2848.jpg"
        escriv = "http://mlb-s2-p.mlstatic.com/mesa-escrivaninha-para-escritorio-4-gavetas-frente-de-vidro-6833-MLB5114582286_092013-F.jpg"

        sala_norte = Sala([isn, isl, iss, iso], NONE)  # rua
        sala_leste = Sala([salac, sala, escriv, salab], NONE)  # pegar relat
        sala_sul = Sala([irn, irl, irs, iro], NONE)  # rua
        sala_oeste = Sala([salaa, salab, salac, sala], NONE)  # mangue
        salas = [sala_norte.norte, sala_leste.leste, sala_sul.sul, sala_oeste.oeste]
        sala_centro = Sala([imn, iml, ims, imo], salas)
        labirinto = Sagitario.Setor = Labirinto([
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

    def pega_relat(self):
        relat = "http://www.ufjf.br/sri-sou-servidor-ufjf/files/2014/04/Very-Basic-Document-icon.jpg"
        flag = None

        def clicou(_):
            # flag apos hint
            input(
                "O caráter altamente mutante da estrutura externa do vírus se deve à própria resposta imune que o organismo dá a esses micro-organismos. " \
                "Quando um corpo estranho invade o organismo, é na parte externa que ocorre o primeiro contato. É nela que o sistema de defesa se baseia para produzir anticorpos." \
                "Da mesma forma que a parede viral é tão difícil de atingir, quando um medicamento consegue danificá-la o resultado é altamente prejudicial à doença. A hemaglutinina tem um papel fundamental na incorporação do vírus à célula." \
                "Assim, se você consegue atingir essa estrutura, barra-se a contaminação de mais células, completa." \
                "Sem capacidade de viver e se reproduzir fora do núcleo celular, os vírus acabam derrotados." \
                "Apesar de ser mais frequente em aves e mamíferos de pequeno porte, como os suínos, a Influenza A é altamente mortífera ao homem exatamente por não ser conhecida do organismo humano." \
                "Quando ocorre uma mutação em um gene, por mais que ele não consiga combater totalmente o vírus, ele consegue enfraquecê-lo," \
                "dependendo do nível de mutação que sofreu. No entanto, quando ocorre uma grande mutação, ao ponto de o vírus que vive em uma ave conseguir se estabelecer em um humano, as consequências são bem mais graves." \
                "O corpo humano não tem memória imunológica alguma de vírus vindos de animais. Por isso, quando o vírus da gripe espanhola atingiu o ser humano, foi tão letal. Essa gripe veio de uma variante do H1N1 que inicialmente infectava porcos." \
                "O mesmo vale para a gripe aviária, que veio de outra variante do H1N1, que infectava frangos. Mas A vacina é segura e raramente causa reações, que podem ser dor e vermelhidão local.")

        if not "relat" in INVENTARIO.inventario:
            input("Você pegou o relatorio.")
            INVENTARIO.bota("relat", relat, clicou)

        else:
            input("A escrivaninha está vazia")

    def ajuda(self):
        hint = "http://icons.iconarchive.com/icons/oxygen-icons.org/oxygen/256/Actions-help-hint-icon.png"
        flag = None

        def clicou(_):
            # caso aconteça flag
            input("Você precisa ir na sala à leste do atendimento.")

        if not "hint" in INVENTARIO.inventario:
            input("Você quer saber sobre o meu relátorio sobre a gripe? Ele na escrivaninha na sala lesta à recepção.")
            INVENTARIO.bota("hint", hint, clicou)
        else:
            input("Achou o relatorio? Procurou na sala certa?")


INSTANCIA = None


def sagitario():
    def cria_sagitario():
        global INSTANCIA
        INSTANCIA = Sagitario()

    if not INSTANCIA:
        cria_sagitario()
    return INSTANCIA


if __name__ == "__main__":
    lab = sagitario()
    print(INSTANCIA)
    lab.vai()

"""
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
"""
