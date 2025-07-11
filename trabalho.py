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
    print("===MENU PRINCIPAL===")
    print("1. Cadastrar Produto")
    print("2. Atualizar Produto")
    print("3. Excluir Produto")
    print("4. Listar Produtos")
    print("5. Buscar Produto")
    print("6. Relatórios:(Valor Total/ Estoque Baixo)")
    print("7. Vender produto")
    print("8. Aplicar Desconto")
    print("9. Sair")
    
lista_produtos = []    
    

def adicionar_produto():
    produto = {}
    
    print("===CADASTRO DE PRODUTO===")
    
    id_produto = input("Digite o ID do produto (formato 'ABC-123'): ")
    nome_produto = input("Digite o nome do produto: ")
    preco_produto = input("Digite o preço do produto: ")
    quantidade_produto = input("Digite a quantidade do produto: ")
    categoria_produto = input("Digite a categoria do produto (Alimentos, Limpeza, Eletrônicos, Vestuário): ")
    
    # Validações
    if id_produto in produto:
        print("Erro: ID do produto já existe.")
    else:
        produto['id'] = id_produto
    return produto
        




def atualizar_produto():
     pass

def excluir_produto():
    pass
    
def listar_produtos():
    pass 
     
def buscar_produto():
    pass
def relatorio():
    pass
    
def vender_produto():
    pass
def aplicar_desconto():
    pass
    

     
     
     
     
     
     
     
                
while True:
    exibir_menu()
    input_menu = input("Selecione uma opção do menu: ")
    
    
    try:
        opcao = int(input_menu)
        
        if opcao == 1:
            adicionar_produto()
        elif opcao == 2:
            atualizar_produto()
        elif opcao == 3:
            excluir_produto()
        elif opcao == 4:
            listar_produtos()
        elif opcao == 5:
            buscar_produto()
        elif opcao == 6:
            relatorio()
        elif opcao == 7:
            vender_produto()
        elif opcao == 8:
            aplicar_desconto()
        elif opcao == 9:
            print("Saindo do sistema. Até Logo!")
            break
        else:
            print("Opção inválida! Por favor, escolha uma opção de 1 a 9.")
            
    except ValueError:
        print("Erro: Por favor, digite apenas números de 1 a 9.") # eu coloquei o try/except para tratar o erro de digitar uma letra ou caractere especial no menu, senão o programa iria parar de funcionar e ia soar meio estranho
    
    print()  
    
    
