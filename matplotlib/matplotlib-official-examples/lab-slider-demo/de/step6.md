# Registrieren der Aktualisierungsfunktion bei den Schiebereglern

Als nächstes registrieren wir die Aktualisierungsfunktion bei jedem Schieberegler, sodass die Funktion jedes Mal aufgerufen wird, wenn wir die Schieberegler anpassen.

```python
freq_slider.on_changed(update)
amp_slider.on_changed(update)
```
