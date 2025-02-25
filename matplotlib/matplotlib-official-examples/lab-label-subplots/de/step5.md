# Bezeichnung mit Titel

Wenn wir möchten, dass die Bezeichnung mit dem Titel ausgerichtet ist, können wir sie in den Titel aufnehmen oder das Schlüsselwortargument `loc` verwenden.

```python
for label, ax in axs.items():
    ax.set_title('Normaler Titel', fontstyle='italic')
    ax.set_title(label, fontfamily='serif', loc='left', fontsize='medium')
```
