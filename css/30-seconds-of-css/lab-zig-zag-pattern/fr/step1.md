# Motif de fond en zigzag

`index.html` et `style.css` ont déjà été fournis dans la machine virtuelle.

Pour créer un motif de fond en zigzag, utilisez les étapes suivantes :

1. Définissez un fond blanc à l'aide de `background-color`.
2. Créez les parties d'un motif en zigzag à l'aide de `background-image` avec quatre valeurs de `linear-gradient()`.
3. Spécifiez la taille du motif à l'aide de `background-size`.
4. Placez les parties du motif à l'emplacement correct à l'aide de `background-position`.
5. Pour répéter le motif, utilisez `background-repeat`.
6. **Remarque** : La `height` et la `width` de l'élément sont fixées uniquement à des fins de démonstration.

Voici un extrait de code d'exemple :

```html
<div class="zig-zag"></div>
```

```css
.zig-zag {
  width: 240px;
  height: 240px;
  background-color: #fff;
  background-image:
    linear-gradient(135deg, #000 25%, transparent 25%),
    linear-gradient(225deg, #000 25%, transparent 25%),
    linear-gradient(315deg, #000 25%, transparent 25%),
    linear-gradient(45deg, #000 25%, transparent 25%);
  background-position:
    -30px 0,
    -30px 0,
    0 0,
    0 0;
  background-size: 60px 60px;
  background-repeat: repeat;
}
```

Veuillez cliquer sur 'Go Live' dans le coin inférieur droit pour exécuter le service web sur le port 8080. Ensuite, vous pouvez actualiser l'onglet **Web 8080** pour prévisualiser la page web.
