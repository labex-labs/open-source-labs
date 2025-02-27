# Construyendo un servidor web de un solo hilo

Comenzaremos haciendo que funcione un servidor web de un solo hilo. Antes de comenzar, echemos un vistazo rápido a una descripción general de los protocolos implicados en la construcción de servidores web. Los detalles de estos protocolos están fuera del alcance de este libro, pero una descripción general les dará la información que necesitan.

Los dos principales protocolos implicados en los servidores web son el _Hypertext Transfer Protocol_ _(HTTP)_ y el _Transmission Control Protocol_ _(TCP)_. Ambos protocolos son de tipo _solicitud-respuesta_, lo que significa que un _cliente_ inicia solicitudes y un _servidor_ escucha las solicitudes y proporciona una respuesta al cliente. El contenido de esas solicitudes y respuestas está definido por los protocolos.

TCP es el protocolo de nivel inferior que describe los detalles de cómo la información llega de un servidor a otro pero no especifica cuál es esa información. HTTP se basa en TCP definiendo el contenido de las solicitudes y respuestas. En principio, es posible utilizar HTTP con otros protocolos, pero en la gran mayoría de los casos, HTTP envía sus datos a través de TCP. Trabajaremos con los bytes crudos de las solicitudes y respuestas de TCP y HTTP.
