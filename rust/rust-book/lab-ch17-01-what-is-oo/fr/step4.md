# L'héritage comme système de types et comme partage de code

L'_héritage_ est un mécanisme grâce auquel un objet peut hériter d'éléments de la définition d'un autre objet, gagnant ainsi les données et le comportement de l'objet parent sans avoir à les définir à nouveau.

Si un langage doit avoir l'héritage pour être orienté objet, alors Rust n'est pas un tel langage. Il n'y a aucun moyen de définir un struct qui hérite des champs et des implémentations de méthodes du struct parent sans utiliser une macro.

Cependant, si vous êtes habitué à avoir l'héritage dans votre outilbox de programmation, vous pouvez utiliser d'autres solutions en Rust, selon votre raison pour laquelle vous avez opté pour l'héritage en premier lieu.

Vous choisiriez l'héritage pour deux raisons principales. La première est la réutilisation du code : vous pouvez implémenter un comportement particulier pour un type, et l'héritage vous permet de réutiliser cette implémentation pour un autre type. Vous pouvez le faire d'une manière limitée dans le code Rust en utilisant les implémentations de méthodes par défaut de traits, que vous avez vue dans le Listing 10-14 lorsque nous avons ajouté une implémentation par défaut de la méthode `summarize` sur le trait `Summary`. Tout type implémentant le trait `Summary` aurait la méthode `summarize` disponible sans aucun code supplémentaire. Cela est similaire à une classe mère ayant une implémentation d'une méthode et une classe enfant héritière ayant également l'implémentation de la méthode. Nous pouvons également remplacer l'implémentation par défaut de la méthode `summarize` lorsque nous implémentons le trait `Summary`, ce qui est similaire à une classe enfant qui remplace l'implémentation d'une méthode héritée d'une classe mère.

L'autre raison d'utiliser l'héritage est liée au système de types : pour permettre à un type enfant d'être utilisé dans les mêmes emplacements que le type parent. Cela s'appelle également _polymorphisme_, ce qui signifie que vous pouvez substituer plusieurs objets les uns aux autres à l'exécution s'ils partagent certaines caractéristiques.

> **Polymorphisme**
>
> Pour de nombreuses personnes, le polymorphisme est synonyme d'héritage. Mais en fait, c'est un concept plus général qui désigne le code qui peut fonctionner avec des données de plusieurs types. Pour l'héritage, ces types sont généralement des sous-classes.
>
> Rust utilise plutôt les génériques pour abstraire sur différents types possibles et les contraintes de traits pour imposer des contraintes sur ce que ces types doivent fournir. Cela s'appelle parfois _polymorphisme paramétrique borné_.

L'héritage est tombé en disgrâce récemment en tant que solution de conception de programmation dans de nombreux langages de programmation car il est souvent exposé au risque de partager plus de code que nécessaire. Les sous-classes ne devraient pas toujours partager toutes les caractéristiques de leur classe parent, mais le feront avec l'héritage. Cela peut rendre la conception d'un programme moins flexible. Il introduit également la possibilité d'appeler des méthodes sur des sous-classes qui n'ont pas de sens ou qui entraînent des erreurs car les méthodes ne s'appliquent pas à la sous-classe. En outre, certains langages ne permettent que l'héritage unique (ce qui signifie qu'une sous-classe ne peut hériter que d'une seule classe), limitant encore plus la flexibilité de la conception d'un programme.

Pour ces raisons, Rust adopte une approche différente en utilisant des objets de trait au lieu de l'héritage. Regardons comment les objets de trait permettent le polymorphisme en Rust.
