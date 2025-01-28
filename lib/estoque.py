import csv
import random
import re


class Estoque:
    def __init__(self, csv_file: str):
        # Inicializa a classe com o caminho do arquivo CSV e carrega os produtos
        self._csv_file = csv_file
        self._fields = tuple()  # Armazena os nomes das colunas do CSV
        self._produtos = dict()  # Dicionário para armazenar produtos por ID
        self._produtos_por_nome = dict()  # Dicionário para armazenar produtos por nome
        self._carregar_produtos()  # Carrega os produtos do arquivo CSV

    def _carregar_produtos(self):
        # Abre o arquivo CSV e carrega os produtos nos dicionários
        with open(self._csv_file, "r", encoding="utf-8", newline="") as file:
            reader = csv.DictReader(file)  # Lê o CSV como um dicionário
            self._fields = tuple(reader.fieldnames)  # Armazena os nomes das colunas
            # Mapeia produtos por ID
            self._produtos = {row["ID"]: row for row in reader}
        self._salvar_produtos_por_nome()  # Atualiza o dicionário de produtos por nome

    def _salvar_produtos(self):
        # Salva os produtos no arquivo CSV
        self._salvar_produtos_por_nome()  # Atualiza o dicionário de produtos por nome
        with open(self._csv_file, "w", encoding="utf-8", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=self._fields)
            writer.writeheader()  # Escreve o cabeçalho no arquivo
            writer.writerows(self._produtos.values())  # Escreve os produtos no arquivo

    def _salvar_produtos_por_nome(self):
        # Atualiza o dicionário de produtos por nome
        self._produtos_por_nome = {
            produto["Nome"].lower(): produto["ID"]  # Mapeia nomes para IDs
            for produto in self._produtos.values()
        }

    def _generate_id(self):
        # Gera um ID único para um novo produto
        while True:
            id = random.randint(1, 99999)  # Gera um número aleatório
            id = f"{id:05}"  # Formata o ID com 5 dígitos
            if id not in self._produtos:  # Verifica se o ID já existe
                return id

    def validate_fields(self, produto: dict, fields: tuple):
        # Valida os campos do produto
        # Remove espaços em branco dos valores
        produto = {key: str(value).strip() for key, value in produto.items()}
        # Verifica se todos os campos obrigatórios estão presentes
        if not all(key in produto for key in fields):
            return False, "Campos inválidos"
        # Valida os campos "Quantidade" e "Preço"
        if not produto["Quantidade"].isdigit():
            return False, "Quantidade inválida"
        if not re.match(r"^\d+\,\d{2}$", produto["Preco"]):
            return False, "Preço inválido"
        return True, ""

    def adicionar_produto(self, produto: dict):
        # Adiciona um novo produto ao estoque
        # Verifica se todos os campos estão presentes e são válidos
        campos = [campo for campo in self._fields if campo != "ID"]
        valid, msg = self.validate_fields(produto, campos)
        if not valid:
            return False, msg
        # Verifica se o nome já existe
        if produto["Nome"].lower() in self._produtos_por_nome:
            return False, "Produto já cadastrado com esse nome"
        id_produto = self._generate_id()  # Gera um ID único
        produto["ID"] = id_produto  # Adiciona o ID ao produto
        self._produtos[id_produto] = produto  # Adiciona o produto ao dicionário
        self._salvar_produtos()  # Salva os produtos no arquivo CSV
        return True, "Produto adicionado com sucesso"

    def remover_produto(self, id_produto: str):
        # Remove um produto do estoque
        if id_produto not in self._produtos:  # Verifica se o produto existe
            return False, "Produto não encontrado"
        del self._produtos[id_produto]  # Remove o produto do dicionário
        self._salvar_produtos()  # Salva os produtos no arquivo CSV
        return True, "Produto removido com sucesso"

    def atualizar_produto(self, id_produto: str, produto: dict):
        # Atualiza um produto existente no estoque
        # Verifica se todos os campos estão presentes e são válidos
        valid, msg = self.validate_fields(produto, self._fields)
        if not valid:
            return False, msg
        if id_produto not in self._produtos:  # Verifica se o produto existe
            return False, "Produto não encontrado"
        nome_produto = produto["Nome"].lower()
        if (
            nome_produto in self._produtos_por_nome
            and self._produtos_por_nome[nome_produto] != id_produto
        ):  # Verifica se o nome já está em uso por outro produto
            return False, "Outro produto já cadastrado com esse nome"
        self._produtos[id_produto] = produto  # Atualiza o produto no dicionário
        self._salvar_produtos()  # Salva os produtos no arquivo CSV
        return True, "Produto atualizado com sucesso"

    def listar_produtos(
        self, nome_produto: str = None, pagina: int = 1, tamanho_pagina: int = 10
    ):
        # Lista os produtos com opção de filtro por nome e paginação
        produtos = list(self._produtos.values())  # Obtém todos os produtos
        if nome_produto:  # Filtra os produtos pelo nome, se fornecido
            produtos = [
                produto
                for produto in produtos
                if nome_produto.lower() in produto["Nome"].lower()
            ]
        inicio = (pagina - 1) * tamanho_pagina  # Calcula o índice inicial da página
        fim = inicio + tamanho_pagina  # Calcula o índice final da página
        return produtos[inicio:fim]  # Retorna os produtos da página solicitada
