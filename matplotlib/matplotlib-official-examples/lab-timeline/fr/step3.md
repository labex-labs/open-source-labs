# Formatage du tracé

Maintenant, nous allons formater le tracé en ajoutant des étiquettes pour l'axe des x et l'axe des y, en configurant le localisateur et le formateur principaux de l'axe des x, et en supprimant l'axe des y et les épines. Voici le code pour formater le tracé :

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
