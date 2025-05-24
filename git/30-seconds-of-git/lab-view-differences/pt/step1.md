# Visualizar Diferenças nas Alterações

Como desenvolvedor, você pode querer visualizar as diferenças entre suas alterações _staged_ ou _unstaged_ e o último _commit_. Isso é útil quando você deseja revisar suas alterações antes de confirmá-las ou quando deseja ver quais alterações você fez desde o último _commit_.

Para demonstrar como visualizar as diferenças nas alterações, usaremos o repositório `git-playground`. Suponha que você tenha feito algumas alterações no arquivo `README.md` e queira visualizar as diferenças entre suas alterações e o último _commit_.

1. Abra seu terminal e navegue até o diretório `git-playground`:

```shell
cd git-playground
```

2. Use o comando `git diff` para visualizar as diferenças entre suas alterações _unstaged_ e o último _commit_:

```shell
git diff
```

3. Alternativamente, você pode usar a opção `--staged` para visualizar as diferenças entre suas alterações _staged_ e o último _commit_:

```shell
git diff --staged
```

Este é o resultado da conclusão da etapa 2:

```
diff --git a/file1.txt b/file1.txt
index bfccc4a..ee23125 100644
--- a/file1.txt
+++ b/file1.txt
@@ -1 +1,2 @@
 This is file1.
+hello,labex
```

Este é o resultado da conclusão da etapa 3:

```
diff --git a/README.md b/README.md
index 0164284..f47591b 100644
--- a/README.md
+++ b/README.md
@@ -1,2 +1,3 @@
 # git-playground
 Git Playground
+hello,world
```
