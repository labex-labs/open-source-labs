# Introduction

Dans ce laboratoire, nous explorons l'annotation des durées de vie dans les méthodes de traits, qui est similaire aux fonctions. Cela implique également d'annoter les durées de vie dans le bloc `impl`. Le code fourni montre un exemple où une structure `Borrowed` a une annotation de durée de vie, et le trait `Default` est implémenté pour elle en utilisant la durée de vie annotée. La fonction principale crée ensuite une instance de `Borrowed` en utilisant la méthode `Default::default()`, mettant en évidence l'utilisation des durées de vie dans les méthodes de traits.

> **Note** : Si le laboratoire ne spécifie pas de nom de fichier, vous pouvez utiliser n'importe quel nom de fichier que vous voulez. Par exemple, vous pouvez utiliser `main.rs`, le compiler et l'exécuter avec `rustc main.rs &&./main`.
