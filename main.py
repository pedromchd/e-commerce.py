import os

from lib.estoque import Estoque
from lib.graphics import *

WIDTH, HEIGHT = 640, 480

X1, Y1, X2, Y2 = 0, 0, 100, 100

C_ROXO = "#521580"  # Roxo
C_ROXO_ESCURO = "#20062a"  # Roxo escuro
C_VERMELHO = "#df0c40"  # Vermelho
C_VERMELHO_ESCURO = "#9c8dfb"  # Vermelho escuro
C_VERDE = "#4CAF50"  # Verde
C_VERDE_ESCURO = "#388E3C"  # Verde escuro
C_LAVANDA = "#c29efb"  # Lavanda

ESTOQUE = os.path.join(os.getcwd(), "data", "estoque.csv")


def main():
    win = GraphWin("Auto-commerce: Peças de Carro e Artigos Esportivos", WIDTH, HEIGHT)
    win.setCoords(X1, Y1, X2, Y2)

    center_window(win)

    bg_img = os.path.join(os.getcwd(), "img", "bg", "1.png")
    draw_image(win, bg_img, 50, 50)

    draw_text(win, 50, 75, "Auto-commerce", 24, "bold", "white")

    botoes = [
        {"xywh": (50, 40, 40, 10), "text": "Gerenciar Estoque"},
        {"xywh": (50, 25, 40, 10), "text": "Realizar Compras"},
        {"xywh": (50, 10, 40, 10), "text": "Sair"},
    ]

    for botao in botoes:
        x, y, w, h = botao["xywh"]
        draw_button(win, x, y, w, h, botao["text"], C_ROXO, C_ROXO_ESCURO)

    while True:
        botao_clicado = check_click(win, botoes)
        match botao_clicado:
            case "Gerenciar Estoque":
                pass
            case "Realizar Compras":
                pass
            case "Sair":
                win.close()
                break


