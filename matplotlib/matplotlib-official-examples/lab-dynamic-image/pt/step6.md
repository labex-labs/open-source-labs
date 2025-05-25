# Criar a Animação

Agora criaremos a animação usando o método `ArtistAnimation`. Passaremos o objeto `figure`, a lista `ims`, o intervalo entre os quadros e o atraso de repetição.

```python
ani = animation.ArtistAnimation(fig, ims, interval=50, blit=True, repeat_delay=1000)
```
