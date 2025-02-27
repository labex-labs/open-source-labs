# Macros ressemblant à des fonctions

Les macros ressemblant à des fonctions définissent des macros qui ressemblent à des appels de fonction. De manière similaire aux macros `macro_rules!`, elles sont plus flexibles que les fonctions ; par exemple, elles peuvent prendre un nombre inconnu d'arguments. Cependant, les macros `macro_rules!` ne peuvent être définies que en utilisant la syntaxe similaire à `match` que nous avons discutée dans "Macros déclaratives avec macro_rules! pour la métaprogrammation générale". Les macros ressemblant à des fonctions prennent un paramètre `TokenStream`, et leur définition manipule ce `TokenStream` à l'aide de code Rust comme le font les autres deux types de macros procédurales. Un exemple de macro ressemblant à une fonction est une macro `sql!` qui pourrait être appelée comme ceci :

```rust
let sql = sql!(SELECT * FROM posts WHERE id=1);
```

Cette macro analyserait l'instruction SQL à l'intérieur d'elle et vérifierait qu'elle est syntaxiquement correcte, ce qui est un traitement bien plus complexe que ce que peut faire une macro `macro_rules!`. La macro `sql!` serait définie comme ceci :

```rust
#[proc_macro]
pub fn sql(input: TokenStream) -> TokenStream {
```

Cette définition est similaire à la signature de la macro personnalisée `derive` : nous recevons les jetons qui se trouvent à l'intérieur des parenthèses et renvoyons le code que nous voulions générer.
