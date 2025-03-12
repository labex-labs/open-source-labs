# Datenanalyse-Aufgabe mit Daten der Chicago Transit Authority

Nachdem Sie sich mit verschiedenen Python-Datenstrukturen und dem `collections`-Modul vertraut gemacht haben, ist es an der Zeit, diese Fähigkeiten in einer echten Datenanalyseaufgabe anzuwenden. In diesem Experiment werden wir die Fahrgastzahlen der Busse der Chicago Transit Authority (CTA) analysieren. Diese praktische Anwendung wird Ihnen helfen, zu verstehen, wie Sie Python nutzen können, um sinnvolle Informationen aus echten Datensätzen zu extrahieren.

## Das Verständnis der Daten

Zunächst werfen wir einen Blick auf die Verkehrsdaten, mit denen wir arbeiten werden. Im Python-Terminal führen Sie Code aus, um die Daten zu laden und deren grundlegende Struktur zu verstehen.

```python
>>> import readrides
>>> rows = readrides.read_rides_as_dicts('/home/labex/project/ctabus.csv')
>>> print(len(rows))
# This will show the number of records in the dataset

>>> # Let's look at the first record to understand the structure
>>> import pprint
>>> pprint.pprint(rows[0])
```

Die Anweisung `import readrides` importiert ein benutzerdefiniertes Modul, das eine Funktion zum Lesen der Daten aus der CSV-Datei enthält. Die Funktion `readrides.read_rides_as_dicts` liest die Daten aus der angegebenen CSV-Datei und wandelt jede Zeile in ein Wörterbuch um. `len(rows)` gibt uns die Gesamtzahl der Datensätze im Datensatz. Indem wir den ersten Datensatz mit `pprint.pprint(rows[0])` ausgeben, können wir die Struktur jedes Datensatzes deutlich sehen.

Die Daten enthalten tägliche Fahrgastzahlen für verschiedene Buslinien. Jeder Datensatz umfasst:

- `route`: Die Busliniennummer
- `date`: Das Datum im Format "YYYY - MM - DD"
- `daytype`: Entweder "W" für Wochentag, "A" für Samstag oder "U" für Sonntag/Ferientag
- `rides`: Die Anzahl der Fahrgäste an diesem Tag

## Analyseaufgaben

Lösen wir die einzelnen Aufgaben nacheinander:

### Frage 1: Wie viele Buslinien gibt es in Chicago?

Um diese Frage zu beantworten, müssen wir alle eindeutigen Liniennummern im Datensatz finden. Hierfür verwenden wir eine Mengen-Komprehension.

```python
>>> # Get all unique route numbers using a set comprehension
>>> unique_routes = {row['route'] for row in rows}
>>> print(len(unique_routes))
```

Eine Mengen-Komprehension ist eine kompakte Methode, um eine Menge zu erstellen. In diesem Fall iterieren wir über jede Zeile in der `rows`-Liste und extrahieren den `route`-Wert. Da eine Menge nur eindeutige Elemente speichert, erhalten wir am Ende eine Menge aller eindeutigen Liniennummern. Das Ausgeben der Länge dieser Menge gibt uns die Gesamtzahl der eindeutigen Buslinien.

Wir können auch einige dieser Linien anzeigen:

```python
>>> # Print a few of the route numbers
>>> print(list(unique_routes)[:10])
```

Hier wandeln wir die Menge der eindeutigen Linien in eine Liste um und geben dann die ersten 10 Elemente dieser Liste aus.

### Frage 2: Wie viele Menschen fuhren am 2. Februar 2011 mit der Linie 22?

Für diese Frage müssen wir die Daten filtern, um den spezifischen Datensatz zu finden, der der angegebenen Linie und dem Datum entspricht.

```python
>>> # Find rides on route 22 on February 2, 2011
>>> target_date = "2011-02-02"
>>> target_route = "22"
>>>
>>> for row in rows:
...     if row['route'] == target_route and row['date'] == target_date:
...         print(f"Rides on route {target_route} on {target_date}: {row['rides']}")
...         break
```

Wir definieren zunächst die Variablen `target_date` und `target_route`. Dann iterieren wir über jede Zeile in der `rows`-Liste. Für jede Zeile prüfen wir, ob die `route` und das `date` unseren Zielwerten entsprechen. Wenn eine Übereinstimmung gefunden wird, geben wir die Anzahl der Fahrgäste aus und brechen die Schleife ab, da wir den gesuchten Datensatz gefunden haben.

Sie können dies ändern, um jede Linie an jedem beliebigen Datum zu überprüfen, indem Sie die Variablen `target_date` und `target_route` ändern.

### Frage 3: Wie viele Fahrgäste nutzen insgesamt jede Buslinie?

