# Hanoï

## Problème

Votre tâche est d'implémenter les Tours d'Hanoï avec 3 tours et N disques. Le but est de déplacer tous les disques de la première tour vers la troisième tour, en respectant les règles simples suivantes :

1. Seul un disque peut être déplacé à la fois.
2. Chaque mouvement consiste à prendre le disque supérieur d'un des empilements et à le placer au-dessus d'un autre empilement ou sur une tige vide.
3. Aucun disque ne peut être placé au-dessus d'un disque plus petit.

## Exigences

Pour résoudre ce problème, vous devez répondre aux exigences suivantes :

- Vous devriez avoir une classe pile qui peut être utilisée pour ce problème.
- Vous devriez valider les entrées avant de les traiter.
- Vous devriez vous assurer que le programme s'adapte à la mémoire.

## Utilisation exemple

Voici quelques exemples de comportement attendu du programme :

- Si il n'y a pas de tours, une exception devrait être levée.
- Si il n'y a pas de disques, le programme devrait renvoyer None.
- Si il n'y a qu'un disque, le programme devrait le déplacer de la première tour vers la troisième tour.
- Si il y a 2 disques ou plus, le programme devrait les déplacer de la première tour vers la troisième tour, en respectant les règles mentionnées ci-dessus.
