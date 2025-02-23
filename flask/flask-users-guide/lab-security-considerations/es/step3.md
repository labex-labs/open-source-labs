# Seguridad de JSON

En Flask, es importante garantizar la seguridad de las respuestas JSON. En versiones anteriores a la 0.10 de Flask, los arrays de nivel superior no se serializaban a JSON debido a una vulnerabilidad de seguridad. Sin embargo, este comportamiento ha cambiado y ahora los arrays de nivel superior se serializan. Se recomienda utilizar la última versión de Flask para aprovechar esta mejora de seguridad.
