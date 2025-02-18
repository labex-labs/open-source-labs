# Updating a Hash Map (Mise à jour d'une table de hachage)

Bien que le nombre de paires clé - valeur puisse augmenter, chaque clé unique ne peut avoir qu'une seule valeur associée à la fois (mais pas l'inverse : par exemple, tant l'équipe Bleue que l'équipe Jaune pourraient avoir la valeur `10` stockée dans la table de hachage `scores`).

Lorsque vous souhaitez modifier les données dans une table de hachage, vous devez décider comment gérer le cas où une clé a déjà une valeur assignée. Vous pouvez remplacer l'ancienne valeur par la nouvelle, en ignorant complètement l'ancienne valeur. Vous pouvez conserver l'ancienne valeur et ignorer la nouvelle, en ajoutant la nouvelle valeur seulement si la clé _n'a pas_ déjà de valeur. Ou vous pouvez combiner l'ancienne valeur et la nouvelle valeur. Voyons comment faire chacun de ces cas!
