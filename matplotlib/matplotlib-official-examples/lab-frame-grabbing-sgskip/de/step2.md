# Konfigurieren des Schreibers

Wir müssen den Schreiber konfigurieren, der verwendet werden soll, um die Bilder in eine Datei zu schreiben. Wir legen die Bilder pro Sekunde (fps) fest und fügen Metadaten wie Titel, Künstler und Kommentar hinzu.

```python
metadata = dict(title='Movie Test', artist='Matplotlib',
                comment='Movie support!')
writer = FFMpegWriter(fps=15, metadata=metadata)
```
