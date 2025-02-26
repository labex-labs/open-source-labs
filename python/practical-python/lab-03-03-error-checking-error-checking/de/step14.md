# Übung 3.8: Ausnahmen auslösen

Die `parse_csv()`-Funktion, die Sie im letzten Abschnitt geschrieben haben, ermöglicht die Auswahl von benutzerdefinierten Spalten, aber das funktioniert nur, wenn die Eingabedatei Spaltenüberschriften hat.

Ändern Sie den Code so, dass eine Ausnahme ausgelöst wird, wenn sowohl die Argumente `select` und `has_headers=False` übergeben werden. Beispielsweise:

```python
>>> parse_csv('/home/labex/project/prices.csv', select=['name','price'], has_headers=False)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "fileparse.py", line 9, in parse_csv
    raise RuntimeError("select argument requires column headers")
RuntimeError: select argument requires column headers
>>>
```

Nachdem Sie diese eine Prüfung hinzugefügt haben, könnten Sie fragen, ob Sie in der Funktion andere Arten von Konsistenzprüfungen durchführen sollten. Beispielsweise sollten Sie überprüfen, ob der Dateiname ein String ist, ob `types` eine Liste ist oder etwas dergleichen?

Im Allgemeinen ist es normalerweise am besten, solche Tests zu überspringen und einfach zuzulassen, dass das Programm bei falschen Eingaben fehlschlägt. Die Fehlermeldung in der Stapelüberwachung wird auf die Quelle des Problems verweisen und kann beim Debuggen helfen.

Der Hauptgrund für das Hinzufügen der obigen Prüfung ist es, das Ausführen des Codes in einem unsinnigen Modus zu vermeiden (z.B. das Verwenden eines Features, das Spaltenüberschriften erfordert, aber gleichzeitig angibt, dass es keine Überschriften gibt).

Dies deutet auf einen Programmierfehler in dem aufrufenden Code hin. Das Überprüfen von Fällen, die "nicht passieren sollten", ist oft eine gute Idee.
