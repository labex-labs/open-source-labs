# Effet de survol de lien en forme de zigzag

`index.html` et `style.css` ont déjà été fournis dans la machine virtuelle.

Pour créer un effet en forme de zigzag lors du survol d'un lien, vous pouvez suivre ces étapes :

1. Créez un fond d'arrière-plan répétitif pour le lien en utilisant un `linear-gradient`.

```css
a.squiggle {
  background: linear-gradient(to bottom, #0087ca 0%, #0087ca 100%);
  background-position: 0 100%;
  background-repeat: repeat-x;
  background-size: 2px 2px;
  color: inherit;
  text-decoration: none;
}
```

2. Créez un état `:hover` pour le lien avec une `background-image` d'une URL de données contenant un SVG avec un tracé en forme de zigzag et une animation.

```css
a.squiggle:hover {
  background-image: url("data:image/svg+xml;charset=utf8,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 20 4'%3E%3Cstyle type='text/css'%3E.squiggle{animation:shift.3s linear infinite;}@keyframes shift {from {transform:translateX(0);}to {transform:translateX(-15px);}}%3C/style%3E%3Cpath fill='none' stroke='%230087ca' stroke-width='2' class='squiggle' d='M0,3.5 c 5,0,5,-3,10,-3 s 5,3,10,3 c 5,0,5,-3,10,-3 s 5,3,10,3'/%3E%3C/svg%3E");
  background-size: auto 4px;
}
```

3. Utilisez le code HTML ci-dessous pour ajouter le lien à la page.

```html
<p>
  Le <a class="squiggle" href="#">magnifique poulpe</a> a nagé gracieusement.
</p>
```

Veuillez cliquer sur 'Go Live' dans le coin inférieur droit pour exécuter le service web sur le port 8080. Ensuite, vous pouvez actualiser l'onglet **Web 8080** pour prévisualiser la page web.
