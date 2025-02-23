# Donut Spinner

`index.html` und `style.css` wurden bereits in der VM bereitgestellt.

Um den Inhaltseintrag anzuzeigen, erstellen Sie einen Donut-Spinner mit einer halbtransparenten `Kante` für das gesamte Element. Ausschließen Sie eine Seite, um als Ladeindikator für den Donut zu dienen. Definieren und verwenden Sie dann eine passende Animation, indem Sie `transform: rotate()` verwenden, um das Element zu drehen. Hier ist ein Beispielcode in HTML und CSS:

HTML:

```html
<div class="donut"></div>
```

CSS:

```css
@keyframes donut-spin {
  0% {
    transform: rotate(0deg);
  }
  100% {
    transform: rotate(360deg);
  }
}

.donut {
  display: inline-block;
  border: 4px solid rgba(0, 0, 0, 0.1);
  border-left-color: #7983ff;
  border-radius: 50%;
  width: 30px;
  height: 30px;
  animation: donut-spin 1.2s linear infinite;
}
```

Klicken Sie bitte in der unteren rechten Ecke auf 'Go Live', um den Webdienst auf Port 8080 auszuführen. Anschließend können Sie die Registerkarte **Web 8080** aktualisieren, um die Webseite anzuschauen.
