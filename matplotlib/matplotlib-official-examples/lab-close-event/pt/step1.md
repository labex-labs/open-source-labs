# Importar Matplotlib e Definir a Função `on_close`

Nesta etapa, importaremos o Matplotlib e definiremos a função `on_close` que será chamada quando a figura for fechada. A função simplesmente imprimirá uma mensagem no console.

```python
import matplotlib.pyplot as plt

def on_close(event):
    print('Closed Figure!')
```
