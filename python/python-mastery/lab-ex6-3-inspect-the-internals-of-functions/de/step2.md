# Verwendung des `inspect`-Moduls

In Python enthält die Standardbibliothek ein sehr nützliches `inspect`-Modul. Dieses Modul ist wie ein Detektivwerkzeug, das uns hilft, Informationen über lebende Objekte in Python zu sammeln. Lebende Objekte können Dinge wie Module, Klassen und Funktionen sein. Anstatt manuell durch die Attribute eines Objekts zu wühlen, um Informationen zu finden, bietet das `inspect`-Modul organisiertere und hochwertigere Methoden, um die Eigenschaften von Funktionen zu verstehen.

Lassen Sie uns weiterhin die gleiche interaktive Python-Shell verwenden, um zu untersuchen, wie dieses Modul funktioniert.

## Funktionssignaturen

Die `inspect.signature()`-Funktion ist ein nützliches Werkzeug. Wenn Sie eine Funktion an sie übergeben, gibt sie ein `Signature`-Objekt zurück. Dieses Objekt enthält wichtige Details über die Parameter der Funktion.

Hier ist ein Beispiel. Nehmen wir an, wir haben eine Funktion namens `add`. Wir können die `inspect.signature()`-Funktion verwenden, um ihre Signatur zu erhalten:

```python
import inspect
sig = inspect.signature(add)
print(sig)
```

Wenn Sie diesen Code ausführen, wird die Ausgabe sein:

```
(x, y)
```

Diese Ausgabe zeigt uns die Signatur der Funktion, die uns sagt, welche Parameter die Funktion akzeptieren kann.

## Untersuchung von Parameterdetails

Wir können einen Schritt weiter gehen und tiefere Informationen über jeden Parameter der Funktion erhalten.

```python
print(sig.parameters)
```

Die Ausgabe dieses Codes wird sein:

```
OrderedDict([('x', <Parameter "x">), ('y', <Parameter "y">)])
```

Die Parameter der Funktion werden in einem geordneten Wörterbuch gespeichert. Manchmal interessieren uns möglicherweise nur die Namen der Parameter. Wir können dieses geordnete Wörterbuch in ein Tupel umwandeln, um nur die Parameternamen zu extrahieren.

```python
param_names = tuple(sig.parameters)
print(param_names)
```

Die Ausgabe wird sein:

```
('x', 'y')
```

## Untersuchung einzelner Parameter

Wir können uns auch genauer jeden einzelnen Parameter ansehen. Der folgende Code durchläuft jeden Parameter in der Funktion und gibt einige wichtige Details darüber aus.

```python
for name, param in sig.parameters.items():
    print(f"Parameter: {name}")
    print(f"  Kind: {param.kind}")
    print(f"  Default: {param.default if param.default is not param.empty else 'No default'}")
```

Dieser Code zeigt uns Details zu jedem Parameter. Er sagt uns die Art des Parameters (ob es sich um einen Positions- oder einen Schlüsselwortparameter handelt usw.) und seinen Standardwert, falls er einen hat.

Das `inspect`-Modul hat viele andere nützliche Funktionen für die Funktionsintrospektion. Hier sind einige Beispiele:

- `inspect.getdoc(obj)`: Diese Funktion ruft die Dokumentationszeichenkette für ein Objekt ab. Dokumentationszeichenketten sind wie Notizen, die Programmierer schreiben, um zu erklären, was ein Objekt tut.
- `inspect.getfile(obj)`: Sie hilft uns herauszufinden, in welcher Datei ein Objekt definiert ist. Dies kann sehr nützlich sein, wenn wir den Quellcode eines Objekts lokalisieren möchten.
- `inspect.getsource(obj)`: Diese Funktion holt den Quellcode eines Objekts. Sie ermöglicht es uns, genau zu sehen, wie das Objekt implementiert ist.
