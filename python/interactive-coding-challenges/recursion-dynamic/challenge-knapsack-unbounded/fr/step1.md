# Sac à dos illimité

## Problème

Étant donné un sac à dos avec une capacité totale de poids et une liste d'objets ayant un poids w(i) et une valeur v(i), déterminer la valeur totale maximale que vous pouvez transporter. Les objets peuvent être sélectionnés plusieurs fois.

## Exigences

Pour résoudre le problème du sac à dos illimité, les exigences suivantes doivent être satisfaites :

- Les objets peuvent être remplacés une fois qu'ils sont placés dans le sac à dos.
- Un objet ne peut pas être divisé.
- Les objets d'entrée ne peuvent pas avoir un poids ou une valeur de 0.
- Seule la valeur totale doit être renvoyée, pas les objets qui composent la valeur totale maximale.
- Les entrées peuvent ne pas être valides, donc une validation est requise.
- Les entrées sont triées par rapport à la valeur/poids.
- Les contraintes de mémoire ne sont pas un problème.

## Utilisation exemple

Le problème du sac à dos illimité peut être utilisé dans diverses situations, telles que l'allocation de ressources et l'optimisation du portefeuille financier. Voici quelques exemples de son utilisation :

- Si le poids total ou les objets sont nuls, une exception doit être levée.
- Si le poids total ou les objets sont égaux à 0, le résultat doit être 0.
- Pour un cas général, supposons que le poids total est de 8 et les objets sont les suivants :

  | v   | w   |
  | --- | --- |
  | 0   | 0   |
  | 1   | 1   |
  | 3   | 2   |
  | 7   | 4   |

  La valeur maximale qui peut être transportée est de 14.
