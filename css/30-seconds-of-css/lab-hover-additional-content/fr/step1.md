# Afficher du contenu supplémentaire au survol

`index.html` et `style.css` ont déjà été fournis dans la machine virtuelle.

Pour créer une carte qui affiche du contenu supplémentaire au survol, suivez ces étapes :

1. Utilisez `overflow: hidden` sur la carte pour cacher tout élément qui dépasse verticalement.
2. Utilisez les sélecteurs de pseudo-classes `:hover` et `:focus-within` pour modifier le style de la carte lorsque l'élément est survolé, au focus ou que l'un de ses descendants est au focus.
3. Définissez `transition: 0.3s ease all` pour créer un effet de transition fluide au survol/au focus.

Voici un exemple de code HTML pour la carte :

```html
<div class="card">
  <img src="https://picsum.photos/id/404/367/267" />
  <h3>Lorem ipsum</h3>
  <div class="focus-content">
    <p>
      Lorem ipsum dolor sit amet, consectetur adipiscing elit.<br />
      <a href="#">Lien vers la source</a>
    </p>
  </div>
</div>
```

Et voici le code CSS pour styliser la carte :

```css
.card {
  width: 300px;
  height: 280px;
  padding: 0;
  box-shadow: 0 2px 4px 0 rgba(0, 0, 0, 0.1);
  border-radius: 8px;
  box-sizing: border-box;
  overflow: hidden;
}

.card * {
  transition: 0.3s ease all;
}

.card img {
  margin: 0;
  width: 300px;
  height: 224px;
  object-fit: cover;
  display: block;
}

.card h3 {
  margin: 0;
  padding: 12px 12px 48px;
  line-height: 32px;
  font-weight: 500;
  font-size: 20px;
}

.card.focus-content {
  display: block;
  padding: 8px 12px;
}

.card p {
  margin: 0;
  line-height: 1.5;
}

.card:hover img,
.card:focus-within img {
  margin-top: -80px;
}

.card:hover h3,
.card:focus-within h3 {
  padding: 8px 12px 0;
}
```

Veuillez cliquer sur 'Go Live' dans le coin inférieur droit pour exécuter le service web sur le port 8080. Ensuite, vous pouvez rafraîchir l'onglet **Web 8080** pour prévisualiser la page web.
