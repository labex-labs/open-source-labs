# Großschreibung jedes Wortes

Nachdem wir nun einen String in Wörter aufteilen können, müssen wir den ersten Buchstaben jedes Wortes groß schreiben und den Rest klein schreiben. Implementieren wir diese Funktionalität.

1. In Ihrer Node.js-Sitzung schreiben wir eine Funktion, um ein einzelnes Wort zu kapitalisieren. Geben Sie ein:

```javascript
function capitalizeWord(word) {
  return word.charAt(0).toUpperCase() + word.slice(1).toLowerCase();
}

// Test with a few examples
console.log(capitalizeWord("hello"));
console.log(capitalizeWord("WORLD"));
console.log(capitalizeWord("javaScript"));
```

Die Ausgabe sollte sein:

```
Hello
World
Javascript
```

2. Jetzt wenden wir diese Funktion auf ein Array von Wörtern mit der `map()`-Methode an. Geben Sie ein:

```javascript
let words = ["hello", "WORLD", "javaScript"];
let capitalizedWords = words.map((word) => capitalizeWord(word));
console.log(capitalizedWords);
```

Die Ausgabe sollte sein:

```
[ 'Hello', 'World', 'Javascript' ]
```

Die `map()`-Methode erstellt ein neues Array, indem sie eine Funktion auf jedes Element des ursprünglichen Arrays anwendet. In diesem Fall wenden wir unsere `capitalizeWord`-Funktion auf jedes Wort an.

3. Schließlich fügen wir die kapitalisierten Wörter zusammen, um einen String im Pascal Case zu bilden:

```javascript
let pascalCase = capitalizedWords.join("");
console.log(pascalCase);
```

Die Ausgabe sollte sein:

```
HelloWorldJavascript
```

Die `join("")`-Methode kombiniert alle Elemente eines Arrays zu einem einzelnen String, wobei das angegebene Trennzeichen (in diesem Fall ein leerer String) zwischen jedem Element verwendet wird.

Diese Schritte zeigen den Kernprozess der Umwandlung eines Strings in Pascal Case:

1. Teilen Sie den String in Wörter auf.
2. Kapitalisieren Sie jedes Wort.
3. Fügen Sie die Wörter ohne Trennzeichen zusammen.
