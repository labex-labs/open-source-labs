# Seitenverhältnis

In der VM wurden bereits `index.html` und `style.css` bereitgestellt.

Dieser Code erstellt mithilfe von CSS-Benutzerdefinieigenschaften und der `calc()`-Funktion einen responsiven Container mit einem bestimmten Seitenverhältnis. Folgen Sie diesen Schritten, um dies zu erreichen:

1. Definieren Sie das gewünschte Seitenverhältnis mithilfe einer CSS-Benutzerdefinieigenschaft, `--aspect-ratio`.
2. Legen Sie die `position`-Eigenschaft des Container-Elements auf `relative` und seine `height`-Eigenschaft auf `0` fest.
3. Berechnen Sie die Höhe des Container-Elements mithilfe der `calc()`-Funktion und der `--aspect-ratio`-Benutzerdefinieigenschaft und legen Sie sie als `padding-bottom`-Eigenschaft fest.
4. Legen Sie das direkte Kind des Container-Elements auf `position: absolute`, `top: 0`, `left: 0`, `width: 100%` und `height: 100%` fest.
5. Halten Sie das Seitenverhältnis des Kind-Elements bei, indem Sie seine `object-fit`-Eigenschaft auf `cover` setzen.

Verwenden Sie den folgenden HTML- und CSS-Code, um den Container zu erstellen:

```html
<div class="container">
  <img src="https://picsum.photos/id/119/800/450" />
</div>
```

```css
.container {
  --aspect-ratio: 16/9;
  position: relative;
  height: 0;
  padding-bottom: calc(100% / var(--aspect-ratio));
}

.container > * {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  object-fit: cover;
}
```

Klicken Sie bitte in der unteren rechten Ecke auf 'Go Live', um den Webdienst auf Port 8080 auszuführen. Anschließend können Sie die Registerkarte **Web 8080** aktualisieren, um die Webseite anzuschauen.
