"""Funcionalidades principais:
    1. Cadastro de produtos:
    ● Adicionar produto:
    ○ ID (formato "ABC-123", onde ABC são 3 letras e 123 são 3 números).
    ○ Nome (sem caracteres especiais, apenas letras, números e espaços).
    ○ Preço (positivo, com validação para números decimais).
    ○ Quantidade (inteiro positivo, não pode ser zero no cadastro).
    ○ Categoria (fixas: "Alimentos", "Limpeza", "Eletrônicos", "Vestuário").
    ● Verificações:
    ○ Se o produto já existe antes de cadastrar.
    ○ ID único (não pode repetir).
    ○ Nome com no mínimo 3 caracteres.

    2. Atualização de produtos:
    ● Alterar informações:
    ○ Campos editáveis: preço, descrição, quantidade.
    ● Aumentar/diminuir estoque (entrada/saída de produtos). Exemplo:
    ○ +5 aumenta a quantidade.
    ○ -3 diminui (se houver estoque suficiente).
    ● Se quantidade for atualizada para zero, alertar "estoque esgotado".
    3. Exclusão de Produtos
    ● Remover produto do sistema:
    ○ Confirmação obrigatória: "Você realmente deseja remover [Nome do
    Produto]? (S/N)".
    ○ Impedir exclusão se o produto estiver sem estoque.

    4. Busca e listagem:
    ● Listar todos os produtos.
    ● Buscar por:
    ○ Nome;
    ○ ID; ou
    ○ Categoria.
    ● Filtrar produtos com estoque baixo (abaixo de um limite definido, a critério do aluno).
    5. Validação de dados:
    ● Impedir entrada inválida:
    ○ Preço negativo ou zero.
    ○ Quantidade não numérica.
    ○ Categoria inexistente.
    6. Interface de usuário (CLI ou GUI)
    ● Menu interativo no terminal (input + loops)."""

print("========================================================")
print("Bem-vindo ao Sistema de Gerenciamento de Produtos!")
print("========================================================\n")

# aqui abaixo estão as funções que implementam o menu principal do sistema
def exibir_menu():
    """
    Função responsável por exibir o menu principal do sistema
    Mostra todas as opções disponíveis para o usuário
    """
    print("===MENU PRINCIPAL===")
    print("1. Cadastrar Produto")
    print("2. Atualizar Produto")
    print("3. Excluir Produto")
    print("4. Listar Produtos")
    print("5. Ordenar Produtos")
    print("6. Buscar Produto")
    print("7. Relatórios:(Valor Total/ Estoque Baixo)")
    print("8. Vender produto")
    print("9. Aplicar Desconto")
    print("10. Visualizar Histórico de vendas")
    print("11. Sair")
    
# esta lista abaixo será responsável por armazenar todos os produtos cadastrados no sistema, será util no final para pode retornar todos os dados.
lista_produtos = [    {
        'id': 'ALM-101',
        'nome': 'Arroz Integral',
        'preco': 12.50,
        'quantidade': 30,
        'categoria': 'Alimentos'
    },
    {
        'id': 'LMP-202',
        'nome': 'Detergente Neutro',
        'preco': 3.75,
        'quantidade': 50,
        'categoria': 'Limpeza'
    },
    {
        'id': 'ELT-303',
        'nome': 'Fone de Ouvido',
        'preco': 89.90,
        'quantidade': 15,
        'categoria': 'Eletrônicos'
    },
    {
        'id': 'VST-404',
        'nome': 'Camiseta Básica',
        'preco': 25.00,
        'quantidade': 40,
        'categoria': 'Vestuário'
    },
    {
        'id': 'ABC-123',
        'nome': 'Banana',
        'preco': 4.00,
        'quantidade': 25,
        'categoria': 'Alimentos'
    }
]
categorias_validas = ["Alimentos", "Limpeza", "Eletrônicos", "Vestuário"]
historico_de_vendas = []

