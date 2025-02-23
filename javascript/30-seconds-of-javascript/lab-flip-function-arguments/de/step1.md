# Funktionsargumente mit `flip` neu anordnen

Um die Reihenfolge von Funktionsargumenten zu tauschen, verwenden Sie die `flip`-Funktion. Diese Funktion nimmt eine Funktion als Argument und gibt eine neue Funktion zurück, die das erste und das letzte Argument tauscht.

Um `flip` zu implementieren:

- Verwenden Sie die Argument-Destrukturierung und eine Closure mit variadischen Argumenten.
- Schneiden Sie das erste Argument mit dem Spread-Operator (`...`) aus, um es zum letzten Argument zu machen, bevor Sie die restlichen Argumente anwenden.

```js
const flip =
  (fn) =>
  (first, ...rest) =>
    fn(...rest, first);
```

Hier ist ein Beispiel dafür, wie Sie `flip` verwenden, um die Argumente von `Object.assign` neu zu ordnen:

```js
let a = { name: "John Smith" };
let b = {};

// Erstellen Sie eine neue Funktion, die die Argumente von Object.assign tauscht
const mergeFrom = flip(Object.assign);

// Erstellen Sie eine neue Funktion, die das erste Argument an a bindet
let mergePerson = mergeFrom.bind(null, a);

// Rufen Sie die neue Funktion mit b als zweites Argument auf
mergePerson(b); // b ist jetzt gleich a

// Alternativ: Fügen Sie a und b zusammen, ohne die neue Funktion zu verwenden
b = {};
Object.assign(b, a); // b ist jetzt gleich a
```
