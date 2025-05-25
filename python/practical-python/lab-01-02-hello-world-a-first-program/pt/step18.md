# Exercício 1.5: A Bola que Quica (The Bouncing Ball)

Uma bola de borracha é solta de uma altura de 100 metros e, cada vez que atinge o chão, ela quica de volta para 3/5 da altura da qual caiu. Escreva um programa `bounce.py` que imprima uma tabela mostrando a altura dos primeiros 10 quiques.

Aqui está uma solução:

```python
# bounce.py

height = 100
bounce = 1
while bounce <= 10:
    height = height * (3 / 5)
    print(bounce, round(height, 4))
    bounce += 1
```

Seu programa deve criar uma tabela que se pareça com isto:

```code
1 60.0
2 36.0
3 21.599999999999998
4 12.959999999999999
5 7.775999999999999
6 4.6655999999999995
7 2.7993599999999996
8 1.6796159999999998
9 1.0077695999999998
10 0.6046617599999998
```

_Nota: Você pode limpar um pouco a saída se usar a função round(). Tente usá-la para arredondar a saída para 4 dígitos._

```code
1 60.0
2 36.0
3 21.6
4 12.96
5 7.776
6 4.6656
7 2.7994
8 1.6796
9 1.0078
10 0.6047
```