def validar_formato_id_produto(id_produto):
    """
    Valida se o ID do produto está no formato correto ABC-123
    separando no caso, temos 3 letras maiúsculas, um hífen e 3 números
    o parametro é id_produto (string) - no caso o id do produto a ser validado
    a função retorna True se o formato estiver correto, False caso contrário
    """
    # Verifica se tem exatamente 7 caracteres
    if len(id_produto) != 7:
        return False
    
    # Verifica se os 3 primeiros caracteres são letras maiúsculas
    for i in range(3):
        if not id_produto[i].isupper() or not id_produto[i].isalpha():
            return False
    
    # Verifica se o 4º caractere é hífen
    if id_produto[3] != '-':
        return False
    
    # Verifica se os 3 últimos caracteres são números
    for i in range(4, 7):
        if not id_produto[i].isdigit():
            return False
    
    return True

def validar_nome_produto(nome):
    """
    Valida se o nome do produto atende aos critérios:
    - Pelo menos 3 caracteres
    - Apenas letras, números e espaços
    Parâmetro: nome (string) - Nome a ser validado
    Retorna: True se válido, False caso contrário
    """
    # Verifica tamanho mínimo
    if len(nome) < 3:
        return False
    
    # Verifica se contém apenas caracteres permitidos
    for char in nome:
        if not (char.isalnum() or char.isspace()):
            return False
    
    return True

def verificar_id_ja_existe(id_produto):
    """
    Verifica se um ID de produto já existe na lista de produtos
    Parâmetro: id_produto (string) - ID a ser verificado
    Retorna: True se já existe, False caso contrário
    """
    for produto in lista_produtos:
        if produto['id'] == id_produto:
            return True
    return False

def cadastrar_novo_produto():
    """
    Função para cadastrar um novo produto no sistema
    Solicita e valida todas as informações necessárias do produto
    Adiciona o produto válido à lista global de produtos
    """
    print("\n===CADASTRO DE PRODUTO===")
    
    # Validação do ID do produto
    while True:
        id_produto = input("Digite o ID do produto (formato 'ABC-123'): ").upper()
        
        # Verifica se o formato está correto
        if not validar_formato_id_produto(id_produto):
            print("Erro: ID deve estar no formato 'ABC-123' (3 letras maiúsculas, hífen, 3 números)")
            continue
            
        # Verifica se o ID já existe no sistema
        if verificar_id_ja_existe(id_produto):
            print("Erro: ID do produto já existe.")
            continue
            
        # ID válido e único, pode prosseguir
        break
    
    # Validação do nome do produto
    while True:
        nome_produto = input("Digite o nome do produto: ").strip()
        
        # Verifica se o nome atende aos critérios
        if validar_nome_produto(nome_produto):
            break
        print("Erro: Nome deve ter pelo menos 3 caracteres e conter apenas letras, números e espaços.")
    
    # Validação do preço do produto
    while True:
        try:
            preco_produto = float(input("Digite o preço do produto: R$ "))
            
            # Verifica se o preço é positivo
            if preco_produto <= 0:
                print("Erro: Preço deve ser positivo.")
                continue
            break
        except ValueError:
            print("Erro: Digite um preço válido.")
    
    # Validação da quantidade do produto
    while True:
        try:
            quantidade_produto = int(input("Digite a quantidade do produto: "))
            
            # Verifica se a quantidade é positiva
            if quantidade_produto <= 0:
                print("Erro: Quantidade deve ser um número inteiro positivo.")
                continue
            break
        except ValueError:
            print("Erro: Digite uma quantidade válida.")
    
    # Validação da categoria do produto
    while True:
        print(f"Categorias disponíveis: {', '.join(categorias_validas)}")
        categoria_produto = input("Digite a categoria do produto: ").strip()
        
        # Verifica se a categoria é válida
        if categoria_produto in categorias_validas:
            break
        print("Erro: Categoria inválida.")
    
    # Criar o dicionário do produto com todas as informações
    produto = {
        'id': id_produto,
        'nome': nome_produto,
        'preco': preco_produto,
        'quantidade': quantidade_produto,
        'categoria': categoria_produto
    }
    
    # Adiciona o produto à lista global
    lista_produtos.append(produto)
    
    # Confirma o cadastro para o usuário
    print(f"\nProduto '{nome_produto}' cadastrado com sucesso!")
    print(f"ID: {id_produto} | Preço: R$ {preco_produto:.2f} | Quantidade: {quantidade_produto}")
    return produto

