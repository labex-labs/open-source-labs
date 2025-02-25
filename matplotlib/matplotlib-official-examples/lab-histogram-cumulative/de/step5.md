# Bezeichnen der Figur

In diesem Schritt werden wir die Figur bezeichnen. Wir werden einen Titel, Rasterlinien und Beschriftungen für die x- und y-Achsen hinzufügen.

```python
fig.suptitle("Cumulative Distributions")
for ax in axs:
    ax.grid(True)
    ax.legend()
    ax.set_xlabel("Annual rainfall (mm)")
    ax.set_ylabel("Probability of occurrence")
    ax.label_outer()

plt.show()
```
