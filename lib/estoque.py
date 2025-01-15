import csv


class Estoque:
    def __init__(self, csv_file: str):
        self.csv_file = csv_file
        self.fields = []
        self.produtos = dict()
        self.carregar_produtos()

    def carregar_produtos(self):
        with open(self.csv_file, "r", encoding="utf-8", newline="") as file:
            reader = csv.DictReader(file)
            self.fields = reader.fieldnames
            self.produtos = {row["ID"]: row for row in reader}

    def salvar_produtos(self):
        with open(self.csv_file, "w", encoding="utf-8", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=self.fields)
            writer.writeheader()
            writer.writerows(self.produtos.values())

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
