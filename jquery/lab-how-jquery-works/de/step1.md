# Wie jQuery funktioniert

> Die Datei `index.html` wurde bereits in der VM bereitgestellt.

Diese Datei wird automatisch während der Umgebungsinitialisierung erstellt. Wenn sie nicht automatisch erstellt wird, erstellen Sie die Datei und implementieren Sie die Funktion wie in der obigen Abbildung gezeigt. Der Funktionscode lautet wie folgt:

```html
<!doctype html>
<html>
  <head>
    <meta charset="utf-8" />
    <title>Demo</title>
  </head>
  <body>
    <p>jQuery</p>
    <script src="jquery.min.js"></script>
    <script>
      // Ihr Code hier.
    </script>
  </body>
</html>
```

Das `src`-Attribut im `<script>`-Element muss auf eine Kopie von jQuery verweisen. Laden Sie eine Kopie von jQuery von der Seite [Downloading jQuery](https://jquery.com/download/) herunter und speichern Sie die Datei `jquery.min.js` im gleichen Verzeichnis wie Ihre HTML-Datei.

> Hinweis: Wenn Sie jQuery herunterladen, kann der Dateiname eine Versionsnummer enthalten, z.B. `jquery-x.y.z.js`. Stellen Sie sicher, dass Sie diese Datei entweder in `jquery.js` umbenennen oder das `src`-Attribut des `<script>`-Elements aktualisieren, um mit dem Dateinamen übereinzustimmen.

#### Ausführen von Code beim Laden des Dokuments

Um sicherzustellen, dass ihr Code nach dem Laden des Dokuments durch den Browser ausgeführt wird, umschließen viele JavaScript-Programmierer ihren Code in einer `onload`-Funktion:

```js
window.onload = function () {
  alert("welcome");
};
```

Leider wird der Code erst ausgeführt, nachdem alle Bilder, einschließlich Banner-Werbung, fertig heruntergeladen sind. Um Code so bald wie möglich auszuführen, wenn das Dokument manipuliert werden kann, hat jQuery eine Anweisung namens [ready event](http://api.jquery.com/ready/):

```js
$(document).ready(function () {
  // Ihr Code hier.
});
```

> Hinweis: Die jQuery-Bibliothek stellt ihre Methoden und Eigenschaften über zwei Eigenschaften des `window`-Objekts namens `jQuery` und `$` zur Verfügung. `$` ist einfach ein Alias für `jQuery` und wird oft verwendet, da es kürzer und schneller zu schreiben ist.

Beispielsweise können Sie innerhalb des ready-Events einen Click-Handler für den Link hinzufügen:

```js
$(document).ready(function () {
  $("button").click(function () {
    $("p").text("Hello jQuery!");
  });
});
```

Kopieren Sie den obigen jQuery-Code in Ihre HTML-Datei, wo es heißt `// Ihr Code hier`. Speichern Sie dann Ihre HTML-Datei und laden Sie die Testseite in Ihrem Browser neu.

#### Vollständiges Beispiel

Das folgende Beispiel veranschaulicht den oben diskutierten Click-Handling-Code, der direkt im HTML-`<body>` eingebettet ist. Beachten Sie, dass es in der Praxis normalerweise besser ist, Ihren Code in einer separaten JS-Datei zu platzieren und ihn mit dem `src`-Attribut eines `<script>`-Elements auf der Seite zu laden.

```html
<!doctype html>
<html>
  <head>
    <meta charset="utf-8" />
    <title>Demo</title>
  </head>
  <body>
    <button>click me</button>
    <p>Hello World</p>
    <script src="jquery.min.js"></script>
    <script>
      $(document).ready(function () {
        $("button").click(function () {
          $("p").text("Hello jQuery!");
        });
      });
    </script>
  </body>
</html>
```

> Klicken Sie bitte in der unteren rechten Ecke auf 'Go Live', um den Webdienst auf Port 8080 auszuführen. Anschließend können Sie die Registerkarte **Web 8080** aktualisieren, um die Webseite anzuschauen.
