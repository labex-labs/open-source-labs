# Definindo Propriedades

A interface pyplot nos permite definir e obter propriedades de objetos para visualizar dados. Podemos usar o método `setp` para definir as propriedades de um objeto. Por exemplo, para definir o estilo de linha (linestyle) de uma linha para tracejado, usamos o seguinte código:

```python
line, = plt.plot([1, 2, 3])
plt.setp(line, linestyle='--')
```

Se quisermos saber os tipos de argumentos válidos, podemos fornecer o nome da propriedade que queremos definir sem um valor:

```python
plt.setp(line, 'linestyle')
```

Isso retornará a seguinte saída:

```
linestyle: {'-', '--', '-.', ':', '', (offset, on-off-seq), ...}
```

Se quisermos ver todas as propriedades que podem ser definidas e seus valores possíveis, podemos usar o seguinte código:

```python
plt.setp(line)
```

Isso retornará uma longa lista de propriedades e seus valores possíveis.
