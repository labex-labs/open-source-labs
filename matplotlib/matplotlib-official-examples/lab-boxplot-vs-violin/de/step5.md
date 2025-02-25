# Horizontale Linien und Labels hinzufügen

Wir werden horizontale Gitternetzlinien hinzufügen und die x- und y-Labels für die Diagramme festlegen.

```python
for ax in axs:
    ax.yaxis.grid(True)
    ax.set_xticks([y + 1 for y in range(len(all_data))], labels=['x1', 'x2', 'x3', 'x4'])
    ax.set_xlabel('Four separate samples')
    ax.set_ylabel('Observed values')
```
