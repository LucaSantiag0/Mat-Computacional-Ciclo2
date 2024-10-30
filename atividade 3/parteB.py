import pandas as pd

def obter_input_usuario():
    # Recebe entradas do usuário
    print("Digite 'V' para Verdadeiro ou 'F' para Falso:")
    p = input("Ana vai à festa (P)? ").strip().upper()
    q = input("Bruno vai à festa (Q)? ").strip().upper()
    m = input("Bruno traz música (M)? ").strip().upper()

    return (p == 'V', q == 'V', m == 'V')

def avaliar_tabela_verdade(p, q, m):
    # Avalia as proposições lógicas
    p_implica_q = not p or q 
    p_ou_q = p or q  
    r = p_ou_q 
    nao_p = not p  
    m_implica_r = not m or r  
    nao_p_implica_m_implica_r = not nao_p or m_implica_r  

    return p_implica_q, p_ou_q, r, nao_p, m_implica_r, nao_p_implica_m_implica_r

def tabela_verdade_interativa():
    colunas = ['P', 'Q', 'M', 'P→Q', 'P∨Q', 'R', '¬P', 'M→R', '¬P→(M→R)']
    df = pd.DataFrame(columns=colunas)


    p, q, m = obter_input_usuario()


    p_implica_q, p_ou_q, r, nao_p, m_implica_r, nao_p_implica_m_implica_r = avaliar_tabela_verdade(p, q, m)


    df = pd.concat([df, pd.DataFrame([{
        'P': p, 
        'Q': q, 
        'M': m, 
        'P→Q': p_implica_q, 
        'P∨Q': p_ou_q, 
        'R': r, 
        '¬P': nao_p, 
        'M→R': m_implica_r, 
        '¬P→(M→R)': nao_p_implica_m_implica_r
    }])], ignore_index=True)

    
    print("\nTabela Verdade:")
    print(df)


tabela_verdade_interativa()
