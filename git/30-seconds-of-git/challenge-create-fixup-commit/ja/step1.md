# fixup コミットを作成する

他の数人の開発者と共同作業をしているプロジェクトに取り組んでいるとしましょう。数日前に作成されたコミットに小さなエラーがあることに気付きました。エラーを修正したいのですが、新しいコミットを作成して他の開発者の作業を混乱させたくありません。このときに便利なのが fixup コミットです。fixup コミットを作成することで、新しいコミットを作成することなく必要な変更を加えることができ、次の rebase の際に fixup コミットは自動的に元のコミットにマージされます。

## タスク

あなたのタスクは、文字列 "hello,world" を `hello.txt` ファイルに書き込み、メッセージ "Added file1.txt" のコミットに対して "fixup" コミットとして追加することです。これにより、後続の rebase 操作で自動的にマージされるようになります。

このチャレンジでは、`https://github.com/labex-labs/git-playground` のリポジトリを使用しましょう。

1. ディレクトリに移動して ID を設定します。
2. `hello.txt` ファイルを作成し、その中に "hello,world" を書き込み、ステージング エリアに追加します。
3. "Added file1.txt" コミット メッセージのハッシュに対して fixup コミットを作成します。
4. fixup コミットを作成したら、次の rebase の際に fixup コミットを元のコミットと自動的にマージできます。対話型エディタを開いたときは、テキストを変更せずに保存して終了します。

これが `git show HEAD~1` コマンドを実行した結果です：

```shell
commit 6f0b8bbfac939af197a44ecd287ef84153817e9d
Author: Hang <huhuhang@users.noreply.github.com>
Date:   Wed Apr 26 14:16:25 2023 +0800

    Added file1.txt

diff --git a/file1.txt b/file1.txt
new file mode 100644
index 0000000..bfccc4a
--- /dev/null
+++ b/file1.txt
@@ -0,0 +1 @@
+This is file1.
diff --git a/hello.txt b/hello.txt
new file mode 100644
index 0000000..2d832d9
--- /dev/null
+++ b/hello.txt
@@ -0,0 +1 @@
+hello,world
```
