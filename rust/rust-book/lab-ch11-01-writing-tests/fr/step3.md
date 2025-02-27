# Vérifier les résultats avec la macro assert!

La macro `assert!`, fournie par la bibliothèque standard, est utile lorsque vous voulez vous assurer qu'une certaine condition dans un test évalue à `true`. Nous donnons à la macro `assert!` un argument qui évalue à un booléen. Si la valeur est `true`, rien ne se passe et le test passe. Si la valeur est `false`, la macro `assert!` appelle `panic!` pour provoquer l'échec du test. Utiliser la macro `assert!` nous aide à vérifier que notre code fonctionne comme nous le souhaitons.

Dans la liste 5-15, nous avons utilisé une struct `Rectangle` et une méthode `can_hold`, qui sont répétées ici dans la liste 11-5. Plaçons ce code dans le fichier `src/lib.rs`, puis écrivons quelques tests pour cela en utilisant la macro `assert!`.

Nom de fichier : `src/lib.rs`

```rust
#[derive(Debug)]
struct Rectangle {
    width: u32,
    height: u32,
}

impl Rectangle {
    fn can_hold(&self, other: &Rectangle) -> bool {
        self.width > other.width && self.height > other.height
    }
}
```

Liste 11-5 : Utilisation de la struct `Rectangle` et de sa méthode `can_hold` du chapitre 5

La méthode `can_hold` renvoie un booléen, ce qui signifie qu'il s'agit d'un cas d'utilisation parfait pour la macro `assert!`. Dans la liste 11-6, nous écrivons un test qui exerce la méthode `can_hold` en créant une instance de `Rectangle` qui a une largeur de 8 et une hauteur de 7 et en affirmant qu'elle peut contenir une autre instance de `Rectangle` qui a une largeur de 5 et une hauteur de 1.

Nom de fichier : `src/lib.rs`

```rust
#[cfg(test)]
mod tests {
  1 use super::*;

    #[test]
  2 fn larger_can_hold_smaller() {
      3 let larger = Rectangle {
            width: 8,
            height: 7,
        };
        let smaller = Rectangle {
            width: 5,
            height: 1,
        };

      4 assert!(larger.can_hold(&smaller));
    }
}
```

Liste 11-6 : Un test pour `can_hold` qui vérifie si un rectangle plus grand peut effectivement contenir un rectangle plus petit

Notez que nous avons ajouté une nouvelle ligne dans le module `tests` : `use super::*;` \[1\]. Le module `tests` est un module normal qui suit les règles de visibilité habituelles que nous avons couvertes dans "Chemins pour faire référence à un élément dans l'arbre de modules". Comme le module `tests` est un module interne, nous devons amener le code à tester dans le module externe dans la portée du module interne. Nous utilisons un glob ici, de sorte que tout ce que nous définissons dans le module externe est disponible pour ce module `tests`.

Nous avons nommé notre test `larger_can_hold_smaller` \[2\], et nous avons créé les deux instances de `Rectangle` dont nous avons besoin \[3\]. Ensuite, nous avons appelé la macro `assert!` et lui avons passé le résultat de l'appel à `larger.can_hold(&smaller)` \[4\]. Cette expression devrait renvoyer `true`, de sorte que notre test devrait passer. Vérifions!

    exécution d'un test
    test tests::larger_can_hold_smaller... ok

    résultat du test : ok. 1 passé ; 0 échoué ; 0 ignoré ; 0 mesuré ; 0
    filtré ; terminé en 0,00 s

Il passe effectivement! Ajoutons un autre test, cette fois en affirmant qu'un rectangle plus petit ne peut pas contenir un rectangle plus grand :

Nom de fichier : `src/lib.rs`

```rust
#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn larger_can_hold_smaller() {
        --extrait--
    }

    #[test]
    fn smaller_cannot_hold_larger() {
        let larger = Rectangle {
            width: 8,
            height: 7,
        };
        let smaller = Rectangle {
            width: 5,
            height: 1,
        };

        assert!(!smaller.can_hold(&larger));
    }
}
```

Comme le résultat correct de la fonction `can_hold` dans ce cas est `false`, nous devons négater ce résultat avant de le passer à la macro `assert!`. En conséquence, notre test passera si `can_hold` renvoie `false` :

    exécution de 2 tests
    test tests::larger_can_hold_smaller... ok
    test tests::smaller_cannot_hold_larger... ok

    résultat du test : ok. 2 passés ; 0 échoués ; 0 ignorés ; 0 mesurés ; 0
    filtrés ; terminé en 0,00 s

Deux tests qui passent! Maintenant, voyons ce qui se passe avec nos résultats de test lorsque nous introduisons une erreur dans notre code. Nous allons modifier l'implémentation de la méthode `can_hold` en remplaçant le signe supérieur par un signe inférieur lorsqu'elle compare les largeurs :

    --extrait--

    impl Rectangle {
        fn can_hold(&self, other: &Rectangle) -> bool {
            self.width < other.width && self.height > other.height
        }
    }

Exécuter les tests produit maintenant ceci :

    exécution de 2 tests
    test tests::smaller_cannot_hold_larger... ok
    test tests::larger_can_hold_smaller... FAILED

    échecs :

    ---- tests::larger_can_hold_smaller sortie standard ----
    thread'main' a généré une erreur à 'assertion failed:
    larger.can_hold(&smaller)', src/lib.rs:28:9
    note : exécutez avec la variable d'environnement `RUST_BACKTRACE=1` pour afficher
    une trace de pile


    échecs :
        tests::larger_can_hold_smaller

    résultat du test : FAILED. 1 passé ; 1 échoué ; 0 ignoré ; 0 mesuré ; 0
    filtré ; terminé en 0,00 s

Nos tests ont détecté l'erreur! Comme `larger.width` est `8` et `smaller.width` est `5`, la comparaison des largeurs dans `can_hold` renvoie maintenant `false` : 8 n'est pas inférieur à 5.
