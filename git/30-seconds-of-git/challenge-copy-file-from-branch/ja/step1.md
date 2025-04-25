# 別のブランチからファイルをコピーする

あなたは `https://github.com/labex-labs/git-playground.git` という名前の Git リポジトリ内のプロジェクトを作業しています。 `feature-1` と `feature-2` という 2 つのブランチがあります。あなたは `feature-1` ブランチから `hello.txt` ファイルを `feature-2` ブランチにコピーする必要があります。

## タスク

1. ディレクトリに移動して ID を設定します。
2. `feature-1` ブランチを作成して切り替え、 `hello.txt` という名前のテキストファイルを作成し、そこに "hello,world" という文字列を書き込み、 "add hello.txt" というメッセージでファイルをコミットします。
3. `master` ブランチに切り替えた後、 `feature-2` ブランチを作成して切り替えます。
4. `feature-1` ブランチから `hello.txt` ファイルを `feature-2` ブランチにコピーし、 "copy hello.txt" というコミットメッセージでコミットします。
5. `hello.txt` ファイルが `feature-2` ブランチにコピーされたことを確認します。

`feature-2` ブランチのファイル一覧に `hello.txt` ファイルが表示されるはずです。

```
-rw-r--r-- 1 labex labex 15 Jul 12 22:43 file1.txt
-rw-r--r-- 1 labex labex 15 Jul 12 22:43 file2.txt
-rw-r--r-- 1 labex labex 12 Jul 12 22:50 hello.txt
-rw-r--r-- 1 labex labex 32 Jul 12 22:43 README.md
```
