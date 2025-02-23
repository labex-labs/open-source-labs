# Inhalt anzeigen und ausblenden

> In der VM wurde bereits `index.html` bereitgestellt.

Mit jQuery können Sie Inhalte sofort mit `.show()` oder `.hide()` anzeigen oder ausblenden:

```js
// Versteckt alle Absätze sofort
$("p").hide();

// Zeigt alle Divs, die die Klasse hidden haben, sofort an
$("div.hidden").show();
```

Wenn jQuery ein Element ausblendet, setzt es seine CSS-Eigenschaft `display` auf `none`. Dies bedeutet, dass der Inhalt eine Breite und Höhe von Null hat; es bedeutet nicht, dass der Inhalt einfach transparent wird und auf der Seite einen leeren Bereich hinterlässt.

jQuery kann auch Inhalte mittels Animationseffekten anzeigen oder ausblenden. Sie können `.show()` und `.hide()` mitteilen, Animationen auf verschiedene Weise zu verwenden. Eine Möglichkeit ist, einen Argument von `'slow'`, `'normal'` oder `'fast'` zu übergeben:

```js
// Versteckt alle Absätze langsam
$("p").hide("slow");

// Zeigt alle Divs, die die Klasse hidden haben, schnell an
$("div.hidden").show("fast");
```

Wenn Sie eine genauere Kontrolle über die Dauer des Animationseffekts bevorzugen, können Sie die gewünschte Dauer in Millisekunden an `.show()` und `.hide()` übergeben:

```js
// Versteckt alle Absätze innerhalb von einer halben Sekunde
$("p").hide(2000);

// Zeigt alle Divs, die die Klasse hidden haben, innerhalb von 1,25 Sekunden an
$("div.hidden").show(1250);
```

Die meisten Entwickler übergeben eine Anzahl von Millisekunden, um eine genauere Kontrolle über die Dauer zu haben.

> Klicken Sie bitte in der unteren rechten Ecke auf 'Go Live', um den Webdienst auf Port 8080 auszuführen. Anschließend können Sie die Registerkarte **Web 8080** aktualisieren, um die Webseite anzuschauen.
