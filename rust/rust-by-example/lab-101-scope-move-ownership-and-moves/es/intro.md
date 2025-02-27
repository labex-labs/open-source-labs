# Introducción

En este laboratorio, se explica que en Rust, las variables tienen la propiedad de los recursos y solo pueden tener un propietario, lo que evita que los recursos se liberen múltiples veces. Cuando se asignan variables o se pasan argumentos de función por valor, se transfiere la propiedad de los recursos, lo que se conoce como un "move". Después del "move", el propietario anterior ya no se puede utilizar para evitar la creación de punteros colgantes. El ejemplo de código demuestra estos conceptos mostrando cómo se transfiere la propiedad de variables asignadas en la pila y en el montón y cómo acceder a una variable después de que se haya transferido su propiedad conduce a errores.

> **Nota:** Si el laboratorio no especifica un nombre de archivo, puede usar cualquier nombre de archivo que desee. Por ejemplo, puede usar `main.rs`, compilar y ejecutarlo con `rustc main.rs &&./main`.
