# ステージング エリアにファイルを追加する

`https://github.com/labex-labs/git-playground` という名前の Git リポジトリに保存されているプロジェクトを作業しています。コードベースにいくつかの変更を加え、これらの変更をリポジトリにコミットしたいと思っています。ただし、特定の変更のみをコミットしたいので、すべての変更をコミットしたくありません。これを行うには、ファイルをステージング エリアに追加する必要があります。

1. `git-playground` ディレクトリでいくつかの変更を行います。

```shell
echo "hello" > index.html
echo "world" > style.css
echo "git" > one.js
echo "labex" > two.js
echo "hello git" > 1.py
echo "hello labex" > 2.py
```

2. これらのファイルをステージング エリアに追加します。

```shell
git add index.html style.css
```

3. 現在の作業ディレクトリとステージング エリアの状態を表示します。これには、どのファイルが変更されたか、どのファイルがステージング エリアに追加されたかなどの情報が含まれます。

```shell
git status
```

4. 代わりに、拡張子が `.js` のすべてのファイルを追加します。

```shell
git add *.js
```

5. 再度、現在の作業ディレクトリとステージング エリアの状態を表示します。

```shell
git status
```

6. また、すべての変更をステージング エリアに追加することもできます。

```shell
git add.
```

7. 再度、現在の作業ディレクトリとステージング エリアの状態を表示します。

```shell
git status
```

これが完成した結果です。

![Git staging area status](../assets/challenge-stage-files-step1-1.png)
