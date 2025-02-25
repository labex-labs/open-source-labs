# Automatisches Shading

Es ist möglich, dass der Benutzer möchte, dass der Code automatisch wählt, welches zu verwenden. In diesem Fall wird `shading='auto'` entscheiden, ob `flat` oder `nearest` Shading verwendet werden soll, basierend auf den Formen von `X`, `Y` und `Z`. Wir können das Gitter mit dem folgenden Codeblock visualisieren:

```python
fig, ax = plt.subplots()
ax.pcolormesh(x, y, Z, shading='auto', cmap='viridis')
ax.set_title('Auto Shading')
plt.show()
```
