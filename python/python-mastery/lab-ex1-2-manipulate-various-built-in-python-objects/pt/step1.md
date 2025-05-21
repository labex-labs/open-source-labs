# Trabalhando com Números Python

Python oferece suporte robusto para operações numéricas. Em programação, números são tipos de dados fundamentais usados para cálculos e representação de quantidades. Este passo irá apresentá-lo à manipulação básica de números em Python, o que é essencial para realizar várias operações matemáticas em seus programas.

## Operações Aritméticas Básicas

Para começar a trabalhar com números Python, você primeiro precisa abrir um shell interativo Python. Você pode fazer isso digitando `python3` no seu terminal. O shell interativo Python permite que você escreva e execute código Python linha por linha, o que é ótimo para testar e aprender.

```bash
python3
```

Uma vez no shell interativo Python, você pode tentar algumas operações aritméticas básicas. Python segue as regras matemáticas padrão para aritmética, como a ordem das operações (PEMDAS: Parênteses, Expoentes, Multiplicação e Divisão, Adição e Subtração).

```python
>>> 3 + 4*5    # A multiplicação tem precedência maior que a adição, então 4*5 é calculado primeiro, depois adicionado a 3
23
>>> 23.45 / 1e-02    # Notação científica para 0.01 é usada aqui. A divisão é realizada para obter o resultado
2345.0
```

## Divisão Inteira

Python 3 lida com a divisão de forma diferente do Python 2. Entender essas diferenças é crucial para evitar resultados inesperados em seu código.

```python
>>> 7 / 4    # Em Python 3, a divisão regular retorna um float, mesmo que o resultado possa ser um inteiro
1.75
>>> 7 // 4   # A divisão inteira (trunca a parte decimal) dá o quociente como um inteiro
1
```

## Métodos de Números

Números em Python têm vários métodos úteis que são frequentemente negligenciados. Esses métodos podem simplificar operações numéricas e conversões complexas. Vamos explorar alguns deles:

```python
>>> x = 1172.5
>>> x.as_integer_ratio()    # Este método representa o float como uma fração, o que pode ser útil para alguns cálculos matemáticos
(2345, 2)
>>> x.is_integer()    # Verifica se o float é um valor inteiro. Neste caso, 1172.5 não é um inteiro, então retorna False
False

>>> y = 12345
>>> y.numerator    # Para inteiros, o numerador é o próprio número
12345
>>> y.denominator    # Para inteiros, o denominador é sempre 1
1
>>> y.bit_length()    # Este método informa o número de bits necessários para representar o número em binário, o que pode ser útil em operações bitwise
14
```

Esses métodos são particularmente úteis quando você precisa realizar operações numéricas ou conversões específicas. Eles podem economizar tempo e tornar seu código mais eficiente.

Quando terminar de explorar o shell interativo Python, você pode sair digitando:

```python
>>> exit()
```
