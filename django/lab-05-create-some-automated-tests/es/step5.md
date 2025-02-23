# Cuando se realizan pruebas, más es mejor

Podría parecer que nuestras pruebas están saliendo de control. A este ritmo, pronto habrá más código en nuestras pruebas que en nuestra aplicación, y la repetición es poco estética en comparación con la elegante concisión del resto de nuestro código.

**No importa**. Déjales crecer. En su mayor parte, puede escribir una prueba una vez y luego olvidarse de ella. Continuará cumpliendo su función útil a medida que siga desarrollando su programa.

A veces, las pruebas necesitarán actualizarse. Supongamos que modificamos nuestras vistas para que solo se publiquen `Questions` con `Choices`. En ese caso, muchas de nuestras pruebas existentes fallarán, _indicándonos exactamente qué pruebas deben modificarse para actualizarlas_, por lo que en ese sentido las pruebas ayudan a autoatenderse.

En el peor de los casos, a medida que siga desarrollando, puede que encuentre que tiene algunas pruebas que ahora son redundantes. Incluso eso no es un problema; en pruebas, la redundancia es una _buena_ cosa.

Mientras sus pruebas estén adecuadamente organizadas, no se volverán inservibles. Buenas reglas generales incluyen tener:

- una `TestClass` separada para cada modelo o vista
- un método de prueba separado para cada conjunto de condiciones que desee probar
- nombres de métodos de prueba que describan su función
