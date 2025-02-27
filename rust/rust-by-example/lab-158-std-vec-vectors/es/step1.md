# Vectores

Los vectores son arrays redimensionables. Al igual que las rebanadas, su tamaño no es conocido en tiempo de compilación, pero pueden crecer o contraerse en cualquier momento. Un vector se representa utilizando 3 parámetros:

- puntero a los datos
- longitud
- capacidad

La capacidad indica cuánta memoria está reservada para el vector. El vector puede crecer siempre y cuando la longitud sea menor que la capacidad. Cuando se necesita superar este umbral, el vector se reasigna con una capacidad mayor.

```rust
fn main() {
    // Los iteradores se pueden recopilar en vectores
    let collected_iterator: Vec<i32> = (0..10).collect();
    println!("Recopilado (0..10) en: {:?}", collected_iterator);

    // La macro `vec!` se puede utilizar para inicializar un vector
    let mut xs = vec![1i32, 2, 3];
    println!("Vector inicial: {:?}", xs);

    // Insertar un nuevo elemento al final del vector
    println!("Agregar 4 al vector");
    xs.push(4);
    println!("Vector: {:?}", xs);

    // Error! Los vectores inmutables no pueden crecer
    collected_iterator.push(0);
    // FIXME ^ Comentar esta línea

    // El método `len` devuelve el número de elementos actualmente almacenados en un vector
    println!("Longitud del vector: {}", xs.len());

    // La indexación se realiza utilizando corchetes (la indexación comienza en 0)
    println!("Segundo elemento: {}", xs[1]);

    // `pop` elimina el último elemento del vector y lo devuelve
    println!("Quitar el último elemento: {:?}", xs.pop());

    // La indexación fuera de los límites produce un error
    println!("Cuarto elemento: {}", xs[3]);
    // FIXME ^ Comentar esta línea

    // Los `Vector`s se pueden iterar fácilmente
    println!("Contenido de xs:");
    for x in xs.iter() {
        println!("> {}", x);
    }

    // Un `Vector` también se puede iterar mientras el recuento de iteración
    // se enumera en una variable separada (`i`)
    for (i, x) in xs.iter().enumerate() {
        println!("En la posición {} tenemos el valor {}", i, x);
    }

    // Gracias a `iter_mut`, los `Vector`s mutables también se pueden iterar
    // de una manera que permite modificar cada valor
    for x in xs.iter_mut() {
        *x *= 3;
    }
    println!("Vector actualizado: {:?}", xs);
}
```

Más métodos de `Vec` se pueden encontrar en el módulo `std::vec`
