# Anzeige verschiedener Elemente umschalten

Wir können die Anzeige verschiedener Elemente des Boxplot-Diagramms mithilfe verschiedener Parameter in der `bxp()`-Funktion umschalten. In diesem Beispiel zeigen wir, wie der Mittelwert, die Box, die Kapfen, die Kerben und die Ausreißer angezeigt oder ausgeblendet werden können.

```python
# Toggle the display of different elements
plt.bxp(stats, showmeans=True, showbox=False, showcaps=False, shownotches=True, showfliers=False)
plt.show()
```
