# Figurengröße in Zentimetern

Wir können auch die Figurengröße in Zentimetern angeben. Dazu müssen wir die in Zentimetern angegebenen Zahlen in Zoll umrechnen. Wir können dies tun, indem wir den Zentimeter-Wert mit dem Umrechnungsfaktor von cm in Zoll multiplizieren, der 1/2,54 beträgt. Wir können diesen Wert dann als figsize-Parameter in der subplots-Funktion verwenden. Der folgende Code zeigt, wie man eine Figur mit einer Größe von 15 cm x 5 cm erstellt.

```python
cm = 1/2.54  # Zentimeter in Zoll
plt.subplots(figsize=(15*cm, 5*cm))
plt.show()
```
