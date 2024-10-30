import pandas as pd

# Função para calcular a razão das partes formadas pela bissetriz interna usando Pandas
def bissetriz_interna(ab, ac, bc):
    # Calcula a divisão do lado oposto (BC) em duas partes usando a fórmula da bissetriz interna
    bd = (ab * bc) / (ab + ac)
    dc = bc - bd
    
    # Criar um DataFrame para exibir os valores de forma organizada
    data = {
        'Lados': ['AB', 'AC', 'BC', 'BD', 'DC'],
        'Comprimentos': [ab, ac, bc, bd, dc],
        'Proporção': [ab/(ab + ac), ac/(ab + ac), bc, bd/bc, dc/bc]
    }
    
    df = pd.DataFrame(data)
    return df

# Entrada dos lados do triângulo
ab = float(input("Digite o valor do lado AB: "))
ac = float(input("Digite o valor do lado AC: "))
bc = float(input("Digite o valor do lado BC: "))

# Cálculo das partes divididas pela bissetriz interna e criação do DataFrame
resultado_df = bissetriz_interna(ab, ac, bc)

# Exibir o DataFrame com os resultados
print("\nDivisão dos lados pela bissetriz interna:")
print(resultado_df)
