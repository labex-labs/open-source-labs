# Exibir a imagem de ressonância magnética (MRI)

Usaremos a função `imshow` do `matplotlib` para exibir a imagem de ressonância magnética em escala de cinza.

```python
fig, ax = plt.subplots(num="MRI_demo")
ax.imshow(im, cmap="gray")
ax.axis('off')
plt.show()
```
