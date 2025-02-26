# Leyendo Atributos con Herencia

Lógicamente, el proceso de encontrar un atributo es el siguiente. Primero, verifica en `__dict__` local. Si no se encuentra, busca en `__dict__` de la clase. Si no se encuentra en la clase, busca en las clases base a través de `__bases__`. Sin embargo, hay algunos aspectos sutiles de esto que se discuten a continuación.
