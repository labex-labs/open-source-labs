# Grundlagen zu Datumsobjekten in Python

Bevor wir die Monatsdifferenz zwischen Daten berechnen, müssen wir verstehen, wie man mit Datumsobjekten in Python arbeitet. In diesem Schritt lernen wir über das `datetime`-Modul und erstellen einige Datumsobjekte.

Zunächst erstellen wir eine neue Python-Datei im Projektverzeichnis. Öffnen Sie die WebIDE und klicken Sie auf das Symbol "Neue Datei" im Explorer-Bereich auf der linken Seite. Benennen Sie die Datei `month_difference.py` und speichern Sie sie im Verzeichnis `/home/labex/project`.

Fügen Sie nun den folgenden Code hinzu, um die erforderlichen Module zu importieren:

```python
from datetime import date
from math import ceil

# Create example date objects
date1 = date(2023, 1, 15)  # January 15, 2023
date2 = date(2023, 3, 20)  # March 20, 2023

# Print the dates to see their format
print(f"Date 1: {date1}")
print(f"Date 2: {date2}")

# Calculate the difference in days
day_difference = (date2 - date1).days
print(f"Difference in days: {day_difference}")
```

Speichern Sie die Datei und führen Sie sie über das Terminal aus:

```bash
python3 ~/project/month_difference.py
```

Sie sollten eine Ausgabe ähnlich der folgenden sehen:

```
Date 1: 2023-01-15
Date 2: 2023-03-20
Difference in days: 64
```

Die `date`-Klasse aus dem `datetime`-Modul ermöglicht es uns, Datumsobjekte zu erstellen, indem wir Jahr, Monat und Tag angeben. Wenn wir ein Datum von einem anderen subtrahieren, gibt Python ein `timedelta`-Objekt zurück. Wir können die Anzahl der Tage in diesem Objekt über das `.days`-Attribut abrufen.

In diesem Beispiel liegen zwischen dem 15. Januar 2023 und dem 20. März 2023 64 Tage.
