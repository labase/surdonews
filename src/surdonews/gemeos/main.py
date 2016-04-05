from browser import document, html

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
            indice_oposto = (indice + 2) % 4
            sala.cenas[indice_oposto].meio = self.centro.cenas[indice_oposto]


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


class Gemeos:
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
        sala_norte = Sala([isn, desk, iss, iso], NONE)  # mar
        sala_leste = Sala([isn, isl, iss, iso], NONE)  # mar
        sala_sul = Sala([irn, irl, irs, iro], NONE)  # deserto
        sala_oeste = Sala([isn, isl, iss, iso], NONE)  # mar
        salas = [sala_norte.norte, sala_leste.leste, sala_sul.sul, sala_oeste.oeste]
        sala_centro = Sala([imn, iml, ims, imo], salas)
        labirinto = Gemeos.SETOR = Labirinto([
            sala_centro, sala_norte, sala_leste, sala_sul, sala_oeste])

        # metro = sargitario()
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
        self.monta = self.nao_monta()
        labirinto.centro.norte.vai()
        return labirinto


instancia = None


def gemeos_criado():
    return instancia


def gemeos():
    def cria_gemeos():
        global instancia
        instancia = Gemeos()

    if not instancia:
        cria_gemeos()
    return instancia


if __name__ == "__main__":
    lab = gemeos()
    print(instancia)
    lab.vai()
