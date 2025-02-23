# Button Swing Animation

`index.html` und `style.css` wurden bereits in der VM bereitgestellt.

Um eine Schaukelanimation beim Fokus zu erstellen, sollten Sie einen geeigneten `transition` verwenden, um Änderungen am Element zu animieren. Anschließend wenden Sie die `:focus`-Pseudo-Klasse auf das Element an und verwenden Sie `animation` mit `transform`, um es zu schaukeln. Schließlich fügen Sie `animation-iteration-count` hinzu, um die Animation nur einmal abzuspielen. Hier ist ein Beispiel dafür, wie dies in HTML und CSS geht:

```html
<button class="button-swing">Submit</button>
```

```css
.button-swing {
  color: #65b5f6;
  background-color: transparent;
  border: 1px solid #65b5f6;
  border-radius: 4px;
  padding: 0 16px;
  cursor: pointer;
  transition: all 0.2s ease-in-out;
}

.button-swing:focus {
  animation: swing 1s ease;
  animation-iteration-count: 1;
}

@keyframes swing {
  15% {
    transform: translateX(5px);
  }
  30% {
    transform: translateX(-5px);
  }
  50% {
    transform: translateX(3px);
  }
  65% {
    transform: translateX(-3px);
  }
  80% {
    transform: translateX(2px);
  }
  100% {
    transform: translateX(0);
  }
}
```

Bitte klicken Sie auf 'Go Live' in der unteren rechten Ecke, um den Webdienst auf Port 8080 auszuführen. Anschließend können Sie die Registerkarte **Web 8080** aktualisieren, um die Webseite anzuschauen.
