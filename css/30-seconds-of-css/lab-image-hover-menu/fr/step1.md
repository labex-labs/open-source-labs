# Menu sur survol d'image

`index.html` et `style.css` ont déjà été fournis dans la machine virtuelle.

Pour afficher un volet de menu lorsque l'utilisateur survole une image, utilisez une balise `<figure>` pour entourer l'élément `<img>` et un élément `<div>` qui contiendra les liens du menu. Appliquez les propriétés CSS suivantes pour animer l'image lors du survol et créer un effet de glissement :

- `opacity`
- `right`
  Définissez l'attribut `left` de l'élément `<div>` sur la valeur négative de la largeur de l'élément. Remettez-le à `0` lorsque vous survolez l'élément parent pour faire apparaître le menu. Enfin, utilisez `display: flex`, `flex-direction: column` et `justify-content: center` sur l'élément `<div>` pour centrer verticalement les éléments du menu.

```html
<figure class="hover-menu">
  <img src="https://picsum.photos/id/1060/800/480.jpg" />
  <div>
    <a href="#">Accueil</a>
    <a href="#">Tarifs</a>
    <a href="#">À propos</a>
  </div>
</figure>
```

```css
.hover-menu {
  position: relative;
  overflow: hidden;
  margin: 8px;
  min-width: 340px;
  max-width: 480px;
  max-height: 290px;
  width: 100%;
  background: #000;
  text-align: center;
  box-sizing: border-box;
}

.hover-menu * {
  box-sizing: border-box;
}

.hover-menu img {
  position: relative;
  max-width: 100%;
  top: 0;
  right: 0;
  opacity: 1;
  transition:
    opacity 0.3s ease-in-out,
    right 0.3s ease-in-out;
}

.hover-menu div {
  position: absolute;
  top: 0;
  left: -120px;
  width: 120px;
  height: 100%;
  padding: 8px 4px;
  background: #000;
  transition:
    left 0.3s ease-in-out,
    opacity 0.3s ease-in-out;
  display: flex;
  flex-direction: column;
  justify-content: center;
}

.hover-menu div a {
  display: block;
  line-height: 2;
  color: #fff;
  text-decoration: none;
  opacity: 0.8;
  padding: 5px 15px;
  position: relative;
  transition: opacity 0.3s ease-in-out;
}

.hover-menu div a:hover {
  text-decoration: underline;
}

.hover-menu:hover img {
  opacity: 0.5;
  right: -120px;
}

.hover-menu:hover div {
  left: 0;
  opacity: 1;
}
```

Veuillez cliquer sur 'Go Live' dans le coin inférieur droit pour exécuter le service web sur le port 8080. Ensuite, vous pouvez actualiser l'onglet **Web 8080** pour prévisualiser la page web.
