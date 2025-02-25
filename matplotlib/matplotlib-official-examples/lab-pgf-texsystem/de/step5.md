# Layout anpassen und Plot speichern

Schließlich kannst du das Layout deines Plots anpassen und ihn mithilfe der Funktionen `fig.tight_layout()` und `fig.savefig()` in eine Datei speichern.

```python
fig.tight_layout(pad=.5)

fig.savefig("pgf_texsystem.pdf")
fig.savefig("pgf_texsystem.png")
```
