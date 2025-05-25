# Exibir a Imagem

Agora podemos exibir a imagem usando o método `imshow` do Matplotlib. Também desativaremos os eixos para que vejamos apenas a imagem.

```python
fig, ax = plt.subplots()
im = ax.imshow(image)
ax.axis('off')
```
