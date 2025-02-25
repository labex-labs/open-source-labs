# Fügen Sie Text zum Graphen hinzu

Wir können Text zu unserem Graphen hinzufügen, indem wir die text()-Funktion verwenden. In diesem Beispiel fügen wir einen LaTeX-Ausdruck zum Graphen hinzu und verwenden das Schriftartwörterbuch, um den Stil anzupassen.

```python
plt.text(2, 0.65, r'$\cos(2 \pi t) \exp(-t)$', fontdict=font)
```
