# Réinitialiser tous les styles

`index.html` et `style.css` ont déjà été fournis dans la machine virtuelle.

Pour réinitialiser tous les styles à leurs valeurs par défaut, utilisez la propriété `all`. Cette propriété n'affectera pas les propriétés `direction` et `unicode-bidi`. Voici un exemple de manière à l'utiliser :

```html
<div class="reset-all-styles">
  <h5>Titre</h5>
  <p>
    Lorem ipsum dolor sit amet consectetur adipisicing elit. Iure id
    exercitationem nulla qui repellat laborum vitae, molestias tempora velit
    natus. Quas, assumenda nisi. Quisquam enim qui iure, consequatur velit sit?
  </p>
</div>
```

```css
.reset-all-styles {
  all: initial;
}
```

Veuillez cliquer sur 'Go Live' dans le coin inférieur droit pour exécuter le service web sur le port 8080. Ensuite, vous pouvez actualiser l'onglet **Web 8080** pour prévisualiser la page web.
