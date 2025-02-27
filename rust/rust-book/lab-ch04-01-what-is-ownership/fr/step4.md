# Le type String

Pour illustrer les règles de propriété, nous avons besoin d'un type de données plus complexe que ceux que nous avons abordés dans "Types de données". Les types abordés précédemment ont une taille connue, peuvent être stockés sur la pile et dépilés lorsqu'ils sortent de portée, et peuvent être rapidement et facilement copiés pour créer une nouvelle instance indépendante si une autre partie du code a besoin d'utiliser la même valeur dans une portée différente. Mais nous voulons examiner les données stockées sur le tas et explorer la manière dont Rust sait quand nettoyer ces données, et le type `String` est un excellent exemple.

Nous nous concentrerons sur les parties de `String` qui sont liées à la propriété. Ces aspects s'appliquent également à d'autres types de données complexes, que ce soit ceux fournis par la bibliothèque standard ou ceux que vous avez créés. Nous aborderons `String` plus en détail au chapitre 8.

Nous avons déjà vu les littéraux de chaîne, où une valeur de chaîne est codée en dur dans notre programme. Les littéraux de chaîne sont pratiques, mais ne conviennent pas à toutes les situations dans lesquelles nous pouvons vouloir utiliser du texte. Une raison est qu'ils sont immuables. Une autre est que pas toutes les valeurs de chaîne peuvent être connues lorsque nous écrivons notre code : par exemple, que se passe-t-il si nous voulons prendre l'entrée de l'utilisateur et la stocker? Pour ces situations, Rust a un deuxième type de chaîne, `String`. Ce type gère les données allouées sur le tas et est donc capable de stocker une quantité de texte inconnue pour nous au moment de la compilation. Vous pouvez créer une `String` à partir d'un littéral de chaîne en utilisant la fonction `from`, comme ceci :

```rust
let s = String::from("hello");
```

L'opérateur double point `::` nous permet de qualifier cette fonction `from` particulière sous le type `String` plutôt que d'utiliser un nom comme `string_from`. Nous aborderons cette syntaxe plus en détail dans "La syntaxe des méthodes", et lorsque nous parlerons de l'espace de noms avec les modules dans "Chemins pour faire référence à un élément dans l'arbre de modules".

Ce type de chaîne _peut_ être modifié :

```rust
let mut s = String::from("hello");

s.push_str(", world!"); // push_str() ajoute un littéral à une chaîne

println!("{s}"); // Cela affichera `hello, world!`
```

Alors, quelle est la différence ici? Pourquoi `String` peut-il être modifié tandis que les littéraux ne le peuvent pas? La différence réside dans la manière dont ces deux types gèrent la mémoire.
