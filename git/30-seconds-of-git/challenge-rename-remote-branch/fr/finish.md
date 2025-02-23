# Résumé

Renommer une branche distante en Git consiste à renommer la branche à la fois localement et sur le distant. Vous pouvez utiliser la commande `git branch -m <ancien-nom> <nouveau-nom>` pour renommer la branche locale et les commandes `git push origin --delete <ancien-nom>` et `git push origin -u <nouveau-nom>` pour supprimer l'ancienne branche distante et définir la nouvelle branche distante, respectivement.
