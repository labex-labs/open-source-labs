# Introducción

En este laboratorio, aprenderemos a convertir a cadenas y de cadenas en Rust. Para convertir cualquier tipo a una cadena, podemos implementar el trato `ToString` para el tipo. Alternativamente, podemos implementar el trato `fmt::Display`, que proporciona automáticamente el trato `ToString` y nos permite imprimir el tipo usando `println!`. Por otro lado, para analizar una cadena en un tipo específico, como un número, podemos usar la función `parse` junto con la inferencia de tipos o especificando el tipo usando la sintaxis 'turbofish'. Esto se basa en el trato `FromStr`, que está implementado para muchos tipos en la biblioteca estándar. Si queremos analizar una cadena en un tipo definido por el usuario, podemos implementar el trato `FromStr` para ese tipo.

> **Nota:** Si el laboratorio no especifica un nombre de archivo, puede usar cualquier nombre de archivo que desee. Por ejemplo, puede usar `main.rs`, compilar y ejecutarlo con `rustc main.rs &&./main`.
