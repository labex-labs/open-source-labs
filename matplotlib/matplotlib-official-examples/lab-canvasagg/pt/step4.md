# Extrair o Buffer do Renderizador para um Array NumPy

A segunda opção para salvar o gráfico é extrair o buffer do renderizador para um array NumPy. Isso permite que você use o Matplotlib em um script cgi sem precisar escrever o gráfico no disco. Neste exemplo, extrairemos o buffer do renderizador e o converteremos em um array NumPy.

```python
import numpy as np

canvas.draw()
rgba = np.asarray(canvas.buffer_rgba())
```
