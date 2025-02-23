# 別のブランチからファイルをコピーする

あなたは `https://github.com/labex-labs/git-playground.git` という名前の Git リポジトリ内のプロジェクトを作業しています。 `feature-1` と `feature-2` という 2 つのブランチがあります。 `feature-1` ブランチから `hello.txt` ファイルを `feature-2` ブランチにコピーする必要があります。

1. リポジトリをクローンする：

```shell
git clone https://github.com/labex-labs/git-playground.git
```

2. ディレクトリに移動して ID を設定する：

```shell
cd git-playground
git config --global user.name "your-username"
git config --global user.email "your-email"
```

3. `feature-1` ブランチを作成して切り替え、 `hello.txt` という名前のテキストファイルを作成し、そこに "hello,world" という文字列を書き込み、 "add hello.txt" というメッセージでファイルをコミットする：

```shell
git checkout -b feature-1
echo "hello,world" > hello.txt
git add.
git commit -m "add hello.txt"
```

4. `master` ブランチに切り替えた後、 `feature-2` ブランチを作成して切り替える：

```shell
git checkout master
git checkout -b feature-2
```

5. `feature-1` ブランチから `hello.txt` ファイルを `feature-2` ブランチにコピーし、 "copy hello.txt" というコミットメッセージでコミットする：

```shell
git checkout feature-1 hello.txt
git commit -am "copy hello.txt"
```

6. `hello.txt` ファイルが `feature-2` ブランチにコピーされたことを確認する：

```shell
ll
```

`feature-2` ブランチのファイル一覧に `hello.txt` ファイルが表示されるはずです：

```
-rw-r--r-- 1 labex labex 15 Jul 12 22:43 file1.txt
-rw-r--r-- 1 labex labex 15 Jul 12 22:43 file2.txt
-rw-r--r-- 1 labex labex 12 Jul 12 22:50 hello.txt
-rw-r--r-- 1 labex labex 32 Jul 12 22:43 README.md
```
