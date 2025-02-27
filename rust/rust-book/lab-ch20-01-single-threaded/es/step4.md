# Un vistazo más detallado a una solicitud HTTP

HTTP es un protocolo basado en texto, y una solicitud tiene este formato:

    Método URI-de-solicitud Versión-HTTP CRLF
    encabezados CRLF
    cuerpo-del-mensaje

La primera línea es la _línea de solicitud_ que contiene información sobre lo que el cliente está solicitando. La primera parte de la línea de solicitud indica el _método_ que se está utilizando, como `GET` o `POST`, que describe cómo el cliente está realizando esta solicitud. Nuestro cliente utilizó una solicitud `GET`, lo que significa que está pidiendo información.

La siguiente parte de la línea de solicitud es _/_, que indica el _identificador de recurso uniforme_ _(URI)_ que el cliente está solicitando: un URI es casi, pero no exactamente, lo mismo que un _localizador de recurso uniforme_ _(URL)_. La diferencia entre URIs y URLs no es importante para nuestros propósitos en este capítulo, pero la especificación HTTP utiliza el término _URI_, así que podemos simplemente sustituir mentalmente _URL_ por _URI_ aquí.

La última parte es la versión de HTTP que el cliente utiliza, y luego la línea de solicitud termina en una secuencia CRLF. (CRLF significa _retorno de carro_ y _salto de línea_, que son términos de los días de la máquina de escribir!) La secuencia CRLF también se puede escribir como `\r\n`, donde `\r` es un retorno de carro y `\n` es un salto de línea. La _secuencia CRLF_ separa la línea de solicitud del resto de los datos de la solicitud. Tenga en cuenta que cuando se imprime la CRLF, vemos que comienza una nueva línea en lugar de `\r\n`.

Mirando los datos de la línea de solicitud que recibimos al ejecutar nuestro programa hasta ahora, vemos que `GET` es el método, _/_ es el URI de solicitud y `HTTP/1.1` es la versión.

Después de la línea de solicitud, las líneas restantes que empiezan por `Host:` en adelante son encabezados. Las solicitudes `GET` no tienen cuerpo.

Intente hacer una solicitud desde un navegador diferente o pedir una dirección diferente, como _127.0.0.1:7878/test_, para ver cómo cambian los datos de la solicitud.

Ahora que sabemos lo que el navegador está pidiendo, ¡vamos a enviar algunos datos de vuelta!
