# La Diferencia Entre Macros y Funciones

En esencia, las macros son una forma de escribir código que escribe otro código, lo que se conoce como _metaprogramación_. En el Apéndice C, discutimos el atributo `derive`, que genera una implementación de varios tratos para ti. También hemos utilizado las macros `println!` y `vec!` en todo el libro. Todas estas macros _se expanden_ para producir más código que el código que has escrito manualmente.

La metaprogramación es útil para reducir la cantidad de código que tienes que escribir y mantener, lo que también es uno de los roles de las funciones. Sin embargo, las macros tienen algunas capacidades adicionales que las funciones no tienen.

La firma de una función debe declarar el número y el tipo de parámetros que tiene la función. Las macros, por otro lado, pueden tomar un número variable de parámetros: podemos llamar a `println!("hello")` con un argumento o `println!("hello {}", name)` con dos argumentos. Además, las macros se expanden antes de que el compilador interprete el significado del código, por lo que una macro puede, por ejemplo, implementar un trato en un tipo dado. Una función no puede, porque se llama en tiempo de ejecución y un trato necesita ser implementado en tiempo de compilación.

La desventaja de implementar una macro en lugar de una función es que las definiciones de macros son más complejas que las definiciones de funciones porque estás escribiendo código de Rust que escribe código de Rust. Debido a esta indirección, las definiciones de macros generalmente son más difíciles de leer, entender y mantener que las definiciones de funciones.

Otra diferencia importante entre macros y funciones es que debes definir las macros o traerlas al ámbito _antes_ de llamarlas en un archivo, al contrario de las funciones que se pueden definir en cualquier lugar y llamar en cualquier lugar.
