# Cómo escribir pruebas

Las pruebas son funciones de Rust que verifican que el código no de prueba funcione de la manera esperada. Los cuerpos de las funciones de prueba generalmente realizan estas tres acciones:

- Configurar cualquier dato o estado necesario.
- Ejecutar el código que desea probar.
- Asegurarse de que los resultados sean los que se esperan.

Echemos un vistazo a las características que Rust proporciona específicamente para escribir pruebas que realicen estas acciones, que incluyen el atributo `test`, algunas macros y el atributo `should_panic`.