def atualizar_informacoes_produto():
    """
    Função para atualizar informações de um produto existente
    Permite editar preço, quantidade e categoria
    """
    print("\n===ATUALIZAÇÃO DE PRODUTO===\n")
    id_para_atualizar = input("Digite o id do produto que você deseja atualizar: ").upper()
    
    while not verificar_id_ja_existe(id_para_atualizar):
        print("Esse produto não existe")
        id_para_atualizar = input("Digite o id do produto que você deseja atualizar: ").upper()    

    # Menu para dizer o que você vai atualizar
    print("O que você deseja atualizar? ")
    print("1. Preço")
    print("2. Nome")
    print("3. Quantidade de estoque")

    opcao_para_editar = int(input("\nSelecione uma opção de 1 a 3: "))
    # Pede para digitar de novo caso aja erro
    while 0 > opcao_para_editar or opcao_para_editar > 3:
        opcao_para_editar = int(input("\nErro: Selecione uma opção de 1 a 3: "))

    def atualizar_informacao(novo_valor, chave):
      """
       Função genérica para atualizar uma informação específica de um produto.
       Mostra um loop que percorre a lista global: lista_produtos e modifica algum valor a partir de um id, que são os paramêtros
      """
      for i in lista_produtos:
        if i["id"] == id_para_atualizar:
          i[chave] = novo_valor

    # Atualização de cada uma das opções
    if opcao_para_editar == 1:
      novo_preco = float(input("Digite um novo preço: "))
      while novo_preco <=0:
          print("O novo preço deve ser superior a 0")
          novo_preco = float(input("Digite um novo preço: "))
      atualizar_informacao(novo_preco, "preco")    
      print("\nPreço atualizado com sucesso!\n")              
    elif opcao_para_editar == 2:
      novo_nome = input("Digite um novo nome: ")
      while not validar_nome_produto(novo_nome):
          print("Erro! Esse nome não é válido!")
          novo_nome = input("Digite um novo nome: ")
      atualizar_informacao(novo_nome, "nome")
      print("\nNome atualizado com sucesso!\n")
    elif opcao_para_editar == 3:
      operacao = input("Digite + pra aumentar o estoque e - para subtrair: ")
      while operacao != "+" and operacao != "-":
          operacao = input("Você digitou algo errado! Digite - ou +: ")
      for i in lista_produtos:
          if i["id"] == id_para_atualizar:
            if operacao == "+":
                quantidade = int(input("Digite o valor que você quer aumentar: + "))
                nova_quantidade = i["quantidade"] + quantidade
            
            elif operacao == "-":
                quantidade = int(input("Digite o valor que você quer diminuir: - "))  
                while quantidade > i["quantidade"]:
                  print(f"Erro: Não há estoque suficiente para remover essa quantidade.")
                  quantidade = int(input(f"Digite um valor de no máximo {i["quantidade"]}: - "))  
                nova_quantidade = i["quantidade"] - quantidade
   
      atualizar_informacao(nova_quantidade, "quantidade")
      print("\nEstoque atualizado com sucesso!\n")
      # Caso o estoque zere
      if nova_quantidade == 0:
          print("Estoque esgotado!") 
    
    else:
        print("Inválido! Digite um número de 1 a 3")

def excluir_produto_do_sistema():
    """
    Função para remover um produto do sistema
    Solicita confirmação antes de excluir
    """
    print("\n===EXCLUIR PRODUTO===\n")
    id_para_excluir = input("Digite o id do produto que você deseja excluir: ").upper()
    
    while not verificar_id_ja_existe(id_para_excluir):
        print("Esse produto não existe")
        id_para_excluir = input("Digite o id do produto que você deseja excluir: ").upper()
    # Verifica se o produto está sem estoque
    for i in lista_produtos:
      if i['id'] == id_para_excluir:
        if i["quantidade"] == 0:
            print("Não é possível excluir produto sem estoque!")
            break
        # Confirmação se o usuário quer mesmo exluir o produto
        confirmacao = input(f"Confirmação obrigatória: Você realmente deseja remover {i['nome']}? (S/N) ").upper()
        while confirmacao != "S" and confirmacao != "N":
            confirmacao = input("Digite S para continuar a exclusão e N para cancelar: ").upper()
        if confirmacao == "S":
            lista_produtos.remove(i)
            print(f"\nExclusão de {i['nome']} feita com sucesso!\n")
            break
        else:
            print("\nExclusão cancelada\n")
    
