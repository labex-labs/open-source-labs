# Ändern von Globalen Variablen

Wenn Sie eine globale Variable ändern müssen, müssen Sie sie als solche deklarieren.

```python
name = 'Dave'

def spam():
    global name
    name = 'Guido' # Ändert die globale Variable oben
```

Die `global`-Deklaration muss vor ihrem Gebrauch erscheinen und die entsprechende Variable muss in derselben Datei wie die Funktion existieren. Nachdem Sie das gesehen haben, wissen Sie, dass dies als schlechte Form angesehen wird. Tatsächlich sollten Sie `global` gänzlich vermeiden, wenn möglich. Wenn Sie eine Funktion benötigen, um einen bestimmten Zustand außerhalb der Funktion zu ändern, ist es besser, eine Klasse zu verwenden (mehr dazu später).
