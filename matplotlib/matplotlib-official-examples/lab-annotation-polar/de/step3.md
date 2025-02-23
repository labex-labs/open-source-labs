# Hinzufügen einer Anmerkung

Wir können einer Anmerkung zum Polarkoordinaten-Graphen hinzufügen, indem wir den Ort der Anmerkung angeben. In diesem Fall wählen wir einen bestimmten Punkt auf dem Graphen und annotieren ihn.

```python
ind = 800
thisr, thistheta = r[ind], theta[ind]
ax.plot([thistheta], [thisr], 'o')
ax.annotate('a polar annotation',
            xy=(thistheta, thisr),  # theta, radius
            xytext=(0.05, 0.05),    # fraction, fraction
            textcoords='figure fraction',
            arrowprops=dict(facecolor='black', shrink=0.05),
            horizontalalignment='left',
            verticalalignment='bottom',
            )
```
