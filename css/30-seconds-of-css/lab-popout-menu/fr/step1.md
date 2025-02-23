# Menu déroulant

`index.html` et `style.css` ont déjà été fournis dans la machine virtuelle.

Pour afficher un menu déroulant interactif au survol/au focus, suivez ces étapes :

1. Utilisez `left: 100%` dans le CSS pour positionner le menu déroulant à droite de l'élément parent.
2. Utilisez `visibility: hidden` au lieu de `display: none` pour cacher initialement le menu déroulant, afin de permettre l'application de transitions.
3. Appliquez les sélecteurs de pseudo-classes `:hover`, `:focus` et `:focus-within` à l'élément parent pour afficher le menu déroulant lorsqu'il est survolé/focusé.
4. Utilisez le code HTML et CSS suivant :

HTML :

```
<div class="reference" tabindex="0">
  <div class="popout-menu">Menu déroulant</div>
</div>
```

CSS :

```
.reference {
  position: relative;
  background: tomato;
  width: 100px;
  height: 80px;
}

.popout-menu {
  position: absolute;
  visibility: hidden;
  left: 100%;
  background: #9C27B0;
  color: white;
  padding: 16px;
}

.reference:hover >.popout-menu,
.reference:focus >.popout-menu,
.reference:focus-within >.popout-menu {
  visibility: visible;
}
```

Veuillez cliquer sur 'Go Live' dans le coin inférieur droit pour exécuter le service web sur le port 8080. Ensuite, vous pouvez actualiser l'onglet **Web 8080** pour prévisualiser la page web.
