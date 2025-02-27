# L'anatomie d'une fonction de test

Au minimum, un test en Rust est une fonction annotée avec l'attribut `test`. Les attributs sont des métadonnées sur des parties de code Rust ; un exemple est l'attribut `derive` que nous avons utilisé avec les structs au chapitre 5. Pour transformer une fonction en fonction de test, ajoutez `#[test]` sur la ligne avant `fn`. Lorsque vous exécutez vos tests avec la commande `cargo test`, Rust construit un binaire exécuteur de tests qui exécute les fonctions annotées et informe si chaque fonction de test passe ou échoue.

Chaque fois que nous créons un nouveau projet de bibliothèque avec Cargo, un module de test contenant une fonction de test est automatiquement généré pour nous. Ce module vous donne un modèle pour écrire vos tests, de sorte que vous n'ayez pas besoin de chercher la structure et la syntaxe exactes chaque fois que vous commencez un nouveau projet. Vous pouvez ajouter autant de fonctions de test supplémentaires et de modules de test que vous le souhaitez!

Nous allons explorer certains aspects de fonctionnement des tests en expérimentant le test modèle avant de tester réellement du code. Ensuite, nous écrirons quelques tests du monde réel qui appellent du code que nous avons écrit et affirmons que son comportement est correct.

Créons un nouveau projet de bibliothèque appelé `adder` qui additionnera deux nombres :

```bash
$ cargo new adder --lib
Créé le projet de bibliothèque $(adder)
$ cd adder
```

Le contenu du fichier `src/lib.rs` dans votre bibliothèque `adder` devrait ressembler à la liste 11-1.

Nom de fichier : `src/lib.rs`

```rust
#[cfg(test)]
mod tests {
  1 #[test]
    fn it_works() {
        let result = 2 + 2;
      2 assert_eq!(result, 4);
    }
}
```

Liste 11-1 : Le module de test et la fonction générés automatiquement par `cargo new`

Pour l'instant, ignorons les deux premières lignes et concentrons-nous sur la fonction. Notez l'annotation `#[test]` \[1\] : cet attribut indique que cette fonction est une fonction de test, de sorte que l'exécuteur de tests sait traiter cette fonction comme un test. Nous pourrions également avoir des fonctions non de test dans le module `tests` pour aider à préparer des scénarios communs ou à effectuer des opérations communes, de sorte que nous devons toujours indiquer quelles fonctions sont des tests.

Le corps d'exemple de fonction utilise la macro `assert_eq!` \[2\] pour affirmer que `result`, qui contient le résultat de l'addition de 2 et 2, est égal à 4. Cette assertion sert d'exemple du format d'un test typique. Exécutons-la pour voir que ce test passe.

La commande `cargo test` exécute tous les tests de notre projet, comme indiqué dans la liste 11-2.

```bash
$ cargo test
   Compiling adder v0.1.0 (file:///projects/adder)
    Finished test [non optimisé + débogage] cibles(s) en 0,57 s
     Exécution des tests unitaires src/lib.rs (cible/debug/deps/adder-
92948b65e88960b4)

1 exécution d'un test
2 test tests::it_works... ok

3 Résultat du test : ok. 1 passé ; 0 échoué ; 0 ignoré ; 0 mesuré ; 0
filtré ; terminé en 0,00 s

  4 Tests de documentation adder

exécution de 0 tests

résultat du test : ok. 0 passé ; 0 échoué ; 0 ignoré ; 0 mesuré ; 0
filtré ; terminé en 0,00 s
```

Liste 11-2 : La sortie de l'exécution du test généré automatiquement

Cargo a compilé et exécuté le test. Nous voyons la ligne `exécution d'un test` \[1\]. La ligne suivante montre le nom de la fonction de test générée, appelée `it_works`, et que le résultat de l'exécution de ce test est `ok` \[2\]. Le résumé global `résultat du test : ok.` \[3\] signifie que tous les tests ont réussi, et la partie qui lit `1 passé ; 0 échoué` totalise le nombre de tests qui ont réussi ou échoué.

Il est possible de marquer un test comme ignoré de sorte qu'il ne s'exécute pas dans une instance particulière ; nous aborderons cela dans "Ignorer certains tests sauf si spécifiquement demandé". Comme nous n'avons pas fait cela ici, le résumé indique `0 ignoré`. Nous pouvons également passer un argument à la commande `cargo test` pour exécuter seulement les tests dont le nom correspond à une chaîne de caractères ; cela s'appelle le _filtrage_ et nous aborderons cela dans "Exécuter un sous-ensemble de tests par nom". Ici, nous n'avons pas filtré les tests en cours d'exécution, de sorte que la fin du résumé indique `0 filtré`.

