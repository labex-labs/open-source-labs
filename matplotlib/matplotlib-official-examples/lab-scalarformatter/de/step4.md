# Plotten von Daten auf Teilplots

Wir werden unsere generierten Daten auf den Teilplots plotten, die wir in Schritt 3 erstellt haben.

```python
for col in axs.T:
    col[0].plot(plot1_x, plot1_y)
    col[1].plot(plot2_x, plot2_y)
    col[2].plot(plot3_x, plot3_y)
```
