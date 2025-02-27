# Using Threads to Run Code Simultaneously

En la mayoría de los sistemas operativos actuales, el código de un programa ejecutado se ejecuta en un _proceso_, y el sistema operativo gestionará múltiples procesos a la vez. Dentro de un programa, también puede haber partes independientes que se ejecutan simultáneamente. Las características que ejecutan estas partes independientes se llaman _hilos_. Por ejemplo, un servidor web podría tener múltiples hilos para que pudiera responder a más de una solicitud al mismo tiempo.

Dividir el cálculo en su programa en múltiples hilos para ejecutar múltiples tareas al mismo tiempo puede mejorar el rendimiento, pero también agrega complejidad. Debido a que los hilos pueden ejecutarse simultáneamente, no hay ninguna garantía inherente sobre el orden en el que se ejecutarán las partes de su código en diferentes hilos. Esto puede dar lugar a problemas, como:

- Condiciones de carrera, donde los hilos acceden a datos o recursos en un orden inconsistente
- Bloqueos mortales, donde dos hilos se están esperando el uno al otro, impidiendo que ambos hilos continúen
- Errores que solo ocurren en ciertas situaciones y son difíciles de reproducir y corregir de manera confiable

Rust intenta mitigar los efectos negativos de utilizar hilos, pero la programación en un contexto multihilo todavía requiere un pensamiento cuidadoso y una estructura de código diferente a la de los programas que se ejecutan en un solo hilo.

Los lenguajes de programación implementan los hilos de varias maneras diferentes, y muchos sistemas operativos proporcionan una API que el lenguaje puede llamar para crear nuevos hilos. La biblioteca estándar de Rust utiliza un modelo _1:1_ de implementación de hilos, según el cual un programa utiliza un hilo del sistema operativo por cada hilo del lenguaje. Hay cajas que implementan otros modelos de subprocesamiento que realizan diferentes concesiones al modelo 1:1.
