import os

from lib.estoque import Estoque
from lib.graphics import *

WIDTH, HEIGHT = 640, 480

X1, Y1, X2, Y2 = 0, 0, 100, 100

C_ROXO = "#521580"  # Roxo
C_ROXO_ESCURO = "#20062a"  # Roxo escuro
C_VERMELHO = "#df0c40"  # Vermelho
C_VERMELHO_ESCURO = "#8B0000"  # Vermelho escuro
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
        {"xywh": (50, 25, 40, 10), "text": "Realizar Compra"},
        {"xywh": (50, 10, 40, 10), "text": "Sair"},
    ]

    for botao in botoes:
        x, y, w, h = botao["xywh"]
        draw_button(win, x, y, w, h, botao["text"], C_ROXO, C_ROXO_ESCURO)

    while True:
        botao_clicado = check_click(win, botoes)
        match botao_clicado:
            case "Gerenciar Estoque":
                win.close()
                gerenciar_estoque()
            case "Realizar Compra":
                win.close()
                realizar_compra()
            case "Sair":
                win.close()
                break


def gerenciar_estoque():
    estoque = Estoque(ESTOQUE)

    win = GraphWin("Gerenciar Estoque", WIDTH, HEIGHT)
    win.setCoords(X1, Y1, X2, Y2)
    win.setBackground(C_LAVANDA)

    center_window(win)

    draw_text(win, 20, 90, "Pesquisar por nome:", 12, "normal", "black")

    botoes = [
        {"xywh": (75, 90, 16, 5), "text": "Pesquisar", "color": C_VERDE},
        {"xywh": (90, 90, 12.5, 5), "text": "Resetar", "color": C_VERMELHO},
        {"xywh": (17.5, 12.5, 30, 5), "text": "Cadastrar Peça", "color": C_ROXO_ESCURO},
        {"xywh": (50, 12.5, 30, 5), "text": "Atualizar Peça", "color": C_ROXO_ESCURO},
        {"xywh": (82.5, 12.5, 30, 5), "text": "Remover Peça", "color": C_ROXO_ESCURO},
        {"xywh": (50, 5, 30, 5), "text": "Exportar Estoque", "color": C_VERDE_ESCURO},
        {"xywh": (10, 20, 16, 5), "text": "Voltar", "color": C_VERMELHO_ESCURO},
        {"xywh": (85, 20, 5, 5), "text": "↑", "color": C_ROXO},
        {"xywh": (95, 20, 5, 5), "text": "↓", "color": C_ROXO},
    ]

    for botao in botoes:
        x, y, w, h = botao["xywh"]
        draw_button(win, x, y, w, h, botao["text"], botao["color"], C_ROXO_ESCURO)

    entry = draw_entry(win, 50, 90, 20)

    headers = ["ID", "Nome", "Categoria", "Quantidade", "Preço"]
    draw_row(win, 0, 75, 20, 5, headers, style="bold")
    current = update_table(win, estoque)

    pagina = 1

    while True:
        botao_clicado = check_click(win, botoes)
        match botao_clicado:
            case "Pesquisar":
                pesquisa = entry.getText().lower()
                current = update_table(
                    win, estoque, pesquisa, update=True, current=current
                )
            case "Resetar":
                entry.setText("")
                current = update_table(win, estoque, update=True, current=current)
            case "Cadastrar Peça":
                win.close()
                cadastrar_peca(estoque)
            case "Atualizar Peça":
                pass
            case "Remover Peça":
                pass
            case "Exportar Estoque":
                pass
            case "Voltar":
                win.close()
                main()
            case "↑":
                if pagina > 1:
                    pagina -= 1
                    current = update_table(
                        win, estoque, pagina=pagina, update=True, current=current
                    )
            case "↓":
                if pagina * 10 < len(estoque.produtos):
                    pagina += 1
                    current = update_table(
                        win, estoque, pagina=pagina, update=True, current=current
                    )
            case "Sair":
                win.close()
                break


def realizar_compra():
    estoque = Estoque(ESTOQUE)

    win = GraphWin("Gerenciar Estoque", WIDTH, HEIGHT)
    win.setCoords(X1, Y1, X2, Y2)
    win.setBackground(C_LAVANDA)

    center_window(win)

    draw_text(win, 20, 90, "Pesquisar por nome:", 12, "normal", "black")

    botoes = [
        {"xywh": (75, 90, 16, 5), "text": "Pesquisar", "color": C_VERDE},
        {"xywh": (90, 90, 12.5, 5), "text": "Resetar", "color": C_VERMELHO},
        {"xywh": (50, 12.5, 30, 5), "text": "Comprar Peça", "color": C_ROXO_ESCURO},
        {"xywh": (50, 5, 30, 5), "text": "Exportar Estoque", "color": C_VERDE_ESCURO},
        {"xywh": (10, 20, 16, 5), "text": "Voltar", "color": C_VERMELHO_ESCURO},
        {"xywh": (85, 20, 5, 5), "text": "↑", "color": C_ROXO},
        {"xywh": (95, 20, 5, 5), "text": "↓", "color": C_ROXO},
    ]

    for botao in botoes:
        x, y, w, h = botao["xywh"]
        draw_button(win, x, y, w, h, botao["text"], botao["color"], C_ROXO_ESCURO)

    entry = draw_entry(win, 50, 90, 20)

    headers = ["Nome", "Categoria", "Quantidade", "Preço", "Comprar"]
    draw_row(win, 0, 75, 20, 5, headers, style="bold")
    current = update_table(win, estoque)

    pagina = 1

    while True:
        botao_clicado = check_click(win, botoes)
        match botao_clicado:
            case "Pesquisar":
                pesquisa = entry.getText().lower()
                current = update_table(
                    win, estoque, pesquisa, update=True, current=current
                )
            case "Resetar":
                entry.setText("")
                current = update_table(win, estoque, update=True, current=current)
            case "Comprar Peça":
                pass
            case "Exportar Estoque":
                pass
            case "Voltar":
                win.close()
                main()
            case "↑":
                if pagina > 1:
                    pagina -= 1
                    current = update_table(
                        win, estoque, pagina=pagina, update=True, current=current
                    )
            case "↓":
                if pagina * 10 < len(estoque.produtos):
                    pagina += 1
                    current = update_table(
                        win, estoque, pagina=pagina, update=True, current=current
                    )
            case "Sair":
                win.close()
                break


def center_window(win):
    screen_width = win.winfo_screenwidth()
    screen_height = win.winfo_screenheight()
    x = (screen_width // 2) - (WIDTH // 2)
    y = (screen_height // 2) - (HEIGHT // 2)
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


def update_table(win, estoque, pesquisa="", pagina=1, update=False, current=None):
    if update:
        for item in win.items[:]:
            if isinstance(item, Text) and item.getText() in current:
                item.undraw()
    produtos = estoque.buscar_produtos(nome_produto=pesquisa, pagina=pagina)
    for i, produto in enumerate(produtos):
        draw_row(win, 0, 70 - i * 5, 20, 5, produto.values(), update=update)
    return [value for produto in produtos for value in produto.values()]


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


if __name__ == "__main__":
    main()
