# Criar um Novo Branch

Para este laboratório, faça um _fork_ do repositório Git chamado `https://github.com/labex-labs/git-playground` para sua conta do GitHub. Você está trabalhando em um projeto em um repositório Git chamado `https://github.com/your-username/git-playground`. Você precisa criar um novo _branch_ chamado `feature-1` para trabalhar em uma nova funcionalidade.

1. Clone o repositório, navegue até o diretório e configure a identidade:

```shell
git clone https://github.com/your-username/git-playground.git
cd git-playground
git config --global user.name "your-username"
git config --global user.email "your-email"
```

2. Verifique o _branch_ atual:

```shell
git branch
```

3. Crie um novo _branch_ chamado `feature-1`:

```shell
git checkout -b feature-1
```

4. Verifique se você está agora no _branch_ `feature-1`:

```shell
git branch
```

5. Envie as alterações para o repositório remoto:

```shell
git push -u origin feature-1
```

Isto é o que acontece quando você executa o comando `git branch -r`:

![git branch remote output](../assets/challenge-create-branch-step1-1.png)
