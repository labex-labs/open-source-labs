# Criando a Esfera

Agora criaremos uma esfera no gráfico definindo uma condição para os valores RGB que estão dentro de uma certa distância do centro do gráfico.

```python
rc = midpoints(r)
gc = midpoints(g)
bc = midpoints(b)

sphere = (rc - 0.5)**2 + (gc - 0.5)**2 + (bc - 0.5)**2 < 0.5**2
```
