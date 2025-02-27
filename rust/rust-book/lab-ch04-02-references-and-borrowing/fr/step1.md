# References and Borrowing

Le problème avec le code de tuple dans la liste 4-5 est que nous devons renvoyer la `String` à la fonction appelante afin que nous puissions toujours utiliser la `String` après l'appel à `calculate_length`, car la `String` a été déplacée dans `calculate_length`. Au lieu de cela, nous pouvons fournir une référence à la valeur `String`. Une _référence_ est comme un pointeur dans le sens où c'est une adresse que nous pouvons suivre pour accéder aux données stockées à cette adresse ; ces données sont possédées par une autre variable. Contrairement à un pointeur, une référence est garantie pour pointer vers une valeur valide d'un type particulier pour la durée de vie de cette référence.

Voici comment vous définiriez et utiliseriez une fonction `calculate_length` qui a une référence à un objet en tant que paramètre au lieu de prendre la propriété de la valeur :

Nom de fichier : `src/main.rs`

```rust
fn main() {
    let s1 = String::from("hello");

    let len = calculate_length(&s1);

    println!("The length of '{s1}' is {len}.");
}

fn calculate_length(s: &String) -> usize {
    s.len()
}
```

Tout d'abord, remarquons que tout le code de tuple dans la déclaration de variable et la valeur de retour de fonction est disparu. Deuxièmement, notons que nous passons `&s1` à `calculate_length` et, dans sa définition, nous prenons `&String` au lieu de `String`. Ces ampersands représentent des _références_, et elles vous permettent de vous référer à une certaine valeur sans en prendre la propriété. La figure 4-5 illustre ce concept.

Figure 4-5 : Un diagramme de `&String s` pointant vers `String s1`

> Note : L'opposé de la référence en utilisant `&` est le _déréférencement_, qui est effectué avec l'opérateur de déréférencement, `*`. Nous verrons quelques utilisations de l'opérateur de déréférencement au chapitre 8 et discuter des détails du déréférencement au chapitre 15.

Examillons de plus près l'appel de fonction ici :

```rust
let s1 = String::from("hello");

let len = calculate_length(&s1);
```

La syntaxe `&s1` nous permet de créer une référence qui _se réfère_ à la valeur de `s1` mais ne la possède pas. Comme elle ne la possède pas, la valeur à laquelle elle pointe ne sera pas supprimée lorsque la référence cesse d'être utilisée.

De même, la signature de la fonction utilise `&` pour indiquer que le type du paramètre `s` est une référence. Ajoutons quelques annotations explicatives :

```rust
fn calculate_length(s: &String) -> usize { // s est une référence à une String
    s.len()
} // Ici, s sort de portée. Mais comme elle n'a pas la propriété de ce à quoi elle
  // se réfère, la String n'est pas supprimée
```

La portée dans laquelle la variable `s` est valide est la même que celle de tout paramètre de fonction, mais la valeur pointée par la référence n'est pas supprimée lorsque `s` cesse d'être utilisée, car `s` n'a pas la propriété. Lorsque les fonctions ont des références comme paramètres au lieu des valeurs réelles, nous n'aurons pas besoin de renvoyer les valeurs pour redonner la propriété, car nous n'avons jamais eu la propriété.

Nous appelons l'action de créer une référence _emprunt_. Comme dans la vie réelle, si une personne possède quelque chose, vous pouvez l'emprunter d'elle. Lorsque vous avez fini, vous devez le lui rendre. Vous ne le possédez pas.

Alors, que se passe-t-il si nous essayons de modifier quelque chose que nous empruntons? Essayez le code de la liste 4-6. Avertissement : ça ne fonctionne pas!

Nom de fichier : `src/main.rs`

```rust
fn main() {
    let s = String::from("hello");

    change(&s);
}

fn change(some_string: &String) {
    some_string.push_str(", world");
}
```

Liste 4-6 : Tentative de modification d'une valeur empruntée

Voici l'erreur :

```bash
error[E0596]: cannot borrow `*some_string` as mutable, as it is behind a `&`
reference
 --> src/main.rs:8:5
  |
7 | fn change(some_string: &String) {
  |                        ------- help: consider changing this to be a mutable
reference: `&mut String`
8 |     some_string.push_str(", world");
  |     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ `some_string` is a `&` reference, so
the data it refers to cannot be borrowed as mutable
```

De même que les variables sont immuables par défaut, les références le sont également. Nous ne sommes pas autorisés à modifier quelque chose à quoi nous avons une référence.
