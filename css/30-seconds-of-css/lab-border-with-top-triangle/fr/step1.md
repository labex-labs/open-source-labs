# Bordure avec triangle en haut

`index.html` et `style.css` ont déjà été fournis dans la machine virtuelle.

Pour créer un conteneur de contenu avec un triangle en haut, suivez ces étapes :

1. Utilisez les pseudo-éléments `::before` et `::after` pour créer deux triangles.
2. Réglez la `couleur de bordure` et la `couleur de fond` des triangles pour correspondre au conteneur.
3. Réglez la `largeur de bordure` du triangle `::before` pour qu'elle soit de `1px` plus large que le triangle `::after` pour servir de bordure.
4. Positionnez le triangle `::after` à `1px` à droite du triangle `::before` pour permettre d'afficher la bordure gauche.

Voici un exemple de code HTML pour le conteneur :

```html
<div class="container">Bordure avec triangle en haut</div>
```

Et voici le code CSS correspondant :

```css
.container {
  position: relative;
  background: #ffffff;
  padding: 15px;
  border: 1px solid #dddddd;
  margin-top: 20px;
}

.container::before,
.container::after {
  content: "";
  position: absolute;
  bottom: 100%;
  left: 19px;
  border: 11px solid transparent;
}

.container::before {
  border-bottom-color: #dddddd;
}

.container::after {
  left: 20px;
  border: 10px solid transparent;
  border-bottom-color: #ffffff;
}
```

Veuillez cliquer sur 'Go Live' dans le coin inférieur droit pour exécuter le service web sur le port 8080. Ensuite, vous pouvez actualiser l'onglet **Web 8080** pour prévisualiser la page web.
