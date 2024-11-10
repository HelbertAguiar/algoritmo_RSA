# Algoritmo RSA e Análise do Código

O RSA é um algoritmo de criptografia assimétrica amplamente utilizado para proteger a troca de informações. Ele se baseia na dificuldade de fatorar números grandes em seus fatores primos, tornando-o seguro para uso em comunicações seguras.

## Visão Geral do Algoritmo RSA

O algoritmo RSA consiste nas seguintes etapas principais:

### 1. **Geração de Chaves**

Para gerar as chaves públicas e privadas, siga os passos abaixo:

1. **Selecione dois números primos grandes**, \( p \) e \( q \).
2. **Calcule \( n \)**:
   \[
   n = p \times q
   \]
   O valor \( n \) será usado como parte da chave pública e privada.
3. **Calcule a função de Euler \( \phi(n) \)**:
   \[
   \phi(n) = (p - 1) \times (q - 1)
   \]
4. **Escolha um número \( e \)** que seja coprimo com \( \phi(n) \), ou seja, \( 1 < e < \phi(n) \) e o máximo divisor comum \( \text{MDC}(e, \phi(n)) = 1 \).
5. **Calcule o inverso modular de \( e \)**, que será o valor \( d \), tal que:
   \[
   d \times e \equiv 1 \mod \phi(n)
   \]
6. A **chave pública** é o par \((e, n)\) e a **chave privada** é o par \((d, n)\).

### 2. **Criptografia**

Para criptografar uma mensagem \( m \):

1. Converta a mensagem para um número inteiro \( m \).
2. Calcule o texto cifrado \( c \):
   \[
   c = m^e \mod n
   \]

### 3. **Descriptografia**

Para descriptografar o texto cifrado \( c \):

1. Use a chave privada \((d, n)\) para obter a mensagem original \( m \):
   \[
   m = c^d \mod n
   \]

## Análise do Código

O código Python fornecido implementa o algoritmo RSA, incluindo a geração de chaves, criptografia e descriptografia. Vou explicar cada função do código.

### **1. Função `calcula_mdc(a, b)`**

Esta função utiliza o Algoritmo de Euclides para calcular o Máximo Divisor Comum (MDC) de dois números. Ela é usada para verificar se \( e \) é coprimo com \( \phi(n) \).

```python
def calcula_mdc(a: int, b: int) -> int:
    while b != 0:
        a, b = b, a % b
    return a
