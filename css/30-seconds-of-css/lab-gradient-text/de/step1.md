# Gradient-Text

`index.html` und `style.css` wurden bereits in der VM zur Verfügung gestellt.

Um Text eine Gradient-Farbe zu geben, können Sie CSS-Eigenschaften verwenden. Zunächst verwenden Sie die `background`-Eigenschaft mit einem `linear-gradient()`-Wert, um dem Textelement einen Gradient-Hintergrund zu geben. Anschließend verwenden Sie `webkit-text-fill-color: transparent`, um den Text mit einer transparenten Farbe zu füllen. Schließlich verwenden Sie `webkit-background-clip: text`, um den Hintergrund mit dem Text zu schneiden und den Text mit dem Gradient-Hintergrund als Farbe zu füllen. Hier ist ein Beispielcodeausschnitt:

```html
<p class="gradient-text">Gradient text</p>
```

```css
.gradient-text {
  background: linear-gradient(#70d6ff, #00072d);
  -webkit-text-fill-color: transparent;
  -webkit-background-clip: text;
  font-size: 32px;
}
```

Bitte klicken Sie auf 'Go Live' in der unteren rechten Ecke, um den Webdienst auf Port 8080 auszuführen. Anschließend können Sie die Registerkarte **Web 8080** aktualisieren, um die Webseite vorab zu sehen.
