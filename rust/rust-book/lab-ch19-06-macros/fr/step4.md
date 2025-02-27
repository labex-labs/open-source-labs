# Macros procédurales pour générer du code à partir d'attributs

La deuxième forme de macros est la macro procédurale, qui fonctionne plus comme une fonction (et est un type de procédure). Les _macros procédurales_ acceptent du code en entrée, opèrent sur ce code et produisent du code en sortie, plutôt que de correspondre à des motifs et de remplacer le code par d'autres code comme le font les macros déclaratives. Les trois types de macros procédurales sont les macros personnalisées `derive`, les macros ressemblant à des attributs et les macros ressemblant à des fonctions, et toutes fonctionnent de manière similaire.

Lors de la création de macros procédurales, les définitions doivent résider dans leur propre crate avec un type de crate spécial. Cela est dû à des raisons techniques complexes que nous espérons éliminer dans l'avenir. Dans l'annexe 19-29, nous montrons comment définir une macro procédurale, où `some_attribute` est un emplacement réservé pour utiliser une variété spécifique de macro.

Nom de fichier : `src/lib.rs`

```rust
use proc_macro::TokenStream;

#[some_attribute]
pub fn some_name(input: TokenStream) -> TokenStream {
}
```

Annexe 19-29 : Exemple de définition d'une macro procédurale

La fonction qui définit une macro procédurale prend un `TokenStream` en entrée et produit un `TokenStream` en sortie. Le type `TokenStream` est défini par la crate `proc_macro` qui est incluse avec Rust et représente une séquence de jetons. C'est le cœur de la macro : le code source sur lequel la macro opère constitue l'entrée `TokenStream`, et le code produit par la macro est la sortie `TokenStream`. La fonction a également un attribut attaché à elle qui spécifie le type de macro procédurale que nous créons. Nous pouvons avoir plusieurs types de macros procédurales dans la même crate.

Examillons les différents types de macros procédurales. Nous commencerons par une macro personnalisée `derive` puis expliquerons les petites différences qui distinguent les autres formes.
