# Funktion zum Hinzufügen von Minuten zu einem Datum

Um einer bestimmten Anzahl von Minuten zu einem angegebenen Datum hinzuzufügen, verwenden Sie die folgende Funktion:

```js
const addMinutesToDate = (date, n) => {
  // Erstellt ein neues Datumsobjekt aus dem angegebenen Datum
  const d = new Date(date);
  // Fügt n Minuten zum Datumsobjekt hinzu
  d.setTime(d.getTime() + n * 60000);
  // Gibt eine Zeichenkettendarstellung des neuen Datums im Format yyyy-mm-dd HH:MM:SS zurück
  return d.toISOString().split(".")[0].replace("T", " ");
};
```

Um diese Funktion zu verwenden, übergeben Sie als erstes Argument eine Zeichenkettendarstellung des Datums und als zweites Argument die Anzahl der hinzuzufügenden (oder abzuziehenden, wenn negativ) Minuten. Beispielsweise:

```js
addMinutesToDate("2020-10-19 12:00:00", 10); // '2020-10-19 12:10:00'
addMinutesToDate("2020-10-19", -10); // '2020-10-18 23:50:00'
```

Beachten Sie, dass die Funktion das neue Datum als Zeichenkette im Format `yyyy-mm-dd HH:MM:SS` zurückgibt.
