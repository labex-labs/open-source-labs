# Git Cherry-Pick

Como desenvolvedor, você está trabalhando em um projeto com múltiplos ramos (branches). Você identificou uma alteração específica que foi feita em um _commit_ anterior que gostaria de aplicar ao seu ramo atual. No entanto, você não quer mesclar (merge) o ramo inteiro, pois ele contém outras alterações que você não precisa. Nesse cenário, você pode usar o comando `git cherry-pick` para aplicar a alteração específica ao seu ramo atual.

Para este laboratório, vamos usar o repositório de `https://github.com/labex-labs/git-playground`. Siga os passos abaixo para completar o desafio:

1. Clone o repositório, navegue até o diretório e configure a identidade:

```shell
git clone https://github.com/labex-labs/git-playground
cd git-playground
git config --global user.name "your-username"
git config --global user.email "your-email"
```

2. Crie e mude para um ramo chamado `one-branch`, crie um arquivo chamado `hello.txt`, escreva "hello,world" nele, adicione-o à área de _staging_ (preparação) e faça o _commit_ com a mensagem "add hello.txt":

```shell
git checkout -b one-branch
echo "hello,world" > hello.txt
git add .
git commit -m "add hello.txt"
```

3. Identifique o _hash_ do _commit_ criado no passo anterior para aplicar ao ramo `master`:

```shell
git log
```

4. Faça o _checkout_ do ramo `master` e aplique a alteração ao ramo `master`:

```shell
git checkout master
git cherry-pick 1609c283ec86ee4
```

5. Verifique se a alteração foi aplicada ao ramo `master`:

```shell
git log
```

Este é o resultado da execução de `git log` no ramo `master`:

```shell
ADD hello.txt
```
