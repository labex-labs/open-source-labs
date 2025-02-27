# Introducción

En este laboratorio, aprendemos sobre la palabra clave `while`, que se utiliza para crear un bucle que continúa ejecutándose mientras una condición especificada sea verdadera. Para ilustrar su uso, escribimos un programa en Rust llamado FizzBuzz. El programa utiliza un bucle `while` para iterar a través de los números del 1 al 100. Dentro del bucle, verifica si el número actual es divisible por 3 y 5 (es decir, un múltiplo de 15) y muestra "fizzbuzz" en tales casos. Si el número es divisible solo por 3, muestra "fizz", y si es divisible solo por 5, muestra "buzz". Para todos los demás números, simplemente muestra el número en sí mismo. El bucle continúa hasta que la variable contador alcanza 101, incrementándola después de mostrar cada número o etiqueta.

> **Nota:** Si el laboratorio no especifica un nombre de archivo, puede usar cualquier nombre de archivo que desee. Por ejemplo, puede usar `main.rs`, compilar y ejecutarlo con `rustc main.rs &&./main`.
