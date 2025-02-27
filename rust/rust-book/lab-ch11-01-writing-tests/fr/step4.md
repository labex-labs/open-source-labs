# Vérifier l'égalité avec les macros assert_eq! et assert_ne!

Un moyen courant de vérifier la fonctionnalité est de tester l'égalité entre le résultat du code à tester et la valeur que vous attendez que le code renvoie. Vous pourriez faire cela en utilisant la macro `assert!` et en lui passant une expression utilisant l'opérateur `==`. Cependant, ce test est si courant que la bibliothèque standard fournit une paire de macros - `assert_eq!` et `assert_ne!` - pour effectuer ce test de manière plus pratique. Ces macros comparent deux arguments pour l'égalité ou l'inégalité, respectivement. Elles afficheront également les deux valeurs si l'assertion échoue, ce qui facilite la compréhension _pourquoi_ le test a échoué ; en revanche, la macro `assert!` indique seulement qu'elle a obtenu une valeur `false` pour l'expression `==`, sans afficher les valeurs qui ont entraîné la valeur `false`.

Dans la liste 11-7, nous écrivons une fonction nommée `add_two` qui ajoute `2` à son paramètre, puis nous testons cette fonction en utilisant la macro `assert_eq!`.

Nom de fichier : `src/lib.rs`

```rust
pub fn add_two(a: i32) -> i32 {
    a + 2
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn it_adds_two() {
        assert_eq!(4, add_two(2));
    }
}
```

Liste 11-7 : Test de la fonction `add_two` en utilisant la macro `assert_eq!`

Vérifions qu'elle passe!

    exécution d'un test
    test tests::it_adds_two... ok

    résultat du test : ok. 1 passé ; 0 échoué ; 0 ignoré ; 0 mesuré ; 0
    filtré ; terminé en 0,00 s

Nous passons `4` comme argument à `assert_eq!`, qui est égal au résultat de l'appel à `add_two(2)`. La ligne pour ce test est `test tests::it_adds_two... ok`, et le texte `ok` indique que notre test a réussi!

Introduisons une erreur dans notre code pour voir à quoi ressemble `assert_eq!` lorsqu'il échoue. Changeons l'implémentation de la fonction `add_two` pour qu'elle ajoute `3` au lieu de `2` :

```rust
pub fn add_two(a: i32) -> i32 {
    a + 3
}
```

Exécutez les tests à nouveau :

    exécution d'un test
    test tests::it_adds_two... FAILED

    échecs :

    ---- tests::it_adds_two sortie standard ----
    1 thread'main' a généré une erreur à 'assertion failed: `(left == right)`
    2   left: `4`,
    3  right: `5`', src/lib.rs:11:9
    note : exécutez avec la variable d'environnement `RUST_BACKTRACE=1` pour afficher
    une trace de pile

    échecs :
        tests::it_adds_two

    résultat du test : FAILED. 0 passé ; 1 échoué ; 0 ignoré ; 0 mesuré ; 0
    filtré ; terminé en 0,00 s

Notre test a détecté l'erreur! Le test `it_adds_two` a échoué, et le message nous indique que l'assertion qui a échoué était `assertion failed: `(left == right)\``[1] et quelles étaient les valeurs de `left`[2] et `right`[3]. Ce message nous aide à commencer le débogage : l'argument `left`était`4`mais l'argument`right`, où nous avions `add_two(2)`, était `5`. Vous pouvez imaginer que cela serait particulièrement utile lorsque nous avons beaucoup de tests en cours.

Notez que dans certains langages et frameworks de test, les paramètres des fonctions d'assertion d'égalité sont appelés `expected` et `actual`, et l'ordre dans lequel nous spécifions les arguments compte. Cependant, en Rust, ils sont appelés `left` et `right`, et l'ordre dans lequel nous spécifions la valeur que nous attendons et la valeur que le code produit n'a pas d'importance. Nous pourrions écrire l'assertion dans ce test comme `assert_eq!(add_two(2), 4)`, ce qui résulterait du même message d'échec qui affiche `assertion failed: `(left == right)\`\`.

La macro `assert_ne!` passera si les deux valeurs que nous lui donnons ne sont pas égales et échouera si elles sont égales. Cette macro est le plus utile dans les cas où nous ne sommes pas sûrs de ce que sera une valeur, mais que nous savons ce que la valeur ne devrait certainement _pas_ être. Par exemple, si nous testons une fonction qui est garantie de modifier son entrée d'une certaine manière, mais que la manière dont l'entrée est modifiée dépend du jour de la semaine où nous exécutons nos tests, le meilleur élément à affirmer pourrait être que la sortie de la fonction n'est pas égale à l'entrée.

Sous le capot, les macros `assert_eq!` et `assert_ne!` utilisent respectivement les opérateurs `==` et `!=`. Lorsque les assertions échouent, ces macros affichent leurs arguments en utilisant le formattage de débogage, ce qui signifie que les valeurs comparées doivent implémenter les traits `PartialEq` et `Debug`. Tous les types primitifs et la plupart des types de la bibliothèque standard implémentent ces traits. Pour les structs et les énumérations que vous définissez vous-même, vous devrez implémenter `PartialEq` pour affirmer l'égalité de ces types. Vous devrez également implémenter `Debug` pour afficher les valeurs lorsque l'assertion échoue. Étant donné que les deux traits sont des traits dérivables, comme mentionné dans la liste 5-12, cela est généralement aussi simple que d'ajouter l'annotation `#[derive(PartialEq, Debug)]` à votre définition de struct ou d'énumération. Consultez l'annexe C pour plus de détails sur ces traits dérivables et d'autres.
