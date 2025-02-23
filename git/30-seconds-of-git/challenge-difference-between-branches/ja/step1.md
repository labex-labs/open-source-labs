# ブランチ間の違い

あなたはチームでプロジェクトを行っており、新機能を開発するために `feature-1` という名前のブランチを作成しました。同僚も別の機能を開発するために `feature-2` という名前のブランチを作成しました。あなたは 2 つのブランチ間の変更を比較して、追加、修正、または削除された内容を確認したいと思っています。2 つのブランチ間の違いをどのように表示できますか？

## タスク

あなたの GitHub アカウントから `https://github.com/labex-labs/git-playground.git` から `git-playground` という名前のリポジトリをクローンしてください。

1. リポジトリディレクトリに移動し、GitHub の ID を設定します。
2. `feature-1` ブランチに切り替え、`README.md` ファイルに "hello" を追加し、ステージングエリアに追加してコミットします。コミットメッセージは "Add new content to README.md" です。
3. `feature-2` ブランチに切り替え、`index.html` ファイルに "world" を追加し、ステージングエリアに追加してコミットします。コミットメッセージは "Update index.html file" です。
4. 2 つのブランチ間の違いを表示します。

出力には、`feature-1` と `feature-2` ブランチ間の違いが表示されます。これが最終結果の見た目を示しています：

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
