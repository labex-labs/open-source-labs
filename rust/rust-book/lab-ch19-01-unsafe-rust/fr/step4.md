# Appeler une fonction ou une méthode non sécurisée

Le second type d'opération que vous pouvez effectuer dans un bloc `unsafe` est d'appeler des fonctions non sécurisées. Les fonctions et les méthodes non sécurisées ressemblent exactement à des fonctions et des méthodes normales, mais elles ont un `unsafe` supplémentaire avant le reste de la définition. Le mot clé `unsafe` dans ce contexte indique que la fonction a des exigences que nous devons respecter lorsque nous appelons cette fonction, car Rust ne peut pas garantir que nous avons rencontré ces exigences. En appelant une fonction non sécurisée à l'intérieur d'un bloc `unsafe`, nous disons que nous avons lu la documentation de cette fonction et que nous prenons la responsabilité de respecter les contrats de la fonction.

Voici une fonction non sécurisée nommée `dangerous` qui ne fait rien dans son corps :

    unsafe fn dangerous() {}

    unsafe {
        dangerous();
    }

Nous devons appeler la fonction `dangerous` à l'intérieur d'un bloc `unsafe` séparé. Si nous essayons d'appeler `dangerous` sans le bloc `unsafe`, nous obtiendrons une erreur :

```bash
error[E0133]: call to unsafe function is unsafe and requires
unsafe function or block
 --> src/main.rs:4:5
  |
4 |     dangerous();
  |     ^^^^^^^^^^^ call to unsafe function
  |
  = note: consult the function's documentation for information on
how to avoid undefined behavior
```

Avec le bloc `unsafe`, nous affirmons à Rust que nous avons lu la documentation de la fonction, que nous comprenons comment l'utiliser correctement et que nous avons vérifié que nous respectons le contrat de la fonction.

Les corps de fonctions non sécurisées sont en fait des blocs `unsafe`, donc pour effectuer d'autres opérations non sécurisées à l'intérieur d'une fonction non sécurisée, nous n'avons pas besoin d'ajouter un autre bloc `unsafe`.
