# Mostrar la imagen de resonancia magnética (MRI)

Utilizaremos la función `imshow` de `matplotlib` para mostrar la imagen de resonancia magnética en escala de grises.

```python
fig, ax = plt.subplots(num="MRI_demo")
ax.imshow(im, cmap="gray")
ax.axis('off')
plt.show()
```
