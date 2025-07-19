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

## 🚫 Funcionalidades Planejadas (Não Implementadas)

### **Funcionalidade 9: Sistema de Vendas** `processar_venda_de_produto()`

**Propósito futuro:** Processar vendas e reduzir estoque automaticamente

**Funcionalidades previstas:**
- Seleção de produto por ID
- Definição de quantidade vendida
- Validação de disponibilidade em estoque
- Atualização automática de quantidade
- Registro de histórico de vendas

### **Funcionalidade 10: Sistema de Descontos** `aplicar_desconto_em_produto()`

**Propósito futuro:** Sistema de gestão de promoções e descontos

**Funcionalidades previstas:**
- Seleção de produto(s) para desconto
- Opções de desconto percentual ou valor fixo
- Validação de novo preço
- Período de validade do desconto
- Histórico de promoções aplicadas

## 🔧 Sistema de Validações Detalhado

### **Validação de ID de Produto**

```python
def validar_formato_id_produto(id_produto):
    """
    Valida se o ID segue o formato ABC-123
    
    Regras:
    - Exatamente 7 caracteres
    - 3 primeiros: letras maiúsculas
    - 4º caractere: hífen (-)
    - 3 últimos: números
    """
    if len(id_produto) != 7:
        print("❌ ID deve ter exatamente 7 caracteres!")
        return False
    
    # Validação das letras (posições 0-2)
    for i in range(3):
        if not id_produto[i].isupper() or not id_produto[i].isalpha():
            print("❌ Os 3 primeiros caracteres devem ser letras maiúsculas!")
            return False
    
    # Validação do hífen (posição 3)
    if id_produto[3] != '-':
        print("❌ O 4º caractere deve ser um hífen (-)!")
        return False
    
    # Validação dos números (posições 4-6)
    for i in range(4, 7):
        if not id_produto[i].isdigit():
            print("❌ Os 3 últimos caracteres devem ser números!")
            return False
    
    return True
```

**Exemplos práticos:**

```text
✅ Válidos: "ABC-123", "XYZ-999", "DEF-001"
❌ Inválidos: "abc-123", "AB-123", "ABC123", "ABC-12A"
```

### **Validação de Nome de Produto**

```python
def validar_nome_produto(nome):
    """
    Valida se o nome atende aos critérios estabelecidos
    
    Regras:
    - Mínimo 3 caracteres
    - Apenas letras, números e espaços
    - Sem caracteres especiais
    """
    if len(nome) < 3:
        print("❌ Nome deve ter pelo menos 3 caracteres!")
        return False
    
    for char in nome:
        if not (char.isalnum() or char == ' '):
            print("❌ Nome deve conter apenas letras, números e espaços!")
            return False
    
    return True
```

**Exemplos práticos:**

```text
✅ Válidos: "Arroz", "Feijão Preto", "Açúcar Cristal 1kg"
❌ Inválidos: "Ar", "Açúcar@", "Feijão#1", "Arroz_integral"
```

### **Validação de Preço**

```python
# Implementada com try/except no cadastro
while True:
    try:
        preco = float(input("Digite o preço do produto: R$"))
        if preco <= 0:
            print("❌ Preço deve ser maior que zero!")
            continue
        break
    except ValueError:
        print("❌ Digite um valor numérico válido!")
```

**Exemplos práticos:**

```text
✅ Válidos: 10.50, 5.99, 100.0, 0.01
❌ Inválidos: -5.50, 0, "abc", ""
```

### **Validação de Quantidade**

```python
# Implementada com try/except no cadastro
while True:
    try:
        quantidade = int(input("Digite a quantidade: "))
        if quantidade < 0:
            print("❌ Quantidade não pode ser negativa!")
            continue
        break
    except ValueError:
        print("❌ Digite um número inteiro válido!")
```

**Exemplos práticos:**

```text
✅ Válidos: 0, 1, 50, 1000
❌ Inválidos: -1, 1.5, "abc", ""
```

## 🎨 Interface e Experiência do Usuário

### **Design Visual da Interface**

O sistema utiliza elementos visuais para melhorar a experiência:

- **Emojis informativos:** 📦 ✅ ❌ ⚠️ 💰 👋
- **Separadores visuais:** Linhas de `=` e `-` para organização
- **Títulos centralizados:** Destaque para seções importantes
- **Formatação consistente:** Alinhamento e espaçamento padronizados

