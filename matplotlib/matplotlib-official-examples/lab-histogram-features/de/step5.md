# Anpassen des Histogramms

In diesem Schritt werden wir das Histogramm anpassen, indem wir Beschriftungen, einen Titel hinzufügen und das Layout anpassen.

```python
ax.set_xlabel('Smarts')
ax.set_ylabel('Wahrscheinlichkeitsdichte')
ax.set_title(r'Histogramm der IQ: $\mu=100$, $\sigma=15$')
fig.tight_layout()
plt.show()
```
