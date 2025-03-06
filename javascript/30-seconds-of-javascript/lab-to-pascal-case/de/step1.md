# Verständnis von Pascal Case und Einrichtung der Umgebung

Pascal Case ist eine Namenskonvention, bei der:

- Der erste Buchstabe jedes Wortes groß geschrieben wird
- Zwischen den Wörtern keine Leerzeichen, Bindestriche oder Unterstriche verwendet werden
- Alle anderen Buchstaben klein geschrieben werden

Beispielsweise:

- "hello world" → "HelloWorld"
- "user_name" → "UserName"
- "first-name" → "FirstName"

Beginnen wir mit der Einrichtung unserer Entwicklungsumgebung.

1. Öffnen Sie das Terminal über die WebIDE-Schnittstelle, indem Sie auf "Terminal" in der oberen Menüleiste klicken.

2. Starten Sie eine Node.js-Interaktionssitzung, indem Sie den folgenden Befehl im Terminal eingeben und die Eingabetaste drücken:

```bash
node
```

Sie sollten das Node.js-Prompt (`>`) sehen, was darauf hinweist, dass Sie nun in der Node.js-Interaktionsumgebung sind.

3. Probieren wir eine einfache String-Manipulation, um uns einzuschwimmen. Geben Sie den folgenden Code am Node.js-Prompt ein:

```javascript
let name = "john doe";
let capitalizedFirstLetter = name.charAt(0).toUpperCase() + name.slice(1);
console.log(capitalizedFirstLetter);
```

Die Ausgabe sollte sein:

```
John doe
```

Dieses einfache Beispiel zeigt, wie man den ersten Buchstaben eines Strings groß schreibt. Wir haben verwendet:

- `charAt(0)`, um das erste Zeichen zu erhalten
- `toUpperCase()`, um es in einen Großbuchstaben umzuwandeln
- `slice(1)`, um den Rest des Strings zu erhalten
- Verkettung mit `+`, um sie zusammenzufügen

Diese String-Methoden werden hilfreich sein, wenn wir unseren Pascal-Case-Konverter erstellen.
