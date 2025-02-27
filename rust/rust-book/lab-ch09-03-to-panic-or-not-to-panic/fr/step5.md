# Creating Custom Types for Validation

Prenons l'idée d'utiliser le système de types de Rust pour nous assurer que nous avons une valeur valide et poussons un peu plus loin en créant un type personnalisé pour la validation. Rappelez-vous le jeu de devinette du Chapitre 2 où notre code demandait à l'utilisateur de deviner un nombre entre 1 et 100. Nous n'avons jamais validé que la proposition de l'utilisateur était comprise entre ces nombres avant de la comparer avec notre nombre secret ; nous n'avons vérifié que la proposition était positive. Dans ce cas, les conséquences n'étaient pas très graves : notre message de "Trop haut" ou "Trop bas" serait toujours correct. Mais il serait un renforcement utile de guider l'utilisateur vers des propositions valides et d'avoir un comportement différent lorsque l'utilisateur devine un nombre en dehors de la plage par rapport à celui où l'utilisateur tape, par exemple, des lettres au lieu de nombres.

Une manière de faire cela serait de parser la proposition en tant qu`i32` au lieu de seulement `u32` pour autoriser des nombres potentiellement négatifs, puis d'ajouter une vérification pour que le nombre soit dans la plage, comme ceci :

Nom de fichier : `src/main.rs`

```rust
loop {
    --snip--

    let guess: i32 = match guess.trim().parse() {
        Ok(num) => num,
        Err(_) => continue,
    };

    if guess < 1 || guess > 100 {
        println!("Le nombre secret sera compris entre 1 et 100.");
        continue;
    }

    match guess.cmp(&secret_number) {
        --snip--
}
```

L'expression `if` vérifie si notre valeur est en dehors de la plage, informe l'utilisateur du problème et appelle `continue` pour démarrer la prochaine itération de la boucle et demander une autre proposition. Après l'expression `if`, nous pouvons procéder avec les comparaisons entre `guess` et le nombre secret en sachant que `guess` est compris entre 1 et 100.

Cependant, ce n'est pas une solution idéale : si il était absolument critique que le programme ne fonctionne que sur des valeurs comprises entre 1 et 100, et qu'il avait de nombreuses fonctions avec cette exigence, avoir une telle vérification dans chaque fonction serait fastidieux (et pourrait avoir un impact sur les performances).

Au lieu de cela, nous pouvons créer un nouveau type et placer les validations dans une fonction pour créer une instance du type plutôt que de répéter les validations partout. De cette manière, il est sécurisé pour les fonctions d'utiliser le nouveau type dans leurs signatures et d'utiliser avec confiance les valeurs qu'elles reçoivent. La Liste 9-13 montre une manière de définir un type `Guess` qui ne créera une instance de `Guess` que si la fonction `new` reçoit une valeur comprise entre 1 et 100.

Nom de fichier : `src/lib.rs`

```rust
1 pub struct Guess {
    value: i32,
}

impl Guess {
  2 pub fn new(value: i32) -> Guess {
      3 if value < 1 || value > 100 {
          4 panic!(
                "La valeur de la proposition doit être comprise entre 1 et 100, obtenu {}.",
                value
            );
        }

      5 Guess { value }
    }

  6 pub fn value(&self) -> i32 {
        self.value
    }
}
```

Liste 9-13 : Un type `Guess` qui ne continuera qu'avec des valeurs comprises entre 1 et 100

Tout d'abord, nous définissons un struct nommé `Guess` qui a un champ nommé `value` qui stocke un `i32` \[1\]. C'est là que le nombre sera stocké.

Ensuite, nous implémentons une fonction associée nommée `new` sur `Guess` qui crée des instances de valeurs `Guess` \[2\]. La fonction `new` est définie pour avoir un paramètre nommé `value` de type `i32` et pour retourner un `Guess`. Le code dans le corps de la fonction `new` teste `value` pour s'assurer qu'il est compris entre 1 et 100 \[3\]. Si `value` ne passe pas ce test, nous effectuons un appel à `panic!` \[4\], qui alertra le programmeur qui écrit le code appelant qu'il a un bogue à corriger, car créer un `Guess` avec une `value` en dehors de cette plage violerait le contrat sur lequel `Guess::new` s'appuie. Les conditions dans lesquelles `Guess::new` pourrait provoquer une panique devraient être discutées dans sa documentation API tournée vers le public ; nous aborderons les conventions de documentation indiquant la possibilité d'un `panic!` dans la documentation API que vous créerez au Chapitre 14. Si `value` passe le test, nous créons un nouveau `Guess` avec son champ `value` défini sur le paramètre `value` et retournons le `Guess` \[5\].

Ensuite, nous implémentons une méthode nommée `value` qui emprunte `self`, n'a pas d'autres paramètres et retourne un `i32` \[6\]. Ce genre de méthode est parfois appelée un _getter_ car son but est d'obtenir des données de ses champs et de les retourner. Cette méthode publique est nécessaire car le champ `value` de la struct `Guess` est privé. Il est important que le champ `value` soit privé afin que le code utilisant la struct `Guess` ne soit pas autorisé à définir directement `value` : le code en dehors du module _doit_ utiliser la fonction `Guess::new` pour créer une instance de `Guess`, ce qui garantit qu'il n'y a pas de moyen pour un `Guess` d'avoir une `value` qui n'a pas été vérifiée par les conditions dans la fonction `Guess::new`.

Une fonction qui a un paramètre ou qui retourne seulement des nombres compris entre 1 et 100 pourrait alors déclarer dans sa signature qu'elle prend ou retourne un `Guess` plutôt qu'un `i32` et n'aurait pas besoin de faire d'autres vérifications dans son corps.
