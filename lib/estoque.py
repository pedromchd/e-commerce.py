import csv


class Estoque:
    def __init__(self, csv_file: str):
        self.csv_file = csv_file
        self.produtos = []
        self.carregar_produtos()

    def carregar_produtos(self):
        with open(self.csv_file, "r", encoding="utf-8", newline="") as file:
            reader = csv.reader(file)
            for row in reader:
                self.produtos.append(row)

    def salvar_produtos(self):
        with open(self.csv_file, "w", encoding="utf-8", newline="") as file:
            writer = csv.writer(file)
            writer.writerows(self.produtos)

    def adicionar_produto(self, produto: list):
        self.produtos.append(produto)
        self.salvar_produtos()

    def remover_produto(self, id_produto: int):
        for produto in self.produtos:
            if int(produto[0]) == id_produto:
                self.produtos.remove(produto)
                self.salvar_produtos()
                return True
        return False
