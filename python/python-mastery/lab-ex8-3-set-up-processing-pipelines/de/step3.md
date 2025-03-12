# Verbessern der Coroutine-Pipeline

Nachdem wir nun eine grundlegende Pipeline eingerichtet und in Betrieb haben, ist es an der Zeit, sie flexibler zu gestalten. In der Programmierung ist Flexibilität von entscheidender Bedeutung, da sie unseren Code in die Lage versetzt, sich an verschiedene Anforderungen anzupassen. Wir werden dies erreichen, indem wir unser `coticker.py`-Programm so ändern, dass es verschiedene Filter- und Formatierungsoptionen unterstützt.

1. Öffnen Sie zunächst die Datei `coticker.py` in Ihrem Code-Editor. Der Code-Editor ist der Ort, an dem Sie alle erforderlichen Änderungen am Programm vornehmen. Er bietet eine bequeme Umgebung, um Ihren Code anzuzeigen, zu bearbeiten und zu speichern.

2. Als Nächstes fügen wir eine neue Coroutine hinzu, die Daten nach Aktienname filtert. Eine Coroutine ist eine spezielle Art von Funktion, die ihre Ausführung anhalten und fortsetzen kann. Dies ermöglicht es uns, eine Pipeline zu erstellen, in der Daten durch verschiedene Verarbeitungsschritte fließen können. Hier ist der Code für die neue Coroutine:

```python
@consumer
def filter_by_name(name, target):
    while True:
        record = yield
        if record.name == name:
            target.send(record)
```

In diesem Code nimmt die `filter_by_name`-Coroutine einen Aktiennamen und eine Ziel-Coroutine als Parameter. Sie wartet kontinuierlich auf einen Datensatz mithilfe des `yield`-Schlüsselworts. Wenn ein Datensatz ankommt, prüft sie, ob der Name des Datensatzes mit dem angegebenen Namen übereinstimmt. Wenn dies der Fall ist, sendet sie den Datensatz an die Ziel-Coroutine.

3. Jetzt fügen wir eine weitere Coroutine hinzu, die basierend auf Preis-Schwellenwerten filtert. Diese Coroutine wird uns helfen, Aktien in einem bestimmten Preisbereich auszuwählen. Hier ist der Code:

```python
@consumer
def price_threshold(min_price, max_price, target):
    while True:
        record = yield
        if min_price <= record.price <= max_price:
            target.send(record)
```

Ähnlich wie die vorherige Coroutine wartet die `price_threshold`-Coroutine auf einen Datensatz. Sie prüft dann, ob der Preis des Datensatzes innerhalb des angegebenen Mindest- und Höchstpreises liegt. Wenn dies der Fall ist, sendet sie den Datensatz an die Ziel-Coroutine.

4. Nachdem wir die neuen Coroutinen hinzugefügt haben, müssen wir das Hauptprogramm aktualisieren, um diese zusätzlichen Filter zu demonstrieren. Das Hauptprogramm ist der Einstiegspunkt unserer Anwendung, in dem wir die Verarbeitungspipelines einrichten und den Datenfluss starten. Hier ist der aktualisierte Code:

```python
if __name__ == '__main__':
    import sys

    # Define the field names to display
    fields = ['name', 'price', 'change', 'high', 'low']

    # Create the processing pipeline with multiple outputs

    # Pipeline 1: Show all negative changes (same as before)
    print("Stocks with negative changes:")
    t1 = ticker('text', fields)
    neg_filter = negchange(t1)
    tick_creator1 = create_ticker(neg_filter)
    csv_parser1 = to_csv(tick_creator1)

    # Start following the file with the first pipeline
    import threading
    threading.Thread(target=follow, args=('stocklog.csv', csv_parser1), daemon=True).start()

    # Wait a moment to see some results
    import time
    time.sleep(5)

    # Pipeline 2: Filter by name (AAPL)
    print("\nApple stock updates:")
    t2 = ticker('text', fields)
    name_filter = filter_by_name('AAPL', t2)
    tick_creator2 = create_ticker(name_filter)
    csv_parser2 = to_csv(tick_creator2)

    # Follow the file with the second pipeline
    threading.Thread(target=follow, args=('stocklog.csv', csv_parser2), daemon=True).start()

    # Wait a moment to see some results
    time.sleep(5)

    # Pipeline 3: Filter by price range
    print("\nStocks priced between 50 and 75:")
    t3 = ticker('text', fields)
    price_filter = price_threshold(50, 75, t3)
    tick_creator3 = create_ticker(price_filter)
    csv_parser3 = to_csv(tick_creator3)

    # Follow with the third pipeline
    follow('stocklog.csv', csv_parser3)
```

In diesem aktualisierten Code erstellen wir drei verschiedene Verarbeitungspipelines. Die erste Pipeline zeigt Aktien mit negativen Änderungen, die zweite Pipeline filtert Aktien nach dem Namen 'AAPL' und die dritte Pipeline filtert Aktien basierend auf einem Preisbereich zwischen 50 und 75. Wir verwenden Threads, um die ersten beiden Pipelines gleichzeitig auszuführen, was es uns ermöglicht, Daten effizienter zu verarbeiten.

5. Nachdem Sie alle Änderungen vorgenommen haben, speichern Sie die Datei. Das Speichern der Datei stellt sicher, dass alle Ihre Änderungen beibehalten werden. Führen Sie dann das aktualisierte Programm mit den folgenden Befehlen in Ihrem Terminal aus:

```bash
cd /home/labex/project
python3 coticker.py
```

Der `cd`-Befehl wechselt das aktuelle Verzeichnis in das Projektverzeichnis, und der Befehl `python3 coticker.py` führt das Python-Programm aus.

6. Nach dem Ausführen des Programms sollten Sie drei verschiedene Ausgaben sehen:
   - Zunächst werden Sie Aktien mit negativen Änderungen sehen.
   - Dann werden Sie alle Aktienaktualisierungen von AAPL sehen.
   - Schließlich werden Sie alle Aktien sehen, deren Preis zwischen 50 und 75 liegt.

## Das Verständnis der verbesserten Pipeline

Das verbesserte Programm demonstriert mehrere wichtige Konzepte:

1. **Mehrere Pipelines**: Wir können mehrere Verarbeitungspipelines aus derselben Datenquelle erstellen. Dies ermöglicht es uns, verschiedene Arten von Analysen an denselben Daten gleichzeitig durchzuführen.
2. **Spezialisierte Filter**: Wir können verschiedene Coroutinen für bestimmte Filteraufgaben erstellen. Diese Filter helfen uns, nur die Daten auszuwählen, die unseren spezifischen Kriterien entsprechen.
3. **Gleichzeitige Verarbeitung**: Mit Hilfe von Threads können wir mehrere Pipelines gleichzeitig ausführen. Dies verbessert die Effizienz unseres Programms, indem es uns ermöglicht, Daten parallel zu verarbeiten.
4. **Pipeline-Zusammensetzung**: Coroutinen können auf verschiedene Weise kombiniert werden, um verschiedene Datenverarbeitungsziele zu erreichen. Dies gibt uns die Flexibilität, unsere Datenverarbeitungspipelines nach unseren Bedürfnissen anzupassen.

Dieser Ansatz bietet eine flexible und modulare Möglichkeit, Streaming-Daten zu verarbeiten. Er ermöglicht es Ihnen, Verarbeitungsschritte hinzuzufügen oder zu ändern, ohne die Gesamtarchitektur des Programms zu ändern.
