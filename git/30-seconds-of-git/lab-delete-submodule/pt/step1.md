# Deletar um Submódulo

Você tem um repositório Git que inclui um submódulo chamado `sha1collisiondetection`. Você deseja deletar este submódulo do seu repositório.

Para este laboratório, usaremos o repositório Git chamado `https://github.com/git/git`. Este repositório inclui um submódulo chamado `sha1collisiondetection`.

Para deletar o submódulo `sha1collisiondetection` do repositório, siga estes passos:

1.  Abra seu terminal e navegue até o diretório raiz do seu repositório Git:
    ```
    cd git
    ```
2.  Execute o seguinte comando para desregistrar o submódulo `sha1collisiondetection`:
    ```
    git submodule deinit -f -- sha1collisiondetection
    ```
3.  Execute o seguinte comando para remover o diretório do submódulo `sha1collisiondetection`:
    ```
    rm -rf .git/modules/sha1collisiondetection
    ```
4.  Execute o seguinte comando para remover a _working tree_ (árvore de trabalho) do submódulo `sha1collisiondetection`:
    ```
    git rm -f sha1collisiondetection
    ```

Após estes passos, o submódulo `sha1collisiondetection` será removido do seu repositório Git. Se você executar o comando `git submodule status`, não obterá nenhuma informação sobre o submódulo.
