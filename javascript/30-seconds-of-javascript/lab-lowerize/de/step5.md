# Erstellen eines wiederverwendbaren Moduls

Nachdem wir nun funktionierende Funktionen haben, erstellen wir eine wiederverwendbare JavaScript-Moduldatei, die wir in andere Projekte importieren können.

Zunächst beenden wir die Node.js interaktive Shell, indem wir zweimal Ctrl+C drücken oder `.exit` eingeben und Enter drücken.

Jetzt erstellen wir eine neue Datei namens `object-utils.js` im Projektverzeichnis:

1. Navigieren Sie im WebIDE zum Dateiexplorer auf der linken Seite.
2. Klicken Sie mit der rechten Maustaste im Projektverzeichnis und wählen Sie "Neue Datei".
3. Benennen Sie die Datei `object-utils.js`.
4. Fügen Sie den folgenden Code in die Datei ein:

```javascript
/**
 * Converts all keys of an object to lowercase
 * @param {Object} obj - The input object
 * @returns {Object} A new object with all keys in lowercase
 */
const lowerizeKeys = (obj) => {
  return Object.keys(obj).reduce((acc, key) => {
    acc[key.toLowerCase()] = obj[key];
    return acc;
  }, {});
};

/**
 * Recursively converts all keys of an object and its nested objects to lowercase
 * @param {Object} obj - The input object
 * @returns {Object} A new object with all keys in lowercase (including nested objects)
 */
const deepLowerizeKeys = (obj) => {
  return Object.keys(obj).reduce((acc, key) => {
    const value = obj[key];
    // Check if the value is an object and not null
    const newValue =
      value && typeof value === "object" && !Array.isArray(value)
        ? deepLowerizeKeys(value)
        : value;

    acc[key.toLowerCase()] = newValue;
    return acc;
  }, {});
};

// Export the functions
module.exports = {
  lowerizeKeys,
  deepLowerizeKeys
};
```

Jetzt erstellen wir eine Testdatei, um zu überprüfen, ob unser Modul korrekt funktioniert. Erstellen Sie eine neue Datei namens `test.js`:

1. Navigieren Sie im WebIDE zum Dateiexplorer auf der linken Seite.
2. Klicken Sie mit der rechten Maustaste im Projektverzeichnis und wählen Sie "Neue Datei".
3. Benennen Sie die Datei `test.js`.
4. Fügen Sie den folgenden Code in die Datei ein:

```javascript
// Import the functions from our module
const { lowerizeKeys, deepLowerizeKeys } = require("./object-utils");

// Test with a simple object
const user = {
  Name: "John",
  AGE: 30,
  Email: "john@example.com"
};

console.log("Original object:");
console.log(user);

console.log("\nObject with lowercase keys:");
console.log(lowerizeKeys(user));

// Test with a nested object
const nestedObject = {
  User: {
    Name: "John",
    Contact: {
      EMAIL: "john@example.com",
      PHONE: "123-456-7890"
    }
  }
};

console.log("\nNested object:");
console.log(nestedObject);

console.log("\nNested object with lowercase keys (shallow):");
console.log(lowerizeKeys(nestedObject));

console.log("\nNested object with lowercase keys (deep):");
console.log(deepLowerizeKeys(nestedObject));
```

Jetzt führen wir die Testdatei aus:

```bash
node test.js
```

Sie sollten eine Ausgabe ähnlich der folgenden sehen:

```
Original object:
{ Name: 'John', AGE: 30, Email: 'john@example.com' }

Object with lowercase keys:
{ name: 'John', age: 30, email: 'john@example.com' }

Nested object:
{
  User: {
    Name: 'John',
    Contact: { EMAIL: 'john@example.com', PHONE: '123-456-7890' }
  }
}

Nested object with lowercase keys (shallow):
{
  user: {
    Name: 'John',
    Contact: { EMAIL: 'john@example.com', PHONE: '123-456-7890' }
  }
}

Nested object with lowercase keys (deep):
{
  user: {
    name: 'John',
    contact: { email: 'john@example.com', phone: '123-456-7890' }
  }
}
```

Herzlichen Glückwunsch! Sie haben erfolgreich ein wiederverwendbares JavaScript-Modul mit Funktionen zum Umwandeln von Objektschlüsseln in Kleinbuchstaben erstellt. Dieses Modul kann nun in alle Ihre JavaScript-Projekte importiert werden.
