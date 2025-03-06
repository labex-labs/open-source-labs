# Application de l'animation

Maintenant que nous avons défini nos keyframes (images clés), nous devons appliquer l'animation à notre élément boîte.

1. Rouvrez le fichier `style.css` et modifiez le sélecteur `.zoom-in-out-box` comme suit :

```css
.zoom-in-out-box {
  margin: 24px;
  width: 50px;
  height: 50px;
  background: #f50057;
  animation: zoom-in-zoom-out 1s ease infinite;
}
```

2. Comprenons la propriété d'animation que nous avons ajoutée :

   - `animation` est une propriété raccourcie qui définit plusieurs propriétés d'animation à la fois
   - `zoom-in-zoom-out` est le nom de notre animation avec des keyframes
   - `1s` spécifie que un cycle de l'animation dure 1 seconde
   - `ease` est la fonction de temporisation qui fait démarrer l'animation lentement, l'accélérer, puis la ralentir à nouveau
   - `infinite` signifie que l'animation se répétera indéfiniment

3. Enregistrez le fichier `style.css` après avoir apporté ces modifications.

4. Si le serveur web est déjà en cours d'exécution, rafraîchissez simplement l'onglet **Web 8080**. Sinon, cliquez sur "Go Live" dans le coin inférieur droit pour démarrer le serveur, puis ouvrez l'onglet **Web 8080**.

Vous devriez maintenant voir votre carré rose zoomer en avant et en arrière de manière fluide dans une animation continue. Le carré grossit jusqu'à atteindre 1,5 fois sa taille d'origine, puis rétrécit pour revenir à la normale. Ce cycle se répète indéfiniment.
