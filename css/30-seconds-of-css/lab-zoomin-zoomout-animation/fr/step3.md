# Création de l'animation avec des keyframes

Les animations CSS fonctionnent en définissant des keyframes (images clés) qui spécifient les styles qu'un élément doit avoir à différents moments de la séquence d'animation. Créons les keyframes pour notre animation de zoom avant et zoom arrière.

1. Rouvrez le fichier `style.css` et ajoutez le code suivant à la fin :

```css
@keyframes zoom-in-zoom-out {
  0% {
    transform: scale(1, 1);
  }
  50% {
    transform: scale(1.5, 1.5);
  }
  100% {
    transform: scale(1, 1);
  }
}
```

2. Comprenons ce que fait ce code :

   - `@keyframes` est une règle @ CSS qui définit les étapes et les styles d'une animation
   - `zoom-in-zoom-out` est le nom que nous donnons à notre animation (nous ferons référence à ce nom plus tard)
   - À l'intérieur des keyframes, nous définissons ce qui se passe à différents moments de l'animation :
     - À `0%` (le début), l'élément est à sa taille normale avec `scale(1, 1)`
     - À `50%` (au milieu), l'élément grossit jusqu'à 1,5 fois sa taille avec `scale(1.5, 1.5)`
     - À `100%` (la fin), l'élément revient à sa taille normale
   - La propriété `transform` avec la fonction `scale()` modifie la taille de l'élément

3. Enregistrez le fichier `style.css` après avoir ajouté ces keyframes.

Les keyframes définissent ce que fera notre animation, mais nous ne l'avons pas encore appliquée à notre élément. Dans l'étape suivante, nous allons connecter l'animation à notre boîte.
