# Secciones Comúnmente Utilizadas

Usamos el encabezado de Markdown `# Ejemplos` en la Lista 14-1 para crear una sección en el HTML con el título "Ejemplos". Aquí hay algunas otras secciones que los autores de cajas suelen utilizar en su documentación:

- **Panics**: Los escenarios en los que la función que se está documentando podría causar un panic. Los llamantes de la función que no quieren que su programa se detenga con un panic deben asegurarse de no llamar a la función en estas situaciones.
- **Errores**: Si la función devuelve un `Result`, describir los tipos de errores que pueden ocurrir y las condiciones que pueden causar que se devuelvan esos errores puede ser útil para los llamantes, para que puedan escribir código para manejar los diferentes tipos de errores de diferentes maneras.
- **Seguridad**: Si la función es `unsafe` para llamar (discutiremos la inseguridad en el Capítulo 19), debe haber una sección que explique por qué la función es insegura y cubra las invariantes que la función espera que los llamantes mantengan.

La mayoría de los comentarios de documentación no necesitan todas estas secciones, pero esta es una buena lista de verificación para recordarte los aspectos de tu código en los que los usuarios estarán interesados en saber.
