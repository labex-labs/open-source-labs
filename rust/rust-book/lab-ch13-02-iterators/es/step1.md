# Procesamiento de una Serie de Elementos con Iteradores

El patrón de iterador te permite realizar una tarea en una secuencia de elementos, uno a la vez. Un iterador es responsable de la lógica de iterar sobre cada elemento y de determinar cuándo ha terminado la secuencia. Cuando utilizas iteradores, no tienes que reimplementar esa lógica por ti mismo.

En Rust, los iteradores son _perezosos_, lo que significa que no tienen ningún efecto hasta que llamas a métodos que consumen el iterador para agotarlo. Por ejemplo, el código de la Lista 13-10 crea un iterador sobre los elementos del vector `v1` llamando al método `iter` definido en `Vec<T>`. Este código por sí solo no hace nada útil.

```rust
let v1 = vec![1, 2, 3];

let v1_iter = v1.iter();
```

Lista 13-10: Creación de un iterador

El iterador se almacena en la variable `v1_iter`. Una vez que hemos creado un iterador, podemos usarlo de varias maneras. En la Lista 3-5, iteramos sobre una matriz usando un bucle `for` para ejecutar un código en cada uno de sus elementos. En el fondo, esto creó implícitamente y luego consumió un iterador, pero hasta ahora nos hemos pasado por alto cómo funciona exactamente eso.

En el ejemplo de la Lista 13-11, separamos la creación del iterador del uso del iterador en el bucle `for`. Cuando se llama al bucle `for` usando el iterador en `v1_iter`, cada elemento del iterador se utiliza en una iteración del bucle, lo que imprime cada valor.

```rust
let v1 = vec![1, 2, 3];

let v1_iter = v1.iter();

for val in v1_iter {
    println!("Got: {val}");
}
```

Lista 13-11: Uso de un iterador en un bucle `for`

En los lenguajes que no tienen iteradores proporcionados por sus bibliotecas estándar, probablemente escribirías la misma funcionalidad comenzando una variable en el índice 0, usando esa variable para acceder al vector y obtener un valor, e incrementando el valor de la variable en un bucle hasta que alcanzara el número total de elementos del vector.

Los iteradores manejan toda esa lógica por ti, reduciendo el código repetitivo que podrías confundir. Los iteradores te dan más flexibilidad para usar la misma lógica con muchos tipos diferentes de secuencias, no solo con estructuras de datos en las que puedes acceder por índice, como los vectores. Veamos cómo lo hacen los iteradores.
