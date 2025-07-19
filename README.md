
# 📦 Sistema de Gerenciamento de Produtos

## 📋 Descrição

Sistema completo de gerenciamento de produtos desenvolvido em Python puro, sem uso de bibliotecas externas. O programa oferece uma interface robusta em linha de comando (CLI) para gerenciar estoque de produtos comerciais com funcionalidades avançadas de CRUD (Create, Read, Update, Delete), sistema inteligente de busca, ordenação dinâmica e relatórios estatísticos detalhados.

### 🎯 Objetivo do Sistema

Este sistema foi projetado para oferecer uma solução prática e eficiente para controlar inventário. Com validações rigorosas e interface intuitiva, garante a integridade dos dados e facilita o dia a dia dos usuários.

## ⚡ Características Técnicas

- **Linguagem:** Python 3.x (compatível com versões 3.6+)
- **Paradigma:** Programação procedural com estruturas funcionais
- **Interface:** CLI interativa com menu numerado
- **Armazenamento:** Lista global em memória
- **Validações:** Sistema robusto com múltiplas camadas
- **Tratamento de Erros:** Loops de recuperação e mensagens específicas

## 🎯 Funcionalidades Implementadas

### ✅ 1. Sistema de Cadastro de Produtos

**Função Principal:** `cadastrar_novo_produto()`

Esta é uma das funcionalidades mais robustas do sistema, implementando validação em múltiplas camadas para garantir a integridade dos dados.

**Exemplo de uso:**

```python
def cadastrar_novo_produto():
    print("\n===CADASTRO DE PRODUTO===")
    
    # Validação rigorosa do ID
    while True:
        id_produto = input("Digite o ID do produto (formato 'ABC-123'): ").upper()
        if validar_formato_id_produto(id_produto) and not verificar_id_ja_existe(id_produto):
            break
        # Exibe mensagens de erro específicas
```

**Funcionalidades detalhadas:**

- **Validação de ID com `validar_formato_id_produto()`:**

```python
def validar_formato_id_produto(id_produto):
    if len(id_produto) != 7:
        return False
    
    # Verifica letras maiúsculas nas 3 primeiras posições
    for i in range(3):
        if not id_produto[i].isupper() or not id_produto[i].isalpha():
            return False
    
    # Verifica hífen na 4ª posição
    if id_produto[3] != '-':
        return False
    
    # Verifica números nas 3 últimas posições
    for i in range(4, 7):
        if not id_produto[i].isdigit():
            return False
    
    return True
```

- **Verificação de unicidade com `verificar_id_ja_existe()`:**

```python
def verificar_id_ja_existe(id_produto):
    for produto in lista_produtos:
        if produto["id"] == id_produto:
            return True
    return False
```

**Validações implementadas:**

- **ID:** Formato obrigatório ABC-123 (3 letras maiúsculas + hífen + 3 números)
- **Nome:** Mínimo 3 caracteres, apenas letras, números e espaços
- **Preço:** Valor numérico positivo com tratamento de erro
- **Quantidade:** Número inteiro positivo
- **Categoria:** Seleção obrigatória de lista pré-definida

### ✅ 2. Sistema de Listagem e Visualização

**Função Principal:** `exibir_lista_de_produtos()`

Sistema de renderização tabular profissional que exibe todos os produtos cadastrados com formatação consistente e informações de status do estoque.

**Recursos principais:**

```python
def exibir_lista_de_produtos():
    if not lista_produtos:
        print("📋 Nenhum produto cadastrado.")
        return
    
    print("\n" + "="*80)
    print("                         LISTA DE PRODUTOS")
    print("="*80)
    
    # Cabeçalho formatado com especificadores de largura
    print(f"{'ID':<8} {'Nome':<20} {'Preço':<10} {'Qtd':<5} {'Categoria':<15} {'Status'}")
    print("-"*80)
    
    for produto in lista_produtos:
        status = "BAIXO" if produto['quantidade'] < 5 else "OK"
        print(f"{produto['id']:<8} {produto['nome']:<20} "
              f"R${produto['preco']:<9.2f} {produto['quantidade']:<5} "
              f"{produto['categoria']:<15} {status}")
```

