# Rc`<T>`{=html}, el puntero inteligente con conteo de referencias

En la mayoría de los casos, la propiedad es clara: sabes exactamente qué variable posee un valor dado. Sin embargo, hay casos en los que un solo valor puede tener múltiples propietarios. Por ejemplo, en las estructuras de datos de gráficos, múltiples aristas pueden apuntar al mismo nodo, y ese nodo es conceptualmente propiedad de todas las aristas que apuntan a él. Un nodo no debe ser eliminado a menos que no tenga ninguna arista apuntando a él y, por lo tanto, no tenga propietarios.

Tienes que habilitar la propiedad múltiple explícitamente mediante el uso del tipo Rust `Rc<T>`, que es una abreviatura de _conteo de referencias_. El tipo `Rc<T>` lleva un registro del número de referencias a un valor para determinar si el valor todavía está en uso. Si no hay referencias a un valor, el valor se puede eliminar sin que ninguna referencia quede invalida.

Imagina `Rc<T>` como un televisor en una sala familiar. Cuando una persona entra a ver la televisión, la enciende. Otros pueden entrar a la habitación y ver la televisión. Cuando la última persona sale de la habitación, apaga el televisor porque ya no se está utilizando. Si alguien apaga el televisor mientras otros todavía están viéndolo, habría un alboroto de los demás espectadores de televisión.

Usamos el tipo `Rc<T>` cuando queremos asignar algunos datos en el montón para que múltiples partes de nuestro programa los lean y no podemos determinar en tiempo de compilación qué parte terminará usando los datos por última vez. Si supiéramos qué parte terminaría última, simplemente podríamos hacer que esa parte fuera la propietaria de los datos, y las reglas normales de propiedad aplicadas en tiempo de compilación entraría en vigor.

Tenga en cuenta que `Rc<T>` solo se puede usar en escenarios de un solo subproceso. Cuando discutamos la concurrencia en el Capítulo 16, cubriremos cómo hacer conteo de referencias en programas multihilo.
