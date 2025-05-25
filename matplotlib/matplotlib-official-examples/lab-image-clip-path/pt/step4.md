# Criar o Patch

Para criar o patch, usaremos o módulo `patches` do Matplotlib. Criaremos um patch circular com um raio de 200 pixels, centrado no ponto (260, 200).

```python
patch = patches.Circle((260, 200), radius=200, transform=ax.transData)
```
