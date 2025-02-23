# Liste avec des titres de section flottants

`index.html` et `style.css` ont déjà été fournis dans la machine virtuelle.

Pour créer une liste avec des titres flottants pour chaque section, suivez ces étapes :

1. Appliquez `overflow-y: auto` au conteneur de liste pour autoriser le défilement vertical.
2. Utilisez `display: grid` sur le conteneur interne (`<dl>`) pour créer une mise en page avec deux colonnes.
3. Définissez les titres (`<dt>`) sur `grid-column: 1` et le contenu (`<dd>`) sur `grid-column: 2`.
4. Enfin, appliquez `position: sticky` et `top: 0,5rem` aux titres pour créer un effet de flottement.

Voici le code HTML :

```html
<div class="container">
  <div class="floating-stack">
    <dl>
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
</div>
```

Et voici le code CSS :

```css
.container {
  display: grid;
  place-items: center;
  min-height: 400px;
}

.floating-stack {
  background: #455a64;
  color: #fff;
  height: 80vh;
  width: 320px;
  border-radius: 1rem;
  overflow-y: auto;
}

.floating-stack > dl {
  margin: 0 0 1rem;
  display: grid;
  grid-template-columns:
    2,
    5rem 1fr;
  align-items: center;
}

.floating-stack dt {
  position: sticky;
  top: 0, 5rem;
  left: 0, 5rem;
  font-weight: bold;
  background: #263238;
  color: #cfd8dc;
  height: 2rem;
  width: 2rem;
  border-radius: 50%;
  padding:
    0,
    25rem 1rem;
  grid-column: 1;
  display: inline-flex;
  align-items: center;
  justify-content: center;
  box-sizing: border-box;
}

.floating-stack dd {
  grid-column: 2;
  margin: 0;
  padding: 0, 75rem;
}

.floating-stack > dl:first-of-type > dd:first-of-type {
  margin-top: 0, 25rem;
}
```

Veuillez cliquer sur 'Go Live' dans le coin inférieur droit pour exécuter le service web sur le port 8080. Ensuite, vous pouvez actualiser l'onglet **Web 8080** pour prévisualiser la page web.
