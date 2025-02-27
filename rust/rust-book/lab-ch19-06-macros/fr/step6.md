# Macros ressemblant à des attributs

Les macros ressemblant à des attributs sont similaires aux macros personnalisées `derive`, mais au lieu de générer du code pour l'attribut `derive`, elles vous permettent de créer de nouveaux attributs. Elles sont également plus flexibles : `derive` ne fonctionne que pour les structs et les enums ; les attributs peuvent également être appliqués à d'autres éléments, tels que les fonctions. Voici un exemple d'utilisation d'une macro ressemblant à un attribut. Disons que vous avez un attribut nommé `route` qui annote les fonctions lorsqu'elles sont utilisées avec un framework d'application web :

```rust
#[route(GET, "/")]
fn index() {
```

Cet attribut `#[route]` serait défini par le framework comme une macro procédurale. La signature de la fonction de définition de la macro serait la suivante :

    #[proc_macro_attribute]
    pub fn route(
        attr: TokenStream,
        item: TokenStream
    ) -> TokenStream {

Ici, nous avons deux paramètres de type `TokenStream`. Le premier est pour le contenu de l'attribut : la partie `GET, "/"`. Le second est le corps de l'élément auquel l'attribut est attaché : dans ce cas, `fn index() {}` et le reste du corps de la fonction.

Autrement, les macros ressemblant à des attributs fonctionnent de la même manière que les macros personnalisées `derive` : vous créez une crate avec le type de crate `proc-macro` et vous implémentez une fonction qui génère le code que vous voulez!
