# -*- coding: utf-8 -*-
# from jqueryui import jq
from browser import document, html, alert
from superpython.virgem.main import Sala, Labirinto, Cena, INVENTARIO

STYLE = dict(position="absolute", width=300, left=0, top=0, background="white")
STYLE["min-height"] = "300px"
IMAGEM = ""
alert


class Touro:
    Setor = None

    def __init__(self):
        pass

    def monta(self):
        NONE = [None] * 4
        # IMAGENS
        imn = "http://redecomsc.com.br/portal/admin/webroot/upload/noticias039fc0a46045ea0cd70a028876fe6cc1.jpg"  # corredor
        iml = "http://www.cruzeirodosul.pr.gov.br/Conferencia_Cruzeiro/farmacia/Imagem%20004.jpg"  # office 2 sala
        ims = "http://www.marica.rj.gov.br/noticias/fotos/2837/dscf4862_sala_de_espera_10_04_2013_fernando_silva.jpg"  # sala espera
        imo = "http://www.araripina.pe.gov.br/wp-content/gallery/esf-do-distrito-do-morais-conta-agora-com-excelencia-em-estrutura-e-atendimento/saude5.jpg"  # sala
        irl = "http://www.franca.sp.gov.br/portal/images/phocagallery/galeria-educacao/uab/img_uab01.jpg"  # sala
        iro = "http://www.fortaleza.ce.gov.br/sites/default/files/styles/390x255/public/noticias/imagem-principal/posto_de_saude_santa_liduina_regional_iii_-_pq_araxa.jpg?itok=jsA7B18B"  # sala
        iro = "http://www.saudepalhoca.sc.gov.br/img/posto-saude/f986160b46a5e935d2356fa94e912ff5.jpg"  # sala
        irn = "http://www.santamaria.rs.gov.br/midia/2012/03/F03-9636.jpg"  # sala(rua)
        irs = "http://rduirapuru.com.br/img/not_201404021739974880_gg.jpg"  # dica aqui
        isn = "https://upload.wikimedia.org/wikipedia/commons/7/79/Rua_Haddock_Lobo.JPG"  # 1
        isl = "http://www.acessibilidadenapratica.com.br/wp-content/uploads/2011/12/DSCN3362.jpg"  # onibus
        iso = "https://upload.wikimedia.org/wikipedia/commons/4/49/Metro_Rio_01_2013_5419.JPG"  # metro
        iss = "http://www.rochaerangelcmp.com.br/posto.gif"  # posto de saude(entrada)
        leitor = "http://netdiario.com.br/wp-content/uploads/2015/08/zseguranca_onibus3-AO.jpg"  # leitor onibus
        sala = "http://joaquimdepaula.com.br/wp-content/uploads/2012/06/posto_de_saude_-01.jpg"  # sala 1
        salaa = "http://www.saudepalhoca.sc.gov.br/img/posto-saude/a70e330121fc5662f23c683de45e2082.jpg"
        salac = "http://1.bp.blogspot.com/-ki2Zx2R_NWE/U7Au950QCBI/AAAAAAAAPG8/Yt7zxHBg7jQ/s1600/10460112_460037514131957_6040610582016373465_n.jpg"
        salab = "http://www2.maringa.pr.gov.br/sistema/imagens/gd_fb46f5574fb2.jpg"
        escriv = "http://www.coqueirobaixo.com.br/imagens/conteudos/00306_g.jpg"  # sala do médico (relatorio aqui)
        sala_medico = "http://www.araripina.pe.gov.br/wp-content/gallery/esf-do-distrito-do-morais-conta-agora-com-excelencia-em-estrutura-e-atendimento/saude5.jpg"

        # SALAS
        sala_norte = Sala([isn, isl, iss, iso], NONE)  # rua
        sala_leste = Sala([salac, sala, escriv, salab], NONE)  # pegar relat
        sala_sul = Sala([irn, irl, irs, iro], NONE)  # rua
        sala_oeste = Sala([salaa, salab, salac, sala], NONE)  # mangue
        salas = [sala_norte.norte, sala_leste.leste, sala_sul.sul, sala_oeste.oeste]
        sala_centro = Sala([imn, iml, ims, imo], salas)
        labirinto = Touro.Setor = Labirinto([sala_centro, sala_norte, sala_leste, sala_sul, sala_oeste])
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

    # Ao encontrar o relatório
    def pega_relat(self):
        relat = "http://www.ufjf.br/sri-sou-servidor-ufjf/files/2014/04/Very-Basic-Document-icon.jpg"
        flag = None

        def clicou(_):
            # Mostra o texto do relatório ao clicar no icone
            alert(
                "O SUS e o Ministério da Saúde promovem a Campanha Nacional de Vacinação contra a Gripe, que começa no dia 4 e vai até o dia 22 de maio " \
                "como o dia de mobilização nacional. Trabalhadores da área de saúde, presos e funcionários do sistema prisional também serão vacinados contra o vírus. ")

        if not "relat" in INVENTARIO.inventario:
            alert("Boa tarde. Sim, você quer o meu relatório.\nBom, aqui está.")
            alert("Você pegou o relatório!")
            # Inclui o relatório ao inventário e retira a dica
            INVENTARIO.bota("relat", relat, clicou)
            if "hint" in INVENTARIO.inventario:
                INVENTARIO.tira("hint")
        else:
            input("Você já pegou o meu relatório.\nTenha um bom dia.")

            # Ao encontrar ajuda

    def ajuda(self):
        hint = "http://icons.iconarchive.com/icons/oxygen-icons.org/oxygen/256/Actions-help-hint-icon.png"
        flag = None

        # Ao clicar na dica
        def clicou(_):
            alert("Procure a sala do médico.\nO relatório está com ele.")

        # Se a dica não está no inventário
        if not "hint" in INVENTARIO.inventario:
            alert("Você quer saber o período de vacinação?\nEle está com o médico em sua sala.")
            INVENTARIO.bota("hint", hint, clicou)
        # Se ela estiver
        else:
            alert("Achou o relatorio? Não?\nVocê procurou na sala certa?")


INSTANCIA = None


# Começo
def touro():
    def cria_touro():
        global INSTANCIA
        INSTANCIA = Touro()

    if not INSTANCIA:
        cria_touro()
    return INSTANCIA


# Inicio
if __name__ == "__main__":
    lab = touro()
    print(INSTANCIA)
    lab.vai()
