# Einrichten mehrerer Ereignisreaktionen

Sehr oft werden Elemente in Ihrer Anwendung an mehrere Ereignisse gebunden. Wenn mehrere Ereignisse die gleiche Behandlungsfunktion teilen sollen, können Sie die Ereignistypen als durch Leerzeichen getrennte Liste an `.on()` übergeben:

```js
// Mehrere Ereignisse, gleiche Behandler
$("div").on(
  "click change", // Binde Handler für mehrere Ereignisse
  function () {
    console.log("An input was clicked or changed!");
  }
);
```

Wenn jedes Ereignis seinen eigenen Behandler hat, können Sie einem Objekt in `.on()` einen oder mehrere Schlüssel-Wert-Paare übergeben, wobei der Schlüssel der Ereignisname und der Wert die Funktion ist, die das Ereignis behandelt.

```js
// Binden mehrerer Ereignisse mit unterschiedlichen Behandlern
$("div").on({
  click: function () {
    console.log("clicked!");
  },
  mouseover: function () {
    console.log("hovered!");
  }
});
```

> Sie können die Registerkarte **Web 8080** aktualisieren, um die Webseite anzuschauen.
