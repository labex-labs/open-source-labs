# Strings Are Not So Simple

Pour résumer, les chaînes de caractères sont complexes. Différentes langues de programmation font des choix différents quant à la manière de présenter cette complexité au programmeur. Rust a choisi de faire du bon traitement des données `String` le comportement par défaut pour tous les programmes Rust, ce qui signifie que les programmeurs doivent réfléchir davantage au traitement des données UTF-8 dès le départ. Ce compromis expose davantage la complexité des chaînes de caractères que ne le fait apparaître d'autres langues de programmation, mais cela vous empêche d'avoir à gérer des erreurs liées à des caractères non ASCII plus tard dans votre cycle de développement.

La bonne nouvelle est que la bibliothèque standard offre beaucoup de fonctionnalités basées sur les types `String` et `&str` pour aider à gérer correctement ces situations complexes. N'oubliez pas de consulter la documentation pour des méthodes utiles telles que `contains` pour effectuer une recherche dans une chaîne et `replace` pour substituer des parties d'une chaîne par une autre chaîne.

Passons à quelque chose un peu moins complexe : les tableaux de hachage!
