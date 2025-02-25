# Hashtabelle

## Problemstellung

Implementieren Sie eine Hashtabelle mit den Methoden set, get und remove. Die Hashtabelle sollte Kettenschlüsse zur Konfliktauflösung verwenden. Die Schlüssel sind ausschließlich Ganzzahlen. Wir müssen uns nicht um Ladefaktoren kümmern oder Eingaben validieren. Wir können davon ausgehen, dass die Hashtabelle in den Arbeitsspeicher passt.

## Anforderungen

- Die Schlüssel sind ausschließlich Ganzzahlen.
- Für die Konfliktauflösung werden Kettenschlüsse verwendet.
- Ladefaktoren müssen nicht berücksichtigt werden.
- Eingaben müssen nicht validiert werden.
- Die Hashtabelle passt in den Arbeitsspeicher.

## Beispielverwendung

- `get`-Methode:
  - Wenn kein passender Schlüssel vorhanden ist, wird eine KeyError-Ausnahme ausgelöst.
  - Wenn ein passender Schlüssel vorhanden ist, wird der entsprechende Wert zurückgegeben.
- `set`-Methode:
  - Wenn kein passender Schlüssel vorhanden ist, wird ein neues Schlüssel-Wert-Paar zur Hashtabelle hinzugefügt.
  - Wenn ein passender Schlüssel vorhanden ist, wird der entsprechende Wert aktualisiert.
- `remove`-Methode:
  - Wenn kein passender Schlüssel vorhanden ist, wird eine KeyError-Ausnahme ausgelöst.
  - Wenn ein passender Schlüssel vorhanden ist, wird das entsprechende Schlüssel-Wert-Paar aus der Hashtabelle entfernt.
