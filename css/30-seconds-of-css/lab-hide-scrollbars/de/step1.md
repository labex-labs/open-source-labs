# Scrollbalken ausblenden

`index.html` und `style.css` wurden bereits in der VM bereitgestellt.

Um ein Element scrollbar zu machen, während die Scrollbalken ausgeblendet werden, folgen Sie diesen Schritten:

- Verwenden Sie `overflow: auto`, um das Scrollen auf dem Element zu aktivieren.
- Verwenden Sie `scrollbar-width: none`, um die Scrollbalken in Firefox auszublenden.
- Verwenden Sie `display: none` auf dem Pseudo-Element `::-webkit-scrollbar`, um die Scrollbalken in WebKit-Browsern (wie Chrome, Edge und Safari) auszublenden.

Hier ist eine Beispiel-Implementierung:

```html
<div class="scrollable">
  <p>
    Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean interdum id
    leo a consectetur. Integer justo magna, ultricies vel enim vitae, egestas
    efficitur leo. Ut nulla orci, rutrum eu augue sed, tempus pellentesque quam.
  </p>
</div>
```

```css
.scrollable {
  width: 200px;
  height: 100px;
  overflow: auto;
  scrollbar-width: none;
}

/* Scrollbalken in WebKit-Browsern ausblenden */
.scrollable::-webkit-scrollbar {
  display: none;
}
```

Bitte klicken Sie auf 'Go Live' in der unteren rechten Ecke, um den Webdienst auf Port 8080 auszuführen. Anschließend können Sie die Registerkarte **Web 8080** aktualisieren, um die Webseite anzuschauen.
