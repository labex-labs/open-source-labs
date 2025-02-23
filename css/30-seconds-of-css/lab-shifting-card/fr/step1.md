# Carte qui bascule

`index.html` et `style.css` ont déjà été fournis dans la machine virtuelle.

Pour créer une carte qui bascule au survol, suivez ces étapes :

1. Définissez la `perspective` appropriée sur l'élément `.container` pour permettre l'effet de basculement.
2. Ajoutez une `transition` pour la propriété `transform` de l'élément `.card`.
3. Utilisez `Document.querySelector()` pour sélectionner l'élément `.card` et ajoutez des écouteurs d'événements pour les événements `mousemove` et `mouseout`.
4. Utilisez `Element.getBoundingClientRect()` pour obtenir les valeurs de `x`, `y`, `width` et `height` de l'élément `.card`.
5. Calculez la distance relative en tant que valeur comprise entre `-1` et `1` pour les axes `x` et `y` et appliquez-la à travers la propriété `transform`.

Voici le code HTML et CSS d'exemple pour la carte :

```html
<div class="container">
  <div class="shifting-card">
    <div class="content">
      <h3>Carte</h3>
      <p>
        Lorem ipsum dolor sit amet consectetur adipisicing elit. Corrupti
        repellat, consequuntur doloribus voluptate esse iure?
      </p>
    </div>
  </div>
</div>
```

```css
.container {
  display: flex;
  padding: 24px;
  justify-content: center;
  align-items: center;
  background: #f3f1fe;
  perspective: 1000px;
}

.shifting-card {
  width: 350px;
  display: flex;
  flex-direction: column;
  align-items: center;
  background: #fff;
  border-radius: 10px;
  margin: 0.5rem;
  transition: transform 0.2s ease-out;
  box-shadow: 0 0 5px -2px rgba(0, 0, 0, 0.1);
}

.shifting-card.content {
  text-align: center;
  margin: 2rem;
  line-height: 1.5;
  color: #101010;
}
```

Voici le code JavaScript pour ajouter l'effet de survol :

```js
const card = document.querySelector(".shifting-card");
const { x, y, width, height } = card.getBoundingClientRect();
const cx = x + width / 2;
const cy = y + height / 2;

const handleMove = (e) => {
  const { pageX, pageY } = e;
  const dx = (cx - pageX) / (width / 2);
  const dy = (cy - pageY) / (height / 2);
  e.target.style.transform = `rotateX(${10 * dy * -1}deg) rotateY(${
    10 * dx
  }deg)`;
};

const handleOut = (e) => {
  e.target.style.transform = "initial";
};

card.addEventListener("mousemove", handleMove);
card.addEventListener("mouseout", handleOut);
```

Veuillez cliquer sur 'Go Live' dans le coin inférieur droit pour exécuter le service web sur le port 8080. Ensuite, vous pouvez actualiser l'onglet **Web 8080** pour prévisualiser la page web.
