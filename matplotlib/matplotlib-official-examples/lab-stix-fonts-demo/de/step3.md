# Den Text plotten

Jetzt, nachdem wir den Text definiert haben, können wir ihn mit Matplotlib plotten. In diesem Schritt erstellen wir eine Figur und fügen den Text hinzu, indem wir die `fig.text()`-Methode verwenden.

```python
fig = plt.figure(figsize=(8, len(tests) + 2))
for i, s in enumerate(tests[::-1]):
    fig.text(0, (i +.5) / len(tests), s, fontsize=32)

plt.show()
```
