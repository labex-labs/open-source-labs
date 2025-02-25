# Formatieren des Plots

Jetzt werden wir den Plot formatieren, indem wir x- und y-Achsenbeschriftungen hinzufügen, den x-Achsen-Major-Locator und -Formatter einstellen und die y-Achse und die Rahmungen entfernen. Hier ist der Code zum Formatieren des Plots:

```python
# format x-axis with 4-month intervals
ax.xaxis.set_major_locator(mdates.MonthLocator(interval=4))
ax.xaxis.set_major_formatter(mdates.DateFormatter("%b %Y"))
plt.setp(ax.get_xticklabels(), rotation=30, ha="right")

# remove y-axis and spines
ax.yaxis.set_visible(False)
ax.spines[["left", "top", "right"]].set_visible(False)

ax.margins(y=0.1)
plt.show()
```
