# Definir as cores

Agora definiremos as cores para cada objeto no gráfico de voxels. Faremos isso criando um array vazio com a mesma forma do array booleano que criamos no Passo 3 e, em seguida, definindo a cor de cada objeto com base em sua localização.

```python
colors = np.empty(voxelarray.shape, dtype=object)
colors[link] = 'red'
colors[cube1] = 'blue'
colors[cube2] = 'green'
```
