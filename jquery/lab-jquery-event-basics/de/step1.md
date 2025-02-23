# Einrichten von Ereignisreaktionen auf DOM-Elemente

> `index.html` wurde bereits in der VM bereitgestellt.

Mit jQuery ist es einfach, ereignisgetriebene Reaktionen auf Seitelementen einzurichten. Diese Ereignisse werden oft durch die Interaktion des Endbenutzers mit der Seite ausgelöst, z. B. wenn Text in ein Formularfeld eingegeben wird oder der Mauszeiger bewegt wird. In einigen Fällen, wie den Ereignissen beim Laden und Entladen der Seite, wird das Ereignis von der Browser selbst ausgelöst.

jQuery bietet bequeme Methoden für die meisten nativen Browserereignisse. Diese Methoden - einschließlich `.click()`, `.focus()`, `.blur()`, `.change()` usw. - sind Kurzschreibweisen für jQuery's `.on()`-Methode. Die `on`-Methode ist nützlich, um die gleiche Ereignisbehandlungsfunktion an mehrere Ereignisse zu binden, wenn Sie Daten an den Ereignisbehandler übergeben möchten, wenn Sie mit benutzerdefinierten Ereignissen arbeiten oder wenn Sie ein Objekt mit mehreren Ereignissen und Behandlern übergeben möchten.

```js
// Ereignisaufstellung mit einer bequemen Methode
$("p").click(function () {
  console.log("You clicked a paragraph!");
});
```

```js
// Äquivalente Ereignisaufstellung mit der `.on()`-Methode
$("p").on("click", function () {
  console.log("click");
});
```

> Klicken Sie bitte auf 'Go Live' in der unteren rechten Ecke, um den Webdienst auf Port 8080 auszuführen. Anschließend können Sie die Registerkarte **Web 8080** aktualisieren, um die Webseite anzuschauen.