def exibir_lista_de_produtos():
    """
    Função para exibir todos os produtos cadastrados
    Mostra os produtos na ordem original de cadastro
    Inclui informações de ID, nome, preço, quantidade, categoria e status do estoque
    """
    # Verifica se há produtos cadastrados
    if not lista_produtos:
        print("\nNenhum produto cadastrado.")
        return
    
    # Cabeçalho da listagem
    print("\nLISTA DE PRODUTOS (ordem de cadastro):")
    print("-" * 90)
    print(f"{'ID':<8} {'Nome':<20} {'Preço':<10} {'Qtd':<5} {'Categoria':<15} {'Preço c/Desc':<15}") # eu usei este estilo de formatação que achei comumente interessante. Eu posso muito bem setar a quantidade de caracteres que eu quero de espaço entre as colunas, tornando a exibição bem mais organizada.
    print("-" * 90)
    
    # Percorre todos os produtos e exibe suas informações
    for produto in lista_produtos:
        # Define status do estoque (baixo se menor que 5 unidades)
        status = "BAIXO" if produto['quantidade'] < 5 else "OK"

        # Define o preço com desconto, se estiver presente em produto
        preco_com_desconto = f"R${produto['preco_com_desconto']:.2f}" if 'preco_com_desconto' in produto else "   --"
        
        # Formata e exibe as informações do produto
        print(f"{produto['id']:<8} {produto['nome']:<20} R${produto['preco']:<9.2f} "
              f"{produto['quantidade']:<5} {produto['categoria']:<15} {preco_com_desconto:<15} {status}")
    
    # logo abaixo é tipo um rodapé com o total de produtos cadastrados
    print("-" * 90)
    print(f"Total de produtos: {len(lista_produtos)}")

def ordenar_produtos_por_criterio():
    """
    Função para ordenar e exibir produtos por diferentes critérios
    Oferece opções de ordenação por nome, preço, quantidade ou categoria
    Permite salvar a nova ordenação como padrão
    """
    # Verifica se há produtos para ordenar
    if not lista_produtos:
        print("\nNenhum produto cadastrado.")
        return
    
    # Menu de opções de ordenação
    print("\n===ORDENAÇÃO DE PRODUTOS===")
    print("Escolha o critério de ordenação:")
    print("1. Por Nome (A-Z)")
    print("2. Por Preço (do mais barato ao mais caro)")
    print("3. Por Quantidade em estoque (do menor para o maior)")
    print("4. Por Categoria (A-Z)")
    
    try:
        opcao = int(input("Digite a opção: "))
        
        # Cria uma cópia da lista para não alterar a original inicialmente
        produtos_ordenados = lista_produtos.copy()
        
        # Aplica a ordenação conforme a opção escolhida
        if opcao == 1:
            # Ordena por nome (sem diferenciação de maiúsculas/minúsculas)
            produtos_ordenados.sort(key=lambda x: x['nome'].lower())
            print("\nProdutos ordenados por NOME (A-Z):")
        elif opcao == 2:
            # Ordena por preço (menor para maior)
            produtos_ordenados.sort(key=lambda x: x['preco'])
            print("\nProdutos ordenados por PREÇO (mais barato → mais caro):")
        elif opcao == 3:
            # Ordena por quantidade (menor para maior)
            produtos_ordenados.sort(key=lambda x: x['quantidade'])
            print("\nProdutos ordenados por QUANTIDADE (menor → maior estoque):")
        elif opcao == 4:
            # Ordena por categoria (ordem alfabética)
            produtos_ordenados.sort(key=lambda x: x['categoria'])
            print("\nProdutos ordenados por CATEGORIA (A-Z):")
        else:
            print("Opção inválida.")
            return
    
    except ValueError:
        print("Entrada inválida.")
        return
    
    # Exibe a lista ordenada
    print("-" * 80)
    print(f"{'ID':<8} {'Nome':<20} {'Preço':<10} {'Qtd':<5} {'Categoria':<15}")
    print("-" * 80)
    
    for produto in produtos_ordenados:
        status = "BAIXO" if produto['quantidade'] < 5 else "OK"
        print(f"{produto['id']:<8} {produto['nome']:<20} R${produto['preco']:<9.2f} "
              f"{produto['quantidade']:<5} {produto['categoria']:<15} {status}")
    
    print("-" * 80)
    print(f"Total de produtos: {len(lista_produtos)}")
    
    # Pergunta se quer salvar a nova ordenação
    try:
        salvar = input("\nDeseja salvar esta ordenação como nova ordem padrão? (S/N): ").upper()
        if salvar == 'S':
            # Substitui a lista original pela lista ordenada
            lista_produtos[:] = produtos_ordenados
            print("Nova ordem salva como padrão!")
        else:
            print("Ordem não foi salva. Lista mantém ordem original.")
    except:
        print("Entrada inválida. Ordem não foi salva.")

