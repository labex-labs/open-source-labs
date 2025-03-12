# Die Erkundung der Metaklassenvererbung

Metaklassen haben eine faszinierende Eigenschaft: Sie sind "haftend". Das bedeutet, dass wenn eine Klasse eine Metaklasse verwendet, alle ihre Subklassen in der Vererbungshierarchie ebenfalls dieselbe Metaklasse verwenden werden. Mit anderen Worten, die Metaklasseigenschaft breitet sich entlang der Vererbungskette aus.

Lassen Sie uns dies in Aktion sehen:

1. Öffnen Sie zunächst die Datei `mymeta.py`. Am Ende dieser Datei werden wir eine neue Klasse hinzufügen. Diese Klasse, namens `MyStock`, wird von der `Stock`-Klasse erben. Die `__init__`-Methode wird verwendet, um die Attribute des Objekts zu initialisieren, und wir rufen die `__init__`-Methode der Elternklasse mit `super().__init__` auf, um die gemeinsamen Attribute zu initialisieren. Die `info`-Methode wird verwendet, um einen formatierten String mit Informationen über die Aktie zurückzugeben. Fügen Sie folgenden Code hinzu:

```python
class MyStock(Stock):
    def __init__(self, name, shares, price, category):
        super().__init__(name, shares, price)
        self.category = category

    def info(self):
        return f"{self.name} ({self.category}): {self.shares} shares at ${self.price}"
```

2. Nachdem Sie den Code hinzugefügt haben, speichern Sie die Datei `mymeta.py`. Das Speichern der Datei stellt sicher, dass die von uns vorgenommenen Änderungen gespeichert werden und später verwendet werden können.

3. Jetzt werden wir eine neue Datei namens `test_inheritance.py` erstellen, um das Vererbungsverhalten der Metaklasse zu testen. In dieser Datei werden wir die `MyStock`-Klasse aus der Datei `mymeta.py` importieren. Dann werden wir eine Instanz der `MyStock`-Klasse erstellen, ihre Methoden aufrufen und die Ergebnisse ausgeben, um zu sehen, wie die Metaklasse über Vererbung funktioniert. Fügen Sie folgenden Code in `test_inheritance.py` hinzu:

```python
# test_inheritance.py
from mymeta import MyStock

# Create a MyStock instance
tech_stock = MyStock("MSFT", 50, 305.75, "Technology")

# Test the methods
print(tech_stock.info())
print(f"Total cost: ${tech_stock.cost()}")

# Sell some shares
tech_stock.sell(5)
print(f"After selling: {tech_stock.shares} shares remaining")
print(f"Updated cost: ${tech_stock.cost()}")
```

4. Schließlich führen Sie die Datei `test_inheritance.py` aus, um die Metaklasse in Aktion über Vererbung zu sehen. Öffnen Sie Ihr Terminal, navigieren Sie zum Verzeichnis, in dem sich die Datei `test_inheritance.py` befindet, und führen Sie den folgenden Befehl aus:

```bash
python3 test_inheritance.py
```

Sie sollten eine Ausgabe ähnlich der folgenden sehen:

```
Creating class : myobject
Base classes   : ()
Attributes     : ['__module__', '__qualname__', '__doc__']
Creating class : Stock
Base classes   : (<class 'mymeta.myobject'>,)
Attributes     : ['__module__', '__qualname__', '__init__', 'cost', 'sell', '__doc__']
Creating class : MyStock
Base classes   : (<class 'mymeta.Stock'>,)
Attributes     : ['__module__', '__qualname__', '__init__', 'info', '__doc__']
MSFT (Technology): 50 shares at $305.75
Total cost: $15287.5
After selling: 45 shares remaining
Updated cost: $13758.75
```

Beachten Sie, dass obwohl wir für die `MyStock`-Klasse keine Metaklasse explizit angegeben haben, die Metaklasse dennoch angewendet wird. Dies zeigt deutlich, wie Metaklassen über Vererbung propagieren.

## Praktische Anwendungen von Metaklassen

In unserem Beispiel gibt die Metaklasse einfach Informationen über Klassen aus. Metaklassen haben jedoch viele praktische Anwendungen in der realen Programmierung:

1. **Validierung**: Sie können Metaklassen verwenden, um zu prüfen, ob eine Klasse die erforderlichen Methoden oder Attribute hat. Dies hilft sicherzustellen, dass Klassen bestimmte Kriterien erfüllen, bevor sie verwendet werden.
2. **Registrierung**: Metaklassen können Klassen automatisch in einem Register eintragen. Dies ist nützlich, wenn Sie alle Klassen eines bestimmten Typs verfolgen müssen.
3. **Schnittstellenimplementierung**: Sie können verwendet werden, um sicherzustellen, dass Klassen erforderliche Schnittstellen implementieren. Dies hilft, eine konsistente Struktur in Ihrem Code aufrechtzuerhalten.
4. **Aspektorientierte Programmierung**: Metaklassen können Verhaltensweisen zu Methoden hinzufügen. Beispielsweise können Sie Protokollierung oder Leistungsüberwachung zu Methoden hinzufügen, ohne den Methodencode direkt zu ändern.
5. **ORM-Systeme**: In Objekt-Relationalen Mapping (ORM)-Systemen wie Django oder SQLAlchemy werden Metaklassen verwendet, um Klassen auf Datenbanktabellen abzubilden. Dies vereinfacht die Datenbankoperationen in Ihrer Anwendung.

Metaklassen sind sehr leistungsstark, sollten jedoch sparsam verwendet werden. Wie Tim Peters (berühmt für die "Zen of Python") einmal sagte: "Metaklassen sind eine tiefere Magie als 99 % der Benutzer jemals befürchten müssen."
