# Parties d'une valeur avec un \_ imbriqué

Nous pouvons également utiliser `_` à l'intérieur d'un autre motif pour ignorer seulement une partie d'une valeur, par exemple, lorsque nous voulons tester seulement une partie d'une valeur mais n'avons pas besoin des autres parties dans le code correspondant que nous voulons exécuter. La Liste 18-18 montre le code responsable de la gestion de la valeur d'un paramètre. Les exigences commerciales sont que l'utilisateur ne doit pas être autorisé à écraser une personnalisation existante d'un paramètre, mais peut annuler le paramètre et lui donner une valeur s'il n'est pas actuellement défini.

Nom de fichier : `src/main.rs`

```rust
let mut setting_value = Some(5);
let new_setting_value = Some(10);

match (setting_value, new_setting_value) {
    (Some(_), Some(_)) => {
        println!("Can't overwrite an existing customized value");
    }
    _ => {
        setting_value = new_setting_value;
    }
}

println!("setting is {:?}", setting_value);
```

Liste 18-18 : Utilisation d'un tiret bas à l'intérieur de motifs qui correspondent à des variantes `Some` lorsque nous n'avons pas besoin d'utiliser la valeur à l'intérieur de `Some`

Ce code imprimera `Can't overwrite an existing customized value` puis `setting is Some(5)`. Dans le premier bras de correspondance, nous n'avons pas besoin de correspondre ou d'utiliser les valeurs à l'intérieur des deux variantes `Some`, mais nous devons tester le cas où `setting_value` et `new_setting_value` sont la variante `Some`. Dans ce cas, nous imprimons la raison pour ne pas modifier `setting_value`, et elle ne sera pas modifiée.

Dans tous les autres cas (si `setting_value` ou `new_setting_value` est `None`) exprimé par le motif `_` dans le second bras, nous voulons autoriser `new_setting_value` à devenir `setting_value`.

Nous pouvons également utiliser des tirets bas en plusieurs endroits à l'intérieur d'un motif pour ignorer des valeurs particulières. La Liste 18-19 montre un exemple d'ignorance de la deuxième et quatrième valeurs dans un tuple de cinq éléments.

Nom de fichier : `src/main.rs`

```rust
let numbers = (2, 4, 8, 16, 32);

match numbers {
    (first, _, third, _, fifth) => {
        println!("Some numbers: {first}, {third}, {fifth}");
    }
}
```

Liste 18-19 : Ignorer plusieurs parties d'un tuple

Ce code imprimera `Some numbers: 2, 8, 32`, et les valeurs `4` et `16` seront ignorées.
