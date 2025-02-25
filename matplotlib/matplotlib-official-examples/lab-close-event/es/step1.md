# Importar Matplotlib y definir la función on_close

En este paso, importaremos Matplotlib y definiremos la función `on_close` que se llamará cuando se cierre la figura. La función simplemente imprimirá un mensaje en la consola.

```python
import matplotlib.pyplot as plt

def on_close(event):
    print('Closed Figure!')
```
