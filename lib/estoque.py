import csv


class Produto:
    def __init__(
        self, id: str, nome: str, categoria: str, quantidade: int, preco: float
    ):
        self.id = id
        self.nome = nome
        self.categoria = categoria
        self.quantidade = quantidade
        self.preco = preco

    def to_dict(self):
        return {
            "ID": self.id,
            "Nome": self.nome,
            "Categoria": self.categoria,
            "Quantidade": self.quantidade,
            "Preço": self.preco,
        }

    @staticmethod
    def from_dict(data: dict):
        return Produto(
            data["ID"],
            data["Nome"],
            data["Categoria"],
            data["Quantidade"],
            data["Preço"],
        )


class Estoque:
    def __init__(self, csv_file: str):
        self._csv_file = csv_file
        self._fields = tuple()
        self._produtos = dict()
        self._carregar_produtos()

    def _carregar_produtos(self):
        with open(self._csv_file, "r", encoding="utf-8", newline="") as file:
            reader = csv.DictReader(file)
            self._fields = tuple(reader.fieldnames)
            self._produtos = {row["ID"]: row for row in reader}

    def _salvar_produtos(self):
        with open(self._csv_file, "w", encoding="utf-8", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=self._fields)
            writer.writeheader()
            writer.writerows(self._produtos.values())

    def adicionar_produto(self, produto: dict):
        id_produto = produto["ID"]
        if id_produto in self._produtos:
            raise ValueError("Produto já cadastrado")
        self._produtos[id_produto] = produto
        self._salvar_produtos()

    def remover_produto(self, id_produto: str):
        if id_produto not in self._produtos:
            raise ValueError("Produto não encontrado")
        del self._produtos[id_produto]
        self._salvar_produtos()

    def atualizar_produto(self, id_produto: str, produto: dict):
        if id_produto not in self._produtos:
            raise ValueError("Produto não encontrado")
        self._produtos[id_produto] = produto
        self._salvar_produtos()

    def listar_produtos(
        self, nome_produto: str = None, pagina: int = 1, tamanho_pagina: int = 10
    ):
        produtos = list(self._produtos.values())
        if nome_produto:
            produtos = [
                produto
                for produto in produtos
                if nome_produto.lower() in produto["Nome"].lower()
            ]
        inicio = (pagina - 1) * tamanho_pagina
        fim = inicio + tamanho_pagina
        return produtos[inicio:fim]
