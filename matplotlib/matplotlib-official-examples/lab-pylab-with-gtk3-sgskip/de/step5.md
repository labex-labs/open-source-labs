# Label zur VBox hinzufügen

Wir werden ein Label zur VBox hinzufügen, um die x,y-Koordinaten der Maus anzuzeigen, wenn diese über der Achse gezogen wird. Zunächst erstellen wir ein Label mit einigen Text und fügen es zur VBox hinzu.

```python
label = Gtk.Label()
label.set_markup('Drag mouse over axes for position')
label.show()
vbox.pack_start(label, False, False, 0)
```
