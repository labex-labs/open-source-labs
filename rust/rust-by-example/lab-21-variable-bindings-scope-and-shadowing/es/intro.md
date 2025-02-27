# Introducción

En este laboratorio, aprendemos sobre los enlaces de variables, su ámbito y el concepto de sombreado en Rust. Los enlaces de variables están confinados a un bloque, que es una colección de declaraciones encerradas entre llaves. Se proporcionan dos ejemplos para ilustrar estos conceptos. El primer ejemplo muestra cómo un enlace de variable declarado dentro de un bloque está limitado al ámbito de ese bloque y no es accesible fuera de él. El segundo ejemplo demuestra el sombreado de variables, donde se declara un nuevo enlace con el mismo nombre dentro de un bloque, lo que efectivamente sombrea el enlace externo.

> **Nota:** Si el laboratorio no especifica un nombre de archivo, puede usar cualquier nombre de archivo que desee. Por ejemplo, puede usar `main.rs`, compilar y ejecutarlo con `rustc main.rs &&./main`.
