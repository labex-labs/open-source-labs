# Usando Box`<T>` para apuntar a datos en el montón

El puntero inteligente más sencillo es una _caja_, cuyo tipo se escribe `Box<T>`. Las cajas te permiten almacenar datos en el montón en lugar de la pila. Lo que queda en la pila es el puntero a los datos del montón. Consulte el Capítulo 4 para revisar la diferencia entre la pila y el montón.

Las cajas no tienen sobrecarga de rendimiento, aparte de almacenar sus datos en el montón en lugar de la pila. Pero tampoco tienen muchas capacidades adicionales. Las usarás con más frecuencia en estas situaciones:

- Cuando tienes un tipo cuyo tamaño no se puede conocer en tiempo de compilación y quieres usar un valor de ese tipo en un contexto que requiere un tamaño exacto
- Cuando tienes una gran cantidad de datos y quieres transferir la propiedad pero asegurarte de que los datos no se copien cuando lo haces
- Cuando quieres poseer un valor y solo te importa que sea un tipo que implemente un determinado trato en lugar de ser de un tipo específico

Demostraremos la primera situación en "Habilitando tipos recursivos con cajas". En el segundo caso, transferir la propiedad de una gran cantidad de datos puede llevar mucho tiempo porque los datos se copian por la pila. Para mejorar el rendimiento en esta situación, podemos almacenar la gran cantidad de datos en el montón en una caja. Luego, solo la pequeña cantidad de datos de puntero se copia por la pila, mientras que los datos a los que hace referencia permanecen en un lugar del montón. El tercer caso se conoce como _objeto de trato_, y "Usando objetos de trato que permiten valores de diferentes tipos" se dedica a ese tema. ¡Así que lo que aprendes aquí lo aplicarás nuevamente en esa sección!
