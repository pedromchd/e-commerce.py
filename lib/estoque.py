import csv


class Estoque:
    def __init__(self, csv_file):
        self.csv_file = csv_file
        self.fields = ["ID", "Nome", "Categoria", "Quantidade", "Preco"]
        self.produtos = self.carregar_produtos()

    def carregar_produtos(self):
        with open(self.csv_file, "r") as f:
            reader = csv.DictReader(f)
            return list(reader)

    def salvar_produtos(self):
        with open(self.csv_file, "w") as f:
            writer = csv.DictWriter(f, fieldnames=self.fields)
            writer.writeheader()
            writer.writerows(self.produtos)

    def adicionar_produto(self, produto):
        self.produtos.append(produto)
        self.salvar_produtos()

    def remover_produto(self, id_produto):
        self.produtos = [p for p in self.produtos if p["ID"] != id_produto]
        self.salvar_produtos()

    def atualizar_produto(self, id_produto, produto):
        for p in self.produtos:
            if p["ID"] == id_produto:
                p.update(produto)
                break
        self.salvar_produtos()

    def buscar_produtos(self, nome_produto="", tamanho_pagina=10, pagina=1):
        produtos = [
            p for p in self.produtos if nome_produto.lower() in p["Nome"].lower()
        ]
        inicio = (pagina - 1) * tamanho_pagina
        fim = inicio + tamanho_pagina
        return produtos[inicio:fim]

    def comprar_produto(self, id_produto, quantidade):
        for p in self.produtos:
            if p["ID"] == id_produto:
                p["Quantidade"] = int(p["Quantidade"]) - quantidade
                break
        self.salvar_produtos()
