# Réinitialisation de la mise en boîte (Box-Sizing)

`index.html` et `style.css` ont déjà été fournis dans la machine virtuelle (VM).

Pour vous assurer que la largeur (`width`) et la hauteur (`height`) d'un élément ne sont pas affectées par la bordure (`border`) ou le rembourrage (`padding`), utilisez la propriété CSS `box-sizing: border-box`. Cela inclut le rembourrage (`padding`) et la bordure (`border`) dans le calcul de la largeur (`width`) et de la hauteur (`height`) de l'élément. Si vous voulez hériter de la propriété `box-sizing` d'un élément parent, utilisez `box-sizing: inherit`.

Voici un exemple d'utilisation de la propriété `box-sizing` avec deux éléments `div` :

```html
<div class="box">border-box</div>
<div class="box content-box">content-box</div>
```

```css
*,
*::before,
*::after {
  box-sizing: inherit;
}

.box {
  display: inline-block;
  width: 120px;
  height: 120px;
  padding: 8px;
  margin: 8px;
  background: #f24333;
  color: white;
  border: 1px solid #ba1b1d;
  border-radius: 4px;
  box-sizing: border-box;
}

.content-box {
  box-sizing: content-box;
}
```

Dans cet exemple, le premier élément `div` a `box-sizing: border-box`, et le second élément `div` a `box-sizing: content-box`.

Veuillez cliquer sur 'Go Live' dans le coin inférieur droit pour exécuter le service web sur le port 8080. Ensuite, vous pouvez actualiser l'onglet **Web 8080** pour prévisualiser la page web.
