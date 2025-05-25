# Criar Função de Animação

Precisamos criar uma função `animate` que gera novos dados aleatórios e atualiza as alturas dos retângulos.

```python
def animate(frame_number):
    # simulate new data coming in
    data = np.random.randn(1000)
    n, _ = np.histogram(data, HIST_BINS)
    for count, rect in zip(n, bar_container.patches):
        rect.set_height(count)
    return bar_container.patches
```
