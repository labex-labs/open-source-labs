# Habilitando tipos recursivos con cajas

Un valor de un _tipo recursivo_ puede tener otro valor del mismo tipo como parte de sí mismo. Los tipos recursivos plantean un problema porque en tiempo de compilación Rust necesita saber cuánto espacio ocupa un tipo. Sin embargo, el anidamiento de valores de tipos recursivos podría teóricamente continuar indefinidamente, por lo que Rust no puede saber cuánto espacio necesita el valor. Debido a que las cajas tienen un tamaño conocido, podemos habilitar tipos recursivos insertando una caja en la definición del tipo recursivo.

Como ejemplo de un tipo recursivo, exploremos la _lista cons_. Este es un tipo de datos común en los lenguajes de programación funcionales. El tipo de lista cons que definiremos es sencillo excepto por la recursividad; por lo tanto, los conceptos en el ejemplo con el que trabajaremos serán útiles en cualquier momento que te enfrentes a situaciones más complejas que involucren tipos recursivos.
