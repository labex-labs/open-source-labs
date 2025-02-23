# Anpassung der Textauswahl

`index.html` und `style.css` wurden bereits in der VM bereitgestellt.

Um den Stil des ausgewählten Texts zu ändern, verwenden Sie den Pseudoselektor `::selection`. Hier ist ein Beispielcodeausschnitt, um Text innerhalb eines Paragraph-Elementes auszuwählen und zu stylen:

```html
<p class="custom-text-selection">Wählen Sie einen Teil dieses Texts aus.</p>
```

```css
::selection {
  background: aquamarine;
  color: schwarz;
}

.custom-text-selection::selection {
  background: deeppink;
  color: weiß;
}
```

Bitte klicken Sie auf 'Go Live' in der unteren rechten Ecke, um den Webdienst auf Port 8080 auszuführen. Anschließend können Sie die Registerkarte **Web 8080** aktualisieren, um die Webseite anzuschauen.
