# Ereignisse

> In der VM wurde bereits `index.html` bereitgestellt.

Echte Interaktivität auf einer Website erfordert Ereignishandler. Dies sind Codestrukturen, die auf Aktivitäten im Browser lauschen und in Antwort Code ausführen. Das offensichtlichste Beispiel ist das Behandeln des [Click-Ereignisses](https://developer.mozilla.org/en-US/docs/Web/API/Element/click_event), das vom Browser ausgelöst wird, wenn Sie mit der Maus auf etwas klicken. Um dies zu demonstrieren, geben Sie Folgendes in Ihre Konsole ein und klicken dann auf die aktuelle Webseite:

```js
document.querySelector("html").addEventListener("click", function () {
  alert("Ouch! Stop poking me!");
});
```

Es gibt mehrere Möglichkeiten, einen Ereignishandler an ein Element anzuhängen.
Hier wählen wir das [`<html>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/html)-Element. Anschließend rufen wir seine [`addEventListener()`](https://developer.mozilla.org/en-US/docs/Web/API/EventTarget/addEventListener)-Funktion auf und übergeben den Namen des Ereignisses, auf das gewartet werden soll (`'click'`), und eine Funktion, die ausgeführt werden soll, wenn das Ereignis eintritt.

Die Funktion, die wir gerade an `addEventListener()` übergeben haben, wird als _anonyme Funktion_ bezeichnet, weil sie keinen Namen hat. Es gibt eine alternative Schreibweise für anonyme Funktionen, die wir als _Arrow-Funktion_ bezeichnen.
Eine Arrow-Funktion verwendet `() =>` anstelle von `function ()`:

```js
document.querySelector("html").addEventListener("click", () => {
  alert("Ouch! Stop poking me!");
});
```

> Klicken Sie bitte in der unteren rechten Ecke auf 'Go Live', um den Webdienst auf Port 8080 auszuführen. Anschließend können Sie die Registerkarte **Web 8080** aktualisieren, um die Webseite anzuschauen.
