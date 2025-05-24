# Clonar Submódulos Ausentes

Você está trabalhando em um projeto que contém submódulos. Quando você clona o projeto, os submódulos não são clonados automaticamente. Isso causa problemas ao tentar construir ou executar o projeto. Você precisa clonar os submódulos ausentes e fazer checkout dos commits corretos.

Para este laboratório, usaremos o repositório Git chamado `https://github.com/git/git`. Este repositório contém submódulos que não são clonados automaticamente quando você clona o repositório.

Para clonar os submódulos ausentes e fazer checkout dos commits corretos, siga estes passos:

1.  Entre no diretório do repositório:
    ```
    cd git
    ```
2.  Inicialize os submódulos:
    ```
    git submodule update --init --recursive
    ```
3.  Faça checkout para o commit correto do submódulo, ou seja, a branch `master`:
    ```
    git submodule foreach git checkout master
    ```
    Aqui está o resultado final:

```shell
Submodule 'sha1collisiondetection' (https://github.com/cr-marcstevens/sha1collisiondetection.git) registered for path 'sha1collisiondetection'
Cloning into '/home/labex/project/git/sha1collisiondetection'...
Submodule path 'sha1collisiondetection': checked out '855827c583bc30645ba427885caa40c5b81764d2'
```
