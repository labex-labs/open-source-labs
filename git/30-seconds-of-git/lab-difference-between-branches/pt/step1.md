# Diferença Entre Branches

Você tem trabalhado em um projeto com sua equipe e criou uma branch chamada `feature-1` para trabalhar em uma nova funcionalidade. Seu colega também criou uma branch chamada `feature-2` para trabalhar em uma funcionalidade diferente. Você quer comparar as alterações entre as duas branches para ver o que foi adicionado, modificado ou excluído. Como você pode visualizar a diferença entre as duas branches?

Suponha que sua conta do GitHub clone um repositório chamado `git-playground` de `https://github.com/labex-labs/git-playground.git`. Siga os passos abaixo:

1.  Mude para o diretório do repositório usando o comando `cd git-playground`.
2.  Configure sua conta do GitHub neste ambiente usando os comandos `git config --global user.name "Seu Nome"` e `git config --global user.email "seu@email.com"`.
3.  Crie e mude para a branch `feature-1` usando o comando `git checkout -b feature-1`, adicione "hello" ao arquivo `README.md`, adicione-o à área de staging (staging area) e faça o commit, com a mensagem de commit "Add new content to README.md" usando os comandos `echo "hello" >> README.md `, `git add .` e `git commit -am "Add new content to README.md"`.
4.  Volte para a branch `master`.
5.  Crie e mude para a branch `feature-2` usando o comando `git checkout -b feature-2`, adicione "world" ao arquivo `index.html`, adicione-o à área de staging e faça o commit, com a mensagem de commit "Update index.html file" usando os comandos `echo "world" > index.htm`, `git add .` e `git commit -am "Update index.html file"`.
6.  Visualize a diferença entre as duas branches usando o comando `git diff feature-1..feature-2`.

A saída deve exibir a diferença entre as branches `feature-1` e `feature-2`. Isso mostra como o resultado final ficará:

```shell
diff --git a/README.md b/README.md
index b66215f..0164284 100644
--- a/README.md
+++ b/README.md
@@ -1,3 +1,2 @@
# git-playground
Git Playground
-hello
diff --git a/index.html b/index.html
new file mode 100644
index 0000000..cc628cc
--- /dev/null
+++ b/index.html
@@ -0,0 +1 @@
+world
```
