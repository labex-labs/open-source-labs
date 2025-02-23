# fixup コミットを作成する

他の数人の開発者と共同作業をしているとしましょう。そして、数日前に作成されたコミットに小さなエラーがあることに気付きました。エラーを修正したいのですが、新しいコミットを作成して他の開発者の作業を混乱させたくありません。このときに便利なのが fixup コミットです。fixup コミットを作成することで、新しいコミットを作成することなく必要な変更を加えることができ、次の rebase の際に fixup コミットは自動的に元のコミットにマージされます。

たとえば、あなたのタスクは文字列 "hello,world" を `hello.txt` ファイルに書き込み、メッセージ "Added file1.txt" のコミットに対して "fixup" コミットとして追加し、それが後続の rebase 操作で自動的にマージされるようにすることです。

この実験では、`https://github.com/labex-labs/git-playground` のリポジトリを使用しましょう。

1. リポジトリをクローンし、ディレクトリに移動して ID を設定します。

```shell
git clone https://github.com/labex-labs/git-playground
cd git-playground
git config --global user.name "your-username"
git config --global user.email "your-email"
```

2. `hello.txt` ファイルを作成し、その中に "hello,world" を書き込み、ステージング エリアに追加します。

```shell
echo "hello,world" > hello.txt
git add.
```

3. fixup コミットを作成するには、`git commit --fixup <commit>` コマンドを使用できます。

```shell
git commit --fixup cf80005
# これはメッセージ "Added file1.txt" のコミットのハッシュです。
```

これにより、指定されたコミットに対する fixup コミットが作成されます。fixup コミットを作成する前には、変更をステージングする必要があることに注意してください。4. fixup コミットを作成したら、`git rebase --interactive --autosquash` コマンドを使用して、次の rebase の際に fixup コミットを自動的に元のコミットにマージできます。たとえば：

```shell
git rebase --interactive --autosquash HEAD~3
```

対話型エディタを開いたとき、テキストを変更せずに保存して終了する必要はありません。これにより、最後の 3 つのコミットに対して rebase が実行され、対応する元のコミットに対してすべての fixup コミットが自動的にマージされます。

これが `git show HEAD~1` コマンドを実行した結果です。

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
