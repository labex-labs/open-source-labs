# Références mutables

Nous pouvons corriger le code de la liste 4-6 pour nous permettre de modifier une valeur empruntée avec quelques petits ajustements qui utilisent, au lieu de cela, une _référence mutable_ :

Nom de fichier : `src/main.rs`

```rust
fn main() {
    let mut s = String::from("hello");

    change(&mut s);
}

fn change(some_string: &mut String) {
    some_string.push_str(", world");
}
```

Tout d'abord, nous changeons `s` en `mut`. Ensuite, nous créons une référence mutable avec `&mut s` où nous appelons la fonction `change`, et nous mettons à jour la signature de la fonction pour accepter une référence mutable avec `some_string: &mut String`. Cela rend très clair que la fonction `change` va modifier la valeur qu'elle emprunte.

Les références mutables ont une grande restriction : si vous avez une référence mutable à une valeur, vous ne pouvez avoir aucune autre référence à cette valeur. Ce code qui tente de créer deux références mutables à `s` échouera :

Nom de fichier : `src/main.rs`

```rust
let mut s = String::from("hello");

let r1 = &mut s;
let r2 = &mut s;

println!("{r1}, {r2}");
```

Voici l'erreur :

```bash
error[E0499]: cannot borrow `s` as mutable more than once at a time
 --> src/main.rs:5:14
  |
4 |     let r1 = &mut s;
  |              ------ first mutable borrow occurs here
5 |     let r2 = &mut s;
  |              ^^^^^^ second mutable borrow occurs here
6 |
7 |     println!("{r1}, {r2}");
  |                -- first borrow later used here
```

Cette erreur indique que ce code est invalide car nous ne pouvons pas emprunter `s` en tant que mutable plus d'une fois à la fois. Le premier emprunt mutable est dans `r1` et doit durer jusqu'à ce qu'il soit utilisé dans le `println!`, mais entre la création de cette référence mutable et son utilisation, nous avons essayé de créer une autre référence mutable dans `r2` qui emprunte les mêmes données que `r1`.

La restriction qui empêche d'avoir plusieurs références mutables à la même donnée en même temps permet la mutation mais de manière très contrôlée. C'est quelque chose avec quoi les nouveaux Rustaceans ont du mal car la plupart des langages vous laissent muter quand vous le voulez. L'avantage de cette restriction est que Rust peut empêcher les courses de données à la compilation. Une _course de données_ est similaire à une condition de course et se produit lorsque ces trois comportements se produisent :

- Deux ou plusieurs pointeurs accèdent à la même donnée en même temps.
- Au moins l'un des pointeurs est utilisé pour écrire dans les données.
- Il n'y a aucun mécanisme utilisé pour synchroniser l'accès aux données.

Les courses de données entraînent un comportement indéfini et peuvent être difficiles à diagnostiquer et à corriger lorsque vous essayez de les repérer à l'exécution ; Rust empêche ce problème en refusant de compiler le code avec des courses de données!

Comme toujours, nous pouvons utiliser des accolades pour créer un nouveau scope, permettant plusieurs références mutables, juste pas des _simultanées_ :

```rust
let mut s = String::from("hello");

{
    let r1 = &mut s;
} // r1 sort de portée ici, donc nous pouvons créer une nouvelle référence sans problème

let r2 = &mut s;
```

Rust applique une règle similaire pour combiner les références mutables et immuables. Ce code entraîne une erreur :

```rust
let mut s = String::from("hello");

let r1 = &s; // pas de problème
let r2 = &s; // pas de problème
let r3 = &mut s; // GRAND PROBLÈME

println!("{r1}, {r2}, and {r3}");
```

Voici l'erreur :

```bash
error[E0502]: cannot borrow `s` as mutable because it is also borrowed as
immutable
 --> src/main.rs:6:14
  |
4 |     let r1 = &s; // pas de problème
  |              -- immutable borrow occurs here
5 |     let r2 = &s; // pas de problème
6 |     let r3 = &mut s; // GRAND PROBLÈME
  |              ^^^^^^ mutable borrow occurs here
7 |
8 |     println!("{r1}, {r2}, and {r3}");
  |                -- immutable borrow later used here
```

Phew! Nous _ne pouvons pas non plus_ avoir une référence mutable tandis que nous avons une référence immuable à la même valeur.

Les utilisateurs d'une référence immuable n'attendent pas que la valeur change soudainement sous leurs yeux! Cependant, plusieurs références immuables sont autorisées car personne qui ne lit que les données n'a la capacité d'affecter la lecture des autres.

Notez que la portée d'une référence commence où elle est introduite et continue jusqu'à la dernière fois que cette référence est utilisée. Par exemple, ce code compilera car la dernière utilisation des références immuables, le `println!`, se produit avant l'introduction de la référence mutable :

```rust
let mut s = String::from("hello");

let r1 = &s; // pas de problème
let r2 = &s; // pas de problème
println!("{r1} and {r2}");
// les variables r1 et r2 ne seront pas utilisées après ce point

let r3 = &mut s; // pas de problème
println!("{r3}");
```

Les portées des références immuables `r1` et `r2` se terminent après le `println!` où elles sont dernièrement utilisées, ce qui est avant la création de la référence mutable `r3`. Ces portées ne se chevauchent pas, donc ce code est autorisé : le compilateur peut voir que la référence n'est plus utilisée à un moment avant la fin de la portée.

Même si les erreurs d'emprunt peuvent parfois être frustrantes, rappelez-vous que c'est le compilateur Rust qui indique un bogue potentiel tôt (au moment de la compilation plutôt qu'à l'exécution) et vous montre exactement où se trouve le problème. Alors, vous n'avez pas à chercher pourquoi vos données ne sont pas ce que vous pensiez qu'elles étaient.
