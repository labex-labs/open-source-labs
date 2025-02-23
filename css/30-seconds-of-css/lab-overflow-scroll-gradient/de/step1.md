# Überlauf Scroll Farbverlauf

In der VM wurden bereits `index.html` und `style.css` bereitgestellt.

Um einem überlaufenden Element einen schwindenden Farbverlauf hinzuzufügen und anzuzeigen, dass es noch mehr Inhalte gibt, die scrollet werden müssen, folgen Sie diesen Schritten:

1. Verwenden Sie die `::after`-Pseudo-Eigenschaft, um einen `linear-gradient()` zu erstellen, der von `transparent` nach `white` (von oben nach unten) schwindet.
2. Positionieren und dimensionieren Sie das Pseudo-Element in seinem Eltern-Element mit `position: absolute`, `width` und `height`.
3. Ausschließen Sie das Pseudo-Element von Mausereignissen, indem Sie `pointer-events: none` verwenden, wodurch der Text dahinter weiterhin auswählbar/interaktiv ist.

Hier ist ein Beispiel für HTML- und CSS-Codeschnipsel:

```html
<div class="overflow-scroll-gradient">
  <div class="overflow-scroll-gradient-scroller">
    Lorem ipsum dolor sit amet consectetur adipisicing elit. <br />
    Iure id exercitationem nulla qui repellat laborum vitae, <br />
    molestias tempora velit natus. Quas, assumenda nisi. <br />
    Quisquam enim qui iure, consequatur velit sit? <br />
    Lorem ipsum dolor sit amet consectetur adipisicing elit.<br />
    Iure id exercitationem nulla qui repellat laborum vitae, <br />
    molestias tempora velit natus. Quas, assumenda nisi. <br />
    Quisquam enim qui iure, consequatur velit sit?
  </div>
</div>
```

```css
.overflow-scroll-gradient {
  position: relative;
}

.overflow-scroll-gradient::after {
  content: "";
  position: absolute;
  bottom: 0;
  width: 250px;
  height: 25px;
  background: linear-gradient(transparent, white);
  pointer-events: none;
}

.overflow-scroll-gradient-scroller {
  overflow-y: scroll;
  background: white;
  width: 240px;
  height: 200px;
  padding: 15px;
  line-height: 1.2;
}
```

Klicken Sie bitte in der unteren rechten Ecke auf 'Go Live', um den Webdienst auf Port 8080 auszuführen. Anschließend können Sie die Registerkarte **Web 8080** aktualisieren, um die Webseite anzuschauen.