### **Padrões de Mensagem**

```python
# Padrões utilizados no sistema
print("✅ Operação realizada com sucesso!")      # Sucesso
print("❌ Erro: [descrição do problema]")        # Erro
print("⚠️ Atenção: [aviso importante]")          # Aviso
print("📋 Informação: [dados informativos]")    # Informação
print("💰 Valor: R$ [quantia]")                 # Valores monetários
```

### **Fluxo de Navegação**

1. **Menu Principal** → **Seleção de Opção** → **Execução da Função**
2. **Validação de Entrada** → **Processamento** → **Feedback**
3. **Retorno ao Menu** ou **Continuação do Fluxo**

## 🐛 Tratamento de Erros e Robustez

O sistema implementa tratamento abrangente de erros em múltiplas camadas:

### **Tipos de Erro Tratados**

**1. Erros de Conversão de Tipo:**

```python
try:
    opcao = int(input_menu)
except ValueError:
    print("❌ Erro: Digite apenas números de 1 a 10.")
```

**2. Validação de Range de Valores:**

```python
if opcao < 1 or opcao > 10:
    print("❌ Opção inválida! Escolha entre 1-10.")
```

**3. Verificações de Estado do Sistema:**

```python
if not lista_produtos:
    print("📋 Nenhum produto cadastrado.")
    return
```

**4. Loops de Validação Persistente:**

```python
while True:
    dados = input("Digite os dados: ")
    if validar_dados(dados):
        break
    print("❌ Dados inválidos. Tente novamente.")
```

### **Estratégias de Recuperação de Erro**

- **Loops de Retry:** Sistema não falha, permite correção
- **Mensagens Específicas:** Cada erro tem explicação clara
- **Validação Preventiva:** Múltiplas verificações antes de processar
- **Estados de Fallback:** Sistema sempre retorna a estado válido

## 📚 DOCUMENTAÇÃO TÉCNICA COMPLETA DAS FUNÇÕES

### 🔧 Módulo de Funções de Validação

#### `validar_formato_id_produto(id_produto)`

**Propósito:** Valida rigorosamente se o ID do produto segue o formato ABC-123.

**Parâmetros:**
- `id_produto` (string): ID a ser validado

**Retorno:** `True` se válido, `False` caso contrário

**Algoritmo Detalhado:**
1. Verifica se tem exatamente 7 caracteres
2. Confirma que os 3 primeiros são letras maiúsculas usando `isupper()` e `isalpha()`
3. Verifica se o 4º caractere é hífen (-)
4. Confirma que os 3 últimos são números usando `isdigit()`

**Exemplo:** `validar_formato_id_produto("ABC-123")` → `True`

**Complexidade:** O(1) - verificação de tamanho fixo

#### `validar_nome_produto(nome)`

**Propósito:** Valida se o nome atende aos critérios de negócio estabelecidos.

**Parâmetros:**
- `nome` (string): Nome a ser validado

**Retorno:** `True` se válido, `False` caso contrário

