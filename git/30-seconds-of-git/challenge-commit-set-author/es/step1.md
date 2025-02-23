# Crear un commit con un autor diferente

Supongamos que estás trabajando en un proyecto con un equipo de desarrolladores y que uno de tus compañeros de equipo ha realizado algunos cambios en el código. Sin embargo, no está disponible para hacer el commit de los cambios por sí mismo y necesitas hacerlo en su nombre. En este escenario, puedes usar la opción `--author` para cambiar el nombre y el correo electrónico del autor del commit. Esta opción es útil cuando necesitas atribuir un commit a una persona diferente, por ejemplo, cuando estás realizando un commit de código en nombre de un compañero de trabajo que está de vacaciones o de licencia médica.

## Tareas

Digamos que estás trabajando en un proyecto alojado en el repositorio `https://github.com/labex-labs/git-playground`. Has realizado algunos cambios en el código, por ejemplo, se ha agregado "Corregir el error" al archivo `README.md` en tu cuenta de GitHub, y necesitas hacer un commit en nombre de tu compañero John Doe, quien no puede hacer estos cambios por sí mismo.

Este comando creará un nuevo commit con el mensaje "Corregir el error" y lo atribuirá a John Doe:

![Git commit author command](../assets/challenge-commit-set-author-step1-1.png)
