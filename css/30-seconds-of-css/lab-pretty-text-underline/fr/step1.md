# Soulignement de texte joli

`index.html` et `style.css` ont déjà été fournis dans la machine virtuelle.

Pour éviter que les descendeurs ne coupent le soulignement, utilisez `text-shadow` avec quatre valeurs pour créer une ombre épaisse qui couvre la ligne où les descendeurs rencontrent le soulignement. Assurez-vous que la couleur de l'`ombre de texte` corresponde à la couleur de l'`arrière-plan` et ajustez les valeurs en `px` pour les polices de caractères plus grandes. Créez le soulignement réel à l'aide d'`background-image` avec un `linear-gradient()` et `currentColor`. Définissez `background-position`, `background-repeat` et `background-size` pour placer le dégradé à la bonne position. Utilisez le sélecteur de pseudo-classe `::selection` pour vous assurer que l'ombre de texte n'interfère pas avec la sélection de texte. Notez que cet effet est nativement implémenté comme `text-decoration-skip-ink: auto`, mais il offre moins de contrôle sur le soulignement.

Voici un extrait de code d'exemple :

```html
<div class="container">
  <p class="pretty-text-underline">
    Pretty text underline without clipping descenders.
  </p>
</div>
```

```css
.container {
  background: #f5f6f9;
  color: #333;
  padding: 8px 0;
}

.pretty-text-underline {
  display: inline;
  text-shadow:
    1px 1px #f5f6f9,
    -1px 1px #f5f6f9,
    -1px -1px #f5f6f9,
    1px -1px #f5f6f9;
  background-image: linear-gradient(90deg, currentColor 100%, transparent 100%);
  background-position: bottom;
  background-repeat: no-repeat;
  background-size: 100% 1px;
}

.pretty-text-underline::selection {
  background-color: rgba(0, 150, 255, 0.3);
  text-shadow: none;
}
```

Veuillez cliquer sur 'Go Live' dans le coin inférieur droit pour exécuter le service web sur le port 8080. Ensuite, vous pouvez actualiser l'onglet **Web 8080** pour prévisualiser la page web.
