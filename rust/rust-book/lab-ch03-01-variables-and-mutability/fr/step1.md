# Variables et mutabilité

Comme mentionné dans "Stockage de valeurs avec des variables", par défaut, les variables sont immuables. C'est l'un des nombreux conseils que Rust vous donne pour écrire votre code de manière à profiter de la sécurité et de la facilité de concurrence que Rust offre. Cependant, vous avez toujours la possibilité de rendre vos variables mutables. Explorerons comment et pourquoi Rust vous encourage à privilégier l'immuabilité et pourquoi parfois vous voudrez peut-être vous en écarter.

Lorsqu'une variable est immutable, une fois qu'une valeur est liée à un nom, vous ne pouvez pas changer cette valeur. Pour illustrer cela, générez un nouveau projet appelé _variables_ dans votre répertoire `projet` en utilisant `cargo new variables`.

Ensuite, dans votre nouveau répertoire `variables`, ouvrez `src/main.rs` et remplacez son code par le code suivant, qui ne compilera pas encore :

Nom de fichier : `src/main.rs`

```rust
fn main() {
    let x = 5;
    println!("The value of x is: {x}");
    x = 6;
    println!("The value of x is: {x}");
}
```

Enregistrez et exécutez le programme en utilisant `cargo run`. Vous devriez recevoir un message d'erreur concernant une erreur d'immuabilité, comme indiqué dans cette sortie :

```bash
$ cargo run
   Compiling variables v0.1.0 (file:///projects/variables)
error[E0384]: cannot assign twice to immutable variable `x`
 --> src/main.rs:4:5
  |
2 |     let x = 5;
  |         -
  |         |
  |         first assignment to `x`
  |         help: consider making this binding mutable: `mut x`
3 |     println!("The value of x is: {x}");
4 |     x = 6;
  |     ^^^^^ cannot assign twice to immutable variable
```

Cet exemple montre comment le compilateur vous aide à trouver des erreurs dans votre programme. Les erreurs du compilateur peuvent être frustrantes, mais en réalité, elles ne signifient que votre programme ne fait pas encore sûrement ce que vous voulez qu'il fasse ; elles ne signifient _pas_ que vous n'êtes pas un bon programmeur! Les Rustaceans expérimentés reçoivent toujours des erreurs du compilateur.

Vous avez reçu le message d'erreur `cannot assign twice to immutable variable`x\``car vous avez essayé d'affecter une deuxième valeur à la variable immutable`x\`.

Il est important que nous recevions des erreurs au moment de la compilation lorsqu'il s'agit d'essayer de changer une valeur qui est désignée comme immutable car cette situation précise peut entraîner des bogues. Si une partie de notre code fonctionne en supposant qu'une valeur ne changera jamais et qu'une autre partie de notre code change cette valeur, il est possible que la première partie du code ne fasse pas ce pour quoi elle a été conçue. La cause de ce type de bogue peut être difficile à repérer après coup, surtout lorsque la deuxième partie du code ne change la valeur que _parfois_. Le compilateur Rust garantit que lorsque vous déclarez qu'une valeur ne changera pas, elle ne changera vraiment pas, de sorte que vous n'avez pas à vous en occuper vous-même. Votre code est donc plus facile à comprendre.

Mais la mutabilité peut être très utile et peut rendre le code plus pratique à écrire. Bien que les variables soient immuables par défaut, vous pouvez les rendre mutables en ajoutant `mut` devant le nom de la variable, comme vous l'avez fait au chapitre 2. Ajouter `mut` indique également l'intention aux lecteurs futurs du code en montrant que d'autres parties du code modifieront la valeur de cette variable.

Par exemple, modifions `src/main.rs` comme suit :

Nom de fichier : `src/main.rs`

```rust
fn main() {
    let mut x = 5;
    println!("The value of x is: {x}");
    x = 6;
    println!("The value of x is: {x}");
}
```

Lorsque nous exécutons le programme maintenant, voici ce que nous obtenons :

```bash
$ cargo run
   Compiling variables v0.1.0 (file:///projects/variables)
    Finished dev [unoptimized + debuginfo] target(s) in 0.30s
     Running `target/debug/variables`
The value of x is: 5
The value of x is: 6
```

Nous sommes autorisés à changer la valeur liée à `x` de `5` à `6` lorsque `mut` est utilisé. En fin de compte, décider d'utiliser ou non la mutabilité vous appartient et dépend de ce que vous trouvez le plus clair dans cette situation particulière.
