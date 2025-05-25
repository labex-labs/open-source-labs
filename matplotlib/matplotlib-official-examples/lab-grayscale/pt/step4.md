# Definindo a Função de Exemplo de Imagem e Patch

Definimos a função `image_and_patch_example` que recebe um objeto de eixo (axis object) como entrada, plota uma imagem aleatória e adiciona um patch ao gráfico.

```python
def image_and_patch_example(ax):
    ax.imshow(np.random.random(size=(20, 20)), interpolation='none')
    c = plt.Circle((5, 5), radius=5, label='patch')
    ax.add_patch(c)
```
