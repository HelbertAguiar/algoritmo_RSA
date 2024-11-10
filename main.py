# Código aprimorado e documentado para o algoritmo RSA

import random
from pprint import pprint

def calcula_mdc(a: int, b: int) -> int:
    """
    Calcula o Máximo Divisor Comum (MDC) de dois números usando o Algoritmo de Euclides.

    Args:
        a (int): Primeiro número.
        b (int): Segundo número.

    Returns:
        int: O MDC de a e b.
    """
    while b != 0:
        a, b = b, a % b
    return a

def calcula_funcao_phi_euler(p: int, q: int) -> int:
    """
    Calcula a função de Euler para dois números primos p e q.

    Args:
        p (int): Primeiro número primo.
        q (int): Segundo número primo.

    Returns:
        int: O valor de phi(n), onde phi(n) = (p-1) * (q-1).
    """
    return (p - 1) * (q - 1)

def calcula_expoente_publico(phi_n: int) -> int:
    """
    Escolhe um número inteiro e que seja coprimo com phi_n.

    Args:
        phi_n (int): O valor da função de Euler.

    Returns:
        int: O valor de e, que é coprimo com phi_n.
    """
    # Valores comuns usados para e
    valores_comuns = [3, 5, 17, 257, 65537]
    for e in valores_comuns:
        if calcula_mdc(e, phi_n) == 1:
            return e

    # Se nenhum valor comum funcionar, escolher aleatoriamente
    while True:
        e = random.randrange(2, phi_n)
        if calcula_mdc(e, phi_n) == 1:
            return e

def calcula_expoente_privado(e: int, phi_n: int) -> int:
    """
    Calcula o inverso multiplicativo de e módulo phi_n usando o Algoritmo de Euclides Estendido.

    Args:
        e (int): O expoente público.
        phi_n (int): O valor da função de Euler.

    Returns:
        int: O valor de d, que é o inverso multiplicativo de e.
    """
    x0, x1 = 0, 1
    a, b = phi_n, e

    while b != 0:
        q = a // b
        a, b = b, a % b
        x0, x1 = x1, x0 - q * x1

    if x0 < 0:
        x0 += phi_n

    return x0

def criptografa(mensagem: int, chave_publica: tuple) -> int:
    """
    Criptografa uma mensagem usando a chave pública (e, n).

    Args:
        mensagem (int): A mensagem a ser criptografada (convertida para número inteiro).
        chave_publica (tuple): A chave pública (e, n).

    Returns:
        int: A mensagem criptografada.
    """
    e, n = chave_publica
    return pow(mensagem, e, n)

def descriptografa(mensagem_cifrada: int, chave_privada: tuple) -> int:
    """
    Descriptografa uma mensagem usando a chave privada (d, n).

    Args:
        mensagem_cifrada (int): A mensagem criptografada.
        chave_privada (tuple): A chave privada (d, n).

    Returns:
        int: A mensagem descriptografada.
    """
    d, n = chave_privada
    return pow(mensagem_cifrada, d, n)

# Passo 1: Escolher dois números primos grandes
p = 997 # outra opcao seria 997
q = 991 # outra opcao seria 991

# Passo 2: Calcular n = p * q
n = p * q

# Passo 3: Calcular a função de Euler phi(n)
phi_n = calcula_funcao_phi_euler(p, q)

# Passo 4: Calcular o expoente público e
e = calcula_expoente_publico(phi_n)

# Passo 5: Calcular o expoente privado d
d = calcula_expoente_privado(e, phi_n)

# Chaves RSA
chave_publica = (e, n)
chave_privada = (d, n)

# parâmetros da operação
params_rsa = {
    'chave_publica'     : chave_publica,
    'chave_privada'     : chave_privada,
    'p'                 : p,
    'q'                 : q,
    'n'                 : n,
    'phi_n'             : phi_n,
    'e'                 : e,
    'd'                 : d
}

# Exemplo de uso: Criptografia e Descriptografia
mensagem                = 20003
mensagem_cifrada        = criptografa(mensagem, chave_publica)
mensagem_descifrada     = descriptografa(mensagem_cifrada, chave_privada)

# Exibir os resultados
resultado = {
    'mensagem_original'     : mensagem,
    'mensagem_cifrada'      : mensagem_cifrada,
    'mensagem_descifrada'   : mensagem_descifrada,
    'params_rsa'            : params_rsa
}

pprint(resultado)