def buscar_produto_no_sistema():
    """
    Função para buscar produtos no sistema por diferentes critérios
    Permite busca por nome (parcial), ID (exato) ou categoria
    Exibe todos os produtos encontrados que correspondem ao critério
    """
    # Verifica se há produtos para buscar
    if not lista_produtos:
        print("\nNenhum produto cadastrado.")
        return
    
    # Menu de opções de busca
    print("\n===BUSCAR PRODUTO===")
    print("Buscar por:")
    print("1. Nome")
    print("2. ID")
    print("3. Categoria")
    
    try:
        opcao = int(input("Digite a opção: "))
        
        # Realiza a busca conforme a opção escolhida
        if opcao == 1:
            # Busca por nome (permite busca parcial, sem diferenciação de maiúsculas)
            termo = input("Digite o nome (ou parte do nome): ").lower()
            produtos_encontrados = [p for p in lista_produtos if termo in p['nome'].lower()]
            tipo_busca = "nome"
            
        elif opcao == 2:
            # Busca por ID (busca exata)
            termo = input("Digite o ID: ").upper()
            produtos_encontrados = [p for p in lista_produtos if p['id'] == termo]
            tipo_busca = "ID"
            
        elif opcao == 3:
            # Busca por categoria (busca exata, sem diferenciação de maiúsculas)
            termo = input("Digite a categoria: ")
            produtos_encontrados = [p for p in lista_produtos if p['categoria'].lower() == termo.lower()]
            tipo_busca = "categoria"
            
        else:
            print("Opção inválida.")
            return
    
    except ValueError:
        print("Entrada inválida.")
        return
    
    # Exibe os resultados da busca
    if produtos_encontrados:
        print(f"\nProdutos encontrados para {tipo_busca} '{termo}':")
        print("-" * 80)
        print(f"{'ID':<8} {'Nome':<20} {'Preço':<10} {'Qtd':<5} {'Categoria':<15}")
        print("-" * 80)
        
        # Exibe cada produto encontrado
        for produto in produtos_encontrados:
            status = "BAIXO" if produto['quantidade'] < 5 else "OK"
            print(f"{produto['id']:<8} {produto['nome']:<20} R${produto['preco']:<9.2f} "
                  f"{produto['quantidade']:<5} {produto['categoria']:<15} {status}")
        
        print("-" * 80)
        print(f"Total encontrado: {len(produtos_encontrados)}")
    else:
        print(f"\nNenhum produto encontrado para {tipo_busca} '{termo}'.")

