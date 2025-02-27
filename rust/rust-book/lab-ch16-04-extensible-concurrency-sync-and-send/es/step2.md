# Permitiendo la transferencia de la propiedad entre hilos con Send

El rasgo marcador `Send` indica que la propiedad de valores del tipo que implementa `Send` puede transferirse entre hilos. Casi todos los tipos de Rust son `Send`, pero hay algunas excepciones, incluyendo `Rc<T>`: esto no puede ser `Send` porque si clonaras un valor `Rc<T>` e intentaras transferir la propiedad del clon a otro hilo, ambos hilos podrían actualizar la cuenta de referencias al mismo tiempo. Por esta razón, `Rc<T>` se implementa para su uso en situaciones de un solo hilo donde no desees pagar la penalización de rendimiento segura para hilos.

Por lo tanto, el sistema de tipos y los límites de rasgos de Rust aseguran que nunca puedas enviar accidentalmente un valor `Rc<T>` entre hilos de manera no segura. Cuando intentamos hacer esto en la Lista 16-14, obtuvimos el error `el rasgo`Send`no está implementado para`Rc\<Mutex`<i32>`{=html}\>\``. Cuando cambiamos a `Arc`<T>`{=html}`, que es `Send`, el código se compiló.

Cualquier tipo compuesto enteramente de tipos `Send` también se marca automáticamente como `Send`. Casi todos los tipos primitivos son `Send`, excepto los punteros crudos, que discutiremos en el Capítulo 19.
