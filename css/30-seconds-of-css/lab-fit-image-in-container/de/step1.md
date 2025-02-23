# Bild in Container anpassen

`index.html` und `style.css` wurden bereits in der VM bereitgestellt.

Um ein Bild in seinem Container anzupassen, während das Seitenverhältnis beibehalten wird, können Sie `object-fit: contain` verwenden. Um den Container mit dem Bild zu füllen, während das Seitenverhältnis beibehalten wird, verwenden Sie `object-fit: cover`. Wenn Sie das Bild in der Mitte des Containers positionieren möchten, können Sie `object-position: center` verwenden.

Hier ist ein Beispiel, wie Sie diese Eigenschaften verwenden können:

```html
<img class="image image-contain" src="https://picsum.photos/600/200" />
<img class="image image-cover" src="https://picsum.photos/600/200" />
```

Und die entsprechende CSS:

```css
.image {
  background: #34495e;
  border: 1px solid #34495e;
  width: 200px;
  height: 200px;
}

.image-contain {
  object-fit: contain;
  object-position: center;
}

.image-cover {
  object-fit: cover;
  object-position: right top;
}
```

Bitte klicken Sie auf 'Go Live' in der unteren rechten Ecke, um den Webdienst auf Port 8080 auszuführen. Anschließend können Sie die Registerkarte **Web 8080** aktualisieren, um die Webseite anzuschauen.
