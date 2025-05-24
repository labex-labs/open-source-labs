# Visualizar um Resumo Curto de Commits sem Merge Commits

Você tem trabalhado em um projeto com vários outros desenvolvedores e deseja ver um resumo de todos os commits feitos no repositório. No entanto, você não quer ver os commits de merge, pois eles não contêm nenhuma alteração real no código. Como você pode visualizar um resumo de todos os commits, excluindo os commits de merge?

Para este laboratório, vamos usar o repositório de `https://github.com/labex-labs/git-playground`.

1. Clone o repositório, navegue até o diretório e configure a identidade:

```shell
git clone https://github.com/labex-labs/git-playground
cd git-playground
git config --global user.name "your-username"
git config --global user.email "your-email"
```

2. Crie e mude para um branch chamado `feature1`, crie um arquivo chamado `file.txt` e escreva `feature 1` nele, adicione-o à área de staging e faça o commit com a mensagem "Add feature 1":

```shell
git checkout -b feature1
echo "Feature 1" >> file.txt
git add .
git commit -m "Add feature 1"
```

3. Volte para o branch `master`, faça o merge do branch `feature1`, desabilite o forward merge, salve e saia sem alterar o texto:

```shell
git checkout master
git merge --no-ff feature1
```

4. Visualize um resumo curto de todos os commits, excluindo os commits de merge:

```shell
git log --oneline --no-merges
```

Isso exibirá uma lista de todos os commits feitos no repositório, excluindo quaisquer commits de merge. A saída será algo parecido com isto:

```shell
430b986 (feature1) Add feature 1
d22f46b (origin/master, origin/HEAD) Added file2.txt
cf80005 Added file1.txt
b00b937 Initial commit
```
