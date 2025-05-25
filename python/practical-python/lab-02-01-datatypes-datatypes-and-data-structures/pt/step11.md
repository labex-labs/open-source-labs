# Exercício 2.1: Tuplas (Tuples)

No prompt interativo, crie a seguinte tupla que representa a linha acima, mas com as colunas numéricas convertidas em números apropriados:

```python
>>> t = (row[0], int(row[1]), float(row[2]))
>>> t
('AA', 100, 32.2)
>>>
```

Usando isso, você pode agora calcular o custo total multiplicando as ações e o preço:

```python
>>> cost = t[1] * t[2]
>>> cost
3220.0000000000005
>>>
```

A matemática está quebrada em Python? Qual é o problema com a resposta 3220.0000000000005?

Este é um artefato do hardware de ponto flutuante (floating point) em seu computador, que só consegue representar com precisão decimais na Base-2, não na Base-10. Mesmo para cálculos simples envolvendo decimais na base 10, pequenos erros são introduzidos. Isso é normal, embora talvez um pouco surpreendente se você não o viu antes.

Isso acontece em todas as linguagens de programação que usam decimais de ponto flutuante, mas muitas vezes fica oculto ao imprimir. Por exemplo:

```python
>>> print(f'{cost:0.2f}')
3220.00
>>>
```

Tuplas são somente leitura (read-only). Verifique isso tentando mudar o número de ações para 75.

```python
>>> t[1] = 75
Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
TypeError: 'tuple' object does not support item assignment
>>>
```

Embora você não possa alterar o conteúdo da tupla, você sempre pode criar uma tupla completamente nova que substitui a antiga.

```python
>>> t = (t[0], 75, t[2])
>>> t
('AA', 75, 32.2)
>>>
```

Sempre que você reatribui um nome de variável existente como este, o valor antigo é descartado. Embora a atribuição acima possa parecer que você está modificando a tupla, você está realmente criando uma nova tupla e jogando a antiga fora.

Tuplas são frequentemente usadas para empacotar e desempacotar valores em variáveis. Tente o seguinte:

```python
>>> name, shares, price = t
>>> name
'AA'
>>> shares
75
>>> price
32.2
>>>
```

Pegue as variáveis acima e empacote-as de volta em uma tupla

```python
>>> t = (name, 2*shares, price)
>>> t
('AA', 150, 32.2)
>>>
```
