# Desenhar textos em uma figura com posicionamento em coordenadas de pixel

Alternativamente, podemos desenhar diretamente texto em uma figura com posicionamento em coordenadas de pixel usando `.Figure.text` juntamente com `.transforms.IdentityTransform`.

```python
fig.text(100, 250, r"IQ: $\sigma_i=15$", color="blue", fontsize=20, transform=IdentityTransform())
fig.text(100, 350, r"some other string", color="red", fontsize=20, transform=IdentityTransform())

plt.show()
```
