# Capturar frames e escrever para o arquivo

Iteramos por 100 iterações e geramos números aleatórios para as coordenadas x e y. Atualizamos os dados para o gráfico de linha e capturamos o frame usando o writer. Finalmente, salvamos os frames em um arquivo.

```python
x0, y0 = 0, 0

with writer.saving(fig, "writer_test.mp4", 100):
    for i in range(100):
        x0 += 0.1 * np.random.randn()
        y0 += 0.1 * np.random.randn()
        l.set_data(x0, y0)
        writer.grab_frame()
```
