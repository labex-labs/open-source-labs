# Adicionar um Submódulo (Submodule)

Sua tarefa é adicionar um novo submódulo a um repositório Git. Você precisará usar o comando `git submodule add` para adicionar o submódulo de um repositório upstream para um diretório local em seu repositório. A sintaxe do comando é a seguinte:

```shell
git submodule add <upstream-path> <local-path>
```

- `<upstream-path>` é a URL ou o caminho para o repositório upstream que você deseja adicionar como um submódulo.
- `<local-path>` é o caminho onde você deseja armazenar o submódulo em seu repositório local.

Suponha que você tenha um repositório Git chamado `meu-projeto` e queira adicionar um submódulo do repositório Git `https://github.com/labex-labs/git-playground.git` a um diretório chamado `git-playground` em seu repositório local. Veja como você pode fazer isso:

```shell
git init my-project
cd my-project
git submodule add https://github.com/labex-labs/git-playground.git ./git-playground
```

Este é o resultado após concluir o laboratório:

![Git submodule add result](../assets/challenge-add-submodule-step1-1.png)
