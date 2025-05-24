# Criar um Commit Fixup

Suponha que você esteja trabalhando em um projeto com vários outros desenvolvedores e perceba um pequeno erro em um commit que foi feito alguns dias atrás. Você quer corrigir o erro, mas não quer criar um novo commit e interromper o trabalho dos outros desenvolvedores. É aqui que os commits fixup são úteis. Ao criar um commit fixup, você pode fazer as alterações necessárias sem criar um novo commit, e o commit fixup será automaticamente mesclado com o commit original durante o próximo rebase.

Por exemplo, sua tarefa é escrever a string "hello,world" no arquivo `hello.txt` e adicioná-lo como um commit "fixup" ao commit com a mensagem "Added file1.txt", para que ele possa ser automaticamente mesclado em uma operação de rebase subsequente.

Para este laboratório, vamos usar o repositório de `https://github.com/labex-labs/git-playground`.

1. Clone o repositório, navegue até o diretório e configure a identidade:

```shell
git clone https://github.com/labex-labs/git-playground
cd git-playground
git config --global user.name "your-username"
git config --global user.email "your-email"
```

2. Crie um arquivo `hello.txt`, escreva "hello,world" nele e adicione-o à área de staging:

```shell
echo "hello,world" > hello.txt
git add .
```

3. Para criar um commit fixup, você pode usar o comando `git commit --fixup <commit>`:

```shell
git commit --fixup cf80005
# This is the hash of the commit message "Added file1.txt".
```

Isso criará um commit fixup para o commit especificado. Observe que você deve fazer o stage de suas alterações antes de criar o commit fixup.

4. Depois de criar o commit fixup, você pode usar o comando `git rebase --interactive --autosquash` para mesclar automaticamente o commit fixup com o commit original durante o próximo rebase. Por exemplo:

```shell
git rebase --interactive --autosquash HEAD~3
```

Ao abrir o editor interativo, você não precisa alterar o texto e salvar para sair. Isso executará um rebase nos últimos 3 commits e mesclará automaticamente quaisquer commits fixup com seus commits originais correspondentes.

Este é o resultado da execução do comando `git show HEAD~1`:

```shell
[object Object]
```
