# Erstellen von Stock-Objekten

Nachdem wir unsere `Stock`-Klasse definiert haben, ist es an der Zeit, sie in Aktion zu setzen. Das Erstellen von Instanzen einer Klasse ist wie das Erstellen spezifischer Beispiele anhand einer allgemeinen Blaupause. In diesem Fall ist die `Stock`-Klasse unsere Blaupause, und wir werden einige Aktienobjekte erstellen. Nachdem wir diese Objekte erstellt haben, lernen wir, wie wir auf ihre Attribute (Eigenschaften) und Methoden (Aktionen, die sie ausführen können) zugreifen können.

1. Zunächst müssen wir ein Terminal im WebIDE öffnen. Das Terminal ist wie ein Befehlszentrum, in dem wir unserem Computer Anweisungen geben können. Um es zu öffnen, klicken Sie im Menü auf "Terminal".

2. Sobald das Terminal geöffnet ist, müssen wir sicherstellen, dass wir uns im richtigen Projektverzeichnis befinden. Das Projektverzeichnis ist der Ort, an dem alle relevanten Dateien für unser Projekt gespeichert sind. Wenn Sie sich noch nicht im Projektverzeichnis befinden, verwenden Sie den folgenden Befehl, um dorthin zu navigieren:

```bash
cd /home/labex/project
```

3. Jetzt möchten wir Python im interaktiven Modus mit unserer `stock.py`-Datei starten. Der interaktive Modus ermöglicht es uns, unseren Code Schritt für Schritt zu testen und die Ergebnisse sofort zu sehen. Die `stock.py`-Datei enthält die Definition unserer `Stock`-Klasse. Verwenden Sie den folgenden Befehl:

```bash
python3 -i stock.py
```

Das `-i`-Flag ist hier wichtig. Es teilt Python mit, das `stock.py`-Skript zuerst auszuführen. Nach dem Ausführen des Skripts startet es eine interaktive Sitzung. In dieser Sitzung können wir auf alle Klassen und Variablen zugreifen, die im `stock.py`-Skript definiert wurden.

4. Erstellen wir ein neues `Stock`-Objekt für Google-Aktien. Das Erstellen eines Objekts ist wie das Erstellen einer spezifischen Instanz der `Stock`-Klasse mit bestimmten Werten. Verwenden Sie den folgenden Code:

```python
s = Stock('GOOG', 100, 490.10)
```

Diese Codezeile erstellt eine neue Instanz der `Stock`-Klasse. Hier ist, was jeder Wert bedeutet:

- Name: 'GOOG' - Dies ist das Symbol für Google-Aktien.
- Anzahl der Anteile: 100 - Sie repräsentiert die Anzahl der Google-Aktien, die wir besitzen.
- Preis pro Anteil: 490.10 - Dies ist der Preis pro Anteil der Google-Aktien.

5. Nun, da wir unser `Stock`-Objekt haben, können wir auf seine Attribute zugreifen. Attribute sind wie die Eigenschaften eines Objekts. Um auf ein Attribut zuzugreifen, verwenden wir den Namen des Objekts, gefolgt von einem Punkt und dem Attributnamen.

```python
s.name
```

Wenn Sie diesen Code ausführen, wird der Name der Aktie ausgegeben:

```
'GOOG'
```

Lassen Sie uns die Anzahl der Anteile abrufen:

```python
s.shares
```

Die Ausgabe wird die Anzahl der Anteile sein, die wir definiert haben:

```
100
```

Schließlich lassen Sie uns den Preis pro Anteil abrufen:

```python
s.price
```

Die Ausgabe wird der Preis pro Anteil sein:

```
490.1
```

6. Unsere `Stock`-Klasse hat eine Methode namens `cost()`. Eine Methode ist wie eine Aktion, die ein Objekt ausführen kann. In diesem Fall berechnet die `cost()`-Methode die Gesamtkosten unserer Anteile. Um diese Methode aufzurufen, verwenden Sie den folgenden Code:

```python
s.cost()
```

Die Ausgabe wird die Gesamtkosten sein:

```
49010.0
```

Die `cost()`-Methode funktioniert, indem sie die Anzahl der Anteile (100) mit dem Preis pro Anteil (490.10) multipliziert, was uns 49010.0 ergibt.