**Características técnicas:**

- **Formatação com f-strings:** `{'texto':<largura}` para alinhamento perfeito
- **Cálculo dinâmico de status:** Alerta automático para estoque baixo (< 5 unidades)
- **Separadores visuais:** Linhas de 80 caracteres para organização
- **Verificação de estado:** Exibe mensagem informativa se não há produtos

### ✅ 3. Sistema de Atualização de Produtos

**Função Principal:** `atualizar_informacoes_produto()`

Sistema versátil que permite modificar informações específicas de produtos já cadastrados, mantendo a integridade dos dados.

**Opções de atualização disponíveis:**

```python
def atualizar_informacoes_produto():
    print("\nO que deseja atualizar?")
    print("1. Preço")
    print("2. Nome") 
    print("3. Quantidade")
    
    escolha = input("Digite sua escolha (1-3): ")
    
    if escolha == "1":
        # Validação de preço com try/except
        while True:
            try:
                novo_preco = float(input("Digite o novo preço: R$"))
                if novo_preco > 0:
                    break
            except ValueError:
                print("❌ Digite um preço válido!")
```

**Funcionalidades especiais:**

- **Sistema inteligente de quantidade:** Operadores +/- para adicionar/remover estoque
- **Validação de dados:** Reutiliza funções de validação do cadastro
- **Busca por ID:** Localiza produto antes de permitir edição
- **Feedback visual:** Confirma alterações realizadas

**Exemplo de uso para quantidade:**

```console
Digite a nova quantidade (ou use +/- para adicionar/remover): +10
✅ Adicionados 10 unidades. Nova quantidade: 25
```

### ✅ 4. Sistema de Exclusão de Produtos

**Função Principal:** `excluir_produto_do_sistema()`

Sistema de remoção segura com múltiplas verificações e confirmação do usuário.

**Protocolo de segurança implementado:**

```python
def excluir_produto_do_sistema():
    # Verificação de existência
    if not verificar_produto_existe(id_produto):
        print("❌ Produto não encontrado!")
        return
    
    # Regra de negócio: não excluir produtos sem estoque
    if produto_encontrado['quantidade'] == 0:
        print("⚠️ Não é possível excluir produtos com estoque zerado!")
        return
    
    # Confirmação do usuário
    confirmacao = input("Tem certeza que deseja excluir? (S/N): ").upper()
    if confirmacao == 'S':
        lista_produtos.remove(produto_encontrado)
        print("✅ Produto excluído com sucesso!")
```

**Recursos de segurança:**

- **Validação de existência:** Confirma que produto existe antes de prosseguir
- **Regras de negócio:** Impede exclusão de produtos com estoque zerado
- **Confirmação explícita:** Usuário deve confirmar a operação
- **Feedback claro:** Mensagens informativas sobre o resultado

### ✅ 5. Sistema de Ordenação Dinâmica

**Função Principal:** `ordenar_produtos_por_criterio()`

Sistema avançado de ordenação com múltiplos critérios e opção de persistência.

**Critérios de ordenação disponíveis:**

```python
def ordenar_produtos_por_criterio():
    print("\nEscolha o critério de ordenação:")
    print("1. Nome (A-Z)")
    print("2. Preço (menor para maior)")
    print("3. Quantidade (menor para maior)")
    print("4. Categoria (A-Z)")
    
    criterio = input("Digite sua escolha (1-4): ")
    
    if criterio == "1":
        produtos_ordenados = sorted(lista_produtos, key=lambda x: x['nome'].lower())
    elif criterio == "2":
        produtos_ordenados = sorted(lista_produtos, key=lambda x: x['preco'])
```

**Características técnicas:**

- **Preservação de dados:** Usa `.copy()` antes de ordenar
- **Lambda functions:** Critérios de ordenação flexíveis
- **Case-insensitive:** Ordenação alfabética ignora maiúsculas/minúsculas
- **Persistência opcional:** Usuário escolhe se mantém nova ordem

### ✅ 6. Sistema de Busca Inteligente

**Função Principal:** `buscar_produto_no_sistema()`

Motor de busca flexível com três modalidades otimizadas para diferentes necessidades.

