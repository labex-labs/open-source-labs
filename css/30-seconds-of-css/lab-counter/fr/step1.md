# Compteur

`index.html` et `style.css` ont déjà été fournis dans la machine virtuelle.

Pour créer un compteur de liste personnalisé qui prend en compte les éléments de liste imbriqués, suivez ces étapes :

1. Utilisez `counter - reset` pour initialiser un compteur variable (valeur par défaut `0`), le nom étant la valeur de l'attribut (par exemple `compteur`).
2. Utilisez `counter - increment` sur le compteur variable pour chaque élément comptable (par exemple chaque `<li>`).
3. Utilisez `counters()` pour afficher la valeur de chaque compteur variable comme partie du `contenu` de l'élément pseudo - élément `::before` pour chaque élément comptable (par exemple chaque `<li>`). La deuxième valeur passée à elle (`'.'`) sert de délimiteur pour les compteurs imbriqués.

Voici un exemple de code HTML :

```html
<ul>
  <li>Élément de liste</li>
  <li>Élément de liste</li>
  <li>
    Élément de liste
    <ul>
      <li>Élément de liste</li>
      <li>Élément de liste</li>
      <li>Élément de liste</li>
    </ul>
  </li>
</ul>
```

Et voici le code CSS pour appliquer le compteur de liste personnalisé :

```css
ul {
  counter - reset: compteur;
  list - style: none;
}

li::before {
  counter - increment: compteur;
  content: counters(compteur, ".") " ";
}
```

Veuillez cliquer sur 'Go Live' dans le coin inférieur droit pour exécuter le service web sur le port 8080. Ensuite, vous pouvez rafraîchir l'onglet **Web 8080** pour prévisualiser la page web.
