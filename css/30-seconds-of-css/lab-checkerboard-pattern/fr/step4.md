# Compléter le motif de damier

Maintenant, ajoutons le deuxième dégradé linéaire pour compléter notre motif de damier et le rendre répétable sur tout l'élément.

1. Ouvrez à nouveau le fichier `style.css`.

2. Modifiez la classe `.checkerboard` pour inclure un deuxième dégradé linéaire qui créera le motif alterné :

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
    ), linear-gradient(-45deg, #000 25%, transparent 25%, transparent 75%, #000
        75%, #000);
  background-size: 60px 60px;
  background-repeat: repeat;
}
```

Ce que nous avons ajouté :

- Un deuxième `linear-gradient()` similaire au premier, mais avec un angle de `-45deg` pour créer le motif alterné
- La propriété `background-repeat: repeat` garantit que les motifs se répètent sur tout l'élément

La combinaison de ces deux dégradés à des angles différents crée le motif de damier classique. Le premier dégradé crée un ensemble de carrés diagonaux, tandis que le deuxième dégradé crée un autre ensemble qui comble les espaces vides.

3. Enregistrez le fichier `style.css`.

4. Actualisez l'onglet **Web 8080** pour voir le résultat final.

Vous devriez maintenant voir un motif de damier complet avec des carrés noirs et blancs alternés. Le motif devrait se répéter sur tout l'élément de 240 pixels de largeur et de hauteur.

## Fonctionnement du motif

L'effet de damier est créé par :

1. L'utilisation de deux dégradés linéaires avec des angles opposés (45deg et -45deg)
2. Chaque dégradé crée un motif de carrés noirs dans les coins
3. Les zones transparentes laissent apparaître le fond blanc
4. La propriété `background-size` contrôle la taille de chaque carré dans le motif
5. La propriété `background-repeat` fait répéter le motif sur tout l'élément

Cette technique démontre la puissance des dégradés CSS pour créer des motifs complexes sans avoir besoin de fichiers d'images, ce qui entraîne des temps de chargement plus rapides et une meilleure évolutivité.
