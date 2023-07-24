# Import Matplotlib and Define the on_close Function

In this step, we will import Matplotlib and define the `on_close` function that will be called when the figure is closed. The function will simply print a message to the console.

```python
import matplotlib.pyplot as plt

def on_close(event):
    print('Closed Figure!')
```