Wir verwenden einen `Counter`, um die Gesamtzahl der Fahrgäste pro Linie zu berechnen. Ein `Counter` ist eine Unterklasse des Wörterbuchs aus dem `collections`-Modul, das zum Zählen von hashbaren Objekten verwendet wird.

```python
>>> from collections import Counter
>>>
>>> # Initialize a counter
>>> total_rides_by_route = Counter()
>>>
>>> # Sum up rides for each route
>>> for row in rows:
...     total_rides_by_route[row['route']] += row['rides']
...
>>> # View the top 5 routes by total ridership
>>> for route, rides in total_rides_by_route.most_common(5):
...     print(f"Route {route}: {rides:,} total rides")
```

Wir importieren zunächst die `Counter`-Klasse aus dem `collections`-Modul. Dann initialisieren wir einen leeren Zähler namens `total_rides_by_route`. Während wir über jede Zeile in der `rows`-Liste iterieren, addieren wir die Anzahl der Fahrgäste für jede Linie zum Zähler. Schließlich verwenden wir die Methode `most_common(5)`, um die 5 Linien mit der höchsten Gesamtzahl der Fahrgäste zu erhalten und die Ergebnisse auszugeben.

### Frage 4: Welche fünf Buslinien hatten die größte Zunahme der Fahrgastzahl von 2001 bis 2011?

Dies ist eine komplexere Aufgabe. Wir müssen die Fahrgastzahlen von 2001 mit denen von 2011 für jede Linie vergleichen.

```python
>>> # Create dictionaries to store total annual rides by route
>>> rides_2001 = Counter()
>>> rides_2011 = Counter()
>>>
>>> # Collect data for each year
>>> for row in rows:
...     if row['date'].startswith('2001-'):
...         rides_2001[row['route']] += row['rides']
...     elif row['date'].startswith('2011-'):
...         rides_2011[row['route']] += row['rides']
...
>>> # Calculate increases
>>> increases = {}
>>> for route in unique_routes:
...     if route in rides_2001 and route in rides_2011:
...         increase = rides_2011[route] - rides_2001[route]
...         increases[route] = increase
...
>>> # Find the top 5 routes with the biggest increases
>>> import heapq
>>> top_5_increases = heapq.nlargest(5, increases.items(), key=lambda x: x[1])
>>>
>>> # Display the results
>>> print("Top 5 routes with the greatest ridership increase from 2001 to 2011:")
>>> for route, increase in top_5_increases:
...     print(f"Route {route}: increased by {increase:,} rides")
...     print(f"  2001 rides: {rides_2001[route]:,}")
...     print(f"  2011 rides: {rides_2011[route]:,}")
...     print()
```

Wir erstellen zunächst zwei `Counter`-Objekte, `rides_2001` und `rides_2011`, um die Gesamtzahl der Fahrgäste für jede Linie in 2001 bzw. 2011 zu speichern. Während wir über jede Zeile in der `rows`-Liste iterieren, prüfen wir, ob das Datum mit '2001 -' oder '2011 -' beginnt und fügen die Fahrgäste dem entsprechenden Zähler hinzu.

Dann erstellen wir ein leeres Wörterbuch `increases`, um die Zunahme der Fahrgastzahl für jede Linie zu speichern. Wir iterieren über die eindeutigen Linien und berechnen die Zunahme, indem wir die Fahrgäste von 2001 von denen von 2011 subtrahieren.

Um die 5 Linien mit der größten Zunahme zu finden, verwenden wir die Funktion `heapq.nlargest`. Diese Funktion nimmt die Anzahl der zurückzugebenden Elemente (in diesem Fall 5), das Iterable (`increases.items()`) und eine Schlüsselfunktion (`lambda x: x[1]`), die angibt, wie die Elemente verglichen werden sollen.

Schließlich geben wir die Ergebnisse aus, wobei wir die Liniennummer, die Zunahme der Fahrgastzahl und die Anzahl der Fahrgäste in 2001 und 2011 anzeigen.

Diese Analyse zeigt, welche Buslinien in der Dekade die stärkste Zunahme der Fahrgastzahl verzeichnet haben, was auf sich ändernde Bevölkerungsmuster, Verbesserungen des Fahrplans oder andere interessante Trends hinweisen könnte.

Sie können diese Analysen auf viele Weise erweitern. Beispielsweise möchten Sie möglicherweise:

- Die Fahrgastmuster nach Wochentag analysieren
- Linien mit abnehmender Fahrgastzahl finden
- Die saisonalen Schwankungen der Fahrgastzahl vergleichen

Die Techniken, die Sie in diesem Lab gelernt haben, bilden eine solide Grundlage für diese Art von Datenexploration und -analyse.
