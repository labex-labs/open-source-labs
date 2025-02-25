# Max Profit K

## Problème

Étant donné une liste de prix d'actions pour chaque jour consécutif, déterminer les profits maximaux avec k transactions. Le problème demande de déterminer le profit maximal qui peut être obtenu à partir d'une liste de prix d'actions sur des jours consécutifs, en considérant k transactions. Les transactions consistent à acheter et à vendre des actions, et le nombre maximal de transactions est limité à k. La solution devrait retourner le profit maximal et les jours pour acheter et vendre.

## Exigences

Les exigences suivantes doivent être satisfaites pour résoudre le problème :

- k représente le nombre de transactions de vente.
- L'entrée prices est un tableau d'entiers.
- Les entrées peuvent ne pas être valides.
- Si les prix diminuent tous et qu'il n'y a pas d'occasion de faire un profit, la solution devrait retourner 0.
- La sortie devrait être le profit maximal et les jours pour acheter et vendre.
- La solution devrait tenir dans la mémoire.

## Utilisation de l'exemple

Les exemples suivants illustrent l'utilisation de la solution :

- Prix : None ou k : None -> None
- Prix : [] ou k <= 0 -> []
- Prix : [0, -1, -2, -3, -4, -5]
  - (profit maximal, liste de transactions)
  - (0, [])
- Prix : [2, 5, 7, 1, 4, 3, 1, 3] k : 3
  - (profit maximal, liste de transactions)
  - (10, [Type.SELL jour : 7 prix : 3,
    Type.BUY jour : 6 prix : 1,
    Type.SELL jour : 4 prix : 4,
    Type.BUY jour : 3 prix : 1,
    Type.SELL jour : 2 prix : 7,
    Type.BUY jour : 0 prix : 2])
