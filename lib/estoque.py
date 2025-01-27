import csv
import random


class Estoque:
    def __init__(self, csv_file: str):
        self._csv_file = csv_file
        self._fields = tuple()
        self._produtos = dict()
        self._produtos_por_nome = dict()
        self._carregar_produtos()

    def _carregar_produtos(self):
        with open(self._csv_file, "r", encoding="utf-8", newline="") as file:
            reader = csv.DictReader(file)
            self._fields = tuple(reader.fieldnames)
            self._produtos = {row["ID"]: row for row in reader}
        self._salvar_produtos_por_nome()

    def _salvar_produtos(self):
        self._salvar_produtos_por_nome()
        with open(self._csv_file, "w", encoding="utf-8", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=self._fields)
            writer.writeheader()
            writer.writerows(self._produtos.values())

    def _salvar_produtos_por_nome(self):
        self._produtos_por_nome = {
            produto["Nome"].lower(): produto["ID"]
            for produto in self._produtos.values()
        }

    def _generate_id(self):
        while True:
            id = random.randint(1, 99999)
            id = f"{id:05}"
            if id not in self._produtos:
                return id

    def adicionar_produto(self, produto: dict):
        if produto["Nome"].lower() in self._produtos_por_nome:
            return False, "Produto já cadastrado com esse nome"
        id_produto = self._generate_id()
        produto["ID"] = id_produto
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
