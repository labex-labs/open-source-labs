# Die Erstellung Ihrer ersten Metaklasse

Jetzt werden wir unsere erste Metaklasse erstellen. Bevor wir mit dem Codieren beginnen, verstehen wir zunächst, was eine Metaklasse ist. In Python ist eine Metaklasse eine Klasse, die andere Klassen erstellt. Sie ist wie ein Bauplan für Klassen. Wenn Sie in Python eine Klasse definieren, verwendet Python eine Metaklasse, um diese Klasse zu erstellen. Standardmäßig verwendet Python die Metaklasse `type`. In diesem Schritt werden wir eine benutzerdefinierte Metaklasse definieren, die Informationen über die Klasse ausgibt, die sie erstellt. Dies wird uns helfen, zu verstehen, wie Metaklassen hinter den Kulissen funktionieren.

1. Öffnen Sie VSCode im WebIDE und erstellen Sie eine neue Datei namens `mymeta.py` im Verzeichnis `/home/labex/project`. Hier werden wir unseren Code für die Metaklasse schreiben.

2. Fügen Sie der Datei folgenden Code hinzu:

```python
# mymeta.py

class mytype(type):
    @staticmethod
    def __new__(meta, name, bases, __dict__):
        print("Creating class :", name)
        print("Base classes   :", bases)
        print("Attributes     :", list(__dict__))
        return super().__new__(meta, name, bases, __dict__)

class myobject(metaclass=mytype):
    pass
```

Lassen Sie uns analysieren, was dieser Code tut:

- Zunächst definieren wir eine neue Klasse namens `mytype`, die von `type` erbt. Da `type` die Standard-Metaklasse in Python ist, erstellen wir durch die Vererbung von ihr unsere eigene benutzerdefinierte Metaklasse.
- Als Nächstes überschreiben wir die Methode `__new__`. In Python ist die Methode `__new__` eine spezielle Methode, die aufgerufen wird, wenn ein neues Objekt erstellt wird. Im Kontext einer Metaklasse wird sie aufgerufen, wenn eine neue Klasse erstellt wird.
- Innerhalb unserer `__new__`-Methode geben wir einige Informationen über die zu erstellende Klasse aus. Wir geben den Namen der Klasse, ihre Basisklassen und ihre Attribute aus. Danach rufen wir die `__new__`-Methode der Elternklasse mit `super().__new__(meta, name, bases, __dict__)` auf. Dies ist wichtig, da es tatsächlich die Klasse erstellt.
- Schließlich erstellen wir eine Basisklasse namens `myobject` und geben an, dass sie unsere benutzerdefinierte Metaklasse `mytype` verwenden soll.

Die `__new__`-Methode nimmt die folgenden Parameter:

- `meta`: Dies bezieht sich auf die Metaklasse selbst. In unserem Fall ist es `mytype`.
- `name`: Dies ist der Name der zu erstellenden Klasse.
- `bases`: Dies ist ein Tupel, das die Basisklassen enthält, von denen die neue Klasse erbt.
- `__dict__`: Dies ist ein Wörterbuch, das die Attribute der Klasse enthält.

3. Speichern Sie die Datei, indem Sie Strg+S drücken oder auf Datei > Speichern klicken. Das Speichern der Datei stellt sicher, dass Ihr Code aufbewahrt wird und später ausgeführt werden kann.
