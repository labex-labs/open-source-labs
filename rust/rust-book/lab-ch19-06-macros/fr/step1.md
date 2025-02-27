# Macros

Nous avons utilisé des macros telles que `println!` tout au long de ce livre, mais nous n'avons pas complètement exploré ce qu'est une macro et comment elle fonctionne. Le terme _macro_ désigne une famille de fonctionnalités en Rust : les macros _déclaratives_ avec `macro_rules!` et trois types de macros _procédurales_ :

- Les macros personnalisées `#[derive]` qui spécifient le code ajouté avec l'attribut `derive` utilisé sur des structs et des énumérations
- Les macros ressemblant à des attributs qui définissent des attributs personnalisés utilisables sur n'importe quel élément
- Les macros ressemblant à des fonctions qui ressemblent à des appels de fonction mais opèrent sur les jetons spécifiés comme leur argument

Nous allons parler de chacun de ces points tour à tour, mais tout d'abord, regardons pourquoi nous avons besoin de macros même si nous avons déjà des fonctions.
