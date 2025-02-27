# Lifetime Annotations in Function Signatures

Pour utiliser des annotations de durée de vie dans les signatures de fonctions, nous devons déclarer les paramètres de _durée de vie_ génériques entre crochets angulaires, entre le nom de la fonction et la liste de paramètres, tout comme nous l'avons fait avec les paramètres de _type_ génériques.

Nous voulons que la signature exprime la contrainte suivante : la référence renvoyée sera valide aussi longtemps que les deux paramètres le seront. C'est la relation entre les durées de vie des paramètres et de la valeur de retour. Nous nommerons la durée de vie `'a` puis l'ajouterons à chaque référence, comme indiqué dans la Liste 10-21.

Nom de fichier : `src/main.rs`

```rust
fn longest<'a>(x: &'a str, y: &'a str) -> &'a str {
    if x.len() > y.len() {
        x
    } else {
        y
    }
}
```

Liste 10-21 : La définition de la fonction `longest` spécifiant que toutes les références dans la signature doivent avoir la même durée de vie `'a`

Ce code devrait compiler et produire le résultat que nous voulons lorsqu'on l'utilise avec la fonction `main` de la Liste 10-19.

La signature de la fonction indique désormais à Rust qu'au cours d'une certaine durée de vie `'a`, la fonction prend deux paramètres, qui sont tous deux des slices de chaîne de caractères qui existent au moins aussi longtemps que la durée de vie `'a`. La signature de la fonction indique également à Rust que la slice de chaîne de caractères renvoyée par la fonction existera au moins aussi longtemps que la durée de vie `'a`. En pratique, cela signifie que la durée de vie de la référence renvoyée par la fonction `longest` est la même que la plus courte des durées de vie des valeurs référencées par les arguments de la fonction. Ces relations sont celles que nous voulons que Rust utilise lors de l'analyse de ce code.

Rappelez-vous, lorsque nous spécifions les paramètres de durée de vie dans cette signature de fonction, nous ne changeons pas les durées de vie de toutes les valeurs passées en paramètre ou renvoyées. Au contraire, nous spécifions que le vérificateur d'emprunt devrait rejeter toutes les valeurs qui ne respectent pas ces contraintes. Notez que la fonction `longest` n'a pas besoin de savoir exactement combien de temps `x` et `y` existeront, seulement qu'un certain contexte peut être substitué à `'a` qui satisfait cette signature.

Lorsque l'on annote les durées de vie dans les fonctions, les annotations se trouvent dans la signature de la fonction, pas dans le corps de la fonction. Les annotations de durée de vie deviennent partie du contrat de la fonction, tout comme les types dans la signature. Le fait que les signatures de fonctions contiennent le contrat de durée de vie signifie que l'analyse effectuée par le compilateur Rust peut être plus simple. Si un problème se produit dans la manière dont une fonction est annotée ou appelée, les erreurs du compilateur peuvent pointer plus précisément vers la partie de notre code et les contraintes. Si, au lieu de cela, le compilateur Rust faisait plus d'inférences sur ce que nous pensions être les relations entre les durées de vie, le compilateur pourrait seulement être en mesure de pointer vers une utilisation de notre code à plusieurs étapes de la cause du problème.

Lorsque nous passons des références concrètes à `longest`, la durée de vie concrète qui est substituée à `'a` est la partie du contexte de `x` qui chevauche le contexte de `y`. En d'autres termes, la durée de vie générique `'a` obtiendra la durée de vie concrète qui est égale à la plus courte des durées de vie de `x` et `y`. Parce que nous avons annoté la référence renvoyée avec le même paramètre de durée de vie `'a`, la référence renvoyée sera également valide pour la durée de la plus courte des durées de vie de `x` et `y`.

Regardons comment les annotations de durée de vie restreignent la fonction `longest` en passant des références qui ont des durées de vie concrètes différentes. La Liste 10-22 est un exemple simple.

Nom de fichier : `src/main.rs`

```rust
fn main() {
    let string1 = String::from("long string is long");

    {
        let string2 = String::from("xyz");
        let result = longest(string1.as_str(), string2.as_str());
        println!("The longest string is {result}");
    }
}
```

Liste 10-22 : Utilisation de la fonction `longest` avec des références à des valeurs de type `String` qui ont des durées de vie concrètes différentes

Dans cet exemple, `string1` est valide jusqu'à la fin du contexte externe, `string2` est valide jusqu'à la fin du contexte interne, et `result` référence quelque chose qui est valide jusqu'à la fin du contexte interne. Exécutez ce code et vous verrez que le vérificateur d'emprunt l'approuve ; il compilera et affichera `The longest string is long string is long`.

Ensuite, essayons un exemple qui montre que la durée de vie de la référence dans `result` doit être la plus courte des deux arguments. Nous allons déplacer la déclaration de la variable `result` en dehors du contexte interne, mais laisser l'affectation de la valeur à la variable `result` à l'intérieur du contexte avec `string2`. Ensuite, nous déplacerons l'instruction `println!` qui utilise `result` en dehors du contexte interne, après que le contexte interne soit terminé. Le code de la Liste 10-23 ne compilera pas.

Nom de fichier : `src/main.rs`

```rust
fn main() {
    let string1 = String::from("long string is long");
    let result;
    {
        let string2 = String::from("xyz");
        result = longest(string1.as_str(), string2.as_str());
    }
    println!("The longest string is {result}");
}
```

Liste 10-23 : Tentative d'utilisation de `result` après que `string2` est sortie de portée

Lorsque nous essayons de compiler ce code, nous obtenons cette erreur :

```bash
error[E0597]: `string2` does not live long enough
 --> src/main.rs:6:44
  |
6 |         result = longest(string1.as_str(), string2.as_str());
  |                                            ^^^^^^^^^^^^^^^^ borrowed value
does not live long enough
7 |     }
  |     - `string2` dropped here while still borrowed
8 |     println!("The longest string is {result}");
  |                                      ------ borrow later used here
```

L'erreur montre que pour que `result` soit valide pour l'instruction `println!`, `string2` devrait être valide jusqu'à la fin du contexte externe. Rust le sait parce que nous avons annoté les durées de vie des paramètres et des valeurs de retour de la fonction en utilisant le même paramètre de durée de vie `'a`.

En tant qu'humains, nous pouvons examiner ce code et voir que `string1` est plus longue que `string2`, et donc, `result` contiendra une référence à `string1`. Parce que `string1` n'est pas sortie de portée encore, une référence à `string1` sera toujours valide pour l'instruction `println!`. Cependant, le compilateur ne peut pas voir que la référence est valide dans ce cas. Nous avons dit à Rust que la durée de vie de la référence renvoyée par la fonction `longest` est la même que la plus courte des durées de vie des références passées en paramètre. Par conséquent, le vérificateur d'emprunt interdit le code de la Liste 10-23 comme pouvant potentiellement avoir une référence invalide.

Essayez de concevoir d'autres expériences qui varient les valeurs et les durées de vie des références passées à la fonction `longest` et la manière dont la référence renvoyée est utilisée. Faites des hypothèses sur le fait que vos expériences passeront le vérificateur d'emprunt avant de compiler ; puis vérifiez si vous avez raison!
