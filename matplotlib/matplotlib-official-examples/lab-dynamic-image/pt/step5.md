# Criar os Quadros da Animação

Agora criaremos os quadros para a animação. Usaremos um loop `for` para gerar 60 quadros. Em cada iteração do loop, atualizaremos os dados x e y e, em seguida, criaremos um novo objeto de imagem usando o método `imshow`. Em seguida, anexaremos o objeto de imagem à lista `ims`.

```python
ims = []
for i in range(60):
    x += np.pi / 15
    y += np.pi / 30
    im = ax.imshow(f(x, y), animated=True)
    if i == 0:
        ax.imshow(f(x, y))  # show an initial one first
    ims.append([im])
```
