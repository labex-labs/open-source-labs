# Speichern des Diagramms

Schließlich können wir unser Diagramm auf der Festplatte speichern. Folgen Sie diesen Schritten:

1. Drucken Sie die unterstützten Dateiformate mit `print(fig.canvas.get_supported_filetypes())`.

```python
print(fig.canvas.get_supported_filetypes())
```

2. Speichern Sie die Figur als Bilddatei mit `fig.savefig(file_path, transparent=False, dpi=80, bbox_inches="tight")`. Entfernen Sie das Kommentarzeichen von dieser Zeile, um die Figur zu speichern.

```python
fig.savefig('sales.png', transparent=False, dpi=80, bbox_inches="tight")
```

Sie können die gespeicherte Bilddatei mithilfe des Dateiexplorers in der linken Seitenleiste öffnen.
