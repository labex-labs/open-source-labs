# Guillemets stylisés

`index.html` et `style.css` ont déjà été fournis dans la machine virtuelle.

Pour personnaliser les guillemets d'inline, modifiez la propriété `quotes` à l'intérieur d'un élément `<q>`.

Par exemple :

```html
<p><q>Do or do not, there is no try.</q> – Yoda</p>
```

peut être stylisé avec des guillemets droits en utilisant le CSS :

```css
q {
  quotes: "“" "”";
}
```

Veuillez cliquer sur 'Go Live' dans le coin inférieur droit pour exécuter le service web sur le port 8080. Ensuite, vous pouvez rafraîchir l'onglet **Web 8080** pour prévisualiser la page web.
