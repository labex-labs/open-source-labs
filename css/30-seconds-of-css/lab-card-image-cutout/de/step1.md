# Karte mit ausgeschnittenem Bild

`index.html` und `style.css` wurden bereits in der VM bereitgestellt.

Um eine Karte mit einem ausgeschnittenen Bild zu erstellen, folgen Sie diesen Schritten:

1. Fügen Sie einem `.container`-Element einen farbigen Hintergrund über die `background`-Eigenschaft hinzu.
2. Erstellen Sie ein `.card`-Element und fügen Sie innerhalb davon ein `figure`-Element mit dem gewünschten Bild und anderen Inhalten hinzu.
3. Verwenden Sie das `::before`-Pseudo-Element, um einen `border` um das `figure`-Element hinzuzufügen. Setzen Sie die Bordfarbe so, dass sie der `background`-Farbe des `.container`-Elements entspricht, um den Eindruck eines Auschnitts in der `.card` zu erzeugen.

Hier ist ein Beispiel für den HTML-Code der Karte:

```html
<div class="container">
  <div class="card">
    <figure>
      <img alt="" src="https://picsum.photos/id/447/400/400" />
    </figure>
    <p class="content">
      Lorem ipsum dolor sit amet consectetur adipisicing elit.
    </p>
  </div>
</div>
```

Und hier ist der entsprechende CSS-Code:

```css
.container {
  display: flex;
  justify-content: center;
  align-items: center;
  padding: 96px 24px 48px;
  background: #f3f1fe;
}

.card {
  width: 350px;
  margin: 8px;
  display: flex;
  flex-direction: column;
  align-items: center;
  background: #fff;
  border-radius: 10px;
  box-shadow: 0 0 5px -2px rgba(0, 0, 0, 0.1);
}

.card figure {
  width: 120px;
  height: 120px;
  margin-top: -60px;
  border-radius: 50%;
  position: relative;
}

.card figure::before {
  content: "";
  position: absolute;
  top: 50%;
  left: 50%;
  width: 100%;
  height: 100%;
  transform: translate(-50%, -50%);
  border-radius: inherit;
  border: 1rem solid #f3f1fe;
  box-shadow: 0 1px rgba(0, 0, 0, 0.1);
}

.card figure img {
  width: 100%;
  height: 100%;
  border-radius: inherit;
  object-fit: cover;
}

.card.content {
  margin: 2rem;
  text-align: center;
  line-height: 1.5;
  color: #101010;
}
```

Klicken Sie bitte in der unteren rechten Ecke auf 'Go Live', um den Webdienst auf Port 8080 auszuführen. Anschließend können Sie die Registerkarte **Web 8080** aktualisieren, um die Webseite anzuschauen.
