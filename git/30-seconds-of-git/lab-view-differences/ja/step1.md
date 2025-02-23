# 変更の違いを表示する

開発者として、ステージング済みまたはステージングされていない変更と最後のコミットの違いを表示したい場合があります。これは、コミットする前に変更を確認したいときや、最後のコミット以降に行った変更を確認したいときに便利です。

変更の違いを表示する方法を示すために、`git-playground` リポジトリを使用します。`README.md` ファイルにいくつかの変更を加え、変更と最後のコミットの違いを表示したいとします。

1. ターミナルを開き、`git-playground` ディレクトリに移動します。

```shell
cd git-playground
```

2. `git diff` コマンドを使用して、ステージングされていない変更と最後のコミットの違いを表示します。

```shell
git diff
```

3. 代わりに、`--staged` オプションを使用して、ステージング済みの変更と最後のコミットの違いを表示することもできます。

```shell
git diff --staged
```

これがステップ 2 を完了した結果です。

```
diff --git a/file1.txt b/file1.txt
index bfccc4a..ee23125 100644
--- a/file1.txt
+++ b/file1.txt
@@ -1 +1,2 @@
 This is file1.
+hello,labex
```

これがステップ 3 を完了した結果です。

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
