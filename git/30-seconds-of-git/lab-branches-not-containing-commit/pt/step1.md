# Encontrar Branches que Não Contêm um Commit

Você está trabalhando em um projeto com múltiplos branches (branches), e precisa encontrar todos os branches que não contêm um commit específico. Isso pode ser útil se você quiser ter certeza de que uma determinada alteração foi aplicada a todos os branches, ou se você quiser saber quais branches estão desatualizados e precisam ser atualizados.

Para este laboratório, usaremos o repositório Git chamado `https://github.com/your-username/git-playground`.

1. Clone este repositório para sua máquina local usando o seguinte comando:

```shell
git clone https://github.com/your-username/git-playground.git
```

2. Após clonar o repositório, use os seguintes comandos para navegar até o diretório e configurar a identidade:

```shell
cd git-playground
git config --global user.name "your-username"
git config --global user.email "your-email"
```

3. Crie e mude para um branch `new-branch` e faça algumas alterações no código nesse branch e, em seguida, faça o commit, a mensagem do commit é "Create a new-branch branch":

```shell
git checkout -b new-branch
echo "hello,world" > file1.txt
git commit -am "Create a new-branch branch"
```

4. Verifique o hash da mensagem do commit "Create a new-branch branch":

```shell
git log
```

5. Encontre todos os branches que não contêm um hash com a mensagem do commit "Create a new-branch branch". Para fazer isso, podemos usar o seguinte comando:

```shell
git branch --no-contains 31c5ac20129151af1
```

Isso exibirá uma lista de todos os branches que não contêm o commit especificado. Neste caso, a saída será:

```shell
master
```

Isso significa que o branch `master` não contém o commit com o hash `31c5ac20129151af1`.
