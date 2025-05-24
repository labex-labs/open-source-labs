# Criar um commit por um autor diferente

Suponha que você esteja trabalhando em um projeto com uma equipe de desenvolvedores, e um dos membros da sua equipe fez algumas alterações no código. No entanto, eles não estão disponíveis para fazer o commit das alterações, e você precisa criar um commit em seu nome. Nesse cenário, você pode usar a opção `--author` para alterar o nome e o e-mail do autor do commit. Essa opção é útil quando você precisa atribuir um commit a uma pessoa diferente, como quando você está fazendo o commit do código em nome de um colega que está de férias ou de licença médica.

Para criar um commit por um autor diferente, você pode usar o seguinte comando:

```shell
git commit -m < message > --author="<name> <email>"
```

Digamos que você esteja trabalhando em um projeto hospedado no repositório `https://github.com/labex-labs/git-playground`. Você fez algumas alterações no código e precisa criar um commit em nome do seu colega, John Doe, que não está disponível para fazer o commit das alterações. Para fazer isso, você pode usar o seguinte comando:

```shell
git clone https://github.com/labex-labs/git-playground
cd git-playground
git config --global user.email "your email"
git config --global user.name "your username"
echo "Fix the network bug" > README.md
git add .
git commit -m "Fix the bug" --author="John Doe <john.doe@example.com>"
```

Este comando criará um novo commit com a mensagem "Fix the bug" e o atribuirá a John Doe.

Este é o resultado final:

![Git commit author change result](../assets/challenge-commit-set-author-step1-1.png)
