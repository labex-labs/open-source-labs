# Carte tournante

`index.html` et `style.css` ont déjà été fournis dans la machine virtuelle.

Pour créer une carte à deux faces qui tourne au survol, suivez ces étapes :

1. Définissez la propriété `backface-visibility` des cartes sur `none` pour empêcher la face arrière d'être visible par défaut.
2. Initialement, définissez `rotateY(-180deg)` pour la face arrière de la carte et `rotateY(0deg)` pour la face avant de la carte.
3. Au survol, définissez `rotateY(180deg)` pour la face avant de la carte et `rotateY(0deg)` pour la face arrière de la carte.
4. Définissez une valeur appropriée de `perspective` pour créer l'effet de rotation.

Voici un exemple de code HTML et CSS :

```html
<div class="card">
  <div class="card-side front">
    <div>Face avant</div>
  </div>
  <div class="card-side back">
    <div>Face arrière</div>
  </div>
</div>
```

```css
.card {
  perspective: 150rem;
  position: relative;
  height: 40rem;
  max-width: 400px;
  margin: 2rem;
  box-shadow: none;
  background: none;
}

.card-side {
  height: 35rem;
  border-radius: 15px;
  transition: all 0.8s ease;
  backface-visibility: hidden;
  position: absolute;
  top: 0;
  left: 0;
  width: 80%;
  padding: 2rem;
  color: white;
}

.card-side.back {
  transform: rotateY(-180deg);
  background: linear-gradient(43deg, #4158d0 0%, #c850c0 46%, #ffcc70 100%);
}

.card-side.front {
  background: linear-gradient(160deg, #0093e9 0%, #80d0c7 100%);
}

.card:hover.card-side.front {
  transform: rotateY(180deg);
}

.card:hover.card-side.back {
  transform: rotateY(0deg);
}
```

Veuillez cliquer sur 'Go Live' dans le coin inférieur droit pour exécuter le service web sur le port 8080. Ensuite, vous pouvez actualiser l'onglet **Web 8080** pour prévisualiser la page web.
