# Utilisation du motif newtype pour la sécurité et l'abstraction de type

> Note : Cette section suppose que vous avez lu la section précédente "Utilisation du motif newtype pour implémenter des traits externes".

Le motif newtype est également utile pour des tâches autres que celles que nous avons discutées jusqu'à présent, notamment pour contraindre statiquement les valeurs à ne jamais être confondues et pour indiquer les unités d'une valeur. Vous avez vu un exemple d'utilisation de newtypes pour indiquer les unités dans la liste 19-15 : rappelez-vous que les structs `Millimeters` et `Meters` ont encapsulé des valeurs `u32` dans un newtype. Si nous écrivons une fonction avec un paramètre de type `Millimeters`, nous ne pourrons pas compiler un programme qui essayerait accidentellement d'appeler cette fonction avec une valeur de type `Meters` ou une simple `u32`.

Nous pouvons également utiliser le motif newtype pour dissimuler certains détails d'implémentation d'un type : le nouveau type peut exposer une API publique différente de l'API du type interne privé.

Les newtypes peuvent également cacher l'implémentation interne. Par exemple, nous pourrions fournir un type `People` pour encapsuler un `HashMap<i32, String>` qui stocke l'identifiant d'une personne associé à son nom. Le code utilisant `People` n'interagirait que avec l'API publique que nous fournissons, telle qu'une méthode pour ajouter une chaîne de nom à la collection `People` ; ce code n'aurait pas besoin de savoir que nous attribuons un identifiant `i32` aux noms en interne. Le motif newtype est un moyen léger d'atteindre l'encapsulation pour cacher les détails d'implémentation, que nous avons discuté dans "L'encapsulation qui cache les détails d'implémentation".
