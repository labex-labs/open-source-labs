# Obtendo Propriedades

Podemos usar o método `getp` para obter as propriedades de um objeto. Podemos usá-lo para consultar o valor de um único atributo:

```python
plt.getp(line, 'linewidth')
```

Isso retornará o valor da propriedade linewidth do objeto line.

Também podemos usar `getp` para obter todos os pares atributo/valor de um objeto:

```python
plt.getp(line)
```

Isso retornará uma longa lista de todas as propriedades e seus valores.
