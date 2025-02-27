# Vérifier les panics avec should_panic

En plus de vérifier les valeurs de retour, il est important de vérifier que notre code gère les conditions d'erreur comme nous le souhaitons. Par exemple, considérons le type `Guess` que nous avons créé dans la liste 9-13. Autre code qui utilise `Guess` dépend de la garantie que les instances de `Guess` ne contiendront que des valeurs comprises entre 1 et 100. Nous pouvons écrire un test qui assure que l'essai de création d'une instance de `Guess` avec une valeur en dehors de cette plage provoque une panique.

Nous le faisons en ajoutant l'attribut `should_panic` à notre fonction de test. Le test passe si le code à l'intérieur de la fonction provoque une panique ; le test échoue si le code à l'intérieur de la fonction ne provoque pas de panique.

La liste 11-8 montre un test qui vérifie que les conditions d'erreur de `Guess::new` se produisent lorsque nous les attendons.

    // src/lib.rs
    pub struct Guess {
        value: i32,
    }

    impl Guess {
        pub fn new(value: i32) -> Guess {
            if value < 1 || value > 100 {
                panic!(
                    "Guess value must be between 1 and 100, got {}.",
                    value
                );
            }

            Guess { value }
        }
    }

    #[cfg(test)]
    mod tests {
        use super::*;

        #[test]
        #[should_panic]
        fn greater_than_100() {
            Guess::new(200);
        }
    }

Liste 11-8 : Vérification qu'une condition entraînera une panique!

Nous plaçons l'attribut `#[should_panic]` après l'attribut `#[test]` et avant la fonction de test à laquelle il s'applique. Voyons le résultat lorsque ce test passe :

    exécution d'un test
    test tests::greater_than_100 - devrait provoquer une panique... ok

    résultat du test : ok. 1 passé ; 0 échoué ; 0 ignoré ; 0 mesuré ; 0
    filtré ; terminé en 0,00 s

Cela semble bon! Maintenant, introduisons une erreur dans notre code en supprimant la condition selon laquelle la fonction `new` provoquera une panique si la valeur est supérieure à 100 :

    // src/lib.rs
    --extrait--

    impl Guess {
        pub fn new(value: i32) -> Guess {
            if value < 1 {
                panic!(
                    "Guess value must be between 1 and 100, got {}.",
                    value
                );
            }

            Guess { value }
        }
    }

Lorsque nous exécutons le test de la liste 11-8, il échouera :

    exécution d'un test
    test tests::greater_than_100 - devrait provoquer une panique... FAILED

    échecs :

    ---- tests::greater_than_100 sortie standard ----
    note : le test n'a pas provoqué de panique comme attendu

    échecs :
        tests::greater_than_100

    résultat du test : FAILED. 0 passé ; 1 échoué ; 0 ignoré ; 0 mesuré ; 0
    filtré ; terminé en 0,00 s

Dans ce cas, nous ne recevons pas un message très utile, mais en regardant la fonction de test, nous voyons qu'elle est annotée avec `#[should_panic]`. L'erreur que nous avons obtenue signifie que le code dans la fonction de test n'a pas entraîné de panique.

Les tests qui utilisent `should_panic` peuvent être imprécis. Un test `should_panic` passerait même si le test provoque une panique pour une raison différente de celle que nous attendions. Pour rendre les tests `should_panic` plus précis, nous pouvons ajouter un paramètre optionnel `expected` à l'attribut `should_panic`. Le harness de test s'assurera que le message d'erreur contient le texte fourni. Par exemple, considérez le code modifié de `Guess` dans la liste 11-9 où la fonction `new` provoque une panique avec des messages différents selon que la valeur est trop petite ou trop grande.

    // src/lib.rs
    --extrait--

    impl Guess {
        pub fn new(value: i32) -> Guess {
            if value < 1 {
                panic!(
                    "Guess value must be greater than or equal to 1, got {}.",
                    value
                );
            } else if value > 100 {
                panic!(
                    "Guess value must be less than or equal to 100, got {}.",
                    value
                );
            }

            Guess { value }
        }
    }

    #[cfg(test)]
    mod tests {
        use super::*;

        #[test]
        #[should_panic(expected = "less than or equal to 100")]
        fn greater_than_100() {
            Guess::new(200);
        }
    }

Liste 11-9 : Vérification d'une `panique!` avec un message de panique contenant une sous-chaîne spécifiée

Ce test passera car la valeur que nous avons placée dans le paramètre `expected` de l'attribut `should_panic` est une sous-chaîne du message avec lequel la fonction `Guess::new` provoque une panique. Nous aurions pu spécifier le message de panique entier que nous attendons, qui dans ce cas serait `Guess value must be less than or equal to 100, got 200`. Ce que vous choisissez de spécifier dépend de la partie du message de panique qui est unique ou dynamique et de la précision que vous voulez donner à votre test. Dans ce cas, une sous-chaîne du message de panique suffit pour s'assurer que le code dans la fonction de test exécute le cas `else if value > 100`.

Pour voir ce qui se passe lorsqu'un test `should_panic` avec un message `expected` échoue, introduisons à nouveau une erreur dans notre code en échangeant les corps des blocs `if value < 1` et `else if value > 100` :

    // src/lib.rs
    --extrait--
    if value < 1 {
        panic!(
            "Guess value must be less than or equal to 100, got {}.",
            value
        );
    } else if value > 100 {
        panic!(
            "Guess value must be greater than or equal to 1, got {}.",
            value
        );
    }
    --extrait--

Cette fois, lorsque nous exécutons le test `should_panic`, il échouera :

    exécution d'un test
    test tests::greater_than_100 - devrait provoquer une panique... FAILED

    échecs :

    ---- tests::greater_than_100 sortie standard ----
    thread'main' a généré une erreur à 'Guess value must be greater than or equal to 1, got
    200.', src/lib.rs:13:13
    note : exécutez avec la variable d'environnement `RUST_BACKTRACE=1` pour afficher une trace de pile
    note : la panique ne contenait pas la chaîne attendue
          message de panique : `"Guess value must be greater than or equal to 1, got
    200."`,
     sous-chaîne attendue : `"less than or equal to 100"`

    échecs :
        tests::greater_than_100

    résultat du test : FAILED. 0 passé ; 1 échoué ; 0 ignoré ; 0 mesuré ; 0 filtré ;
    terminé en 0,00 s

Le message d'erreur indique que ce test a effectivement provoqué une panique comme nous l'attendions, mais le message de panique n'a pas inclus la chaîne attendue `'Guess value must be less than or equal to 100'`. Le message de panique que nous avons obtenu dans ce cas était `Guess value must be greater than or equal to 1, got 200`. Maintenant, nous pouvons commencer à localiser notre bogue!
