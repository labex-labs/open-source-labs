# Etwas nach Abschluss einer Animation

Ein häufiger Fehler bei der Implementierung von jQuery-Effekten besteht darin, anzunehmen, dass die Ausführung der nächsten Methode in Ihrer Kette bis zum Abschluss der Animation gewartet wird.

```js
$("div.hidden").fadeIn(1500).addClass("lookAtMe");
```

Es ist wichtig zu verstehen, dass `.fadeIn()` oben nur die Animation startet. Sobald gestartet, wird die Animation durch schnelle Änderungen von CSS-Eigenschaften in einer JavaScript-`setInterval()`-Schleife implementiert. Wenn Sie `.fadeIn()` aufrufen, startet es die Animationsschleife und gibt dann das jQuery-Objekt zurück, das an `.addClass()` weitergegeben wird, das dann die `lookAtMe`-Stilklasse hinzufügt, während die Animationsschleife gerade erst beginnt.

Um eine Aktion bis nach Abschluss einer Animation zu verschieben, müssen Sie eine Animationsrückruffunktion verwenden. Sie können Ihre Animationsrückruf als zweites Argument an eine beliebige der oben diskutierten Animationsmethoden angeben. Für den obigen Codeausschnitt können wir einen Rückruf wie folgt implementieren:

```js
// Fade in alle versteckten Absätze; fügen Sie dann eine Stilklasse hinzu (korrekt mit Animationsrückruf)
$("div.hidden").fadeIn(1500, function () {
  // this = DOM-Element, das gerade die Animation abgeschlossen hat
  $(this).addClass("lookAtMe");
});
```

Beachten Sie, dass Sie das Schlüsselwort this verwenden können, um sich auf das animierte DOM-Element zu beziehen. Beachten Sie auch, dass der Rückruf für jedes Element im jQuery-Objekt aufgerufen wird. Dies bedeutet, dass wenn Ihr Selektort keine Elemente zurückgibt, Ihr Animationsrückruf niemals ausgeführt wird! Sie können dieses Problem dadurch lösen, indem Sie testen, ob Ihre Auswahl Elemente zurückgegeben hat; wenn nicht, können Sie den Rückruf einfach sofort ausführen.

```js
// Führen Sie einen Rückruf aus, auch wenn es keine Elemente zum Animieren gab
var someElement = $("#nonexistent");

var cb = function () {
  console.log("fertig!");
};

if (someElement.length) {
  someElement.fadeIn(300, cb);
} else {
  cb();
}
```

> Sie können die Registerkarte **Web 8080** aktualisieren, um die Webseite anzuschauen.
