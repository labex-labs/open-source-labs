# Erstellen von benutzerdefinierten Descriptor

In diesem Schritt werden wir unsere eigene Descriptor-Klasse erstellen. Aber zunächst verstehen wir, was ein Descriptor ist. Ein Descriptor ist ein Python-Objekt, das das Descriptor-Protokoll implementiert, das aus den Methoden `__get__`, `__set__` und `__delete__` besteht. Diese Methoden ermöglichen es dem Descriptor, zu verwalten, wie auf ein Attribut zugegriffen, es festgelegt und gelöscht wird. Indem wir unsere eigene Descriptor-Klasse erstellen, können wir besser verstehen, wie dieses Protokoll funktioniert.

Erstellen Sie im Projektverzeichnis eine neue Datei namens `descrip.py`. Diese Datei wird unsere benutzerdefinierte Descriptor-Klasse enthalten. Hier ist der Code:

```python
# descrip.py

class Descriptor:
    def __init__(self, name):
        self.name = name

    def __get__(self, instance, cls):
        print(f'{self.name}:__get__')
        # In a real descriptor, you would return a value here

    def __set__(self, instance, value):
        print(f'{self.name}:__set__ {value}')
        # In a real descriptor, you would store the value here

    def __delete__(self, instance):
        print(f'{self.name}:__delete__')
        # In a real descriptor, you would delete the value here
```

In der `Descriptor`-Klasse initialisiert die `__init__`-Methode den Descriptor mit einem Namen. Die `__get__`-Methode wird aufgerufen, wenn auf das Attribut zugegriffen wird, die `__set__`-Methode wird aufgerufen, wenn das Attribut festgelegt wird, und die `__delete__`-Methode wird aufgerufen, wenn das Attribut gelöscht wird.

Jetzt erstellen wir eine Testdatei, um mit unserem benutzerdefinierten Descriptor zu experimentieren. Dies hilft uns zu verstehen, wie sich der Descriptor in verschiedenen Szenarien verhält. Erstellen Sie eine Datei namens `test_descrip.py` mit dem folgenden Code:

```python
# test_descrip.py

from descrip import Descriptor

class Foo:
    a = Descriptor('a')
    b = Descriptor('b')
    c = Descriptor('c')

# Create an instance and try accessing the attributes
if __name__ == '__main__':
    f = Foo()
    print("Accessing attribute f.a:")
    f.a

    print("\nAccessing attribute f.b:")
    f.b

    print("\nSetting attribute f.a = 23:")
    f.a = 23

    print("\nDeleting attribute f.a:")
    del f.a
```

In der `test_descrip.py`-Datei importieren wir die `Descriptor`-Klasse aus `descrip.py`. Dann erstellen wir eine Klasse `Foo` mit drei Attributen `a`, `b` und `c`, die jeweils von einem Descriptor verwaltet werden. Wir erstellen eine Instanz von `Foo` und führen Operationen wie Zugriff, Festlegung und Löschung von Attributen aus, um zu sehen, wie die Descriptor-Methoden aufgerufen werden.

Jetzt führen wir diese Testdatei aus, um die Descriptor in Aktion zu sehen. Öffnen Sie Ihr Terminal, navigieren Sie zum Projektverzeichnis und führen Sie die Testdatei mit den folgenden Befehlen aus:

```bash
cd ~/project
python3 test_descrip.py
```

Sie sollten eine Ausgabe wie diese sehen:

```
Accessing attribute f.a:
a:__get__

Accessing attribute f.b:
b:__get__

Setting attribute f.a = 23:
a:__set__ 23

Deleting attribute f.a:
a:__delete__
```

Wie Sie sehen können, wird jedes Mal, wenn Sie auf ein Attribut zugreifen, es festlegen oder löschen, das von einem Descriptor verwaltet wird, die entsprechende magische Methode (`__get__`, `__set__` oder `__delete__`) aufgerufen.

Lassen Sie uns auch unseren Descriptor interaktiv untersuchen. Dies ermöglicht es uns, den Descriptor in Echtzeit zu testen und die Ergebnisse sofort zu sehen. Öffnen Sie Ihr Terminal, navigieren Sie zum Projektverzeichnis und starten Sie eine interaktive Python-Sitzung mit der `descrip.py`-Datei:

```bash
cd ~/project
python3 -i descrip.py
```

Geben Sie jetzt diese Befehle in der interaktiven Python-Sitzung ein, um zu sehen, wie das Descriptor-Protokoll funktioniert:

```python
class Foo:
    a = Descriptor('a')
    b = Descriptor('b')
    c = Descriptor('c')

f = Foo()
f.a         # Should call __get__
f.b         # Should call __get__
f.a = 23    # Should call __set__
del f.a     # Should call __delete__
exit()
```

Der wichtigste Aspekt hier ist, dass Descriptor eine Möglichkeit bieten, den Zugriff auf Attribute abzufangen und anzupassen. Dies macht sie leistungsstark für die Implementierung von Datenvalidierung, berechneten Attributen und anderen fortgeschrittenen Verhaltensweisen. Mit Descriptor haben Sie mehr Kontrolle darüber, wie auf die Klassenattribute zugegriffen, sie festgelegt und gelöscht werden.
