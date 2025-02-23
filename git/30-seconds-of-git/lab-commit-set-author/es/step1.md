# Crear un commit con un autor diferente

Supongamos que estás trabajando en un proyecto con un equipo de desarrolladores y que uno de tus compañeros de equipo ha realizado algunos cambios en el código. Sin embargo, no está disponible para hacer el commit de los cambios por sí mismo y necesitas hacerlo en su nombre. En este escenario, puedes usar la opción `--author` para cambiar el nombre y el correo electrónico del autor del commit. Esta opción es útil cuando necesitas atribuir un commit a una persona diferente, por ejemplo, cuando estás realizando un commit de código en nombre de un compañero de trabajo que está de vacaciones o de licencia médica.

Para crear un commit con un autor diferente, puedes usar el siguiente comando:

```shell
git commit -m < mensaje > --author="<nombre> <correo electrónico>"
```

Digamos que estás trabajando en un proyecto alojado en el repositorio `https://github.com/labex-labs/git-playground`. Has realizado algunos cambios en el código y necesitas crear un commit en nombre de tu compañero de trabajo, John Doe, quien no está disponible para hacer el commit de los cambios por sí mismo. Para hacer esto, puedes usar el siguiente comando:

```shell
git clone https://github.com/labex-labs/git-playground
cd git-playground
git config --global user.email "tu correo electrónico"
git config --global user.name "tu nombre de usuario"
echo "Corrige el error de red" > README.md
git add.
git commit -m "Corrige el error" --author="John Doe <john.doe@example.com>"
```

Este comando creará un nuevo commit con el mensaje "Corrige el error" y lo atribuirá a John Doe.

Este es el resultado final:

![Git commit author change result](../assets/challenge-commit-set-author-step1-1.png)