def gerar_relatorios_do_sistema():
    """
    Função para gerar diferentes tipos de relatórios do sistema
    Oferece relatórios de valor total, estoque baixo e relatório completo
    Calcula e exibe estatísticas importantes do estoque
    """
    # Verifica se há produtos para gerar relatórios
    if not lista_produtos:
        print("\nNenhum produto cadastrado.")
        return
    
    # Menu de tipos de relatórios
    print("\n===RELATÓRIOS===")
    print("1. Valor Total do Estoque")
    print("2. Produtos com Estoque Baixo")
    print("3. Relatório Completo")
    
    try:
        opcao = int(input("Digite a opção: "))
        
        if opcao == 1:
            # Relatório 1: Valor total do estoque
            # Calcula o valor total multiplicando preço por quantidade de cada produto
            valor_total = sum(p['preco'] * p['quantidade'] for p in lista_produtos)
            print(f"\nVALOR TOTAL DO ESTOQUE: R$ {valor_total:.2f}")
            
        elif opcao == 2:
            # Relatório 2: Produtos com estoque baixo
            limite = 5  # Define o limite para considerar estoque baixo
            produtos_baixo = [p for p in lista_produtos if p['quantidade'] < limite]
            
            print(f"\nPRODUTOS COM ESTOQUE BAIXO (menos de {limite} unidades):")
            if produtos_baixo:
                print("-" * 80)
                print(f"{'ID':<8} {'Nome':<20} {'Preço':<10} {'Qtd':<5} {'Categoria':<15}")
                print("-" * 80)
                
                # Exibe cada produto com estoque baixo
                for produto in produtos_baixo:
                    print(f"{produto['id']:<8} {produto['nome']:<20} R${produto['preco']:<9.2f} "
                          f"{produto['quantidade']:<5} {produto['categoria']:<15}")
                
                print("-" * 80)
                print(f"Total com estoque baixo: {len(produtos_baixo)}")
            else:
                print("Todos os produtos têm estoque adequado!")
                
        elif opcao == 3:
            # Relatório 3: Relatório completo
            # Calcula valor total do estoque
            valor_total = sum(p['preco'] * p['quantidade'] for p in lista_produtos)
            produtos_baixo = [p for p in lista_produtos if p['quantidade'] < 5]
            
            # Agrupa produtos por categoria para estatísticas
            categorias = {}
            for produto in lista_produtos:
                cat = produto['categoria']
                if cat not in categorias:
                    categorias[cat] = {'count': 0, 'valor': 0}
                categorias[cat]['count'] += 1
                categorias[cat]['valor'] += produto['preco'] * produto['quantidade']
            
            # Exibe o relatório completo
            print("\nRELATÓRIO COMPLETO DO ESTOQUE")
            print("=" * 50)
            print(f"Valor total do estoque: R$ {valor_total:.2f}")
            print(f"Total de produtos: {len(lista_produtos)}")
            print(f"Produtos com estoque baixo: {len(produtos_baixo)}")
            
            # Resumo por categoria
            print("\nRESUMO POR CATEGORIA:")
            print("-" * 40)
            for cat, dados in categorias.items():
                print(f"{cat}: {dados['count']} produtos | R$ {dados['valor']:.2f}")
            
            # Lista produtos com estoque baixo se houver
            if produtos_baixo:
                print(f"\nPRODUTOS COM ESTOQUE BAIXO:")
                for produto in produtos_baixo:
                    print(f"- {produto['nome']} ({produto['id']}): {produto['quantidade']} unidades")
        else:
            print("Opção inválida.")
            
    except ValueError:
        print("Entrada inválida.")
    
def processar_venda_de_produto():
    """
    Função para processar a venda de produtos
    Reduz a quantidade em estoque quando um produto é vendido
    """
    print("\n===Menu de Venda===")
    # Verifica se há produtos para buscar
    if len(lista_produtos) == 0:
        print("\nNenhum produto cadastrado.")
        
    # Procurar produto por ID
    id_para_vender = input("\nDigite o id do produto que você deseja vender: ").upper()
    
    while not verificar_id_ja_existe(id_para_vender):
        print("Esse produto não existe")
        id_para_vender = input("Digite o id do produto que você deseja vender: ").upper()
    
    # Verifica se é valida a quantidade 
    quantidade = int(input("Digite quantos produtos você deseja vender: "))
    
    for i in lista_produtos:
      if i['id'] == id_para_vender:
        while quantidade <1 or quantidade>i['quantidade']:
          print(f"Você deve digitar um número entre 0 e {i['quantidade']}")
          quantidade = int(input("Digite quantos produtos você deseja vender: "))

    # Data
    dia = int(input("Digite o dia: "))
    while dia<1 or dia>31:
      print("Dia inválido!")
      dia = int(input("Digite um número de 1 a 31: "))
    
    mes = int(input("Digite o mês no formato MM: "))
    while len(str(mes)) == 2 and mes<1 or mes>12 :
        print("Mês inválido!")
        mes = int(input("Digite o mês no formato MM de 1 a 12: "))
    mes = str(mes).zfill(2)

    ano = int(input("Digite o ano no formato AAAA: "))
    while len(str(ano)) != 4:
      print("Esse ano é inválido!")
      ano = input("Digite o ano no formato AAAA: ")

    # Registrar venda
    for i in lista_produtos:
      if i['id'] == id_para_vender:
        i['quantidade'] = i['quantidade'] - quantidade
        novo_estoque = i['quantidade']
    # Cálculo de Preço total 
    for i in lista_produtos:
      if i['id'] == id_para_vender:
        preco = i['preco']
        preco_total = i['preco'] * quantidade
        nome = i['nome'] 
    print("\nProduto vendido com sucesso!")
    # Alerta de estoque vazio
    if novo_estoque == 0:
        print("Alerta: Estoque vazio!")
    # Recibo de venda
    preco_total_str = str(preco_total)
    largura = max(len(nome), len(preco_total_str))
    preco_formatado = f"R${preco:.2f}"
    preco_total_formatado = f"R${preco_total:.2f}"

    print("\n===RECIBO===")
    print(f"{'Nome do produto':40} {nome:>{largura}}")
    print(f"{'Quantidade de produtos em estoque':40} {novo_estoque:>{largura}}")
    print(f"{'Preço unitário':40} {preco_formatado:>{largura}}")
    print(f"{'Preço total':40} {preco_total_formatado:>{largura}}\n")
    
    # dicionário e lista com histórico de venda 
    produto_vendido = {"data":f"{dia}/{mes}/{ano}", "produto": nome, "quantidade_vendida": quantidade}
    historico_de_vendas.append(produto_vendido)

