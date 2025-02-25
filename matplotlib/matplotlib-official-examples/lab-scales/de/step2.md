# Erstellen eines Plots mit linearer Skala

Die erste Art von Skalierungsumformung, die wir untersuchen werden, ist die lineare Skala. Dies ist die Standardskala, die in Matplotlib verwendet wird. Um einen Plot mit linearer Skala zu erstellen, verwenden wir die Methode `set_yscale()` und übergeben den String `'linear'`. Wir fügen auch einen Titel und ein Gitter zum Plot hinzu.

```python
# linear
plt.plot(x, y)
plt.yscale('linear')
plt.title('Linear Scale')
plt.grid(True)
```
