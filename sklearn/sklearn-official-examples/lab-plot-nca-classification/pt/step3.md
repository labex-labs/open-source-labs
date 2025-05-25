# Criar Mapas de Cores

Agora criaremos mapas de cores para plotar os limites de decisão das classes. Usaremos cores claras para o fundo e cores fortes para as cores das classes.

```python
h = 0.05  # tamanho do passo na malha

# Criar mapas de cores
cmap_light = ListedColormap(["#FFAAAA", "#AAFFAA", "#AAAAFF"])
cmap_bold = ListedColormap(["#FF0000", "#00FF00", "#0000FF"])
```
