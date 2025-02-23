# Perspektivtransformation bei Hover

`index.html` und `style.css` wurden bereits in der VM bereitgestellt.

Um eine Perspektivtransformation mit einer Hover-Animation auf einem Element zu erstellen:

1. Verwenden Sie die `transform`-Eigenschaft mit den `perspective()`- und `rotateY()`-Funktionen, um eine Perspektive auf das Element anzuwenden. Beispielsweise um eine linke Perspektive zu erstellen, verwenden Sie `transform: perspective(1500px) rotateY(15deg);`. Um eine rechte Perspektive zu erstellen, verwenden Sie `transform: perspective(1500px) rotateY(-15deg);`.

2. Verwenden Sie die `transition`-Eigenschaft, um die `transform`-Eigenschaft zu animieren, wenn das Element angehoben wird. Beispielsweise `transition: transform 1s ease 0s;`.

3. Um den Perspektiveffekt von links nach rechts zu spiegeln, ändern Sie den `rotateY()`-Wert auf der rechten Perspektive in negativ. Beispielsweise verwenden Sie `transform: perspective(1500px) rotateY(-15deg);`.

Beispiel-HTML:

```html
<div class="card-container">
  <div class="image-card perspective-left"></div>
  <div class="image-card perspective-right"></div>
</div>
```

Beispiel-CSS:

```css
.image-card {
  display: inline-block;
  box-sizing: border-box;
  margin: 1rem;
  width: 240px;
  height: 320px;
  padding: 8px;
  border-radius: 1rem;
  background: url("https://picsum.photos/id/1049/240/320");
  box-shadow: rgba(0, 0, 0, 0.25) 0px 25px 50px -12px;
}

.perspective-left {
  transform: perspective(1500px) rotateY(15deg);
  transition: transform 1s ease 0s;
}

.perspective-left:hover {
  transform: perspective(3000px) rotateY(5deg);
}

.perspective-right {
  transform: perspective(1500px) rotateY(-15deg);
  transition: transform 1s ease 0s;
}

.perspective-right:hover {
  transform: perspective(3000px) rotateY(-5deg);
}
```

Bitte klicken Sie in der unteren rechten Ecke auf 'Go Live', um den Webdienst auf Port 8080 auszuführen. Anschließend können Sie die Registerkarte **Web 8080** aktualisieren, um die Webseite anzuschauen.
