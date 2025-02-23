# Fluid Typografie

`index.html` und `style.css` wurden bereits in der VM zur Verfügung gestellt.

Um Text zu erstellen, der sich in der Größe nach der Breite der Anzeige anpasst, können Sie CSS verwenden. Ein Möglichkeit dazu besteht darin, die `clamp()`-Funktion zu verwenden, um die minimale und maximale Schriftgröße festzulegen. Eine andere Möglichkeit ist, eine Formel zu verwenden, um einen responsive Wert für die Schriftgröße zu berechnen. Hier ist ein Beispiel für ein HTML-Element mit der Klasse `fluid-type`:

```html
<p class="fluid-type">Hello World!</p>
```

Hier ist der entsprechende CSS-Code, der die Schriftgröße so einstellt, dass sie sich zwischen `1rem` und `3rem` basierend auf der Breite der Anzeige anpasst:

```css
.fluid-type {
  font-size: clamp(1rem, 8vw - 2rem, 3rem);
}
```

Bitte klicken Sie auf 'Go Live' in der unteren rechten Ecke, um den Webdienst auf Port 8080 auszuführen. Anschließend können Sie die Registerkarte **Web 8080** aktualisieren, um die Webseite anzuschauen.
