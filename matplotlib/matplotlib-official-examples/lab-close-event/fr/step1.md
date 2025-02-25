# Import Matplotlib et définir la fonction on_close

Dans cette étape, nous allons importer Matplotlib et définir la fonction `on_close` qui sera appelée lorsque la figure est fermée. La fonction imprimera simplement un message dans la console.

```python
import matplotlib.pyplot as plt

def on_close(event):
    print('Closed Figure!')
```
