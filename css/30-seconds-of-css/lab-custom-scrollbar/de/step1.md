# Benutzerdefinierter Scrollbalken

`index.html` und `style.css` wurden bereits in der VM bereitgestellt.

Um den Scrollbarkeystil für Elemente mit scrollbarem Überlauf anzupassen, können Sie `::-webkit-scrollbar` verwenden, um das Scrollbarelement zu gestalten, `::-webkit-scrollbar-track` um die Scrollbarkennlinie (den Hintergrund des Scrollbalkens) zu gestalten und `::-webkit-scrollbar-thumb` um den Scrollbalkenknopf (das ziehbare Element) zu gestalten. Beachten Sie jedoch, dass diese Technik nur in WebKit-basierten Browsern funktioniert und die Scrollbarkeystilgebung nicht auf einem Standardsweg steht. Hier ist ein Beispiel dafür, wie diese Selektoren in HTML und CSS verwendet werden:

```html
<div class="custom-scrollbar">
  <p>
    Lorem ipsum dolor sit amet consectetur adipisicing elit.<br />
    Iure id exercitationem nulla qui repellat laborum vitae, <br />
    molestias tempora velit natus. Quas, assumenda nisi. <br />
    Quisquam enim qui iure, consequatur velit sit?
  </p>
</div>
```

```css
.custom-scrollbar {
  height: 70px;
  overflow-y: scroll;
}

.custom-scrollbar::-webkit-scrollbar {
  width: 8px;
}

.custom-scrollbar::-webkit-scrollbar-track {
  background: #1e3f20;
  border-radius: 12px;
}

.custom-scrollbar::-webkit-scrollbar-thumb {
  background: #4a7856;
  border-radius: 12px;
}
```

Klicken Sie bitte in der unteren rechten Ecke auf 'Go Live', um den Webdienst auf Port 8080 auszuführen. Anschließend können Sie die Registerkarte **Web 8080** aktualisieren, um die Webseite anzuschauen.
