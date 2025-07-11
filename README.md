﻿# 📦 Sistema de Gerenciamento de Produtos

## 📋 Descrição

Sistema de gerenciamento de produtos desenvolvido em Python puro, sem uso de bibliotecas externas. O programa oferece uma interface em linha de comando (CLI) intuitiva para gerenciar estoque de produtos com funcionalidades completas de CRUD (Create, Read, Update, Delete), busca, ordenação e relatórios.

## 🎯 Funcionalidades

### ✅ **Funcionalidades Implementadas**
- **Cadastro de Produtos**: Adicionar novos produtos com validação completa
- **Listagem de Produtos**: Visualizar todos os produtos cadastrados
- **Ordenação**: Organizar produtos por nome, preço, quantidade ou categoria
- **Busca**: Localizar produtos por nome, ID ou categoria
- **Relatórios**: Gerar relatórios de estoque e análises financeiras
- **Validações**: Sistema robusto de validação de dados

### 🚧 **Funcionalidades Planejadas**
- **Atualização de Produtos**: Editar informações de produtos existentes
- **Exclusão de Produtos**: Remover produtos do sistema
- **Sistema de Vendas**: Processar vendas e controlar estoque
- **Aplicação de Descontos**: Gerenciar promoções e descontos

## 🛠️ Tecnologias Utilizadas

- **Python 3.x** (sem bibliotecas externas)
- **Estruturas de dados nativas**: Listas e dicionários
- **Interface CLI**: Menu interativo no terminal

## 📁 Estrutura do Projeto

```
trabalho_larisse/
├── trabalho.py          # Arquivo principal do sistema
├── README.md           # Documentação do projeto
└── docs/              # Documentação adicional (planejado)
```

## 🚀 Como Executar

### Pré-requisitos
- Python 3.6 ou superior instalado
- Sistema operacional: Windows, Linux ou macOS

### Instalação e Execução
1. **Clone ou baixe o repositório**
   ```bash
   git clone https://github.com/levyrodrigues23/Trabalho_Gerencia_ProfLarisse.git
   cd Trabalho_Gerencia_ProfLarisse
   ```

2. **Execute o programa**
   ```bash
   python trabalho.py
   ```

3. **Navegue pelo menu**
   - Use as opções numéricas (1-10) para navegar
   - Siga as instruções na tela
   - Digite '10' para sair do sistema

## 📖 Manual de Uso

### 1. **Cadastro de Produto**
- Selecione a opção `1` no menu principal
- Informe o ID no formato `ABC-123` (3 letras maiúsculas + hífen + 3 números)
- Digite o nome do produto (mínimo 3 caracteres)
- Informe o preço (valor positivo)
- Digite a quantidade (número inteiro positivo)
- Selecione uma categoria: Alimentos, Limpeza, Eletrônicos ou Vestuário

### 2. **Listar Produtos**
- Selecione a opção `4` no menu principal
- Visualize todos os produtos com informações organizadas em tabela
- Status do estoque é exibido automaticamente (BAIXO/OK)

### 3. **Ordenar Produtos**
- Selecione a opção `5` no menu principal
- Escolha o critério de ordenação:
  - Por Nome (A-Z)
  - Por Preço (menor para maior)
  - Por Quantidade (menor para maior)
  - Por Categoria (A-Z)
- Decida se deseja salvar a nova ordem como padrão

### 4. **Buscar Produtos**
- Selecione a opção `6` no menu principal
- Escolha o tipo de busca:
  - Por Nome (busca parcial)
  - Por ID (busca exata)
  - Por Categoria (busca exata)

### 5. **Relatórios**
- Selecione a opção `7` no menu principal
- Escolha o tipo de relatório:
  - Valor Total do Estoque
  - Produtos com Estoque Baixo
  - Relatório Completo (análise detalhada)

## 🔧 Regras de Validação

### **ID do Produto**
- Formato obrigatório: `ABC-123`
- 3 letras maiúsculas + hífen + 3 números
- Deve ser único no sistema
- Exemplos válidos: `CAF-001`, `LIM-123`, `ELE-999`

