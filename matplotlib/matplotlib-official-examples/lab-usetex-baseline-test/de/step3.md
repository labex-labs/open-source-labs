# Erstellen der Teilplots

Wir werden eine Figur erstellen, die zwei Teilplots enthält, einen mit mathtext und einen mit usetex. Wir werden die `subplots()`-Methode verwenden, um die Teilplots zu erstellen.

```python
fig, axs = plt.subplots(1, 2, figsize=(2 * 3, 6.5))
```
