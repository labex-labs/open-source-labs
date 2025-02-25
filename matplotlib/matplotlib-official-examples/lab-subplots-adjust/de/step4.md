# Die Position der Farbskala anpassen

Wir können auch die Position der Farbskala mit `plt.axes` anpassen. Diese Funktion nimmt eine Liste von `[left, bottom, width, height]`-Werten als Argumente, um die Position und Größe der Achsen anzugeben. Führen Sie folgenden Code aus:

```python
cax = plt.axes([0.85, 0.1, 0.075, 0.8])
plt.colorbar(cax=cax)
```
