# Lifetime Annotations in Method Definitions

Lorsque nous implémentons des méthodes sur un struct avec des durées de vie, nous utilisons la même syntaxe que celle des paramètres de type générique montrée dans la Liste 10-11. Où nous déclarons et utilisons les paramètres de durée de vie dépend de leur relation avec les champs du struct ou les paramètres et valeurs de retour de la méthode.

Les noms de durées de vie pour les champs du struct doivent toujours être déclarés après le mot clé `impl` puis utilisés après le nom du struct car ces durées de vie font partie du type du struct.

Dans les signatures de méthodes à l'intérieur du bloc `impl`, les références peuvent être liées à la durée de vie des références dans les champs du struct, ou elles peuvent être indépendantes. De plus, les règles d'élision de durée de vie font souvent en sorte qu'aucune annotation de durée de vie n'est nécessaire dans les signatures de méthodes. Regardons quelques exemples en utilisant le struct nommé `ImportantExcerpt` que nous avons défini dans la Liste 10-24.

Tout d'abord, nous utiliserons une méthode nommée `level` dont le seul paramètre est une référence à `self` et dont la valeur de retour est un `i32`, qui n'est pas une référence à quoi que ce soit :

```rust
impl<'a> ImportantExcerpt<'a> {
    fn level(&self) -> i32 {
        3
    }
}
```

La déclaration du paramètre de durée de vie après `impl` et son utilisation après le nom du type est requise, mais nous n'avons pas besoin d'annoter la durée de vie de la référence à `self` en raison de la première règle d'élision.

Voici un exemple où la troisième règle d'élision de durée de vie s'applique :

```rust
impl<'a> ImportantExcerpt<'a> {
    fn announce_and_return_part(&self, announcement: &str) -> &str {
        println!("Attention please: {announcement}");
        self.part
    }
}
```

Il y a deux durées de vie d'entrée, donc Rust applique la première règle d'élision de durée de vie et attribue à `&self` et `announcement` leurs propres durées de vie. Ensuite, parce que l'un des paramètres est `&self`, le type de retour obtient la durée de vie de `&self`, et toutes les durées de vie ont été prises en compte.