**Algoritmo:**
1. Verifica tamanho mínimo de 3 caracteres usando `len()`
2. Itera através de cada caractere verificando se é alfanumérico ou espaço
3. Rejeita caracteres especiais (@, #, $, etc.)

**Exemplo:** `validar_nome_produto("Arroz Integral")` → `True`

**Complexidade:** O(n) onde n é o tamanho do nome

#### `verificar_id_ja_existe(id_produto)`

**Propósito:** Verifica unicidade do ID no sistema, prevenindo duplicatas.

**Parâmetros:**
- `id_produto` (string): ID a ser verificado

**Retorno:** `True` se já existe, `False` caso contrário

**Algoritmo:** Busca linear através da lista global de produtos

**Complexidade:** O(n) onde n é o número de produtos cadastrados

### 🏗️ Módulo de Funções CRUD Principais

#### `cadastrar_novo_produto()`

**Propósito:** Orquestra o processo completo de cadastro com validação em múltiplas etapas.

**Retorno:** Dicionário do produto criado

**Fluxo de Execução:**
1. **Validação de ID:** Loop até obter ID válido e único
2. **Validação de Nome:** Loop até obter nome com critérios corretos
3. **Validação de Preço:** Try/except para garantir valor numérico positivo
4. **Validação de Quantidade:** Try/except para garantir inteiro positivo
5. **Validação de Categoria:** Loop até selecionar categoria válida
6. **Criação do Objeto:** Monta dicionário com todas as informações
7. **Persistência:** Adiciona produto à lista global `lista_produtos`
8. **Feedback:** Exibe confirmação com resumo das informações

**Tratamento de Erros:** Cada etapa tem seu próprio loop de validação

#### `exibir_lista_de_produtos()`

**Propósito:** Renderiza interface tabular profissional para visualização de dados.

**Algoritmo de Formatação:**
1. Verifica se há produtos cadastrados
2. Cria cabeçalho formatado usando f-strings com especificadores de largura
3. Itera através da lista calculando status do estoque
4. Exibe cada produto com formatação consistente
5. Adiciona rodapé com estatísticas

**Recursos Técnicos:**
- Formatação com `{'texto':<largura}` para alinhamento
- Cálculo dinâmico de status: `"BAIXO" if quantidade < 5 else "OK"`
- Separadores visuais de 80 caracteres

#### `atualizar_informacoes_produto()`

**Propósito:** Permite modificação segura de dados de produtos existentes.

**Opções de Atualização:**
1. **Preço:** Validação de valor positivo
2. **Nome:** Reutiliza `validar_nome_produto()`
3. **Quantidade:** Sistema único de operadores +/-

**Função Auxiliar Interna:**

```python
def atualizar_informacao(novo_valor, chave):
    for produto in lista_produtos:
        if produto["id"] == id_para_atualizar:
            produto[chave] = novo_valor
```

**Sistema de Estoque Avançado:**
- Operador "+" para adicionar unidades
- Operador "-" para remover com validação de estoque suficiente
- Alerta automático quando estoque atinge zero

#### `excluir_produto_do_sistema()`

**Propósito:** Remove produtos com múltiplas camadas udział

System: I apologize for the oversight. Based on your request to remove the "estabelecimento" reference and keep everything together in Markdown, I’ve revised the document to exclude the specific mention of "pequenos e médios estabelecimentos comerciais" from the "Objetivo do Sistema" section. The entire content is now provided as a single, cohesive Markdown artifact, ensuring no separation of sections and maintaining all original details except for the requested change.

<xaiArtifact artifact_id="fcbd8ff5-52e2-42c4-ab5d-8b9f8977a74c" artifact_version_id="c09e0205-9544-4c97-823e-d4aa91164ef7" title="Sistema de Gerenciamento de Produtos.md" contentType="text/markdown">

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

### ✅ 4. Sistema1910 de Exclusão de Produtos

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

## 🚫 Funcionalidades Planejadas (Não Implementadas)

### **Funcionalidade 9: Sistema de Vendas** `processar_venda_de_produto()`

**Propósito futuro:** Processar vendas e reduzir estoque automaticamente

**Funcionalidades previstas:**
- Seleção de produto por ID
- Definição de quantidade vendida
- Validação de disponibilidade em estoque
- Atualização automática de quantidade
- Registro de histórico de vendas

### **Funcionalidade 10: Sistema de Descontos** `aplicar_desconto_em_produto()`

**Propósito futuro:** Sistema de gestão de promoções e descontos

**Funcionalidades previstas:**
- Seleção de produto(s) para desconto
- Opções de desconto percentual ou valor fixo
- Validação de novo preço
- Período de validade do desconto
- Histórico de promoções aplicadas

## 🔧 Sistema de Validações Detalhado

### **Validação de ID de Produto**

```python
def validar_formato_id_produto(id_produto):
    """
    Valida se o ID segue o formato ABC-123
    
    Regras:
    - Exatamente 7 caracteres
    - 3 primeiros: letras maiúsculas
    - 4º caractere: hífen (-)
    - 3 últimos: números
    """
    if len(id_produto) != 7:
        print("❌ ID deve ter exatamente 7 caracteres!")
        return False
    
    # Validação das letras (posições 0-2)
    for i in range(3):
        if not id_produto[i].isupper() or not id_produto[i].isalpha():
            print("❌ Os 3 primeiros caracteres devem ser letras maiúsculas!")
            return False
    
    # Validação do hífen (posição 3)
    if id_produto[3] != '-':
        print("❌ O 4º caractere deve ser um hífen (-)!")
        return False
    
    # Validação dos números (posições 4-6)
    for i in range(4, 7):
        if not id_produto[i].isdigit():
            print("❌ Os 3 últimos caracteres devem ser números!")
            return False
    
    return True
```

**Exemplos práticos:**

```text
✅ Válidos: "ABC-123", "XYZ-999", "DEF-001"
❌ Inválidos: "abc-123", "AB-123", "ABC123", "ABC-12A"
```

### **Validação de Nome de Produto**

```python
def validar_nome_produto(nome):
    """
    Valida se o nome atende aos critérios estabelecidos
    
    Regras:
    - Mínimo 3 caracteres
    - Apenas letras, números e espaços
    - Sem caracteres especiais
    """
    if len(nome) < 3:
        print("❌ Nome deve ter pelo menos 3 caracteres!")
        return False
    
    for char in nome:
        if not (char.isalnum() or char == ' '):
            print("❌ Nome deve conter apenas letras, números e espaços!")
            return False
    
    return True
```

**Exemplos práticos:**

```text
✅ Válidos: "Arroz", "Feijão Preto", "Açúcar Cristal 1kg"
❌ Inválidos: "Ar", "Açúcar@", "Feijão#1", "Arroz_integral"
```

### **Validação de Preço**

```python
# Implementada com try/except no cadastro
while True:
    try:
        preco = float(input("Digite o preço do produto: R$"))
        if preco <= 0:
            print("❌ Preço deve ser maior que zero!")
            continue
        break
    except ValueError:
        print("❌ Digite um valor numérico válido!")
```

**Exemplos práticos:**

```text
✅ Válidos: 10.50, 5.99, 100.0, 0.01
❌ Inválidos: -5.50, 0, "abc", ""
```

### **Validação de Quantidade**

```python
# Implementada com try/except no cadastro
while True:
    try:
        quantidade = int(input("Digite a quantidade: "))
        if quantidade < 0:
            print("❌ Quantidade não pode ser negativa!")
            continue
        break
    except ValueError:
        print("❌ Digite um número inteiro válido!")
```

**Exemplos práticos:**

```text
✅ Válidos: 0, 1, 50, 1000
❌ Inválidos: -1, 1.5, "abc", ""
```

## 🎨 Interface e Experiência do Usuário

### **Design Visual da Interface**

O sistema utiliza elementos visuais para melhorar a experiência:

- **Emojis informativos:** 📦 ✅ ❌ ⚠️ 💰 👋
- **Separadores visuais:** Linhas de `=` e `-` para organização
- **Títulos centralizados:** Destaque para seções importantes
- **Formatação consistente:** Alinhamento e espaçamento padronizados

### **Padrões de Mensagem**

```python
# Padrões utilizados no sistema
print("✅ Operação realizada com sucesso!")      # Sucesso
print("❌ Erro: [descrição do problema]")        # Erro
print("⚠️ Atenção: [aviso importante]")          # Aviso
print("📋 Informação: [dados informativos]")    # Informação
print("💰 Valor: R$ [quantia]")                 # Valores monetários
```

### **Fluxo de Navegação**

1. **Menu Principal** → **Seleção de Opção** → **Execução da Função**
2. **Validação de Entrada** → **Processamento** → **Feedback**
3. **Retorno ao Menu** ou **Continuação do Fluxo**

## 🐛 Tratamento de Erros e Robustez

O sistema implementa tratamento abrangente de erros em múltiplas camadas:

### **Tipos de Erro Tratados**

**1. Erros de Conversão de Tipo:**

```python
try:
    opcao = int(input_menu)
except ValueError:
    print("❌ Erro: Digite apenas números de 1 a 10.")
```

**2. Validação de Range de Valores:**

```python
if opcao < 1 or opcao > 10:
    print("❌ Opção inválida! Escolha entre 1-10.")
```

**3. Verificações de Estado do Sistema:**

```python
if not lista_produtos:
    print("📋 Nenhum produto cadastrado.")
    return
```

**4. Loops de Validação Persistente:**

```python
while True:
    dados = input("Digite os dados: ")
    if validar_dados(dados):
        break
    print("❌ Dados inválidos. Tente novamente.")
```

### **Estratégias de Recuperação de Erro**

- **Loops de Retry:** Sistema não falha, permite correção
- **Mensagens Específicas:** Cada erro tem explicação clara
- **Validação Preventiva:** Múltiplas verificações antes de processar
- **Estados de Fallback:** Sistema sempre retorna a estado válido

## 📚 DOCUMENTAÇÃO TÉCNICA COMPLETA DAS FUNÇÕES

### 🔧 Módulo de Funções de Validação

#### `validar_formato_id_produto(id_produto)`

**Propósito:** Valida rigorosamente se o ID do produto segue o formato ABC-123.

**Parâmetros:**
- `id_produto` (string): ID a ser validado

**Retorno:** `True` se válido, `False` caso contrário

**Algoritmo Detalhado:**
1. Verifica se tem exatamente 7 caracteres
2. Confirma que os 3 primeiros são letras maiúsculas usando `isupper()` e `isalpha()`
3. Verifica se o 4º caractere é hífen (-)
4. Confirma que os 3 últimos são números usando `isdigit()`

**Exemplo:** `validar_formato_id_produto("ABC-123")` → `True`

**Complexidade:** O(1) - verificação de tamanho fixo

#### `validar_nome_produto(nome)`

**Propósito:** Valida se o nome atende aos critérios de negócio estabelecidos.

**Parâmetros:**
- `nome` (string): Nome a ser validado

**Retorno:** `True` se válido, `False` caso contrário

**Algoritmo:**
1. Verifica tamanho mínimo de 3 caracteres usando `len()`
2. Itera através de cada caractere verificando se é alfanumérico ou espaço
3. Rejeita caracteres especiais (@, #, $, etc.)

**Exemplo:** `validar_nome_produto("Arroz Integral")` → `True`

**Complexidade:** O(n) onde n é o tamanho do nome

#### `verificar_id_ja_existe(id_produto)`

**Propósito:** Verifica unicidade do ID no sistema, prevenindo duplicatas.

**Parâmetros:**
- `id_produto` (string): ID a ser verificado

**Retorno:** `True` se já existe, `False` caso contrário

**Algoritmo:** Busca linear através da lista global de produtos

**Complexidade:** O(n) onde n é o número de produtos cadastrados

### 🏗️ Módulo de Funções CRUD Principais

#### `cadastrar_novo_produto()`

**Propósito:** Orquestra o processo completo de cadastro com validação em múltiplas etapas.

**Retorno:** Dicionário do produto criado

**Fluxo de Execução:**
1. **Validação de ID:** Loop até obter ID válido e único
2. **Validação de Nome:** Loop até obter nome com critérios corretos
3. **Validação de Preço:** Try/except para garantir valor numérico positivo
4. **Validação de Quantidade:** Try/except para garantir inteiro positivo
5. **Validação de Categoria:** Loop até selecionar categoria válida
6. **Criação do Objeto:** Monta dicionário com todas as informações
7. **Persistência:** Adiciona produto à lista global `lista_produtos`
8. **Feedback:** Exibe confirmação com resumo das informações

**Tratamento de Erros:** Cada etapa tem seu próprio loop de validação

#### `exibir_lista_de_produtos()`

**Propósito:** Renderiza interface tabular profissional para visualização de dados.

**Algoritmo de Formatação:**
1. Verifica se há produtos cadastrados
2. Cria cabeçalho formatado usando f-strings com especificadores de largura
3. Itera através da lista calculando status do estoque
4. Exibe cada produto com formatação consistente
5. Adiciona rodapé com estatísticas

**Recursos Técnicos:**
- Formatação com `{'texto':<largura}` para alinhamento
- Cálculo dinâmico de status: `"BAIXO" if quantidade < 5 else "OK"`
- Separadores visuais de 80 caracteres

#### `atualizar_informacoes_produto()`

**Propósito:** Permite modificação segura de dados de produtos existentes.

**Opções de Atualização:**
1. **Preço:** Validação de valor positivo
2. **Nome:** Reutiliza `validar_nome_produto()`
3. **Quantidade:** Sistema único de operadores +/-

**Função Auxiliar Interna:**

```python
def atualizar_informacao(novo_valor, chave):
    for produto in lista_produtos:
        if produto["id"] == id_para_atualizar:
            produto[chave] = novo_valor
```

**Sistema de Estoque Avançado:**
- Operador "+" para adicionar unidades
- Operador "-" para remover com validação de estoque suficiente
- Alerta automático quando estoque atinge zero

#### `excluir_produto_do_sistema()`

**Propósito:** Remove produtos com múltiplas camadas de segurança.

**Protocolo de Segurança:**
1. Validação de existência do produto
2. Verificação de regra de negócio (não excluir se estoque = 0)
3. Confirmação explícita do usuário (S/N)
4. Validação da resposta de confirmação
5. Execução da remoção ou cancelamento

**Regras de Negócio:** Impede exclusão de produtos sem estoque

### 🔍 Módulo de Busca e Ordenação

#### `buscar_produto_no_sistema()`

**Propósito:** Motor de busca flexível com três modalidades otimizadas.

**Modalidades de Busca:**
1. **Por Nome:** Busca parcial e case-insensitive usando `in` e `.lower()`
2. **Por ID:** Busca exata com comparação direta
3. **Por Categoria:** Busca exata ignorando case

**Implementação com List Comprehension:**

```python
produtos_encontrados = [p for p in lista_produtos if critério_de_busca]
```

**Tratamento de Resultados:** Exibe produtos encontrados ou mensagem informativa

#### `ordenar_produtos_por_criterio()`

**Propósito:** Sistema versátil de ordenação com persistência opcional.

**Critérios Disponíveis:**
1. Nome (A-Z) com `key=lambda x: x['nome'].lower()`
2. Preço (menor→maior) com `key=lambda x: x['preco']`
3. Quantidade (menor→maior) com `key=lambda x: x['quantidade']`
4. Categoria (A-Z) com `key=lambda x: x['categoria']`

**Preservação de Dados:** Usa `lista_produtos.copy()` antes de ordenar

**Persistência Opcional:** Usuário escolhe se mantém nova ordem como padrão

### 📊 Módulo de Relatórios e Análises

#### `gerar_relatorios_do_sistema()`

**Propósito:** Gera análises estatísticas e financeiras abrangentes.

**Tipos de Relatório:**

**1. Valor Total do Estoque:**

```python
valor_total = sum(p['preco'] * p['quantidade'] for p in lista_produtos)
```

**2. Produtos com Estoque Baixo:**

```python
produtos_baixo = [p for p in lista_produtos if p['quantidade'] < 5]
```

**3. Relatório Completo com Agrupamento:**

```python
categorias = {}
for produto in lista_produtos:
    cat = produto['categoria']
    if cat not in categorias:
        categorias[cat] = {'count': 0, 'valor': 0}
    categorias[cat]['count'] += 1
    categorias[cat]['valor'] += produto['preco'] * produto['quantidade']
```

**Análises Geradas:**
- Valor total do estoque
- Contagem de produtos por categoria
- Valor financeiro por categoria
- Lista de produtos com estoque crítico

### 🔄 Sistema de Controle Principal

#### `exibir_menu()`

**Propósito:** Interface principal do sistema.

**Design:** Menu numerado com 10 opções claramente descritas

#### Loop Principal de Controle

**Estrutura:**

```python
while True:
    exibir_menu()
    input_menu = input("Selecione uma opção: ")
    
    try:
        opcao = int(input_menu)
        # Estrutura if/elif para direcionamento
    except ValueError:
        # Tratamento de erro
```

**Características:**
- **Try/except:** Captura erros de conversão para inteiro
- **Estrutura condicional:** Direciona para função correspondente
- **Validação de range:** Verifica se opção está entre 1-10
- **Loop infinito controlado:** Continua até usuário escolher sair (opção 10)
- **Formatação visual:** Linha em branco entre iterações para organização

**Robustez:** Sistema nunca falha, sempre retorna ao menu principal

## 🚀 Como Usar o Sistema

### Pré-requisitos

- Python 3.6 ou superior instalado
- Terminal/Prompt de comando

### Instalação e Execução

1. **Clone ou baixe o repositório**

   ```bash
   git clone [url-do-repositorio]
   cd trabalho_larisse
   ```

2. **Execute o programa**

   ```bash
   python trabalho.py
   ```

## 📖 Exemplos Práticos de Uso

### 1. Cadastro de Produto

- Selecione a opção `1` no menu principal
- Digite um ID no formato `ABC-123`
- Insira o nome do produto (mínimo 3 caracteres)
- Defina o preço (valor positivo)
- Especifique a quantidade (número inteiro)
- Escolha uma categoria da lista

### 2. Listar Produtos

- Selecione a opção `4` no menu principal
- O sistema exibirá todos os produtos em formato tabular
- Verá também o status do estoque (OK/BAIXO)

### 3. Ordenar Produtos

- Selecione a opção `5` no menu principal
- Escolha um critério de ordenação (nome, preço, quantidade, categoria)
- Dec持ち
System: I apologize for the incomplete response. Below is the complete Markdown document with the "estabelecimento" reference removed from the "Objetivo do Sistema" section, presented as a single, cohesive artifact as requested. The content remains intact except for the specified change, and I’ve ensured all sections are included without separation.

<xaiArtifact artifact_id="d8b4ccc4-cfb5-43a1-a347-52dc904fb4e7" artifact_version_id="c5e09c5f-52e0-4b23-b3c6-2411418a4197" title="Sistema de Gerenciamento de Produtos.md" contentType="text/markdown">

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

## 🚫 Funcionalidades Planejadas (Não Implementadas)

### **Funcionalidade 9: Sistema de Vendas** `processar_venda_de_produto()`

**Propósito futuro:** Processar vendas e reduzir estoque automaticamente

**Funcionalidades previstas:**
- Seleção de produto por ID
- Definição de quantidade vendida
- Validação de disponibilidade em estoque
- Atualização automática de quantidade
- Registro de histórico de vendas

### **Funcionalidade 10: Sistema de Descontos** `aplicar_desconto_em_produto()`

**Propósito futuro:** Sistema de gestão de promoções e descontos

**Funcionalidades previstas:**
- Seleção de produto(s) para desconto
- Opções de desconto percentual ou valor fixo
- Validação de novo preço
- Período de validade do desconto
- Histórico de promoções aplicadas

## 🔧 Sistema de Validações Detalhado

### **Validação de ID de Produto**

```python
def validar_formato_id_produto(id_produto):
    """
    Valida se o ID segue o formato ABC-123
    
    Regras:
    - Exatamente 7 caracteres
    - 3 primeiros: letras maiúsculas
    - 4º caractere: hífen (-)
    - 3 últimos: números
    """
    if len(id_produto) != 7:
        print("❌ ID deve ter exatamente 7 caracteres!")
        return False
    
    # Validação das letras (posições 0-2)
    for i in range(3):
        if not id_produto[i].isupper() or not id_produto[i].isalpha():
            print("❌ Os 3 primeiros caracteres devem ser letras maiúsculas!")
            return False
    
    # Validação do hífen (posição 3)
    if id_produto[3] != '-':
        print("❌ O 4º caractere deve ser um hífen (-)!")
        return False
    
    # Validação dos números (posições 4-6)
    for i in range(4, 7):
        if not id_produto[i].isdigit():
            print("❌ Os 3 últimos caracteres devem ser números!")
            return False
    
    return True
```

**Exemplos práticos:**

```text
✅ Válidos: "ABC-123", "XYZ-999", "DEF-001"
❌ Inválidos: "abc-123", "AB-123", "ABC123", "ABC-12A"
```

### **Validação de Nome de Produto**

```python
def validar_nome_produto(nome):
    """
    Valida se o nome atende aos critérios estabelecidos
    
    Regras:
    - Mínimo 3 caracteres
    - Apenas letras, números e espaços
    - Sem caracteres especiais
    """
    if len(nome) < 3:
        print("❌ Nome deve ter pelo menos 3 caracteres!")
        return False
    
    for char in nome:
        if not (char.isalnum() or char == ' '):
            print("❌ Nome deve conter apenas letras, números e espaços!")
            return False
    
    return True
```

**Exemplos práticos:**

```text
✅ Válidos: "Arroz", "Feijão Preto", "Açúcar Cristal 1kg"
❌ Inválidos: "Ar", "Açúcar@", "Feijão#1", "Arroz_integral"
```

### **Validação de Preço**

```python
# Implementada com try/except no cadastro
while True:
    try:
        preco = float(input("Digite o preço do produto: R$"))
        if preco <= 0:
            print("❌ Preço deve ser maior que zero!")
            continue
        break
    except ValueError:
        print("❌ Digite um valor numérico válido!")
```

**Exemplos práticos:**

```text
✅ Válidos: 10.50, 5.99, 100.0, 0.01
❌ Inválidos: -5.50, 0, "abc", ""
```

### **Validação de Quantidade**

```python
# Implementada com try/except no cadastro
while True:
    try:
        quantidade = int(input("Digite a quantidade: "))
        if quantidade < 0:
            print("❌ Quantidade não pode ser negativa!")
            continue
        break
    except ValueError:
        print("❌ Digite um número inteiro válido!")
```

**Exemplos práticos:**

```text
✅ Válidos: 0, 1, 50, 1000
❌ Inválidos: -1, 1