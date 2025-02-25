# Personnaliser l'apparence du tracé

Nous allons personnaliser l'apparence du tracé en supprimant les étiquettes de l'axe des y et en ajoutant un titre au tracé.

```python
for ax in axs.flat:
    ax.set_yticklabels([])

fig.suptitle("Violin Plotting Examples")
fig.subplots_adjust(hspace=0.4)
plt.show()
```
