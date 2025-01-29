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
                cadastrar_peca()
            case "Atualizar Peça":
                win.close()
                atualizar_peca()
            case "Remover Peça":
                win.close()
                remover_peca()
            case "Exportar Estoque":
                exportar_estoque(current)
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
                win.close()
                comprar_peca()
            case "Exportar Estoque":
                exportar_estoque(current)
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


def cadastrar_peca():
    estoque = Estoque(ESTOQUE)

    win = GraphWin("Gerenciar Estoque", WIDTH, HEIGHT)
    win.setCoords(X1, Y1, X2, Y2)
    win.setBackground(C_LAVANDA)

    center_window(win)

    draw_text(win, 50, 85, "Cadastrar Peça", 24, "bold", "black")

    botoes = [
        {"xywh": (50, 17.5, 30, 5), "text": "Cadastrar", "color": C_VERDE_ESCURO},
        {"xywh": (50, 10, 30, 5), "text": "Voltar", "color": C_VERMELHO_ESCURO},
    ]

    for botao in botoes:
        x, y, w, h = botao["xywh"]
        draw_button(win, x, y, w, h, botao["text"], botao["color"], C_ROXO_ESCURO)

    draw_text(win, 50, 72.5, "Nome", 12, "normal", "black")
    nome = draw_entry(win, 50, 67.5, 20)
    draw_text(win, 50, 60, "Categoria", 12, "normal", "black")
    categoria = draw_entry(win, 50, 55, 20)
    draw_text(win, 50, 47.5, "Quantidade", 12, "normal", "black")
    quantidade = draw_entry(win, 50, 42.5, 20)
    draw_text(win, 50, 35, "Preço", 12, "normal", "black")
    preco = draw_entry(win, 50, 30, 20)

    while True:
        botao_clicado = check_click(win, botoes)
        match botao_clicado:
            case "Cadastrar":
                produto = {
                    "Nome": nome.getText(),
                    "Categoria": categoria.getText(),
                    "Quantidade": quantidade.getText(),
                    "Preco": preco.getText(),
                }
                estoque.adicionar_produto(produto)
                win.close()
                gerenciar_estoque()
            case "Voltar":
                win.close()
                gerenciar_estoque()
            case "Sair":
                win.close()
                break


def atualizar_peca():
    estoque = Estoque(ESTOQUE)

    win = GraphWin("Gerenciar Estoque", WIDTH, HEIGHT)
    win.setCoords(X1, Y1, X2, Y2)
    win.setBackground(C_LAVANDA)

    center_window(win)

    draw_text(win, 50, 85, "Atualizar Peça", 24, "bold", "black")

    botoes = [
        {"xywh": (70, 7.5, 30, 5), "text": "Atualizar", "color": C_VERDE_ESCURO},
        {"xywh": (30, 7.5, 30, 5), "text": "Voltar", "color": C_VERMELHO_ESCURO},
    ]

    for botao in botoes:
        x, y, w, h = botao["xywh"]
        draw_button(win, x, y, w, h, botao["text"], botao["color"], C_ROXO_ESCURO)

    draw_text(win, 50, 72.5, "ID", 12, "normal", "black")
    id = draw_entry(win, 50, 67.5, 20)
    draw_text(win, 50, 60, "Nome", 12, "normal", "black")
    nome = draw_entry(win, 50, 55, 20)
    draw_text(win, 50, 47.5, "Categoria", 12, "normal", "black")
    categoria = draw_entry(win, 50, 42.5, 20)
    draw_text(win, 50, 35, "Quantidade", 12, "normal", "black")
    quantidade = draw_entry(win, 50, 30, 20)
    draw_text(win, 50, 22.5, "Preço", 12, "normal", "black")
    preco = draw_entry(win, 50, 17.5, 20)

    while True:
        botao_clicado = check_click(win, botoes)
        match botao_clicado:
            case "Atualizar":
                produto = {
                    "ID": id.getText(),
                    "Nome": nome.getText(),
                    "Categoria": categoria.getText(),
                    "Quantidade": quantidade.getText(),
                    "Preco": preco.getText(),
                }
                for key, value in produto.items():
                    if not value:
                        produto[key] = estoque.produtos[id.getText()][key]
                estoque.atualizar_produto(id.getText(), produto)
                win.close()
                gerenciar_estoque()
            case "Voltar":
                win.close()
                gerenciar_estoque()
            case "Sair":
                win.close()
                break


