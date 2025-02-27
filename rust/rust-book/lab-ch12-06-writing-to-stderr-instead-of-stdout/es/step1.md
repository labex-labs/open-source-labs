# Escribir mensajes de error en el error estándar en lugar de la salida estándar

En este momento, estamos escribiendo toda nuestra salida en la terminal utilizando la macro `println!`. En la mayoría de las terminales, hay dos tipos de salida: _salida estándar_ (`stdout`) para información general y _error estándar_ (`stderr`) para mensajes de error. Esta distinción permite a los usuarios elegir dirigir la salida exitosa de un programa a un archivo, pero aún así imprimir los mensajes de error en la pantalla.

La macro `println!` solo es capaz de imprimir en la salida estándar, por lo que tenemos que utilizar algo más para imprimir en el error estándar.
