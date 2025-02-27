# Usando Mutex para Permitir el Acceso a Datos de un Hilo a la Vez

_Mutex_ es la abreviatura de _mutual exclusion_ (exclusión mutua), ya que un mutex permite que solo un hilo acceda a ciertos datos en cualquier momento dado. Para acceder a los datos de un mutex, un hilo debe primero señalar que desea acceder pidiendo adquirir el _cerrojo_ del mutex. El cerrojo es una estructura de datos que es parte del mutex y que lleva un registro de quién tiene actualmente acceso exclusivo a los datos. Por lo tanto, el mutex se describe como _protegiendo_ los datos que contiene a través del sistema de bloqueo.

Los mutex tienen la reputación de ser difíciles de usar porque hay que recordar dos reglas:

1. Debes intentar adquirir el cerrojo antes de usar los datos.
2. Cuando hayas terminado con los datos que el mutex protege, debes desbloquear los datos para que otros hilos puedan adquirir el cerrojo.

Para una metáfora del mundo real de un mutex, imagina una mesa redonda en una conferencia con solo un micrófono. Antes de que un ponente pueda hablar, tiene que pedir o señalar que desea usar el micrófono. Cuando obtiene el micrófono, puede hablar durante el tiempo que desee y luego entregar el micrófono al siguiente ponente que solicite hablar. Si un ponente olvida entregar el micrófono cuando ha terminado con él, nadie más podrá hablar. Si la gestión del micrófono compartido sale mal, la mesa redonda no funcionará como se planeó.

La gestión de los mutex puede resultar increíblemente complicada de hacer bien, lo que es por lo que mucha gente está entusiasmada por los canales. Sin embargo, gracias al sistema de tipos y las reglas de propiedad de Rust, no se puede equivocar al bloquear y desbloquear.
