# Carte avec découpage d'image

`index.html` et `style.css` ont déjà été fournis dans la machine virtuelle.

Pour créer une carte avec un découpage d'image, suivez ces étapes :

1. Ajoutez un fond couleur à un élément `.container` à l'aide de la propriété `background`.
2. Créez un élément `.card` et ajoutez un élément `figure` à l'intérieur avec l'image souhaitée et tout autre contenu.
3. Utilisez le pseudo-élément `::before` pour ajouter une `bordure` autour de l'élément `figure`. Définissez la couleur de la bordure pour correspondre à la couleur de `background` de l'élément `.container` pour créer l'illusion d'un découpage dans la `.card`.

Voici un exemple de code HTML pour la carte :

```html
<div class="container">
  <div class="card">
    <figure>
      <img alt="" src="https://picsum.photos/id/447/400/400" />
    </figure>
    <p class="content">
      Lorem ipsum dolor sit amet consectetur adipisicing elit.
    </p>
  </div>
</div>
```

Et voici le code CSS correspondant :

```css
.container {
  display: flex;
  justify-content: center;
  align-items: center;
  padding: 96px 24px 48px;
  background: #f3f1fe;
}

.card {
  width: 350px;
  margin: 8px;
  display: flex;
  flex-direction: column;
  align-items: center;
  background: #fff;
  border-radius: 10px;
  box-shadow: 0 0 5px -2px rgba(0, 0, 0, 0.1);
}

.card figure {
  width: 120px;
  height: 120px;
  margin-top: -60px;
  border-radius: 50%;
  position: relative;
}

.card figure::before {
  content: "";
  position: absolute;
  top: 50%;
  left: 50%;
  width: 100%;
  height: 100%;
  transform: translate(-50%, -50%);
  border-radius: inherit;
  border: 1rem solid #f3f1fe;
  box-shadow: 0 1px rgba(0, 0, 0, 0.1);
}

.card figure img {
  width: 100%;
  height: 100%;
  border-radius: inherit;
  object-fit: cover;
}

.card.content {
  margin: 2rem;
  text-align: center;
  line-height: 1.5;
  color: #101010;
}
```

Veuillez cliquer sur 'Go Live' dans le coin inférieur droit pour exécuter le service web sur le port 8080. Ensuite, vous pouvez rafraîchir l'onglet **Web 8080** pour prévisualiser la page web.