La statistique `0 mesuré` est pour les tests de benchmark qui mesurent les performances. Les tests de benchmark sont, à l'heure actuelle, uniquement disponibles dans la version nocturne de Rust. Consultez la documentation sur les tests de benchmark à *https://doc.rust-lang.org/unstable-book/library-features/test.html* pour en savoir plus.

La partie suivante de la sortie de test commençant par `Tests de documentation adder` \[4\] est pour les résultats de tous les tests de documentation. Nous n'avons pas encore de tests de documentation, mais Rust peut compiler tous les exemples de code qui apparaissent dans notre documentation API. Cette fonction aide à maintenir vos documents et votre code synchronisés! Nous discuterons de la manière d'écrire des tests de documentation dans "Commentaires de documentation en tant que tests". Pour l'instant, nous ignorerons la sortie `Tests de documentation`.

Commencons à personnaliser le test selon nos besoins. Premièrement, changeons le nom de la fonction `it_works` en un nom différent, tel que `exploration`, comme ceci :

Nom de fichier : `src/lib.rs`

```rust
#[cfg(test)]
mod tests {
    #[test]
    fn exploration() {
        let result = 2 + 2;
        assert_eq!(result, 4);
    }
}
```

Ensuite, exécutez `cargo test` à nouveau. La sortie montre maintenant `exploration` au lieu de `it_works` :

    exécution d'un test
    test tests::exploration... ok

    résultat du test : ok. 1 passé ; 0 échoué ; 0 ignoré ; 0 mesuré ; 0
    filtré ; terminé en 0,00 s

Maintenant, ajoutons un autre test, mais cette fois-ci, nous allons créer un test qui échoue! Les tests échouent lorsqu'une erreur survient dans la fonction de test. Chaque test est exécuté dans un nouveau fil, et lorsque le fil principal constate qu'un fil de test est mort, le test est marqué comme échoué. Au chapitre 9, nous avons parlé de la manière la plus simple de générer une erreur est d'appeler la macro `panic!`. Entrez le nouveau test sous forme d'une fonction nommée `another`, de sorte que votre fichier `src/lib.rs` ressemble à la liste 11-3.

Nom de fichier : `src/lib.rs`

```rust
#[cfg(test)]
mod tests {
    #[test]
    fn exploration() {
        assert_eq!(2 + 2, 4);
    }

    #[test]
    fn another() {
        panic!("Faites échouer ce test");
    }
}
```

Liste 11-3 : Ajout d'un deuxième test qui échouera car nous appelons la macro `panic!`

Exécutez les tests à nouveau en utilisant `cargo test`. La sortie devrait ressembler à la liste 11-4, qui montre que notre test `exploration` a réussi et que `another` a échoué.

    exécution de 2 tests
    test tests::exploration... ok
    1 test tests::another... FAILED

    2 échecs :

    ---- tests::another sortie standard ----
    thread'main' a généré une erreur à 'Faites échouer ce test', src/lib.rs:10:9
    note : exécutez avec la variable d'environnement `RUST_BACKTRACE=1` pour afficher
    une trace de pile

    3 échecs :
        tests::another

    4 résultat du test : FAILED. 1 passé ; 1 échoué ; 0 ignoré ; 0 mesuré ; 0
    filtré ; terminé en 0,00 s

    erreur : le test a échoué, pour le relancer passez '--lib'

Liste 11-4 : Résultats des tests lorsqu'un test passe et qu'un test échoue

Au lieu de `ok`, la ligne `test tests::another` montre `FAILED` \[1\]. Deux nouvelles sections apparaissent entre les résultats individuels et le résumé : la première \[2\] affiche la raison détaillée de chaque échec de test. Dans ce cas, nous obtenons les détails selon lesquels `another` a échoué car il a `généré une erreur à 'Faites échouer ce test'` à la ligne 10 dans le fichier `src/lib.rs`. La section suivante \[3\] liste uniquement les noms de tous les tests qui ont échoué, ce qui est utile lorsqu'il y a beaucoup de tests et beaucoup de sortie détaillée d'échec de test. Nous pouvons utiliser le nom d'un test qui a échoué pour exécuter uniquement ce test pour le déboguer plus facilement ; nous parlerons plus de façons d'exécuter des tests dans "Contrôler la manière dont les tests sont exécutés".

La ligne de résumé s'affiche à la fin \[4\] : globalement, notre résultat de test est `FAILED`. Nous avons eu un test qui a réussi et un test qui a échoué.

Maintenant que vous avez vu à quoi ressemblent les résultats des tests dans différents scénarios, examinons quelques macros autres que `panic!` qui sont utiles dans les tests.
