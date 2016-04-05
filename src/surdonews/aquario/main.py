from browser import document, html

STYLE = dict(position="absolute", width=300, left=0, top=0,
             background="white")
STYLE["min-height"] = "300px"
IMAGEM = "http://www.susanasteil.com.br/wp-content/uploads/2012/09/mar.jpg"


class Labirinto:
    def __init__(self, salas):
        self.salas = salas
        self.centro, self.norte, self.leste, self.sul, self.oeste = self.salas
        for indice, sala in enumerate(self.salas[1:]):
            self.centro.cenas[indice].meio = sala.cenas[indice]
            indice_oposto = (indice + 2) % 4
            sala.cenas[indice_oposto].meio = self.centro.cenas[indice_oposto]


class Sala:
    def __init__(self, imagensnlso, saidasnlso):
        self.cenas = []
        for img in imagensnlso:
            self.cenas.append(Parede(img))
        self.norte, self.leste, self.sul, self.oeste = self.cenas
        for cena, saida in enumerate(saidasnlso):
            self.cenas[cena].meio = saida
        for esquerda in range(4):
            cena_a_direita = (esquerda + 1) % 4
            self.cenas[esquerda].direita = self.cenas[cena_a_direita]
            self.cenas[cena_a_direita].esquerda = self.cenas[esquerda]


class Parede:
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


class Aquario:
    SETOR = None

    def __init__(self):
        pass

    def monta(self):
        NONE = [None] * 4
        imn = "http://caxias.ma.gov.br/uploads/images/sa%C3%BAde/ubs_cohab_interno.jpg"
        iml = "http://www.saudepalhoca.sc.gov.br/img/posto-saude/05b5e390a01cebd29445cb1e1cfa7f60.jpg"
        ims = "http://c1.staticflickr.com/5/4053/4330022675_156b6fa1cd_z.jpg?zz=1"
        imo = "http://www.rochaerangelcmp.com.br/posto.gif"
        irn = "http://www.rio.rj.gov.br/igstatic/15/60/45/1560456.jpg"
        irl = "https://pixabay.com/static/uploads/photo/2012/02/23/10/42/skyscraper-16045_640.jpg"
        irs = "https://bhemciclo.files.wordpress.com/2012/11/53610_414615851939059_151834020_o.jpg"
        iro = "http://s2.glbimg.com/O78MjRK8uw8N0w8AFnFT-_yWRLQ=/s.glbimg.com/jo/g1/f/original/2013/12/14/metro620.jpg"
        ipraia = "http://amulherequemanda.sapo.pt/wp-content/uploads/2014/05/praia-paradisiaca.jpg"
        iflor = "https://encrypted-tbn3.gstatic.com/images?q=tbn:ANd9GcQuGiy6IP1xVD5EnsvZfUcrkTkTSknqcr7l8egbgszaKZzd0FkfCg"
        iarvore = "http://41.media.tumblr.com/tumblr_lyyp66z5eY1r82vfco1_500.jpg"
        imontanha = "https://encrypted-tbn3.gstatic.com/images?q=tbn:ANd9GcTyYJKtj3VFOn6R1akD30Ji4a9hpmk2gPIz5BnGTjrST3Fq0JPN"
        itorre = "http://3.bp.blogspot.com/-3YXtTltGRkI/U_DMA_2tMwI/AAAAAAAAAQY/LRhnLMvb5_o/s1600/paris%2B2.png"
        isol = "http://www.fundospaisagens.com/1024x768/por-do-sol-romantico.jpg"
        iceu = "http://41.media.tumblr.com/tumblr_malkhoQDaT1qfx4e6o1_500.jpg"
        ilua = "https://40.media.tumblr.com/1d729febda949bb81a84d0f6cd5207b5/tumblr_mk1fmejJKf1s8khtjo1_500.png"
        sala_norte = Sala([ipraia, ipraia, iflor, ipraia], NONE)  # mar
        sala_leste = Sala([iarvore, iarvore, iarvore, imontanha], NONE)  # mar
        sala_sul = Sala([irn, irl, irs, iro], NONE)  # deserto
        sala_oeste = Sala([ilua, iceu, iceu, iceu], NONE)  # mar
        salas = [sala_norte.norte, sala_leste.leste, sala_sul.sul, sala_oeste.oeste]
        # sala_centro = Sala([ipraia,imonte,ideserto,imangue], salas)
        sala_centro = Sala([imn, iml, ims, imo], salas)
        labirinto = Aquario.SETOR = Labirinto([
            sala_centro, sala_norte, sala_leste, sala_sul, sala_oeste])
        from superpython.leao.main import leao
        from superpython.ofiuco.main import ofiuco
        labirinto.sul.leste.meio = leao()
        labirinto.sul.sul.meio = ofiuco()
        # self.inventario = Inventario()
        return labirinto

    def nao_monta(self):
        pass

    def vai(self):
        labirinto = self.monta()
        self.monta = self.nao_monta
        labirinto.centro.norte.vai()
        return labirinto


class Inventario:
    def __init__(self, tela=document["pydiv"]):
        self.inventario = {}
        self.opacity = 0
        self.style = dict(STYLE)
        self.style["min-height"] = "30px"
        self.bolsa = html.DIV(Id="__inv__", style=self.style)
        self.bolsa.onclick = self.mostra
        self.limbo = html.DIV(style=self.style)
        self.limbo.style.left = "4000px"
        tela <= self.bolsa

    def mostra(self):
        self.opacity = abs(self.opacity - 1.0)
        self.bolsa.style.display = self.opacity

    def bota(self, nome_item, item, acao):
        item_img = html.IMG(Id=nome_item, src=item, width=30, style=self.style)
        item_img.onclick = acao
        self.inventario[item] = acao
        self.bolsa <= item_img

    def tira(self, nome_item):
        item_img = document[nome_item]
        self.inventario.pop(nome_item, None)
        self.limbo <= item_img


INSTANCIA = None


def aquario():
    def cria_aquario():
        global INSTANCIA
        INSTANCIA = Aquario()

    if not INSTANCIA:
        cria_aquario()
    return INSTANCIA


if __name__ == "__main__":
    lab = aquario()
    print (INSTANCIA)
    # lab.centro.norte.vai()
    lab.vai()
