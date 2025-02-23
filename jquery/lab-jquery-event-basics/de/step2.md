# Erweitern von Ereignissen auf neue Seitelemente

Es ist wichtig zu beachten, dass `.on()` nur Ereignislistener auf Elementen erstellen kann, die zu dem Zeitpunkt existieren, zu dem Sie die Listener einrichten. Beispielsweise:

```js
$(document).ready(function () {
  // Erstellen Sie jetzt ein neues Buttonelement mit der alert-Klasse.
  $("<button class='alert'>Alert!</button>").appendTo(document.body);
  // Legt das Klickverhalten für alle Buttonelemente mit der alert-Klasse fest,
  // die im DOM existieren, wenn die Anweisung ausgeführt wird
  $("button.alert").on("click", function () {
    console.log("A button with the alert class was clicked!");
  });
});
```

Wenn ähnliche Elemente nach dem Einrichten der Ereignislistener erstellt werden, übernehmen sie nicht automatisch die zuvor eingerichteten Ereignisverhaltensweisen.

> Sie können die Registerkarte **Web 8080** aktualisieren, um die Webseite anzuschauen.
