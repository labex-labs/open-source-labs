# Visualizar um Resumo Curto dos Commits

Como desenvolvedor, você está trabalhando em um projeto com múltiplos contribuidores. Você precisa visualizar um resumo de todos os commits feitos no projeto para entender as alterações que foram feitas e identificar quaisquer problemas potenciais. No entanto, você não quer gastar muito tempo vasculhando todas as mensagens de commit para encontrar as informações que precisa.

Para visualizar um resumo curto de todos os commits feitos em um repositório Git, você pode usar o comando `git log --oneline`. Por exemplo, digamos que você esteja trabalhando em um projeto hospedado no GitHub chamado `git-playground`.

1. Você pode clonar o repositório para sua máquina local usando o seguinte comando:

```shell
git clone https://github.com/labex-labs/git-playground.git
```

2. Depois de clonar o repositório, navegue até o diretório do projeto e execute o seguinte comando para visualizar um resumo curto de todos os commits:

```shell
cd git-playground
git log --oneline
```

Isso exibirá uma lista de todos os commits feitos no repositório, juntamente com um resumo curto de cada mensagem de commit. Por exemplo:

```shell
d22f46b (HEAD -> master, origin/master, origin/feature-branch, origin/HEAD) Added file2.txt
cf80005 Added file1.txt
b00b937 Initial commit
```
