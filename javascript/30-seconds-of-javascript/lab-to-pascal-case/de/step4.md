# Erstellen der vollständigen toPascalCase-Funktion

Nachdem wir nun alle benötigten Komponenten verstehen, erstellen wir eine vollständige `toPascalCase`-Funktion, die jeden Eingabestring verarbeiten kann.

1. Erstellen wir eine JavaScript-Datei, um unsere Funktion zu speichern. Beenden Sie Ihre Node.js-Sitzung, indem Sie zweimal Ctrl+C drücken oder `.exit` eingeben.

2. Im WebIDE erstellen Sie eine neue Datei, indem Sie in der oberen Menüleiste auf "File" > "New File" klicken.

3. Speichern Sie die Datei als `pascalCase.js` im Verzeichnis `/home/labex/project`.

4. Kopieren und fügen Sie den folgenden Code in den Editor ein:

```javascript
/**
 * Converts a string to Pascal case.
 * @param {string} str - The input string to convert.
 * @returns {string} The Pascal cased string.
 */
function toPascalCase(str) {
  // Use regex to match words regardless of delimiter
  const words = str.match(
    /[A-Z]{2,}(?=[A-Z][a-z]+[0-9]*|\b)|[A-Z]?[a-z]+[0-9]*|[A-Z]|[0-9]+/g
  );

  // If no words are found, return an empty string
  if (!words) {
    return "";
  }

  // Capitalize each word and join them
  return words
    .map((word) => word.charAt(0).toUpperCase() + word.slice(1).toLowerCase())
    .join("");
}

// Test cases
console.log(toPascalCase("hello world")); // "HelloWorld"
console.log(toPascalCase("some_database_field_name")); // "SomeDatabaseFieldName"
console.log(toPascalCase("Some label that needs to be pascalized")); // "SomeLabelThatNeedsToBePascalized"
console.log(toPascalCase("some-javascript-property")); // "SomeJavascriptProperty"
console.log(
  toPascalCase("some-mixed_string with spaces_underscores-and-hyphens")
); // "SomeMixedStringWithSpacesUnderscoresAndHyphens"
```

5. Speichern Sie die Datei, indem Sie Ctrl+S drücken oder im Menü "File" > "Save" auswählen.

6. Führen Sie die Datei mit Node.js aus, indem Sie das Terminal öffnen und eingeben:

```bash
node pascalCase.js
```

Sie sollten die folgende Ausgabe sehen:

```
HelloWorld
SomeDatabaseFieldName
SomeLabelThatNeedsToBePascalized
SomeJavascriptProperty
SomeMixedStringWithSpacesUnderscoresAndHyphens
```

Unsere `toPascalCase`-Funktion funktioniert nun korrekt. Lassen Sie uns überprüfen, wie sie funktioniert:

1. Wir verwenden einen regulären Ausdruck, um Wörter im Eingabestring zu finden, unabhängig von den verwendeten Trennzeichen.
2. Wir prüfen, ob Wörter gefunden wurden. Wenn nicht, geben wir einen leeren String zurück.
3. Wir verwenden `map()`, um jedes Wort zu kapitalisieren, und `join('')`, um sie ohne Trennzeichen zu verbinden.
4. Das Ergebnis ist ein String im Pascal Case, bei dem jedes Wort mit einem Großbuchstaben beginnt und der Rest klein geschrieben ist.
