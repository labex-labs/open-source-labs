# Buscar as Últimas Alterações do Remoto

Suponha que você esteja trabalhando em um projeto com uma equipe de desenvolvedores, e o projeto está armazenado em um repositório remoto. Você deseja obter as últimas alterações do repositório remoto sem aplicá-las ao seu repositório local. É aqui que o comando `git fetch` é útil.

O comando `git fetch` baixa as últimas alterações do repositório remoto para o seu repositório local, mas não as aplica ao seu diretório de trabalho. Isso significa que você pode revisar as alterações antes de mesclá-las em seu repositório local.

Para demonstrar como buscar as últimas alterações de um repositório remoto, usaremos o repositório Git `git-playground` da sua conta do GitHub, que vem de um fork de `https://github.com/labex-labs/git-playground.git`. Siga os passos abaixo:

1. Clone o repositório, navegue até o diretório:

```shell
git clone https://github.com/your-username/git-playground.git
cd git-playground
```

2. Encontre o repositório `git-playground` em sua conta no site do Github, crie e mude para um branch chamado `fetch-branch`, crie um arquivo chamado `hello.txt`, adicione "hello, world" e faça o commit com a mensagem "Create hello.txt".
3. Visualize os branches em repositórios remotos:

```shell
git branch -r
```

4. Busque as últimas alterações do repositório remoto:

```shell
git fetch
```

5. Visualize os branches em repositórios remotos novamente e verifique se as últimas alterações foram buscadas:

```shell
git branch -r
git log origin/fetch-branch
```

Isso mostrará os últimos commits no branch `origin/fetch-branch`. Este é o resultado da execução de `git log origin/fetch-branch`:

```shell
commit f3125b4c99e0ef2ce58bc0b1287c966c9e68c577 (origin/fetch-branch)
Author: xiaoshengyunan <131872312+xiaoshengyunan@users.noreply.github.com>
Date:   Thu Jul 20 20:17:23 2023 +0800

    Create hello.txt
```
