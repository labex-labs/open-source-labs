# Anpassen von Standardparametern

Um die Standardparameter für eine bestimmte Figur anzupassen, können Sie die Methode `rcParams.update()` erneut verwenden. Diesmal übergeben Sie ein Wörterbuch mit Parameternamen und -werten, die Sie für diese Figur festlegen möchten. Hier ist ein Beispiel, das einige Standardparameter für eine bestimmte Figur setzt:

```python
import matplotlib.pyplot as plt

plt.rcParams.update({
    "font.weight": "bold",
    "xtick.major.size": 5,
    "xtick.major.pad": 7,
    "xtick.labelsize": 15,
    "grid.color": "0.5",
    "grid.linestyle": "-",
    "grid.linewidth": 5,
    "lines.linewidth": 2,
    "lines.color": "g",
})
```
