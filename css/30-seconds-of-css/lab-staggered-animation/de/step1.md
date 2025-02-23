# Gestaffelte Animation

`index.html` und `style.css` wurden bereits in der VM bereitgestellt.

Dieser Code erstellt eine gestaffelte Animation für die Elemente einer Liste. Dazu tun Sie Folgendes:

1. Machen Sie die Listelemente transparent und bewegen Sie sie bis ganz nach rechts, indem Sie `opacity: 0` und `transform: translateX(100%)` einstellen.
2. Geben Sie für die Listelemente die gleichen `transition`-Eigenschaften an, außer `transition-delay`.
3. Verwenden Sie Inline-Styles, um einen Wert für `--i` für jedes Listelement anzugeben. Dies wird für `transition-delay` verwendet, um den Stagger-Effekt zu erzeugen.
4. Verwenden Sie den `:checked`-Pseudo-Klassen-Selektor für die Checkbox, um die Listelemente zu gestalten. Um sie erscheinen zu lassen und in den sichtbaren Bereich zu gleiten, setzen Sie `opacity` auf `1` und `transform` auf `translateX(0)`.

Hier ist der HTML- und CSS-Code, um diesen Effekt zu erzielen:

```html
<div class="container">
  <input type="checkbox" name="menu" id="menu" class="menu-toggler" />
  <label for="menu" class="menu-toggler-label">Menu</label>
  <ul class="stagger-menu">
    <li style="--i: 0">Home</li>
    <li style="--i: 1">Pricing</li>
    <li style="--i: 2">Account</li>
    <li style="--i: 3">Support</li>
    <li style="--i: 4">About</li>
  </ul>
</div>
```

```css
.container {
  overflow-x: hidden;
  width: 100%;
}

.menu-toggler {
  display: none;
}

.menu-toggler-label {
  cursor: pointer;
  font-size: 20px;
  font-weight: bold;
}

.stagger-menu {
  list-style-type: none;
  margin: 16px 0;
  padding: 0;
}

.stagger-menu li {
  margin-bottom: 8px;
  font-size: 18px;
  opacity: 0;
  transform: translateX(100%);
  transition:
    opacity 0.3s cubic-bezier(0.75, -0.015, 0.565, 1.055),
    transform 0.3s cubic-bezier(0.75, -0.015, 0.565, 1.055);
}

.menu-toggler:checked ~ .stagger-menu li {
  opacity: 1;
  transform: translateX(0);
  transition-delay: calc(0.055s * var(--i));
}
```

Bitte klicken Sie in der unteren rechten Ecke auf 'Go Live', um den Webdienst auf Port 8080 auszuführen. Anschließend können Sie die Registerkarte **Web 8080** aktualisieren, um die Webseite anzuschauen.
