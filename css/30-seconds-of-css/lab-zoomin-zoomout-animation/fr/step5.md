# Expérimentation avec les propriétés d'animation

Personnalisons notre animation en expérimentant avec différentes propriétés d'animation. Cela vous aidera à comprendre comment ces propriétés influencent le comportement de l'animation.

1. Ouvrez le fichier `style.css` et modifiez le sélecteur `.zoom-in-out-box` pour tester différentes propriétés d'animation :

```css
.zoom-in-out-box {
  margin: 24px;
  width: 50px;
  height: 50px;
  background: #f50057;
  animation: zoom-in-zoom-out 2s ease-in-out infinite;
  /* Ajoute une légère rotation pendant l'animation */
  border-radius: 10px;
}
```

2. Comprenons ce que nous avons modifié :

   - Nous avons étendu la durée de l'animation à `2s` (2 secondes)
   - Nous avons changé la fonction de temporisation en `ease-in-out`, ce qui rend le début et la fin de l'animation fluides
   - Nous avons ajouté un `border-radius` de 10px pour arrondir les coins de notre boîte

3. Modifions également nos keyframes (images clés) pour ajouter un effet de rotation :

```css
@keyframes zoom-in-zoom-out {
  0% {
    transform: scale(1, 1) rotate(0deg);
  }
  50% {
    transform: scale(1.5, 1.5) rotate(45deg);
    background-color: #2196f3;
  }
  100% {
    transform: scale(1, 1) rotate(0deg);
  }
}
```

4. Dans cette définition mise à jour des keyframes :

   - Nous avons ajouté une fonction `rotate()` à la propriété `transform`
   - À 50 %, l'élément tourne maintenant de 45 degrés tout en grossissant
   - Nous avons également changé la couleur de fond en bleu à 50 %

5. Enregistrez le fichier `style.css` après avoir apporté ces modifications.

6. Rafraîchissez l'onglet **Web 8080** pour voir votre animation améliorée.

Votre animation devrait maintenant être plus lente (2 secondes par cycle), avoir des coins arrondis, tourner pendant le zoom et changer de couleur à mi-chemin de l'animation. Cela démontre comment les animations CSS peuvent combiner plusieurs changements de propriétés pour des effets visuels riches.

N'hésitez pas à expérimenter davantage avec différentes propriétés et valeurs pour voir comment elles influencent votre animation.
