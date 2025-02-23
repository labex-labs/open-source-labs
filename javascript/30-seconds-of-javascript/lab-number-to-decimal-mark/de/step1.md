# Wie man eine Zahl in Dezimaltrennzeichenformat umwandelt

Um eine Zahl in Dezimaltrennzeichenformat umzuwandeln, folgen Sie diesen Schritten:

1. Öffnen Sie das Terminal/SSH und geben Sie `node` ein, um mit der Codeausführung zu beginnen.
2. Verwenden Sie `Number.prototype.toLocaleString()`, um die Zahl in Dezimaltrennzeichenformat umzuwandeln.
3. Für diesen Vorgang kann der folgende Code verwendet werden:

```js
const toDecimalMark = (num) => num.toLocaleString("en-US");
```

Hier ist ein Beispiel dafür, wie diese Funktion verwendet wird:

```js
toDecimalMark(12305030388.9087); // '12,305,030,388.909'
```

Dies wird die Zahl `12305030388.9087` in den mit Dezimaltrennzeichen formatierten String `'12,305,030,388.909'` umwandeln.
