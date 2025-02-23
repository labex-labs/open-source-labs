# Wie man in Node.js einen Tilde-Pfad in einen absoluten Pfad umwandelt

Um mit der Code-Praxis in Node.js zu beginnen, öffnen Sie das Terminal oder SSH und geben Sie `node` ein. Um einen Tilde-Pfad in einen absoluten Pfad umzuwandeln, verwenden Sie folgenden Code:

```js
const untildify = (str) =>
  str.replace(/^~($|\/|\\)/, `${require("os").homedir()}$1`);
```

Der Code verwendet `String.prototype.replace()` mit einem regulären Ausdruck und `os.homedir()`, um das `~` am Anfang des Pfads durch das Home-Verzeichnis zu ersetzen. Hier ist ein Beispiel dafür, wie die `untildify`-Funktion verwendet werden kann:

```js
untildify("~/node"); // gibt '/Users/aUser/node' zurück
```
