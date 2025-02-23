# Barre de défilement personnalisée

`index.html` et `style.css` ont déjà été fournis dans la machine virtuelle.

Pour personnaliser le style de la barre de défilement pour les éléments avec un débordement défilable, vous pouvez utiliser `::-webkit-scrollbar` pour styliser l'élément de barre de défilement, `::-webkit-scrollbar-track` pour styliser la piste de la barre de défilement (le fond de la barre de défilement) et `::-webkit-scrollbar-thumb` pour styliser le bouton de la barre de défilement (l'élément pouvant être déplacé). Cependant, notez que cette technique ne fonctionne que sur les navigateurs basés sur WebKit, et le style de la barre de défilement n'est pas sur aucune voie de standardisation. Voici un exemple de manière d'utiliser ces sélecteurs en HTML et CSS :

```html
<div class="custom-scrollbar">
  <p>
    Lorem ipsum dolor sit amet consectetur adipisicing elit.<br />
    Iure id exercitationem nulla qui repellat laborum vitae, <br />
    molestias tempora velit natus. Quas, assumenda nisi. <br />
    Quisquam enim qui iure, consequatur velit sit?
  </p>
</div>
```

```css
.custom-scrollbar {
  height: 70px;
  overflow-y: scroll;
}

.custom-scrollbar::-webkit-scrollbar {
  width: 8px;
}

.custom-scrollbar::-webkit-scrollbar-track {
  background: #1e3f20;
  border-radius: 12px;
}

.custom-scrollbar::-webkit-scrollbar-thumb {
  background: #4a7856;
  border-radius: 12px;
}
```

Veuillez cliquer sur 'Go Live' dans le coin inférieur droit pour exécuter le service web sur le port 8080. Ensuite, vous pouvez actualiser l'onglet **Web 8080** pour prévisualiser la page web.
