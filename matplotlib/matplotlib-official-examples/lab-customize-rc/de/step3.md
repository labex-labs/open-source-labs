# Erstellen von Teilplots

Um Teilplots in Matplotlib zu erstellen, können Sie die Methode `subplot()` verwenden. Diese Methode nimmt drei Argumente entgegen: die Anzahl der Zeilen, die Anzahl der Spalten und die Plot-Nummer. Hier ist ein Beispiel, das drei Teilplots erstellt:

```python
plt.subplot(311)
plt.plot([1, 2, 3])

plt.subplot(312)
plt.plot([1, 2, 3])
plt.grid(True)

plt.subplot(313)
plt.plot([1, 2, 3])
plt.grid(True)
```
