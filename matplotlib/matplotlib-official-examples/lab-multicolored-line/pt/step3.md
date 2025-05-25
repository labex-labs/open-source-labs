# Criar Segmentos de Linha

Criaremos um conjunto de segmentos de linha para que possamos colori-los individualmente. Usaremos a função numpy `concatenate` para concatenar dois arrays `points[:-1]` e `points[1:]` ao longo do segundo eixo. Em seguida, remodelaremos o array resultante para um array N x 1 x 2 para que possamos empilhar pontos facilmente para obter os segmentos. O array de segmentos para a coleção de linhas precisa ser (número de linhas) x (pontos por linha) x 2 (para x e y).

```python
points = np.array([x, y]).T.reshape(-1, 1, 2)
segments = np.concatenate([points[:-1], points[1:]], axis=1)
```
