# Schnelle interaktive Arbeit

Für schnelle interaktive Arbeiten sind Pixel normalerweise eine gute Größeseinheit. Wir können den Standard-dpi-Wert von 100 verwenden, um Pixelwerte in Zoll umzurechnen. Wir können diesen Wert dann als figsize-Parameter in der subplots-Funktion verwenden. Der folgende Code zeigt, wie man eine Figur mit einer Größe von 6 Zoll x 2 Zoll mithilfe von Pixelwerten erstellt.

```python
plt.subplots(figsize=(600/100, 200/100))
plt.show()
```
