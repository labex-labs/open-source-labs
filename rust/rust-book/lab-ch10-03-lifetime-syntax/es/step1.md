# Validando referencias con lifetimes

Los lifetimes son otro tipo de genéricos que ya hemos estado utilizando. En lugar de garantizar que un tipo tenga el comportamiento que queremos, los lifetimes aseguran que las referencias sean válidas durante el tiempo que las necesitamos.

Un detalle que no discutimos en "Referencias y préstamos" es que cada referencia en Rust tiene un _lifetime_, que es el alcance durante el cual esa referencia es válida. En la mayoría de los casos, los lifetimes son implícitos e inferidos, al igual que en la mayoría de los casos, los tipos son inferidos. Solo debemos anotar los tipos cuando son posibles múltiples tipos. De manera similar, debemos anotar los lifetimes cuando los lifetimes de las referencias pueden estar relacionados de varias maneras diferentes. Rust nos obliga a anotar las relaciones utilizando parámetros de lifetime genéricos para garantizar que las referencias reales utilizadas en tiempo de ejecución definitivamente serán válidas.

La anotación de lifetimes ni siquiera es un concepto que la mayoría de los otros lenguajes de programación tienen, por lo que esto puede resultar desconocido. Aunque no cubriremos los lifetimes en su totalidad en este capítulo, discutiremos las formas comunes en las que puede encontrarse la sintaxis de lifetimes para que te sientas cómodo con el concepto.
