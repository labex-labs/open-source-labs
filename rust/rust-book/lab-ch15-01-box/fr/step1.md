# Utiliser Box`<T>` pour pointer vers des données sur le tas

Le pointeur intelligent le plus simple est une _boîte_, dont le type est écrit `Box<T>`. Les boîtes vous permettent de stocker des données sur le tas plutôt que sur la pile. Ce qui reste sur la pile est le pointeur vers les données du tas. Consultez le Chapitre 4 pour revoir la différence entre la pile et le tas.

Les boîtes n'ont pas de surcoût de performance, autre que le fait de stocker leurs données sur le tas au lieu de sur la pile. Mais elles n'ont pas non plus de nombreuses capacités supplémentaires. Vous les utiliserez le plus souvent dans les situations suivantes :

- Lorsque vous avez un type dont la taille ne peut pas être connue à la compilation et que vous voulez utiliser une valeur de ce type dans un contexte qui nécessite une taille exacte
- Lorsque vous avez une grande quantité de données et que vous voulez transférer la propriété tout en vous assurant que les données ne seront pas copiées lors de ce transfert
- Lorsque vous voulez posséder une valeur et que vous vous souciez seulement du fait qu'il s'agit d'un type qui implémente un trait particulier plutôt que d'un type spécifique

Nous démontrerons la première situation dans "Autoriser les types récursifs avec des boîtes". Dans le second cas, le transfert de la propriété d'une grande quantité de données peut prendre beaucoup de temps car les données sont copiées sur la pile. Pour améliorer les performances dans cette situation, nous pouvons stocker la grande quantité de données sur le tas dans une boîte. Ensuite, seule la petite quantité de données de pointeur est copiée sur la pile, tandis que les données qu'elle référence restent au même endroit sur le tas. Le troisième cas est connu sous le nom d'_objet de trait_, et "Utiliser des objets de trait qui autorisent des valeurs de différents types" est consacré à ce sujet. Donc, ce que vous apprenez ici, vous le réappliquerez dans cette section!