# Função para centralizar a janela
def center_window(win):
    # Obtém as dimensões da tela
    screen_width = win.winfo_screenwidth()
    screen_height = win.winfo_screenheight()

    # Calcula a posição x e y para centralizar a janela
    x = (screen_width // 2) - (WIDTH // 2)
    y = (screen_height // 2) - (HEIGHT // 2)

    # Define a geometria da janela
    win.master.geometry(f"{WIDTH}x{HEIGHT}+{x}+{y}")


def draw_image(win, img_path, x, y):
    img = Image(Point(x, y), img_path)
    img.draw(win)
    return img


def draw_text(win, x, y, text, size=12, style="bold", color="black"):
    text = Text(Point(x, y), text)
    text.setSize(size)
    text.setStyle(style)
    text.setTextColor(color)
    text.draw(win)
    return text


def draw_rectangle(win, x1, y1, x2, y2, color, outline, width=2):
    rect = Rectangle(Point(x1, y1), Point(x2, y2))
    rect.setFill(color)
    rect.setOutline(outline)
    rect.setWidth(width)
    rect.draw(win)
    return rect


def draw_button(win, x, y, w, h, text, color, outline, width=2):
    x1, y1, x2, y2 = x - w / 2, y - h / 2, x + w / 2, y + h / 2
    draw_rectangle(win, x1, y1, x2, y2, color, outline, width)
    draw_text(win, x, y, text, 12, "bold", "white")


def draw_entry(win, x, y, w):
    entry = Entry(Point(x, y), w)
    entry.draw(win)
    return entry


def draw_row(
    win,
    x,
    y,
    w,
    h,
    values,
    size=12,
    style="normal",
    color="black",
    bgcolor="white",
    outline="black",
    width=1,
    update=False,
):
    for i, value in enumerate(values):
        x1, y1, x2, y2 = x + i * w, y, x + (i + 1) * w, y + h
        tx, ty = x + i * w + w / 2, y + h / 2
        if not update:
            draw_rectangle(win, x1, y1, x2, y2, bgcolor, outline, width)
            draw_text(win, tx, ty, value, size, style, color)
        else:
            for item in win.items[:]:
                if isinstance(item, Text):
                    ix, iy = item.getAnchor().getX(), item.getAnchor().getY()
                if ix == tx and iy == ty:
                    item.setText(value)
                    break


def check_click(win, buttons):
    try:
        click = win.getMouse()
    except GraphicsError:
        return "Sair"
    for button in buttons:
        x, y, w, h = button["xywh"]
        x1, y1, x2, y2 = x - w / 2, y - h / 2, x + w / 2, y + h / 2
        if x1 <= click.getX() <= x2 and y1 <= click.getY() <= y2:
            return button["text"]
    return None


# função pra verificar o estoque
def verificar_estoque(estoque: Estoque):
    win = GraphWin("Verificar Estoque", 600, 600)
    win.setCoords(0, 0, 50, 50)

    # Centraliza a janela no meio do monitor
    screen_width = win.winfo_screenwidth()
    screen_height = win.winfo_screenheight()
    x = (screen_width // 2) - (600 // 2)
    y = (screen_height // 2) - (600 // 2)
    win.master.geometry(f"+{x}+{y}")

    # título da janela
    titulo = Text(Point(25, 48), "Estoque Atual")
    titulo.setSize(16)
    titulo.setStyle("bold")
    titulo.draw(win)

    # campo de pesquisa
    pesquisa_label = Text(Point(10, 45), "Pesquisar por Nome:")
    pesquisa_label.draw(win)
    pesquisa_entry = Entry(Point(25, 45), 20)
    pesquisa_entry.draw(win)
    pesquisar_button = Rectangle(Point(37, 44), Point(42, 46))
    pesquisar_button.setFill("#4CAF50")
    pesquisar_button.setOutline("#388E3C")
    pesquisar_button.setWidth(2)
    pesquisar_button.draw(win)
    pesquisar_text = Text(Point(39.5, 45), "🔍 Pesquisar")
    pesquisar_text.setSize(12)
    pesquisar_text.setStyle("bold")
    pesquisar_text.setTextColor("white")
    pesquisar_text.draw(win)

    resetar_button = Rectangle(Point(43, 44), Point(48, 46))
    resetar_button.setFill("red")
    resetar_button.setOutline("darkred")
    resetar_button.setWidth(2)
    resetar_button.draw(win)
    resetar_text = Text(Point(45.5, 45), "Resetar")
    resetar_text.setSize(12)
    resetar_text.setStyle("bold")
    resetar_text.setTextColor("white")
    resetar_text.draw(win)

    # cabeçalhos da tabela
    headers = ["ID", "Nome", "Categoria", "Quantidade", "Preço"]
    for i, header in enumerate(headers):
        header_text = Text(Point(5 + i * 10, 40), header)
        header_text.setSize(12)
        header_text.setStyle("bold")
        header_text.draw(win)

    # função pra mostrar o estoque na tela
    def mostrar_estoque(estoque: Estoque, offset=1):
        filtrado_estoque = estoque.buscar_produtos(pagina=offset)
        win.setBackground("#c29efb")
        for item in win.items[:]:
            if isinstance(item, Text) and item.getText() not in headers:
                item.undraw()
        for i, produto in enumerate(filtrado_estoque):
            y_pos = 38 - i * 2
            if y_pos < 0:
                break
            id_text = Text(Point(5, y_pos), produto["ID"])
            id_text.draw(win)
            nome_text = Text(Point(15, y_pos), produto["Nome"])
            nome_text.draw(win)
            categoria_text = Text(Point(25, y_pos), produto["Categoria"])
            categoria_text.draw(win)
            quantidade_text = Text(Point(35, y_pos), produto["Quantidade"])
            quantidade_text.draw(win)
            preco_text = Text(Point(45, y_pos), f"R$ {produto['Preco']}")
            preco_text.draw(win)

            # linha divisória horizontal
            line = Line(Point(0, y_pos - 1), Point(50, y_pos - 1))
            line.setFill("lightgrey")
            line.draw(win)

            # linha divisória vertical
            for x in range(10, 50, 10):
                vline = Line(Point(x, y_pos + 1), Point(x, y_pos - 1))
                vline.setFill("lightgrey")
                vline.draw(win)

    # mostra o estoque inicial
    mostrar_estoque(estoque)

    # botão de voltar
    voltar_button = Rectangle(Point(20, 2), Point(30, 4))
    voltar_button.setFill("lightblue")
    voltar_button.draw(win)
    voltar_text = Text(Point(25, 3), "Voltar")
    voltar_text.setSize(12)
    voltar_text.draw(win)

    # botões de rolagem
    scrobble_up_button = Rectangle(Point(35, 2), Point(40, 4))
    scrobble_up_button.setFill("lightgrey")
    scrobble_up_button.draw(win)
    scrobble_up_text = Text(Point(37.5, 3), "⬆")
    scrobble_up_text.setSize(12)
    scrobble_up_text.draw(win)

    scrobble_down_button = Rectangle(Point(45, 2), Point(50, 4))
    scrobble_down_button.setFill("lightgrey")
    scrobble_down_button.draw(win)
    scrobble_down_text = Text(Point(47.5, 3), "⬇")
    scrobble_down_text.setSize(12)
    scrobble_down_text.draw(win)

    offset = 1

    # loop pra detectar cliques nos botões
    while True:
        click = win.getMouse()
        if 20 <= click.getX() <= 30 and 2 <= click.getY() <= 4:
            win.close()
            interface_principal()
            break
        elif 37 <= click.getX() <= 42 and 44 <= click.getY() <= 46:
            pesquisa = pesquisa_entry.getText().lower()
            filtrado_estoque = [
                produto for produto in estoque if pesquisa in produto["Nome"].lower()
            ]
            mostrar_estoque(filtrado_estoque)
        elif 43 <= click.getX() <= 48 and 44 <= click.getY() <= 46:
            pesquisa_entry.setText("")
            mostrar_estoque(estoque)
        elif 35 <= click.getX() <= 40 and 2 <= click.getY() <= 4:
            if offset > 1:
                offset -= 1
                mostrar_estoque(estoque, offset)
        elif 45 <= click.getX() <= 50 and 2 <= click.getY() <= 4:
            if offset * 10 < len(estoque.produtos):
                offset += 1
                mostrar_estoque(estoque, offset)


# função pra cadastrar uma nova peça
def cadastrar_peca(estoque: Estoque):
    win = GraphWin("Cadastrar Peça", 600, 600)
    win.setCoords(0, 0, 50, 50)
    win.setBackground("#c29efb")
    # Centraliza a janela no meio do monitor
    screen_width = win.winfo_screenwidth()
    screen_height = win.winfo_screenheight()
    x = (screen_width // 2) - (600 // 2)
    y = (screen_height // 2) - (600 // 2)
    win.master.geometry(f"+{x}+{y}")

    # título da janela
    titulo = Text(Point(25, 48), "Cadastrar Nova Peça")
    titulo.setSize(16)
    titulo.setStyle("bold")
    titulo.draw(win)

    nome_label = Text(
        Point(10, 36), "Nome:"
    )  # campo de entrada do nome a diferenaça é que o nome é um texto
    nome_label.draw(win)
    nome_entry = Entry(Point(25, 36), 20)  # campo de entrada do nome
    nome_entry.draw(win)

    categoria_label = Text(Point(10, 32), "Categoria:")
    categoria_label.draw(win)
    categoria_entry = Entry(Point(25, 32), 20)
    categoria_entry.draw(win)

    quantidade_label = Text(Point(10, 28), "Quantidade:")
    quantidade_label.draw(win)
    quantidade_entry = Entry(Point(25, 28), 20)
    quantidade_entry.draw(win)

    preco_label = Text(Point(10, 24), "Preço:")
    preco_label.draw(win)
    preco_entry = Entry(Point(25, 24), 20)
    preco_entry.draw(win)

    # botão de cadastrar
    cadastrar_button = Rectangle(Point(15, 18), Point(35, 20))
    cadastrar_button.setFill("lightgreen")
    cadastrar_button.draw(win)
    cadastrar_text = Text(Point(25, 19), "Cadastrar")
    cadastrar_text.setSize(12)
    cadastrar_text.draw(win)

    # botão de voltar
    voltar_button = Rectangle(Point(20, 2), Point(30, 4))
    voltar_button.setFill("lightblue")
    voltar_button.draw(win)
    voltar_text = Text(Point(25, 3), "Voltar")
    voltar_text.setSize(12)
    voltar_text.draw(win)

    # loop pra detectar cliques nos botões o loop aqui alem de detectar cliques serve pra salvar os dados no estoque
    while True:
        click = win.getMouse()
        if (
            15 <= click.getX() <= 35 and 18 <= click.getY() <= 20
        ):  # verifica se o clique foi no botão de cadastrar
            nome = nome_entry.getText()
            categoria = categoria_entry.getText()
            quantidade = quantidade_entry.getText()
            preco = preco_entry.getText()

            if (
                nome and categoria and quantidade and preco
            ):  # verifica se todos os campos foram preenchidos
                produto = {
                    "Nome": nome,
                    "Categoria": categoria,
                    "Quantidade": quantidade,
                    "Preco": preco,
                }
                estoque.adicionar_produto(produto)
                break

        if (
            20 <= click.getX() <= 30 and 2 <= click.getY() <= 4
        ):  # verifica se o clique foi no botão de voltar
            win.close()
            interface_principal()
            break

    win.close()
    interface_principal()


# # função pra gerar a lista de estoque
# def gerar_lista(estoque: Estoque):
#     # cria a pasta reports se nao existir
#     os.makedirs(os.path.join(os.getcwd(), "reports"), exist_ok=True)

#     file_path = os.path.join(os.getcwd(), "reports", "estoque_report.csv")

#     with open(
#         file_path,
#         mode="w",
#         newline="",
#         encoding="utf-8",  # abre o arquivo csv pra escrever
#     ) as file:
#         fieldnames = ["ID", "Nome", "Categoria", "Quantidade", "Preco"]
#         writer = csv.DictWriter(
#             file, fieldnames=fieldnames
#         )  # escreve no arquivo csv com os cabeçalhos do arquivo
#         writer.writeheader()  # escreve os cabeçalhos
#         writer.writerows(estoque.produtos.values())  # escreve as linhas do estoque

#     print(
#         f"Lista de estoque gerada em {file_path}!"
#     )  # imprime a mensagem de que a lista foi gerada
#     interface_principal()


# função pra realizar uma compra
def realizar_compra(estoque: Estoque):
    win = GraphWin("Realizar Compra", 800, 600)  # cria a janela de realizar compra
    win.setCoords(0, 0, 80, 65)  # define as coordenadas da janela
    win.setBackground("#c29efb")

    # Centraliza a janela no meio do monitor
    screen_width = win.winfo_screenwidth()
    screen_height = win.winfo_screenheight()
    x = (screen_width // 2) - (600 // 2)
    y = (screen_height // 2) - (600 // 2)
    win.master.geometry(f"+{x}+{y}")

    # título da janela
    titulo = Text(Point(40, 58), "Realizar Compra")
    titulo.setSize(16)
    titulo.setStyle("bold")
    titulo.draw(win)

    # campo de pesquisa
    pesquisa_label = Text(Point(10, 60), "Pesquisar por Nome:")
    pesquisa_label.draw(win)
    pesquisa_entry = Entry(Point(30, 60), 20)
    pesquisa_entry.draw(win)
    pesquisar_button = Rectangle(Point(52, 59), Point(62, 61))
    pesquisar_button.setFill("#4CAF50")
    pesquisar_button.setOutline("#388E3C")
    pesquisar_button.setWidth(2)
    pesquisar_button.draw(win)
    pesquisar_text = Text(Point(57, 60), "🔍 Pesquisar")
    pesquisar_text.setSize(12)
    pesquisar_text.setStyle("bold")
    pesquisar_text.setTextColor("white")
    pesquisar_text.draw(win)

    resetar_button = Rectangle(
        Point(64, 59), Point(74, 61)
    )  # botão de resetar que funciona como um botão de limpar a pesquisa e voltar ao estoque inicial
    resetar_button.setFill("red")
    resetar_button.setOutline("darkred")
    resetar_button.setWidth(2)
    resetar_button.draw(win)
    resetar_text = Text(Point(69, 60), "Resetar")
    resetar_text.setSize(12)
    resetar_text.setStyle("bold")
    resetar_text.setTextColor("white")
    resetar_text.draw(win)
    space = Text(Point(40, 54), " ")
    space.draw(win)
    # cabeçalhos da tabela
    headers = ["ID", "Nome", "Categoria", "Quantidade", "Preço", "Ação"]
    for i, header in enumerate(headers):
        header_text = Text(
            Point(10 + i * 12, 56), header
        )  # texto do cabeçalho da tabela com base no índice do loop 10 + i * 12 significa que o texto começa em 10 e vai incrementando de 12 em 12 e o 52 é a posição do texto na tela
        header_text.setSize(12)
        header_text.setStyle("bold")
        header_text.draw(win)

    # Adiciona um espaço entre o cabeçalho da tabela e os botões

    offset = 1

    # função para mostrar os produtos na tela
    def mostrar_produtos(
        estoque: Estoque, offset=1, pesquisa=""
    ):  # função pra mostrar os produtos na tela offset=0 é o valor padrão do offset
        filtrado_estoque = estoque.buscar_produtos(nome_produto=pesquisa, pagina=offset)
        for item in win.items[
            :
        ]:  # [ : ] significa que o loop vai percorrer todos os itens da tela
            if (
                isinstance(item, Text) and item.getText() not in headers
            ):  # verifica se o item é um texto e se o texto não está nos cabeçalhos isinstance(item, Text) and item.getText() not in headers significa que o item é um texto e o texto não está nos cabeçalhos
                item.undraw()
        for i, produto in enumerate(filtrado_estoque):
            y_pos = (
                52 - i * 3
            )  # posição do produto na tela com base no índice por isso o i * 3 pra dar um espaçamento entre os produtos
            if y_pos < 0:  # se a posição do produto for menor que 0, quebra o loop
                break
            id_text = Text(Point(10, y_pos), produto["ID"])  # texto do ID do produto
            id_text.draw(win)
            nome_text = Text(Point(22, y_pos), produto["Nome"])
            nome_text.draw(win)
            categoria_text = Text(Point(34, y_pos), produto["Categoria"])
            categoria_text.draw(win)
            quantidade_text = Text(Point(46, y_pos), produto["Quantidade"])
            quantidade_text.draw(win)
            preco_text = Text(Point(58, y_pos), f"R$ {produto['Preco']}")
            preco_text.draw(win)

            # botão de comprar
            comprar_button = Rectangle(Point(66, y_pos - 1), Point(76, y_pos + 1))
            comprar_button.setFill("lightgreen")
            comprar_button.draw(win)
            comprar_text = Text(Point(71, y_pos), "Comprar")
            comprar_text.setSize(12)
            comprar_text.draw(win)

    # mostra os produtos iniciais
    mostrar_produtos(estoque)

    # botão de voltar
    voltar_button = Rectangle(Point(35, 2), Point(45, 4))
    voltar_button.setFill("lightblue")
    voltar_button.draw(win)
    voltar_text = Text(Point(40, 3), "Voltar")
    voltar_text.setSize(12)
    voltar_text.draw(win)

    # botões de rolagem
    scrobble_up_button = Rectangle(Point(50, 2), Point(55, 4))
    scrobble_up_button.setFill("lightgrey")
    scrobble_up_button.draw(win)
    scrobble_up_text = Text(Point(52.5, 3), "⬆")
    scrobble_up_text.setSize(12)
    scrobble_up_text.draw(win)

    scrobble_down_button = Rectangle(Point(60, 2), Point(65, 4))
    scrobble_down_button.setFill("lightgrey")
    scrobble_down_button.draw(win)
    scrobble_down_text = Text(Point(62.5, 3), "⬇")
    scrobble_down_text.setSize(12)
    scrobble_down_text.draw(win)

    # loop para detectar cliques nos botões
    while True:
        click = win.getMouse()
        for i, produto in enumerate(
            estoque.buscar_produtos(pagina=offset + 1)
        ):  # loop pra detectar cliques nos botões de comprar e decrementar a quantidade do produto
            y_pos = (
                52 - i * 3
            )  # posição do produto na tela com base no índice por isso o i * 3 pra dar um espaçamento entre os produtos
            if y_pos < 0:
                break
            if (
                66 <= click.getX() <= 76 and y_pos - 1 <= click.getY() <= y_pos + 1
            ):  # verifica se o clique foi no botão de comprar
                if int(produto["Quantidade"]) > 0:
                    estoque.comprar_produto(produto["ID"], 1)
                    win.close()
                    realizar_compra(estoque)
                    return

        if (
            35 <= click.getX() <= 45 and 2 <= click.getY() <= 4
        ):  # verifica se o clique foi no botão de voltar
            win.close()
            interface_principal()
            break
        elif (
            50 <= click.getX() <= 55 and 2 <= click.getY() <= 4
        ):  # verifica se o clique foi no botão de rolar pra cima
            if offset > 1:
                offset -= 1
                mostrar_produtos(estoque, offset)
        elif (
            60 <= click.getX() <= 65 and 2 <= click.getY() <= 4
        ):  # verifica se o clique foi no botão de rolar pra baixo
            if offset * 10 < len(estoque.produtos):
                offset += 1
                mostrar_produtos(estoque, offset)
        elif (
            52 <= click.getX() <= 62 and 55 <= click.getY() <= 57
        ):  # verifica se o clique foi no botão de pesquisar
            pesquisa = pesquisa_entry.getText().lower()
            mostrar_produtos(estoque, pesquisa=pesquisa)
        elif (
            64 <= click.getX() <= 74 and 55 <= click.getY() <= 57
        ):  # verifica se o clique foi no botão de resetar o vermelho
            pesquisa_entry.setText("")
            mostrar_produtos(estoque)


if __name__ == "__main__":
    main()
