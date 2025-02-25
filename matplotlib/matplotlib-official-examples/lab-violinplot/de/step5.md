# Anpassen der Plot-Appearanz

Wir werden die Appearanz des Plots anpassen, indem wir die y-Achsenbeschriftungen entfernen und einen Titel für den Plot hinzufügen.

```python
for ax in axs.flat:
    ax.set_yticklabels([])

fig.suptitle("Violin Plotting Examples")
fig.subplots_adjust(hspace=0.4)
plt.show()
```
