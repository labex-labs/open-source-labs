# Mise en page responsive avec barre latérale

`index.html` et `style.css` ont déjà été fournis dans la machine virtuelle.

Pour créer une mise en page responsive avec une zone de contenu et une barre latérale, utilisez `display: grid` sur le conteneur parent, `minmax()` pour la deuxième colonne (barre latérale) pour lui permettre de prendre entre `150px` et `20%`, et `1fr` pour la première colonne (contenu principal) pour prendre le reste de l'espace restant. Voici un exemple de code HTML et CSS :

```html
<div class="container">
  <main>This element is 1fr large.</main>
  <aside>Min: 150px / Max: 20%</aside>
</div>
```

```css
.container {
  display: grid;
  grid-template-columns: 1fr minmax(150px, 20%);
  height: 100px;
}

main,
aside {
  padding: 12px;
  text-align: center;
}

main {
  background: #d4f2c4;
}

aside {
  background: #81cfd9;
}
```

Veuillez cliquer sur 'Go Live' dans le coin inférieur droit pour exécuter le service web sur le port 8080. Ensuite, vous pouvez rafraîchir l'onglet **Web 8080** pour prévisualiser la page web.
