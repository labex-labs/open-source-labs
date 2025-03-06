# Créer le premier dégradé

Maintenant, nous allons commencer à créer notre motif de damier en utilisant des dégradés CSS. Ajoutons le premier dégradé linéaire pour créer une partie du motif.

## Comprendre les dégradés linéaires CSS

Les dégradés linéaires CSS vous permettent de créer des transitions fluides entre deux couleurs ou plus sur une ligne droite. La fonction `linear-gradient()` prend un angle et une série de points de couleur (color stops) en tant que paramètres. Nous utiliserons cette technique pour créer les carrés de notre damier.

Suivez ces étapes :

1. Ouvrez le fichier `style.css`.

2. Modifions notre classe `.checkerboard` pour inclure le premier dégradé linéaire :

```css
.checkerboard {
  width: 240px;
  height: 240px;
  background-color: #fff;
  background-image: linear-gradient(
    45deg,
    #000 25%,
    transparent 25%,
    transparent 75%,
    #000 75%,
    #000
  );
  background-size: 60px 60px;
}
```

Permettez - moi d'expliquer ce que ce dégradé fait :

- `45deg` spécifie l'angle du dégradé
- `#000 25%` crée une couleur noire de 0 % à 25 % de l'espace disponible
- `transparent 25%` crée une couleur transparente à partir de 25 %
- `transparent 75%` maintient la couleur transparente jusqu'à 75 %
- `#000 75%` repasse à la couleur noire à 75 % et continue jusqu'à la fin
- `background-size: 60px 60px` définit la taille de chaque cellule de dégradé répétée

3. Enregistrez le fichier `style.css`.

4. Actualisez l'onglet **Web 8080** pour voir les modifications.

Vous devriez maintenant voir un motif commencer à se former, mais ce n'est pas encore un damier complet. Le premier dégradé crée seulement une partie du motif. Dans l'étape suivante, nous ajouterons un deuxième dégradé pour compléter le damier.
