# Funktion, um Sekunden als ISO-Zeit zu formatieren

Um diesen Code zu verwenden, öffnen Sie das Terminal/SSH und geben Sie `node` ein. Diese Funktion nimmt die Anzahl der Sekunden als Argument entgegen und gibt das ISO-Zeitenformat zurück. So funktioniert es:

- Teilen Sie die Anzahl der Sekunden durch die entsprechenden Werte, um die entsprechenden Werte für `Stunde`, `Minute` und `Sekunde` zu erhalten.
- Speichern Sie das Vorzeichen der Zahl in einer Variable, um es am Anfang des Ergebnisses anzuhaften.
- Verwenden Sie `Array.prototype.map()` in Kombination mit `Math.floor()` und `String.prototype.padStart()`, um jedes Segment in eine Zeichenkette zu wandeln und zu formatieren.
- Verwenden Sie `Array.prototype.join()`, um die Werte zu einer Zeichenkette zu kombinieren.

Hier ist der Code:

```js
const formatSeconds = (s) => {
  const [hour, minute, second, sign] =
    s > 0
      ? [s / 3600, (s / 60) % 60, s % 60, ""]
      : [-s / 3600, (-s / 60) % 60, -s % 60, "-"];

  return (
    sign +
    [hour, minute, second]
      .map((v) => `${Math.floor(v)}`.padStart(2, "0"))
      .join(":")
  );
};
```

Sie können die Funktion mit diesen Beispielen testen:

```js
formatSeconds(200); // '00:03:20'
formatSeconds(-200); // '-00:03:20'
formatSeconds(99999); // '27:46:39'
```
