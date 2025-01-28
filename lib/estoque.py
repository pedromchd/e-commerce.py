import csv


class Estoque:
    def __init__(self, csv_file):
        self.csv_file = csv_file
        self.fields = ["ID", "Nome", "Categoria", "Quantidade", "Preco"]
        self.produtos = self.carregar_produtos()

    def carregar_produtos(self):
        with open(self.csv_file, "r") as f:
            reader = csv.DictReader(f)
            return {row["ID"]: row for row in reader}

    def salvar_produtos(self):
        with open(self.csv_file, "w") as f:
            writer = csv.DictWriter(f, fieldnames=self.fields)
            writer.writeheader()
            writer.writerows(self.produtos.values())

    def adicionar_produto(self, produto):
        self.produtos[produto["ID"]] = produto
        self.salvar_produtos()

    def remover_produto(self, id_produto):
        if id_produto in self.produtos:
            del self.produtos[id_produto]
            self.salvar_produtos()

    def atualizar_produto(self, id_produto, produto):
        if id_produto in self.produtos:
            self.produtos[id_produto].update(produto)
            self.salvar_produtos()

    def buscar_produtos(self, nome_produto="", tamanho_pagina=10, pagina=1):
        produtos_filtrados = [
            p
            for p in self.produtos.values()
            if nome_produto.lower() in p["Nome"].lower()
        ]
        inicio = (pagina - 1) * tamanho_pagina
        fim = inicio + tamanho_pagina
        return produtos_filtrados[inicio:fim]

    def comprar_produto(self, id_produto, quantidade):
        if id_produto in self.produtos:
            self.produtos[id_produto]["Quantidade"] = (
                int(self.produtos[id_produto]["Quantidade"]) - quantidade
            )
            self.salvar_produtos()
