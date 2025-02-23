# Liste avec des titres de section collants

`index.html` et `style.css` ont déjà été fournis dans la machine virtuelle.

Pour créer une liste avec des titres collants pour chaque section, suivez ces étapes :

1. Autorisez le conteneur de liste (`<dl>`) à déborder verticalement en utilisant `overflow-y: auto`.
2. Collez les titres (`<dt>`) au sommet du conteneur en définissant leur `position` sur `sticky` et en appliquant `top: 0`.
3. Utilisez le code HTML et CSS suivant :

HTML :

```html
<div class="container">
  <dl class="sticky-stack">
    <dt>A</dt>
    <dd>Algérie</dd>
    <dd>Angola</dd>

    <dt>B</dt>
    <dd>Bénin</dd>
    <dd>Botswana</dd>
    <dd>Burkina Faso</dd>
    <dd>Burundi</dd>

    <dt>C</dt>
    <dd>Cabo Verde</dd>
    <dd>Cameroun</dd>
    <dd>République centrafricaine</dd>
    <dd>Tchad</dd>
    <dd>Comores</dd>
    <dd>Congo, République démocratique du</dd>
    <dd>Congo, République du</dd>
    <dd>Côte d'Ivoire</dd>

    <dt>D</dt>
    <dd>Djibouti</dd>

    <dt>E</dt>
    <dd>Égypte</dd>
    <dd>Guinée équatoriale</dd>
    <dd>Érythrée</dd>
    <dd>Eswatini (anciennement Swaziland)</dd>
    <dd>Éthiopie</dd>
  </dl>
</div>
```

CSS :

```css
.container {
  display: grid;
  place-items: center;
  min-height: 400px;
}

.sticky-stack {
  background: #37474f;
  color: #fff;
  margin: 0;
  height: 320px;
  border-radius: 1rem;
  overflow-y: auto;
}

.sticky-stack dt {
  position: sticky;
  top: 0;
  font-weight: bold;
  background: #263238;
  color: #cfd8dc;
  padding: 0.25rem 1rem;
}

.sticky-stack dd {
  margin: 0;
  padding: 0.75rem 1rem;
}

.sticky-stack dd + dt {
  margin-top: 1rem;
}
```

Veuillez cliquer sur 'Go Live' dans le coin inférieur droit pour exécuter le service web sur le port 8080. Ensuite, vous pouvez actualiser l'onglet **Web 8080** pour prévisualiser la page web.