### **Nome do Produto**
- Mínimo 3 caracteres
- Apenas letras, números e espaços
- Não permite caracteres especiais (@, #, $, etc.)

### **Preço**
- Deve ser um valor positivo
- Aceita números decimais (ex: 15.99)
- Não permite valores zero ou negativos

### **Quantidade**
- Deve ser um número inteiro positivo
- Não permite zero no cadastro inicial
- Sistema alerta quando estoque < 5 unidades

### **Categoria**
- Opções fixas: "Alimentos", "Limpeza", "Eletrônicos", "Vestuário"
- Entrada é case-sensitive

## 🎨 Interface

O sistema utiliza uma interface de texto limpa e organizada:

```
========================================================
Bem-vindo ao Sistema de Gerenciamento de Produtos!
========================================================

===MENU PRINCIPAL===
1. Cadastrar Produto
2. Atualizar Produto
3. Excluir Produto
4. Listar Produtos
5. Ordenar Produtos
6. Buscar Produto
7. Relatórios:(Valor Total/ Estoque Baixo)
8. Vender produto
9. Aplicar Desconto
10. Sair
```

## 📊 Estrutura de Dados

Cada produto é armazenado como um dicionário com a seguinte estrutura:

```python
produto = {
    'id': 'ABC-123',           # String: Identificador único
    'nome': 'Nome do Produto', # String: Nome do produto
    'preco': 25.99,           # Float: Preço do produto
    'quantidade': 50,         # Int: Quantidade em estoque
    'categoria': 'Alimentos'  # String: Categoria do produto
}
```

## 🐛 Tratamento de Erros

O sistema inclui tratamento robusto de erros:
- **Entradas inválidas**: Validação de tipos de dados
- **Valores fora do range**: Verificação de limites
- **IDs duplicados**: Prevenção de conflitos
- **Campos obrigatórios**: Validação de preenchimento
- **Formato incorreto**: Verificação de padrões

---

## 📚 DOCUMENTAÇÃO TÉCNICA DAS FUNÇÕES

### 🔧 **Funções de Validação**

#### `validar_formato_id_produto(id_produto)`
**Propósito**: Valida se o ID do produto segue o formato correto ABC-123.
**Parâmetros**: 
- `id_produto` (string): ID a ser validado
**Retorno**: `True` se válido, `False` caso contrário
**Lógica**: 
- Verifica se tem exatamente 7 caracteres
- Confirma que os 3 primeiros são letras maiúsculas
- Verifica se o 4º caractere é hífen (-)
- Confirma que os 3 últimos são números
**Exemplo**: `validar_formato_id_produto("ABC-123")` → `True`

#### `validar_nome_produto(nome)`
**Propósito**: Valida se o nome atende aos critérios estabelecidos.
**Parâmetros**:
- `nome` (string): Nome a ser validado
**Retorno**: `True` se válido, `False` caso contrário
**Lógica**:
- Verifica tamanho mínimo de 3 caracteres
- Permite apenas letras, números e espaços
- Rejeita caracteres especiais
**Exemplo**: `validar_nome_produto("Açúcar Cristal")` → `True`

#### `verificar_id_ja_existe(id_produto)`
**Propósito**: Verifica se um ID já está em uso no sistema.
**Parâmetros**:
- `id_produto` (string): ID a ser verificado
**Retorno**: `True` se já existe, `False` caso contrário
**Lógica**: Percorre a lista global de produtos comparando IDs

### 🏗️ **Funções Principais**

#### `exibir_menu()`
**Propósito**: Exibe o menu principal do sistema.
**Parâmetros**: Nenhum
**Retorno**: Nenhum (apenas imprime na tela)
**Lógica**: Apresenta todas as opções numeradas de 1 a 10

#### `cadastrar_novo_produto()`
**Propósito**: Conduz o processo completo de cadastro de um novo produto.
**Parâmetros**: Nenhum
**Retorno**: Dicionário do produto criado
**Lógica Detalhada**:
1. **Validação do ID**: Loop até obter ID válido e único
2. **Validação do Nome**: Loop até obter nome com critérios corretos
3. **Validação do Preço**: Try/except para garantir valor numérico positivo
4. **Validação da Quantidade**: Try/except para garantir inteiro positivo
5. **Validação da Categoria**: Loop até selecionar categoria válida
6. **Criação do Produto**: Monta dicionário com todas as informações
7. **Adição à Lista**: Inclui produto na lista global
8. **Confirmação**: Exibe mensagem de sucesso com resumo

#### `exibir_lista_de_produtos()`
**Propósito**: Mostra todos os produtos cadastrados em formato tabular.
**Parâmetros**: Nenhum
**Retorno**: Nenhum
**Lógica**:
- Verifica se há produtos cadastrados
- Cria cabeçalho formatado da tabela
- Percorre lista exibindo cada produto
- Calcula status do estoque (BAIXO/OK)
- Exibe total de produtos no final

#### `ordenar_produtos_por_criterio()`
**Propósito**: Permite ordenar produtos por diferentes critérios.
**Parâmetros**: Nenhum
**Retorno**: Nenhum
**Lógica**:
- Apresenta menu de opções de ordenação
- Cria cópia da lista para não alterar original
- Aplica ordenação usando função `sort()` com `key=lambda`
- Exibe produtos ordenados
- Oferece opção de salvar nova ordem como padrão

#### `buscar_produto_no_sistema()`
**Propósito**: Permite buscar produtos por diferentes critérios.
**Parâmetros**: Nenhum
**Retorno**: Nenhum
**Lógica**:
- Menu de opções de busca (Nome, ID, Categoria)
- **Busca por Nome**: Busca parcial usando `in` e `.lower()`
- **Busca por ID**: Busca exata comparando IDs
- **Busca por Categoria**: Busca exata ignorando case
- List comprehension para filtrar resultados
- Exibe produtos encontrados ou mensagem de "não encontrado"

#### `gerar_relatorios_do_sistema()`
**Propósito**: Gera diferentes tipos de relatórios do estoque.
**Parâmetros**: Nenhum
**Retorno**: Nenhum
**Lógica**:
- **Relatório 1 - Valor Total**: Usa `sum()` com generator expression
- **Relatório 2 - Estoque Baixo**: List comprehension para filtrar produtos < 5
- **Relatório 3 - Completo**: Combina análises + agrupamento por categoria
- **Agrupamento por Categoria**: Loop criando dicionário de estatísticas
- Exibe dados formatados com cálculos financeiros

### 🔄 **Loop Principal do Sistema**

#### **Estrutura do Loop**
```python
while True:  # Loop infinito até usuário escolher sair
    exibir_menu()
    input_menu = input("Selecione uma opção do menu: ")
    
    try:
        opcao = int(input_menu)  # Converte para inteiro
        
        if opcao == 1:
            cadastrar_novo_produto()
        # ... outras opções ...
        elif opcao == 10:
            print("Saindo do sistema. Até Logo!")
            break  # Encerra o loop
        else:
            print("Opção inválida!")
            
    except ValueError:
        print("Erro: Digite apenas números de 1 a 10.")
    
    print()  # Linha em branco para formatação
```

**Características**:
- **Try/Except**: Captura erros de conversão para inteiro
- **Estrutura if/elif**: Direciona para função correspondente
- **Validação de Range**: Verifica se opção está entre 1-10
- **Break**: Encerra loop quando usuário escolhe sair
- **Formatação**: Linha em branco entre iterações

### 🎯 **Funções Não Implementadas (Planejadas)**

#### `atualizar_informacoes_produto()`
**Propósito Planejado**: Editar informações de produtos existentes
**Funcionalidades Previstas**:
- Buscar produto por ID
- Permitir edição de preço, quantidade, categoria
- Validar novas informações
- Atualizar produto na lista

#### `excluir_produto_do_sistema()`
**Propósito Planejado**: Remover produtos do sistema
**Funcionalidades Previstas**:
- Buscar produto por ID
- Solicitar confirmação (S/N)
- Verificar regras de negócio (estoque zerado)
- Remover da lista global

#### `processar_venda_de_produto()`
**Propósito Planejado**: Processar vendas e reduzir estoque
**Funcionalidades Previstas**:
- Selecionar produto para venda
- Informar quantidade vendida
- Validar disponibilidade em estoque
- Atualizar quantidade do produto

#### `aplicar_desconto_em_produto()`
**Propósito Planejado**: Aplicar descontos promocionais
**Funcionalidades Previstas**:
- Selecionar produto(s)
- Definir percentual ou valor fixo de desconto
- Validar novo preço
- Atualizar preço na lista

## 🤝 Contribuição

Este é um projeto acadêmico. Para contribuições:

1. Fork o repositório
2. Crie uma branch para sua feature (`git checkout -b feature/nova-funcionalidade`)
3. Commit suas mudanças (`git commit -m 'Adiciona nova funcionalidade'`)
4. Push para a branch (`git push origin feature/nova-funcionalidade`)
5. Abra um Pull Request

## 📄 Licença

Este projeto é desenvolvido para fins acadêmicos.

## 👨‍💻 Autor

**José Levy ** e **Thais Ávila**
- GitHub: [@levyrodrigues23](https://github.com/levyrodrigues23)
-GitHub: [@thaisavila](https://github.com/thaisavila)
- Repositório: [Trabalho_Gerencia_ProfLarisse](https://github.com/levyrodrigues23/Trabalho_Gerencia_ProfLarisse)

## 📝 Notas de Desenvolvimento

- **Versão Python**: 3.6+
- **Paradigma**: Programação procedural
- **Sem dependências externas**: Apenas Python padrão
- **Interface**: CLI (Command Line Interface)
- **Armazenamento**: Em memória (dados são perdidos ao fechar o programa)

---

*Sistema desenvolvido como trabalho acadêmico - Prof. Larisse*
