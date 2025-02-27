# Pruebas Unitarias

El propósito de las pruebas unitarias es probar cada unidad de código de manera aislada del resto del código para localizar rápidamente dónde el código está y no está funcionando como se esperaba. Colocará las pruebas unitarias en el directorio `src` en cada archivo con el código que están probando. La convención es crear un módulo llamado `tests` en cada archivo para contener las funciones de prueba y anotar el módulo con `cfg(test)`.
