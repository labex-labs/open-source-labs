# Animation en gradation

`index.html` et `style.css` ont déjà été fournis dans la machine virtuelle.

Ce code crée une animation en gradation pour les éléments d'une liste. Pour ce faire :

1. Rendre les éléments de la liste transparents et les déplacer jusqu'à la droite en définissant `opacity: 0` et `transform: translateX(100%)`.
2. Spécifier les mêmes propriétés `transition` pour les éléments de la liste, sauf `transition-delay`.
3. Utiliser des styles en ligne pour spécifier une valeur pour `--i` pour chaque élément de la liste. Cela sera utilisé pour `transition-delay` pour créer l'effet en gradation.
4. Utiliser le sélecteur pseudo-classe `:checked` pour la case à cocher pour styliser les éléments de la liste. Pour les faire apparaître et glisser en vue, définir `opacity` sur `1` et `transform` sur `translateX(0)`.

Voici le code HTML et CSS pour obtenir cet effet :

```html
<div class="container">
  <input type="checkbox" name="menu" id="menu" class="menu-toggler" />
  <label for="menu" class="menu-toggler-label">Menu</label>
  <ul class="stagger-menu">
    <li style="--i: 0">Accueil</li>
    <li style="--i: 1">Tarifs</li>
    <li style="--i: 2">Compte</li>
    <li style="--i: 3">Support</li>
    <li style="--i: 4">À propos</li>
  </ul>
</div>
```

```css
.container {
  overflow-x: hidden;
  width: 100%;
}

.menu-toggler {
  display: none;
}

.menu-toggler-label {
  cursor: pointer;
  font-size: 20px;
  font-weight: bold;
}

.stagger-menu {
  list-style-type: none;
  margin: 16px 0;
  padding: 0;
}

.stagger-menu li {
  margin-bottom: 8px;
  font-size: 18px;
  opacity: 0;
  transform: translateX(100%);
  transition:
    opacity 0.3s cubic-bezier(0.75, -0.015, 0.565, 1.055),
    transform 0.3s cubic-bezier(0.75, -0.015, 0.565, 1.055);
}

.menu-toggler:checked ~ .stagger-menu li {
  opacity: 1;
  transform: translateX(0);
  transition-delay: calc(0.055s * var(--i));
}
```

Veuillez cliquer sur 'Go Live' dans le coin inférieur droit pour exécuter le service web sur le port 8080. Ensuite, vous pouvez actualiser l'onglet **Web 8080** pour prévisualiser la page web.
