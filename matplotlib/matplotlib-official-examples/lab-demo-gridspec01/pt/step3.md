# Definir Subplots Usando subplot2grid

Para definir subplots usando `subplot2grid`, primeiro precisamos especificar o tamanho da grade usando uma tupla com o número desejado de linhas e colunas. Também precisamos especificar a localização do subplot dentro da grade usando outra tupla.

Por exemplo, para criar uma grade 3x3 com um subplot que abrange toda a primeira linha e todas as três colunas, usamos o seguinte código:

```python
ax1 = plt.subplot2grid((3, 3), (0, 0), colspan=3)
```

Para criar um subplot que abrange a segunda linha e as duas primeiras colunas, usamos:

```python
ax2 = plt.subplot2grid((3, 3), (1, 0), colspan=2)
```

Para criar um subplot que abrange as duas últimas linhas e a última coluna, usamos:

```python
ax3 = plt.subplot2grid((3, 3), (1, 2), rowspan=2)
```

Para criar um subplot na última linha e na primeira coluna, usamos:

```python
ax4 = plt.subplot2grid((3, 3), (2, 0))
```

Para criar um subplot na última linha e na segunda coluna, usamos:

```python
ax5 = plt.subplot2grid((3, 3), (2, 1))
```
