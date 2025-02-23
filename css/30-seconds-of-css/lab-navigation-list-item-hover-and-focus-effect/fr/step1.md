# Effet de survol et de focus sur les éléments de la liste de navigation

`index.html` et `style.css` ont déjà été fournis dans la machine virtuelle.

Pour créer un effet de survol et de focus personnalisé pour les éléments de navigation, utilisez les transformations CSS comme suit :

1. Utilisez le pseudo-élément `::before` au niveau de l'ancrage de l'élément de liste pour créer un effet de survol. Cachez-le en utilisant `transform: scale(0)`.
2. Utilisez les sélecteurs de pseudo-classes `:hover` et `:focus` pour transférer le pseudo-élément à `transform: scale(1)` et afficher son fond de couleur.
3. Empêchez le pseudo-élément de recouvrir l'élément ancrage en utilisant `z-index`.

Vous pouvez utiliser le code HTML suivant pour votre menu de navigation :

```html
<nav class="hover-nav">
  <ul>
    <li><a href="#">Accueil</a></li>
    <li><a href="#">À propos</a></li>
    <li><a href="#">Contact</a></li>
  </ul>
</nav>
```

Et appliquez les règles CSS suivantes :

```css
.hover-nav ul {
  list-style: none;
  margin: 0;
  padding: 0;
  overflow: hidden;
}

.hover-nav li {
  float: left;
}

.hover-nav li a {
  position: relative;
  display: block;
  color: #fff;
  text-align: center;
  padding: 8px 12px;
  text-decoration: none;
  z-index: 0;
}

.hover-nav li a::before {
  position: absolute;
  content: "";
  width: 100%;
  height: 100%;
  bottom: 0;
  left: 0;
  background-color: #2683f6;
  z-index: -1;
  transform: scale(0);
  transition: transform 0.5s ease-in-out;
}

.hover-nav li a:hover::before,
.hover-nav li a:focus::before {
  transform: scale(1);
}
```

Veuillez cliquer sur 'Go Live' dans le coin inférieur droit pour exécuter le service web sur le port 8080. Ensuite, vous pouvez actualiser l'onglet **Web 8080** pour prévisualiser la page web.
