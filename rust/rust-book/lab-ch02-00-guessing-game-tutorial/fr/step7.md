# Printing Values with println! Placeholders

En dehors de la accolade fermante, il ne reste plus qu'une seule ligne à discuter dans le code jusqu'à présent :

```rust
println!("You guessed: {guess}");
```

Cette ligne imprime la chaîne de caractères qui contient maintenant l'entrée de l'utilisateur. Le groupe de parenthèses accoladées `{}` est un emplacement réservé : pensez à `{}` comme de petites pinces de crabe qui retiennent une valeur en place. Lorsque vous imprimez la valeur d'une variable, le nom de la variable peut être placé à l'intérieur des parenthèses accoladées. Lorsque vous imprimez le résultat de l'évaluation d'une expression, placez des parenthèses accoladées vides dans la chaîne de formatage, puis suivez la chaîne de formatage avec une liste séparée par des virgules d'expressions à imprimer dans chaque emplacement réservé de parenthèses accoladées vides dans le même ordre. Imprimer une variable et le résultat d'une expression dans un seul appel à `println!` serait comme ceci :

```rust
let x = 5;
let y = 10;

println!("x = {x} and y + 2 = {}", y + 2);
```

Ce code imprimerait `x = 5 and y = 12`.
