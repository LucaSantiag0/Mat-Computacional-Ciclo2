import pandas as pd  # Importa a biblioteca Pandas para trabalhar com tabelas de dados

# Função para verificar semelhança pelo critério LAL (Lado-Ângulo-Lado)
def verifica_LAL(df_t1, df_t2):
    # Verifica se os dois primeiros lados dos triângulos são proporcionais
    proporcao_lados = df_t1[['lado1', 'lado2']].div(df_t2[['lado1', 'lado2']].values).all(axis=1).all()
    # Verifica se o ângulo entre os lados é o mesmo
    angulo_congruente = df_t1['angulo2'].equals(df_t2['angulo2'])
    # Retorna True se as duas condições forem satisfeitas, senão retorna False
    return proporcao_lados and angulo_congruente

# Função para verificar semelhança pelo critério AA (Ângulo-Ângulo)
def verifica_AA(df_t1, df_t2):
    # Verifica se todos os ângulos dos triângulos são iguais
    return df_t1[['angulo1', 'angulo2', 'angulo3']].equals(df_t2[['angulo1', 'angulo2', 'angulo3']])

# Função para verificar semelhança pelo critério LLL (Lado-Lado-Lado)
def verifica_LLL(df_t1, df_t2):
    # Verifica se os três lados dos triângulos são proporcionais
    proporcao_lados = df_t1[['lado1', 'lado2', 'lado3']].div(df_t2[['lado1', 'lado2', 'lado3']].values).all(axis=1).all()
    return proporcao_lados

# Função para pedir ao usuário os dados de lados e ângulos dos triângulos
def entrada_dados(triangulo):
    lados = []  # Lista para armazenar os lados do triângulo
    angulos = []  # Lista para armazenar os ângulos do triângulo
    print(f"Digite os lados e ângulos do {triangulo}:")
    
    # Coleta os lados do triângulo
    for i in range(3):
        lado = float(input(f"Digite o lado {i+1}: "))  # Pede o valor do lado
        lados.append(lado)  # Adiciona o valor à lista de lados
    
    # Coleta os ângulos do triângulo
    for i in range(3):
        angulo = float(input(f"Digite o ângulo {i+1} (em graus): "))  # Pede o valor do ângulo
        angulos.append(angulo)  # Adiciona o valor à lista de ângulos
    
    # Cria um DataFrame com os lados e ângulos
    df = pd.DataFrame({
        'lado1': [lados[0]],
        'lado2': [lados[1]],
        'lado3': [lados[2]],
        'angulo1': [angulos[0]],
        'angulo2': [angulos[1]],
        'angulo3': [angulos[2]]
    })
    
    return df  # Retorna o DataFrame com os dados

# Função principal para verificar a semelhança
def verificar_semelhanca():
    print("Verificação de Semelhança de Triângulos\n")
    
    # Coleta os dados do primeiro triângulo
    df_t1 = entrada_dados("primeiro triângulo")
    
    # Coleta os dados do segundo triângulo
    df_t2 = entrada_dados("segundo triângulo")
    
    # Verifica se os triângulos são semelhantes pelo critério LAL
    if verifica_LAL(df_t1, df_t2):
        print("Os triângulos são semelhantes pelo critério LAL.")
    
    # Verifica se os triângulos são semelhantes pelo critério AA
    elif verifica_AA(df_t1, df_t2):
        print("Os triângulos são semelhantes pelo critério AA.")
    
    # Verifica se os triângulos são semelhantes pelo critério LLL
    elif verifica_LLL(df_t1, df_t2):
        print("Os triângulos são semelhantes pelo critério LLL.")
    
    # Caso não sejam semelhantes por nenhum critério
    else:
        print("Os triângulos não são semelhantes.")

# Execução do programa
verificar_semelhanca()