# Sistema de Gestão de Estoque para E-commerce

Este sistema foi desenvolvido para gerenciar o estoque de uma loja de e-commerce. Ele utiliza um arquivo CSV para armazenar os dados de estoque e fornece funcionalidades essenciais para manter o controle dos produtos.

## Funcionalidades

1. **Leitura do CSV de Estoque**  
   O sistema carrega os dados do estoque a partir de um arquivo CSV no formato padrão. Caso o arquivo não exista, ele será criado automaticamente ao salvar o estoque.

2. **Cadastro e Atualização de Produtos**  
   Permite cadastrar novos produtos ou atualizar produtos existentes no estoque. Ao cadastrar um produto existente, a quantidade será somada à existente e o preço atualizado.

3. **Geração de Lista de Estoque**  
   O sistema exibe uma lista completa de todos os produtos disponíveis no estoque, incluindo informações como ID, nome, quantidade e preço.

4. **Verificação de Quantidade de Produtos**  
   Permite verificar a quantidade disponível de um produto específico no estoque, utilizando seu identificador único (ID).

5. **Redução do Estoque em Caso de Compra**  
   Quando uma compra é registrada, o sistema reduz automaticamente a quantidade do produto no estoque. Caso a quantidade disponível seja insuficiente, o sistema exibirá uma mensagem de alerta.

## TODO

- [ ] Adicionar um mesmo produto e somar no produto já integrado no sistema.
- [ ] Produto com preço diferente é um produto diferente, apesar de estar com o mesmo nome.
- [ ] Adicionar ID de forma automática diretamente pelo sistema.
