# Permitir la transferencia de propiedad entre hilos con Send

El rasgo marcador `Send` indica que la propiedad de los valores del tipo que implementa `Send` puede ser transferida entre hilos. Casi todos los tipos de Rust son `Send`, pero hay algunas excepciones, incluyendo `Rc<T>`: este no puede ser `Send` porque si clonaras un valor `Rc<T>` e intentaras transferir la propiedad del clon a otro hilo, ambos hilos podrían actualizar el contador de referencias al mismo tiempo. Por esta razón, `Rc<T>` está implementado para su uso en situaciones de un solo hilo donde no quieres pagar la penalización de rendimiento de la seguridad de hilos.

Por lo tanto, el sistema de tipos y los límites de rasgos de Rust aseguran que nunca puedas enviar accidentalmente un valor `Rc<T>` a través de hilos de forma insegura. Cuando intentamos hacer esto en el Listado 16-14, obtuvimos el error `the trait Send is not implemented for Rc<Mutex<i32>>`. Cuando cambiamos a `Arc<T>`, que es `Send`, el código compiló.

Cualquier tipo compuesto enteramente por tipos `Send` se marca automáticamente como `Send` también. Casi todos los tipos primitivos son `Send`, aparte de los punteros sin procesar (raw pointers), que discutiremos en el Capítulo 19.
