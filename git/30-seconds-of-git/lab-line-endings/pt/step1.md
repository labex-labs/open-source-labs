# Configurar Quebras de Linha (Line Endings)

Você está trabalhando em um projeto com uma equipe de desenvolvedores e percebe que alguns membros da equipe estão usando diferentes quebras de linha (line endings) do que outros. Isso pode causar problemas ao mesclar código e pode levar a conflitos. Você precisa configurar as quebras de linha para o repositório para garantir a consistência e evitar conflitos.

Em sistemas Unix ou semelhantes ao Unix, cada linha de texto termina com o terminador de linha `LF` (Line Feed). Quando você usa o comando `cat` para visualizar um arquivo, os terminadores de linha normalmente não são exibidos na tela porque são considerados o fim da linha, não parte da linha.

Ao visualizar um arquivo com o comando `cat -vet`, a opção `-v` exibe caracteres não imprimíveis como sequências de caracteres visíveis, como o símbolo `$`. Portanto, se você vir o símbolo `$` em um arquivo, isso significa que cada linha no arquivo termina com o terminador de linha `LF`. `LF` e `\n` são o mesmo conceito, indicando um terminador de linha.

Para configurar as quebras de linha para o repositório `git-playground`, siga estas etapas:

1.  Abra o prompt de comando ou terminal no seu computador.
2.  Navegue até o diretório onde o repositório `git-playground` está localizado no diretório `~/project`.
3.  Execute o seguinte comando para configurar as quebras de linha para usar as quebras de linha UNIX:

    ```shell
    git config core.eol lf
    ```

    Isso configurará as quebras de linha para usar a quebra de linha UNIX (`\n`).

4.  Execute o seguinte comando para verificar se as quebras de linha foram configuradas corretamente:

    ```shell
    git config core.eol
    ```

    Isso exibirá a configuração atual das quebras de linha.

Este é o resultado da execução de `cat -vet file2.txt`:

```shell
This is file2.$
```
