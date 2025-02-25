# Erstellen des PdfPages-Objekts

Als nächstes musst du ein PdfPages-Objekt erstellen, in das du die Seiten der PDF-Datei speichern wirst. Du kannst die `with`-Anweisung verwenden, um sicherzustellen, dass das PdfPages-Objekt am Ende des Blocks richtig geschlossen wird, auch wenn eine Ausnahme auftritt.

```python
with PdfPages('multipage_pdf.pdf') as pdf:
```