def remover_peca():
    estoque = Estoque(ESTOQUE)

    win = GraphWin("Gerenciar Estoque", WIDTH, HEIGHT)
    win.setCoords(X1, Y1, X2, Y2)
    win.setBackground(C_LAVANDA)

    center_window(win)

    draw_text(win, 50, 85, "Remover Peça", 24, "bold", "black")

    botoes = [
        {"xywh": (70, 7.5, 30, 5), "text": "Remover", "color": C_VERMELHO_ESCURO},
        {"xywh": (30, 7.5, 30, 5), "text": "Voltar", "color": C_VERMELHO_ESCURO},
    ]

    for botao in botoes:
        x, y, w, h = botao["xywh"]
        draw_button(win, x, y, w, h, botao["text"], botao["color"], C_ROXO_ESCURO)

    draw_text(win, 50, 72.5, "ID", 12, "normal", "black")
    id = draw_entry(win, 50, 67.5, 20)

    while True:
        botao_clicado = check_click(win, botoes)
        match botao_clicado:
            case "Remover":
                estoque.remover_produto(id.getText())
                win.close()
                gerenciar_estoque()
            case "Voltar":
                win.close()
                gerenciar_estoque()
            case "Sair":
                win.close()
                break


def comprar_peca():
    estoque = Estoque(ESTOQUE)

    win = GraphWin("Gerenciar Estoque", WIDTH, HEIGHT)
    win.setCoords(X1, Y1, X2, Y2)
    win.setBackground(C_LAVANDA)

    center_window(win)

    draw_text(win, 50, 85, "Comprar Peça", 24, "bold", "black")

    botoes = [
        {"xywh": (70, 7.5, 30, 5), "text": "Comprar", "color": C_VERDE_ESCURO},
        {"xywh": (30, 7.5, 30, 5), "text": "Voltar", "color": C_VERMELHO_ESCURO},
    ]

    for botao in botoes:
        x, y, w, h = botao["xywh"]
        draw_button(win, x, y, w, h, botao["text"], botao["color"], C_ROXO_ESCURO)

    draw_text(win, 50, 72.5, "ID", 12, "normal", "black")
    id = draw_entry(win, 50, 67.5, 20)
    draw_text(win, 50, 60, "Quantidade", 12, "normal", "black")
    quantidade = draw_entry(win, 50, 55, 20)

    while True:
        botao_clicado = check_click(win, botoes)
        match botao_clicado:
            case "Comprar":
                estoque.comprar_produto(id.getText(), int(quantidade.getText()))
                win.close()
                realizar_compra()
            case "Voltar":
                win.close()
                realizar_compra()
            case "Sair":
                win.close()
                break


def exportar_estoque(current):
    matrix = [current[i : i + 5] for i in range(0, len(current), 5)]
    html = """
    <h1>Estoque</h1>
    <html>
    <head><title>Tabela</title></head>
    <body>
    <table border='1'>
    """
    for row in matrix:
        html += "<tr>" + "".join(f"<td>{cell}</td>" for cell in row) + "</tr>"
    html += "</table></body></html>"
    reports = os.path.join(os.getcwd(), "reports")
    os.makedirs(reports, exist_ok=True)
    temp_file = os.path.join(reports, "estoque_report.html")
    with open(temp_file, "w", encoding="utf-8") as f:
        f.write(html)


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


if __name__ == "__main__":
    main()
