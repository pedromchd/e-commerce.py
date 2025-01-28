import csv
import os
import webbrowser
from lib.graphics import *

# nome do arquivo csv que guarda o estoque, eh onde a gente salva tudo
CSV_FILE = os.path.join(os.getcwd(), "data", "estoque.csv")


# função pra carregar o estoque do arquivo csv
def carregar_estoque():
    if not os.path.exists(CSV_FILE):
        return []
    with open(CSV_FILE, mode="r", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)  # lê o arquivo csv
        return list(reader)


# função pra salvar o estoque no arquivo csv
def salvar_estoque(estoque):
    with open(
        CSV_FILE, mode="w", newline="", encoding="utf-8"
    ) as file:  # abre o arquivo csv
        fieldnames = [
            "ID",
            "Nome",
            "Categoria",
            "Quantidade",
            "Preco",
        ]  # cabeçalhos do arquivo csv
        writer = csv.DictWriter(file, fieldnames=fieldnames)  # escreve no arquivo csv
        writer.writeheader()  # escreve os cabeçalhos
        writer.writerows(estoque)  # escreve as linhas do estoque


# função principal da interface gráfica
def interface_principal():

    win = GraphWin(
        "E-commerce: Peças de Carro e Artigos Esportivos", 600, 600
    )  # cria a janela principal
    win.setCoords(0, 0, 50, 50)  # define as coordenadas da janela

    # Centraliza a janela no meio do monitor
    screen_width = win.winfo_screenwidth()
    screen_height = win.winfo_screenheight()
    x = (screen_width // 2) - (600 // 2)
    y = (screen_height // 2) - (600 // 2)
    win.master.geometry(f"+{x}+{y}")

    # Caminho da imagem corrigido para garantir o diretório correto
    logo_path = os.path.join(os.path.dirname(__file__), "img", "roxo5.png")
    if not os.path.exists(logo_path):
        raise FileNotFoundError(f"Imagem não encontrada no caminho: {logo_path}")

    # Adiciona imagens na tela inicial
    logo = Image(Point(25, 25), logo_path)  # Ajusta a posição da imagem
    logo.draw(win)

    # Redimensiona a imagem para preencher a janela
    logo_width = win.getWidth()
    logo_height = win.getHeight()
    logo = logo.clone()
    logo.move(0, 0)
    logo.draw(win)

    # logo do e-commerce, eh pra ficar bonitinho
    logo = Text(Point(25, 43), "🏢 Auto & Sport")
    logo.setSize(28)  # tamanho da fonte'
    logo.setStyle("bold")
    logo.setTextColor("#df0c40")  #
    logo.draw(win)  # desenha o logo na tela
    # Adiciona uma imagem
    image_path = os.path.join(os.getcwd(), "img", "logo.png")
    if os.path.exists(image_path):
        logo_image = Image(Point(25, 35), image_path)
        logo_image.draw(win)

    # botões principais, eh onde a mágica acontece
    buttons = {
        "Verificar Estoque": Rectangle(Point(15, 35), Point(35, 37)),
        "Cadastrar Peça": Rectangle(Point(15, 30), Point(35, 32)),
        "Gerar Lista": Rectangle(Point(15, 25), Point(35, 27)),
        "Realizar Compra": Rectangle(Point(15, 20), Point(35, 22)),
        "Sair": Rectangle(Point(15, 15), Point(35, 17)),
    }

    # desenha os botões na tela
    for (
        label,
        rect,
    ) in (
        buttons.items()
    ):  # loop pra desenhar os botões que funciona como um dicionário e pega o label e o retângulo
        if label == "Sair":  # botão de sair
            rect.setFill("#df0c40")  # cor vermelha para o botão de sair
            rect.setOutline("#9c8dfb")  # borda vermelha escura
        else:
            rect.setFill("#521580")  # cor roxa
            rect.setOutline("#20062a")  # borda roxa escura
        rect.setWidth(2)  # largura da borda
        rect.draw(win)
        button_text = Text(rect.getCenter(), label)  # texto do botão
        button_text.setSize(12)
        button_text.setStyle("bold")
        button_text.setTextColor("white")  # texto branco
        button_text.draw(win)  # desenha o texto do botão

    # carrega o estoque do arquivo csv
    estoque = carregar_estoque()  # carrega o estoque do arquivo csv

    # loop principal pra detectar cliques nos botões
    while True:
        click = win.getMouse()

        # verificar estoque
        if (
            15 <= click.getX() <= 35 and 35 <= click.getY() <= 37
        ):  # verifica se o clique foi no botão de verificar estoque
            win.close()
            verificar_estoque(estoque)
            break

        # cadastrar peça
        elif (
            15 <= click.getX() <= 35 and 30 <= click.getY() <= 32
        ):  # verifica se o clique foi no botão de cadastrar peça
            win.close()
            cadastrar_peca(estoque)
            break

        # gerar lista
        elif (
            15 <= click.getX() <= 35 and 25 <= click.getY() <= 27
        ):  # verifica se o clique foi no botão de gerar lista
            win.close()
            gerar_lista(estoque)
            break

        # realizar compra
        elif (
            15 <= click.getX() <= 35 and 20 <= click.getY() <= 22
        ):  # verifica se o clique foi no botão de realizar compra
            win.close()
            realizar_compra(estoque)
            break

        # sair do programa
        elif (
            15 <= click.getX() <= 35 and 15 <= click.getY() <= 17
        ):  # verifica se o clique foi no botão de sair
            win.close()
            break


# função pra verificar o estoque
def verificar_estoque(estoque):
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
    def mostrar_estoque(filtrado_estoque, offset=0):
        win.setBackground("#c29efb")
        for item in win.items[:]:
            if isinstance(item, Text) and item.getText() not in headers:
                item.undraw()
        for i, produto in enumerate(filtrado_estoque[offset : offset + 10]):
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

    offset = 0

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
            if offset > 0:
                offset -= 10
                mostrar_estoque(estoque, offset)
        elif 45 <= click.getX() <= 50 and 2 <= click.getY() <= 4:
            if offset + 10 < len(estoque):
                offset += 10
                mostrar_estoque(estoque, offset)


# função pra cadastrar uma nova peça
def cadastrar_peca(estoque):
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

    # campos de entrada
    id_label = Text(Point(10, 40), "ID:")
    id_label.draw(win)
    id_entry = Entry(Point(25, 40), 20)
    id_entry.draw(win)

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
            id = id_entry.getText()
            nome = nome_entry.getText()
            categoria = categoria_entry.getText()
            quantidade = quantidade_entry.getText()
            preco = preco_entry.getText()

            if (
                id and nome and categoria and quantidade and preco
            ):  # verifica se todos os campos foram preenchidos
                estoque.append(
                    {
                        "ID": id,
                        "Nome": nome,
                        "Categoria": categoria,
                        "Quantidade": quantidade,
                        "Preco": preco,
                    }
                )
                salvar_estoque(estoque)
                break

        if (
            20 <= click.getX() <= 30 and 2 <= click.getY() <= 4
        ):  # verifica se o clique foi no botão de voltar
            win.close()
            interface_principal()
            break

    win.close()
    interface_principal()


# função pra gerar a lista de estoque
def gerar_lista(estoque):
    # cria a pasta reports se nao existir
    os.makedirs(os.path.join(os.getcwd(), "reports"), exist_ok=True)

    file_path = os.path.join(os.getcwd(), "reports", "estoque_report.csv")

    with open(
        file_path,
        mode="w",
        newline="",
        encoding="utf-8",  # abre o arquivo csv pra escrever
    ) as file:
        fieldnames = ["ID", "Nome", "Categoria", "Quantidade", "Preco"]
        writer = csv.DictWriter(
            file, fieldnames=fieldnames
        )  # escreve no arquivo csv com os cabeçalhos do arquivo
        writer.writeheader()  # escreve os cabeçalhos
        writer.writerows(estoque)  # escreve as linhas do estoque

    print(
        f"Lista de estoque gerada em {file_path}!"
    )  # imprime a mensagem de que a lista foi gerada
    interface_principal()


# função pra realizar uma compra
def realizar_compra(estoque):
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

    offset = 0

    # função para mostrar os produtos na tela
    def mostrar_produtos(
        filtrado_estoque, offset=0
    ):  # função pra mostrar os produtos na tela offset=0 é o valor padrão do offset
        for item in win.items[
            :
        ]:  # [ : ] significa que o loop vai percorrer todos os itens da tela
            if (
                isinstance(item, Text) and item.getText() not in headers
            ):  # verifica se o item é um texto e se o texto não está nos cabeçalhos isinstance(item, Text) and item.getText() not in headers significa que o item é um texto e o texto não está nos cabeçalhos
                item.undraw()
        for i, produto in enumerate(filtrado_estoque[offset : offset + 10]):
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
    mostrar_produtos(estoque, offset)

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
            estoque[offset : offset + 10]
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
                    produto["Quantidade"] = str(
                        int(produto["Quantidade"]) - 1
                    )  # decrementa a quantidade do produto
                    salvar_estoque(estoque)
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
            if offset > 0:
                offset -= 10
                mostrar_produtos(estoque, offset)
        elif (
            60 <= click.getX() <= 65 and 2 <= click.getY() <= 4
        ):  # verifica se o clique foi no botão de rolar pra baixo
            if offset + 10 < len(estoque):
                offset += 10
                mostrar_produtos(estoque, offset)
        elif (
            52 <= click.getX() <= 62 and 55 <= click.getY() <= 57
        ):  # verifica se o clique foi no botão de pesquisar
            pesquisa = pesquisa_entry.getText().lower()
            filtrado_estoque = [
                produto
                for produto in estoque
                if pesquisa
                in produto[
                    "Nome"
                ].lower()  # pesquisa o produto pelo nome do produto tudo em lowercase pra evitar erros e etc
            ]
            mostrar_produtos(filtrado_estoque)
        elif (
            64 <= click.getX() <= 74 and 55 <= click.getY() <= 57
        ):  # verifica se o clique foi no botão de resetar o vermelho
            pesquisa_entry.setText("")
            mostrar_produtos(estoque)


# inicia a interface principal quando o script é executado
if __name__ == "__main__":
    interface_principal()