def visualizar_historico_de_vendas():
    print("\n===Histórico de vendas===\n")
    cont=0
    for i in historico_de_vendas:
      cont+=1
      print(f"\n{cont}.")
      print(i['data'])
      print(f"Produto: {i['produto']}")
      print(f"Qauntidade vendida: {i['quantidade_vendida']}\n")

def aplicar_desconto_em_produto():
    """
    Função para aplicar desconto no preço de produtos
    Permite reduzir o preço de produtos específicos
    """

    print("\n===Descontos===\n")
    desconto = int(input("Digite a porcentagem do desconto que deseja aplicar: "))
    
    while desconto>95 or desconto<1:
        print("Esse desconto não é válido!")
        desconto = int(input("Digite a porcentagem do desconto que deseja aplicar (Entre 1 e 95): "))
    
    categoria = input("Digite em qual categoria você deseja aplicar o desconto: ")
    while categoria not in categorias_validas:
        print("Erro: Essa categoria não está disponível")
        print(f"\nCategorias disponíveis: {', '.join(categorias_validas)}")
        categoria = input("Digite em qual categoria você deseja aplicar o desconto: ")
    print(f"\nDefinido {desconto}% de desconto na categoria {categoria}\n")

    for i in lista_produtos:
      if i['categoria'] == categoria:
        preco = i['preco']
        preco_com_desconto = preco * (1 - desconto / 100)
        i['preco_com_desconto'] = round(preco_com_desconto, 2)

#Ínicio do código para saída do menu
while True:
    # Exibe o menu principal para o usuário
    exibir_menu()
    input_menu = input("Selecione uma opção do menu: ")
    
    # Tratamento de entrada do usuário com validação de erro
    try:
        # Converte a entrada para número inteiro
        opcao = int(input_menu)
        
        # Executa a função correspondente à opção escolhida
        if opcao == 1:
            cadastrar_novo_produto()  # Chama função de cadastro
        elif opcao == 2:
            atualizar_informacoes_produto()  # Chama função de atualização
        elif opcao == 3:
            excluir_produto_do_sistema()  # Chama função de exclusão
        elif opcao == 4:
            exibir_lista_de_produtos()  # Chama função de listagem
        elif opcao == 5:
            ordenar_produtos_por_criterio()  # Chama função de ordenação
        elif opcao == 6:
            buscar_produto_no_sistema()  # Chama função de busca
        elif opcao == 7:
            gerar_relatorios_do_sistema()  # Chama função de relatórios
        elif opcao == 8:
            processar_venda_de_produto()  # Chama função de venda
        elif opcao == 9:
            aplicar_desconto_em_produto()  # Chama função de desconto
        elif opcao == 10:
            visualizar_historico_de_vendas()
        elif opcao == 11:
            # Opção para sair do sistema
            print("Saindo do sistema. Até Logo!")
            break  # Encerra o loop principal
        else:
            # Trata opções inválidas (números fora do range)
            print("Opção inválida! Por favor, escolha uma opção de 1 a 11.")
            
    except ValueError:
        # Trata entradas não numéricas (letras, símbolos, etc.)
        print("Erro: Por favor, digite apenas números de 1 a 11.")
