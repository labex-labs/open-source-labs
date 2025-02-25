# Plots erstellen

Als nächstes erstellen wir zwei Plots mit `imshow` und mit von `numpy.random` erzeugten Zufallszahlenarrays. Wir fügen auch eine Farbskala zu den Plots hinzu. Führen Sie folgenden Code aus:

```python
# Fixing random state for reproducibility
np.random.seed(19680801)

plt.subplot(211)
plt.imshow(np.random.random((100, 100)))
plt.subplot(212)
plt.imshow(np.random.random((100, 100)))

cax = plt.axes([0.85, 0.1, 0.075, 0.8])
plt.colorbar(cax=cax)

plt.show()
```
