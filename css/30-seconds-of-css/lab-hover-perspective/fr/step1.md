# Transformation en perspective au survol

`index.html` et `style.css` ont déjà été fournis dans la machine virtuelle.

Pour créer une transformation en perspective avec une animation au survol sur un élément :

1. Utilisez la propriété `transform` avec les fonctions `perspective()` et `rotateY()` pour appliquer une perspective à l'élément. Par exemple, pour créer une perspective gauche, utilisez `transform: perspective(1500px) rotateY(15deg);`. Pour créer une perspective droite, utilisez `transform: perspective(1500px) rotateY(-15deg);`.

2. Utilisez la propriété `transition` pour animer la propriété `transform` lorsque l'élément est survolé. Par exemple, `transition: transform 1s ease 0s;`.

3. Pour refléter l'effet en perspective d'un côté à l'autre, changez la valeur de `rotateY()` en négative pour la perspective droite. Par exemple, utilisez `transform: perspective(1500px) rotateY(-15deg);`.

Exemple de code HTML :

```html
<div class="card-container">
  <div class="image-card perspective-left"></div>
  <div class="image-card perspective-right"></div>
</div>
```

Exemple de code CSS :

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

Veuillez cliquer sur 'Go Live' dans le coin inférieur droit pour exécuter le service web sur le port 8080. Ensuite, vous pouvez actualiser l'onglet **Web 8080** pour prévisualiser la page web.
