# Alle Stile zurücksetzen

`index.html` und `style.css` wurden bereits in der VM bereitgestellt.

Um alle Stile auf ihre Standardwerte zurückzusetzen, verwenden Sie die `all`-Eigenschaft. Diese Eigenschaft hat keine Auswirkungen auf die `direction`- und `unicode-bidi`-Eigenschaften. Hier ist ein Beispiel dafür, wie Sie sie verwenden können:

```html
<div class="reset-all-styles">
  <h5>Title</h5>
  <p>
    Lorem ipsum dolor sit amet consectetur adipisicing elit. Iure id
    exercitationem nulla qui repellat laborum vitae, molestias tempora velit
    natus. Quas, assumenda nisi. Quisquam enim qui iure, consequatur velit sit?
  </p>
</div>
```

```css
.reset-all-styles {
  all: initial;
}
```

Bitte klicken Sie auf 'Go Live' in der unteren rechten Ecke, um den Webdienst auf Port 8080 auszuführen. Anschließend können Sie die Registerkarte **Web 8080** aktualisieren, um die Webseite anzuschauen.
