# Stylage CSS de base

Maintenant que nous avons notre structure HTML en place, créons le stylage CSS de base pour notre élément d'animation.

1. Ouvrez le fichier `style.css` dans l'éditeur.

2. Si le fichier est vide ou manquant, créez - le avec le contenu suivant :

```css
body {
  font-family: Arial, sans-serif;
  max-width: 800px;
  margin: 0 auto;
  padding: 20px;
}

h1 {
  color: #333;
}

.zoom-in-out-box {
  margin: 24px;
  width: 50px;
  height: 50px;
  background: #f50057;
}
```

3. Comprenons ce que fait ce CSS :

   - Nous définissons un stylage de base pour la page (police, largeur et marges)
   - Nous stylisons l'en - tête avec une couleur gris foncé
   - Pour notre élément d'animation `.zoom - in - out - box`, nous :
     - Ajoutons une marge de 24px autour de lui
     - Fixons sa largeur et sa hauteur à 50px
     - Lui donnons une couleur de fond rose vif

4. Enregistrez le fichier `style.css` après avoir apporté ces modifications.

5. Pour voir votre progression, cliquez sur le bouton "Go Live" dans le coin inférieur droit de VSCode. Cela démarrera un serveur web sur le port 8080. Ensuite, rafraîchissez l'onglet **Web 8080** pour voir votre boîte stylisée.

Vous devriez maintenant voir un petit carré rose sur votre page web. Ce carré est l'élément que nous allons animer dans les étapes suivantes.
