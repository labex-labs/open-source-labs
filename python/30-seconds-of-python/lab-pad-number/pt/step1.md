# Preencher Número (Pad Number)

Escreva uma função `pad_number(n, l)` que recebe um número `n` e um comprimento `l` e retorna uma string que representa o número preenchido. A função deve preencher o número com zeros à esquerda para que ele tenha `l` dígitos de comprimento. Se o número já tiver `l` dígitos de comprimento, a função deve retornar o número como uma string.

Para preencher o número, você pode usar o método `str.zfill()`. Este método recebe um comprimento e preenche a string com zeros à esquerda até que ela tenha esse comprimento. Por exemplo, `"7".zfill(6)` retornaria `"000007"`.

```python
def pad_number(n, l):
  return str(n).zfill(l)
```

```python
pad_number(1234, 6); # '001234'
```
