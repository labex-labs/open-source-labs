# ブランチ間の違い

あなたはチームでプロジェクトを進めており、新機能を開発するために `feature-1` という名前のブランチを作成しました。同僚も別の機能を開発するために `feature-2` という名前のブランチを作成しました。あなたは 2 つのブランチ間の変更を比較して、追加、修正、または削除された内容を確認したいと思っています。2 つのブランチ間の違いをどのように表示できますか？

あなたの GitHub アカウントが `https://github.com/labex-labs/git-playground.git` から `git-playground` というリポジトリをクローンしているとします。以下の手順に従ってください。

1. `cd git-playground` コマンドを使ってリポジトリのディレクトリに移動します。
2. `git config --global user.name "Your Name"` および `git config --global user.email "your@email.com"` コマンドを使って、この環境で GitHub アカウントを設定します。
3. `git checkout -b feature-1` コマンドを使って `feature-1` ブランチを作成して切り替え、`README.md` ファイルに "hello" を追加し、ステージングエリアに追加してコミットします。コミットメッセージは "Add new content to README.md" で、`echo "hello" >> README.md `、`git add.`、および `git commit -am "Add new content to README.md"` コマンドを使います。
4. `master` ブランチに戻ります。
5. `git checkout -b feature-2` コマンドを使って `feature-2` ブランチを作成して切り替え、`index.html` ファイルに "world" を追加し、ステージングエリアに追加してコミットします。コミットメッセージは "Update index.html file" で、`echo "world" > index.htm`、`git add.`、および `git commit -am "Update index.html file"` コマンドを使います。
6. `git diff feature-1..feature-2` コマンドを使って 2 つのブランチ間の違いを表示します。

出力には `feature-1` と `feature-2` ブランチ間の違いが表示されます。これが最終結果の見た目を示しています。

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
