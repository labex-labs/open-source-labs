# Imprimiendo valores con marcadores de posición de println!

Aparte de la llave curva de cierre, solo queda una línea más por discutir en el código hasta ahora:

```rust
println!("You guessed: {guess}");
```

Esta línea imprime la cadena que ahora contiene la entrada del usuario. El conjunto de llaves `{}` es un marcador de posición: piensa en `{}` como pequeños pinzas de cangrejo que mantienen un valor en su lugar. Cuando se imprime el valor de una variable, el nombre de la variable puede ir dentro de las llaves. Cuando se imprime el resultado de evaluar una expresión, coloca llaves vacías en la cadena de formato, luego sigue la cadena de formato con una lista separada por comas de expresiones para imprimir en cada marcador de posición de llaves vacías en el mismo orden. Imprimir una variable y el resultado de una expresión en una llamada a `println!` se vería así:

```rust
let x = 5;
let y = 10;

println!("x = {x} and y + 2 = {}", y + 2);
```

Este código imprimiría `x = 5 and y = 12`.
