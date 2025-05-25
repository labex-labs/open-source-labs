# Criar uma Função para Calcular a Distância

Precisamos criar uma função que calcula a distância entre um ponto e um segmento de reta. Esta função será usada posteriormente para determinar se um novo vértice deve ser adicionado ao polígono.

```python
def dist_point_to_segment(p, s0, s1):
    """
    Obter a distância do ponto *p* ao segmento (*s0*, *s1*), onde
    *p*, *s0*, *s1* são arrays ``[x, y]``.
    """
    s01 = s1 - s0
    s0p = p - s0
    if (s01 == 0).all():
        return np.hypot(*s0p)
    # Projetar no segmento, sem ultrapassar as extremidades do segmento.
    p1 = s0 + np.clip((s0p @ s01) / (s01 @ s01), 0, 1) * s01
    return np.hypot(*(p - p1))
```
