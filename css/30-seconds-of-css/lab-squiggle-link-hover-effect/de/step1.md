# Squiggle Link Hover Effekt

`index.html` und `style.css` wurden bereits in der VM bereitgestellt.

Um einen Squiggle Effekt zu erzeugen, wenn man über einen Link fährt, können Sie die folgenden Schritte ausführen:

1. Erstellen Sie einen wiederholenden Hintergrund für den Link, indem Sie einen `linear-gradient` verwenden.

```css
a.squiggle {
  background: linear-gradient(to bottom, #0087ca 0%, #0087ca 100%);
  background-position: 0 100%;
  background-repeat: repeat-x;
  background-size: 2px 2px;
  color: inherit;
  text-decoration: none;
}
```

2. Erstellen Sie einen `:hover`-Zustand für den Link mit einem `background-image` einer Data-URL, die einen SVG mit einem gewellten Pfad und einer Animation enthält.

```css
a.squiggle:hover {
  background-image: url("data:image/svg+xml;charset=utf8,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 20 4'%3E%3Cstyle type='text/css'%3E.squiggle{animation:shift.3s linear infinite;}@keyframes shift {from {transform:translateX(0);}to {transform:translateX(-15px);}}%3C/style%3E%3Cpath fill='none' stroke='%230087ca' stroke-width='2' class='squiggle' d='M0,3.5 c 5,0,5,-3,10,-3 s 5,3,10,3 c 5,0,5,-3,10,-3 s 5,3,10,3'/%3E%3C/svg%3E");
  background-size: auto 4px;
}
```

3. Verwenden Sie den folgenden HTML-Code, um den Link zur Seite hinzuzufügen.

```html
<p>
  The <a class="squiggle" href="#">magnificent octopus</a> swam along
  gracefully.
</p>
```

Bitte klicken Sie auf 'Go Live' in der unteren rechten Ecke, um den Webdienst auf Port 8080 auszuführen. Anschließend können Sie die Registerkarte **Web 8080** aktualisieren, um die Webseite anzuschauen.
