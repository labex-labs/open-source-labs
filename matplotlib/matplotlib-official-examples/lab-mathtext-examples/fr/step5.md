# Tracer la formule de démonstration d'en-tête

Dans cette étape, nous allons tracer la formule de démonstration d'en-tête.

```python
full_demo = mathtext_demos['Header demo']
ax.annotate(full_demo,
            xy=(0.5, 1. - 0.59 * line_axesfrac),
            color='tab:orange', ha='center', fontsize=20)
```
