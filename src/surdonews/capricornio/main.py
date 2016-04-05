from browser import document, html

STYLE = dict(position="absolute", width=300, left=0, top=0,
             background="white")
STYLE["min-height"] = "300px"
IMAGEM = "http://www.susanasteil.com.br/wp-content/uploads/2012/09/mar.jpg"


class Labirinto:
    def __init__(self, salas):
        self.salas = salas
        self.centro, self.norte, self.leste, self.sul, self.oeste = self.salas
        for indice, sala in enumerate(self.salas[1:]):  # excluindo centro
            self.centro.cenas[indice].meio = sala.cenas[indice]
            sala.cenas[(indice + 2) % 4].meio = self.centro.cenas[indice]


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


def capricornio():
    NONE = [None] * 4
    imgnorte = "http://www.medeirosneto.com/uploads/imagens/DSC04835.JPG"
    imgleste = "http://oc-cerqueira.zip.net/images/praca.JPG"
    imgsul = "http://polorealestate.com.br/institucional/Handler/ImagemDB.ashx?m=Prop&w=600&h=500&i=105"
    imgoeste = "http://cartilhapacienterenal.cursoseconcursosnosite.com.br/wp-content/uploads/2012/01/SOS-urg-e-emerg..jpg"
    irnorte = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRDEanD8KxPRBrIlWLLUQsNcAnXTq3jyNXzOy7TmoV9NpsbCH_L"
    irsul = "https://encrypted-tbn3.gstatic.com/images?q=tbn:ANd9GcQjlN218gf57IcN4lrmqxIpon9JBYoWOIuWaJ8zFDcWltl7vPWtcw"
    iroeste = "http://www.ebc.com.br/sites/_portalebc2014/files/atoms_image/banco_do_brasil.jpg"
    irleste = "http://portaldoleblon.com.br/wp-content/uploads/2012/07/Metro-Azul.jpg"
    isn = "http://www.medeirosneto.com/uploads/imagens/DSC04835.JPG"
    isl = "http://oc-cerqueira.zip.net/images/praca.JPG"
    iso = "http://polorealestate.com.br/institucional/Handler/ImagemDB.ashx?m=Prop&w=600&h=500&i=105"
    iss = "http://cartilhapacienterenal.cursoseconcursosnosite.com.br/wp-content/uploads/2012/01/SOS-urg-e-emerg..jpg"

    sala_norte = Sala([isn, isl, iss, iso], NONE)  # praia
    sala_leste = Sala([isn, isl, iss, iso], NONE)  # praia
    sala_sul = Sala([irn, irl, irs, iro], NONE)  # torre
    sala_oeste = Sala([irn, irl, irs, iro], NONE)  # praia
    salas = [sala_norte.norte, sala_leste.leste, sala_sul.sul, sala_oeste.oeste]
    # sala_centro = Sala([imar, imontanha, iceu, ilua], salas)
    sala_centro = Sala([imn, iml, ims, imo], salas)
    labirinto = Labirinto([sala_centro, sala_norte, sala_sul, sala_oeste, sala_leste])
    salas = [sala_norte.norte, sala_leste.leste, sala_sul.sul, sala_oeste.oeste]


    return labirinto

if __name__ == "__main__":
    lab = capricornio()
    lab.centro.norte.vai()


def __():
    NONE = [None] * 4
    imgcentro = "http://www.saude.rs.gov.br/upload/HD_201204021427356892823544_3f78461006.jpg"

    imn = "http://www.medeirosneto.com/uploads/imagens/DSC04835.JPG"
    iml = "http://oc-cerqueira.zip.net/images/praca.JPG"
    ims = "http://polorealestate.com.br/institucional/Handler/ImagemDB.ashx?m=Prop&w=600&h=500&i=105"
    imo = "http://cartilhapacienterenal.cursoseconcursosnosite.com.br/wp-content/uploads/2012/01/SOS-urg-e-emerg..jpg"

    ir = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRDEanD8KxPRBrIlWLLUQsNcAnXTq3jyNXzOy7TmoV9NpsbCH_L"
    irs = "https://encrypted-tbn3.gstatic.com/images?q=tbn:ANd9GcQjlN218gf57IcN4lrmqxIpon9JBYoWOIuWaJ8zFDcWltl7vPWtcw"
    iro = "http://www.ebc.com.br/sites/_portalebc2014/files/atoms_image/banco_do_brasil.jpg"
    irl = "http://portaldoleblon.com.br/wp-content/uploads/2012/07/Metro-Azul.jpg"

    ipraia = "http://amulherequemanda.sapo.pt/wp-content/uploads/2014/05/praia-paradisiaca.jpg"
    imar = "https://encrypted-tbn1.gstatic.com/images?q=tbn:ANd9GcTWlZSc8fjE0XmAbyHb8d3DX9rH1Hr19d77O8NtO4zf4yumrUbcg-HfeSE"

    isol = "http://www.fundospaisagens.com/1024x768/por-do-sol-romantico.jpg"
    ilua = "https://40.media.tumblr.com/1d729febda949bb81a84d0f6cd5207b5/tumblr_mk1fmejJKf1s8khtjo1_500.png"

    iarvore = "http://41.media.tumblr.com/tumblr_lyyp66z5eY1r82vfco1_500.jpg"
    imontanha = "https://encrypted-tbn3.gstatic.com/images?q=tbn:ANd9GcTyYJKtj3VFOn6R1akD30Ji4a9hpmk2gPIz5BnGTjrST3Fq0JPN"

    itorre = "http://3.bp.blogspot.com/-3YXtTltGRkI/U_DMA_2tMwI/AAAAAAAAAQY/LRhnLMvb5_o/s1600/paris%2B2.png"
    iceu = "http://41.media.tumblr.com/tumblr_malkhoQDaT1qfx4e6o1_500.jpg"

    sala_norte = Sala([ipraia, ipraia, imar, ipraia], NONE)  # praia
    sala_leste = Sala([iarvore, iarvore, iarvore, imontanha], NONE)  # arvore
    sala_sul = Sala([itorre, iceu, itorre, itorre], NONE)  # torre
    sala_oeste = Sala([ilua, isol, isol, isol], NONE)  # ceu
    salas = [sala_norte.norte, sala_leste.leste, sala_sul.sul, sala_oeste.oeste]
    labirinto = Labirinto([sala_centro, sala_norte, sala_sul, sala_oeste, sala_leste])

    sala_centro.norte.vai()
    sala_norte.sul.meio = sala_centro.sul
    sala_leste.oeste.meio = sala_centro.oeste
    sala_sul.norte.meio = sala_centro.norte
    sala_oeste.leste.meio = sala_centro.leste
    """
from browser import document, html

STYLE = dict(position="absolute", width=300, left=0, top=0,
background="white")
STYLE["min-height"]="300px"
IMAGEM = "http://s16.postimg.org/k81hwi2n9/Desert.jpg"
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

if __name__ == "__main__":
    NONE = [None] * 4
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
    sala_sul = Sala([ideserto,iareia,iareia,iareia], NONE) #deserto
    sala_oeste = Sala([ipantano,imangue,ipantano,ipantano], NONE)
    salas = [sala_norte.norte, sala_leste.leste, sala_sul.sul, sala_oeste.oeste]
    sala_centro = Sala([ipraia,imonte,ideserto,imangue], salas)
    sala_centro.norte.vai()
    sala_norte.sul.meio = sala_centro.sul
    sala_leste.oeste.meio = sala_centro.oeste
    sala_sul.norte.meio = sala_centro.norte
    sala_oeste.leste.meio = sala_centro.leste
    """
