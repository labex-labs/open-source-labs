# Grundlagen von Python-Klassen

In Python dient eine Klasse als Blaupause für die Erstellung von Objekten. Die objektorientierte Programmierung ist ein leistungsstarkes Verfahren, das es uns ermöglicht, unseren Code effektiv zu organisieren. Dies geschieht, indem verwandte Daten und Funktionen zusammengefasst werden. Auf diese Weise können wir komplexe Programme leichter verwalten und unseren Code modularer und wartbarer gestalten.

Eine Python-Klasse besteht aus zwei Hauptkomponenten:

- **Attribute**: Dies sind Variablen, die Daten innerhalb einer Klasse speichern. Stellen Sie sich Attribute als die Eigenschaften oder Merkmale eines Objekts vor. Wenn wir beispielsweise eine Klasse erstellen, um eine Person darzustellen, könnten die Attribute der Name, das Alter und die Größe der Person sein.
- **Methoden**: Dies sind Funktionen, die zu einer Klasse gehören und deren Attribute zugreifen oder ändern können. Methoden definieren die Aktionen, die ein Objekt ausführen kann. Im Beispiel der Personenklasse könnte eine Methode eine Funktion sein, die das Alter der Person in Monaten berechnet.

Klassen sind äußerst nützlich, da sie eine Möglichkeit bieten, wiederverwendbaren Code zu erstellen und reale Konzepte zu modellieren. In diesem Lab werden wir eine `Stock`-Klasse erstellen. Diese Klasse wird verwendet, um Aktieninformationen wie den Namen der Aktie, die Anzahl der Anteile und den Preis pro Anteil darzustellen.

Hier ist die grundlegende Struktur einer Python-Klasse:

```python
class ClassName:
    def __init__(self, parameter1, parameter2):
        self.attribute1 = parameter1
        self.attribute2 = parameter2

    def method_name(self):
        # Code that uses the attributes
        return result
```

Die `__init__`-Methode ist eine spezielle Methode in Python-Klassen. Sie wird automatisch aufgerufen, wenn wir ein neues Objekt aus der Klasse erstellen. Diese Methode wird verwendet, um die Attribute des Objekts zu initialisieren. Der Parameter `self` ist eine Referenz auf die Instanz der Klasse. Er wird verwendet, um von innerhalb der Klasse auf Attribute und Methoden zuzugreifen. Wenn wir eine Methode auf einem Objekt aufrufen, übergibt Python automatisch das Objekt selbst als erstes Argument, weshalb wir `self` in den Methodendefinitionen verwenden. Dies ermöglicht es uns, mit den Attributen der spezifischen Instanz zu arbeiten und Operationen darauf auszuführen.
