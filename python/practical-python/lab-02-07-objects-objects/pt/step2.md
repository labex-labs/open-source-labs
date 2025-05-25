# Exemplo de atribuição

Considere este fragmento de código.

```python
a = [1,2,3]
b = a
c = [a,b]
```

Uma imagem das operações de memória subjacentes. Neste exemplo, existe apenas um objeto lista `[1,2,3]`, mas existem quatro referências diferentes a ele.

![Memory reference diagram example](../assets/references.png)

Isso significa que modificar um valor afeta _todas_ as referências.

```python
>>> a.append(999)
>>> a
[1,2,3,999]
>>> b
[1,2,3,999]
>>> c
[[1,2,3,999], [1,2,3,999]]
>>>
```

Observe como uma alteração na lista original aparece em todos os outros lugares (ai!). Isso ocorre porque nenhuma cópia foi feita. Tudo está apontando para a mesma coisa.
