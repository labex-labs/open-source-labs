# Organización de las Pruebas

Como se mencionó al principio del capítulo, la prueba es una disciplina compleja y diferentes personas utilizan diferentes terminologías y organizaciones. La comunidad de Rust piensa en las pruebas en términos de dos categorías principales: pruebas unitarias e integración. Las **pruebas unitarias** son pequeñas y más enfocadas, probando un módulo aisladamente a la vez y pueden probar interfaces privadas. Las **pruebas de integración** son completamente externas a su biblioteca y utilizan su código de la misma manera que cualquier otro código externo, utilizando solo la interfaz pública y posiblemente probando múltiples módulos por cada prueba.

Es importante escribir ambos tipos de pruebas para asegurarse de que las piezas de su biblioteca estén haciendo lo que se espera que hagan, por separado y juntas.
