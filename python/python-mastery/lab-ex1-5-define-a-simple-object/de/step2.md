# Erstellen der Stock-Klasse

In Python ist eine Klasse eine Blaupause für die Erstellung von Objekten. Sie ermöglicht es Ihnen, Daten und Funktionalität zusammenzufassen. Jetzt erstellen wir unsere `Stock`-Klasse, um Aktieninformationen darzustellen. Eine Aktie hat bestimmte Eigenschaften, wie ihren Namen, die Anzahl der Anteile und den Preis pro Anteil. Wir werden Attribute für diese Aspekte innerhalb unserer Klasse definieren.

1. Zunächst müssen Sie sich im richtigen Verzeichnis im WebIDE befinden. Wenn Sie sich noch nicht im Verzeichnis `/home/labex/project` befinden, navigieren Sie dorthin. Hier werden wir an unserem `Stock`-Klassencode arbeiten.

2. Sobald Sie sich im richtigen Verzeichnis befinden, erstellen Sie eine neue Datei im Editor. Benennen Sie diese Datei `stock.py`. In dieser Datei wird der Code für unsere `Stock`-Klasse gespeichert.

3. Jetzt fügen wir den Code hinzu, um die `Stock`-Klasse zu definieren. Kopieren Sie den folgenden Code und fügen Sie ihn in die Datei `stock.py` ein:

```python
class Stock:
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price

    def cost(self):
        return self.shares * self.price
```

In diesem Code:

- Die Anweisung `class Stock:` erstellt eine neue Klasse mit dem Namen `Stock`. Dies ist wie eine Vorlage für die Erstellung von Aktienobjekten.
- Die `__init__`-Methode ist eine spezielle Methode in Python-Klassen. Sie wird Konstruktor genannt. Wenn Sie ein neues Objekt der `Stock`-Klasse erstellen, wird die `__init__`-Methode automatisch ausgeführt. Sie nimmt drei Parameter entgegen: `name`, `shares` und `price`. Diese Parameter repräsentieren die Informationen über die Aktie.
- Innerhalb der `__init__`-Methode verwenden wir `self`, um auf die Instanz der Klasse zu verweisen. Wir speichern die Werte der Parameter als Instanzattribute. Beispielsweise speichert `self.name = name` den `name`-Parameter als Attribut des Objekts.
- Die `cost()`-Methode ist eine benutzerdefinierte Methode, die wir definiert haben. Sie berechnet die Gesamtkosten der Aktie, indem sie die Anzahl der Anteile (`self.shares`) mit dem Preis pro Anteil (`self.price`) multipliziert.

4. Nachdem Sie den Code hinzugefügt haben, speichern Sie die Datei. Sie können dies tun, indem Sie `Strg+S` drücken oder auf das Speicher-Symbol klicken. Das Speichern der Datei stellt sicher, dass Ihre Änderungen beibehalten werden.

Lassen Sie uns den Code erneut untersuchen, um sicherzustellen, dass wir ihn verstehen:

- Wir haben eine Klasse mit dem Namen `Stock` definiert. Diese Klasse wird verwendet, um Aktienobjekte zu erstellen.
- Die `__init__`-Methode nimmt drei Parameter entgegen: `name`, `shares` und `price`. Sie initialisiert die Attribute des Objekts mit diesen Werten.
- Innerhalb von `__init__` speichern wir diese Parameter als Instanzattribute unter Verwendung von `self`. Dies ermöglicht es jedem Objekt, seine eigenen Werte für diese Attribute zu haben.
- Wir haben eine `cost()`-Methode hinzugefügt, die die Gesamtkosten berechnet, indem sie die Anzahl der Anteile mit dem Preis multipliziert. Dies ist eine nützliche Funktionalität für unsere Aktienobjekte.

Wenn wir ein `Stock`-Objekt erstellen, wird die `__init__`-Methode automatisch ausgeführt und setzt den Anfangszustand unseres Objekts mit den Werten, die wir angeben, fest. Auf diese Weise können wir problemlos mehrere Aktienobjekte mit verschiedenen Namen, Anzahlen von Anteilen und Preisen erstellen.