**Modalidades de busca:**

```python
def buscar_produto_no_sistema():
    print("\nTipo de busca:")
    print("1. Buscar por nome")
    print("2. Buscar por ID")
    print("3. Buscar por categoria")
    
    tipo_busca = input("Escolha o tipo (1-3): ")
    
    if tipo_busca == "1":
        # Busca parcial e case-insensitive
        nome_busca = input("Digite parte do nome: ").lower()
        produtos_encontrados = [p for p in lista_produtos 
                               if nome_busca in p['nome'].lower()]
```

**Recursos avançados:**

- **Busca parcial por nome:** Encontra produtos com substring
- **Busca exata por ID:** Localização precisa e rápida
- **Filtro por categoria:** Agrupa produtos similares
- **List comprehension:** Filtragem eficiente com `[p for p in lista_produtos if ...]`

### ✅ 7. Sistema de Relatórios Estatísticos

**Função Principal:** `gerar_relatorios_do_sistema()`

Módulo avançado de análise de dados com múltiplos tipos de relatório para tomada de decisão.

**Tipos de relatório disponíveis:**

```python
def gerar_relatorios_do_sistema():
    print("\nTipos de relatório:")
    print("1. Valor total do estoque")
    print("2. Produtos com estoque baixo")
    print("3. Relatório completo por categoria")
    
    # Relatório 1: Valor total
    valor_total = sum(p['preco'] * p['quantidade'] for p in lista_produtos)
    print(f"💰 Valor total do estoque: R$ {valor_total:.2f}")
    
    # Relatório 2: Estoque baixo
    produtos_baixo = [p for p in lista_produtos if p['quantidade'] < 5]
    
    # Relatório 3: Agrupamento por categoria
    categorias = {}
    for produto in lista_produtos:
        cat = produto['categoria']
        if cat not in categorias:
            categorias[cat] = {'count': 0, 'valor': 0}
        categorias[cat]['count'] += 1
        categorias[cat]['valor'] += produto['preco'] * produto['quantidade']
```

**Análises geradas:**

- **Valor financeiro total:** Soma do valor de todos os produtos (preço × quantidade)
- **Alertas de estoque:** Lista produtos com quantidade crítica (< 5 unidades)
- **Relatório por categoria:** Agrupamento com contagem e valor por categoria
- **Estatísticas resumidas:** Contadores e totalizadores automáticos

**Recursos técnicos:**

- **Generator expressions:** `sum(p['preco'] * p['quantidade'] for p in lista_produtos)`
- **Dictionary comprehension:** Agrupamento eficiente de dados
- **Filtros condicionais:** Identificação automática de situações críticas

### ✅ 8. Sistema de Menu Principal

**Função Principal:** `exibir_menu()` + Loop de controle

Interface principal que coordena todas as funcionalidades do sistema com tratamento robusto de erros.

**Design da interface:**

```text
===============================================
         SISTEMA DE GERENCIAMENTO DE PRODUTOS
===============================================
1 - Cadastrar novo produto
2 - Atualizar informações de um produto
3 - Excluir produto
4 - Exibir lista de produtos
5 - Ordenar produtos por critério
6 - Buscar produto
7 - Gerar relatórios
8 - [Funcionalidade planejada]
9 - [Funcionalidade planejada]
10 - Sair
===============================================
```

**Loop principal de controle:**


```python
while True:
    exibir_menu()
    input_menu = input("Selecione uma opção: ")
    
    try:
        opcao = int(input_menu)
        if opcao < 1 or opcao > 10:
            print("❌ Opção inválida! Escolha entre 1-10.")
            continue
            
        if opcao == 1:
            cadastrar_novo_produto()
        # ... outras opções
        elif opcao == 10:
            print("👋 Obrigado por usar nosso sistema!")
            break
            
    except ValueError:
        print("❌ Erro: Digite apenas números de 1 a 10.")
```

**Características de robustez:**

- **Try/except robusto:** Captura erros de conversão de tipo
- **Validação de range:** Verifica se opção está entre 1-10
- **Loop infinito controlado:** Continua até usuário escolher sair
- **Tratamento de erro específico:** Mensagens claras para cada tipo de erro



