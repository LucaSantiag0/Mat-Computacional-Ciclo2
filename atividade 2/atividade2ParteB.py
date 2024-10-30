import pandas as pd

# Função para calcular a divisão do lado oposto pela bissetriz externa usando Pandas
def bissetriz_externa(ab, ac, bc):
    # Calcula a divisão do lado oposto (BC) em duas partes usando a fórmula da bissetriz externa
    # BD = (AB * BC) / (AC - AB) e DC = BC - BD
    bd = (ab * bc) / (ac - ab) if ac > ab else None  # Evita divisão por zero ou valor negativo
    dc = bc - bd if bd is not None else None
    
    # Criar um DataFrame para exibir os valores de forma organizada
    data = {
        'Lados': ['AB', 'AC', 'BC', 'BD', 'DC'],
        'Comprimentos': [ab, ac, bc, bd, dc],
        'Proporção': [ab/(ac - ab) if ac > ab else None, ac/(ac - ab) if ac > ab else None, bc, bd/bc if bd is not None else None, dc/bc if dc is not None else None]
    }
    
    df = pd.DataFrame(data)
    return df

# Entrada dos lados do triângulo
ab = float(input("Digite o valor do lado AB: "))
ac = float(input("Digite o valor do lado AC: "))
bc = float(input("Digite o valor do lado BC: "))

# Cálculo das partes divididas pela bissetriz externa e criação do DataFrame
resultado_df = bissetriz_externa(ab, ac, bc)

# Exibir o DataFrame com os resultados
print("\nDivisão dos lados pela bissetriz externa:")
print(resultado_df)
