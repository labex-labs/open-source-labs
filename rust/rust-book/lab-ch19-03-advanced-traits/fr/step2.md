# Types associées

Les _types associés_ relient un type générique à un trait de sorte que les définitions de méthodes de trait puissent utiliser ces types génériques dans leurs signatures. L'implémentateur d'un trait spécifiera le type concret à utiliser au lieu du type générique pour une implémentation particulière. De cette manière, nous pouvons définir un trait qui utilise certains types sans avoir besoin de savoir exactement quels sont ces types avant que le trait ne soit implémenté.

Nous avons décrit la plupart des fonctionnalités avancées de ce chapitre comme étant rarement nécessaires. Les types associés se situent au milieu : ils sont utilisés moins fréquemment que les fonctionnalités expliquées dans le reste du livre, mais plus fréquemment que de nombreuses autres fonctionnalités discutées dans ce chapitre.

Un exemple de trait avec un type associé est le trait `Iterator` fourni par la bibliothèque standard. Le type associé est nommé `Item` et représente le type des valeurs sur lesquelles itère le type implémentant le trait `Iterator`. La définition du trait `Iterator` est comme montrée dans la Liste 19-12.

```rust
pub trait Iterator {
    type Item;

    fn next(&mut self) -> Option<Self::Item>;
}
```

Liste 19-12 : La définition du trait `Iterator` qui a un type associé `Item`

Le type `Item` est un type générique, et la définition de la méthode `next` montre qu'elle renverra des valeurs de type `Option<Self::Item>`. Les implémentateurs du trait `Iterator` spécifieront le type concret pour `Item`, et la méthode `next` renverra une `Option` contenant une valeur de ce type concret.

Les types associés peuvent sembler être un concept similaire aux génériques, en ce sens que les derniers nous permettent de définir une fonction sans spécifier quels types elle peut gérer. Pour examiner la différence entre les deux concepts, nous allons considérer une implémentation du trait `Iterator` sur un type nommé `Counter` qui spécifie que le type `Item` est `u32` :

Nom de fichier : `src/lib.rs`

```rust
impl Iterator for Counter {
    type Item = u32;

    fn next(&mut self) -> Option<Self::Item> {
        --snip--
```

Cette syntaxe semble comparable à celle des génériques. Alors pourquoi ne pas simplement définir le trait `Iterator` avec des génériques, comme montré dans la Liste 19-13?

```rust
pub trait Iterator<T> {
    fn next(&mut self) -> Option<T>;
}
```

Liste 19-13 : Une définition hypothétique du trait `Iterator` utilisant des génériques

La différence est que lorsqu'on utilise des génériques, comme dans la Liste 19-13, nous devons annoter les types dans chaque implémentation ; car nous pouvons également implémenter `Iterator<``String``> pour Counter` ou tout autre type, nous pourrions avoir plusieurs implémentations de `Iterator` pour `Counter`. En d'autres termes, lorsqu'un trait a un paramètre générique, il peut être implémenté pour un type plusieurs fois, en changeant les types concret des paramètres de type générique à chaque fois. Lorsque nous utilisons la méthode `next` sur `Counter`, nous devons fournir des annotations de type pour indiquer quelle implémentation de `Iterator` nous voulons utiliser.

Avec les types associés, nous n'avons pas besoin d'annoter les types car nous ne pouvons pas implémenter un trait pour un type plusieurs fois. Dans la Liste 19-12 avec la définition qui utilise des types associés, nous ne pouvons choisir le type de `Item` qu'une seule fois car il ne peut y avoir qu'une seule `impl Iterator for Counter`. Nous n'avons pas besoin de spécifier que nous voulons un itérateur de valeurs de type `u32` partout où nous appelons `next` sur `Counter`.

Les types associés deviennent également partie du contrat du trait : les implémentateurs du trait doivent fournir un type pour remplacer le type générique associé. Les types associés ont souvent un nom qui décrit la manière dont le type sera utilisé, et il est une bonne pratique de documenter le type associé dans la documentation de l'API.
