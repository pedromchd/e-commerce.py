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

    def adicionar_produto(self, produto: dict):
        id_produto = produto["ID"]
        if id_produto in self.produtos:
            raise ValueError("Produto já cadastrado")
        self.produtos[id_produto] = produto
        self.salvar_produtos()

    def remover_produto(self, id_produto: str):
        if id_produto not in self.produtos:
            raise ValueError("Produto não encontrado")
        del self.produtos[id_produto]
        self.salvar_produtos()

    def atualizar_produto(self, id_produto: str, produto: dict):
        if id_produto not in self.produtos:
            raise ValueError("Produto não encontrado")
        self.produtos[id_produto] = produto
        self.salvar_produtos()

    def listar_produtos(
        self, nome_produto: str = None, pagina: int = 1, tamanho_pagina: int = 10
    ):
        produtos = list(self.produtos.values())
        if nome_produto:
            produtos = [
                produto
                for produto in produtos
                if nome_produto.lower() in produto["Nome"].lower()
            ]
        inicio = (pagina - 1) * tamanho_pagina
        fim = inicio + tamanho_pagina
        return produtos[inicio:fim]
