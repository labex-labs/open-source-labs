# Wie man ein Date-Objekt aus einem Unix-Zeitstempel erstellt

Um ein `Date`-Objekt aus einem Unix-Zeitstempel zu erstellen, folgen Sie diesen Schritten:

1. Öffnen Sie das Terminal/SSH und geben Sie `node` ein, um mit der Code-Praxis zu beginnen.
2. Multiplizieren Sie den Zeitstempel mit `1000`, um ihn in Millisekunden umzuwandeln.
3. Verwenden Sie den `Date`-Konstruktor, um ein neues `Date`-Objekt zu erstellen.

Hier ist ein Beispiel-Codeausschnitt:

```js
const fromTimestamp = (timestamp) => new Date(timestamp * 1000);
```

Sie können diese Funktion verwenden, um einen Unix-Zeitstempel in ein `Date`-Objekt umzuwandeln, wie folgt:

```js
fromTimestamp(1602162242); // 2020-10-08T13:04:02.000Z
```
