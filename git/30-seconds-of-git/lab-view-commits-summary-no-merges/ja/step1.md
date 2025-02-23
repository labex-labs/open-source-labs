# マージコミットを含まないコミットの短い要約を表示する

他の数人の開発者と共同作業をしているプロジェクトに取り組んでおり、リポジトリに対して行われたすべてのコミットの要約を見たいと思っています。ただし、マージコミットはコードに実際の変更が含まれていないため、見たくありません。マージコミットを除外したすべてのコミットの要約をどのように表示できますか？

この実験では、`https://github.com/labex-labs/git-playground` のリポジトリを使用します。

1. リポジトリをクローンし、ディレクトリに移動して ID を設定します。

```shell
git clone https://github.com/labex-labs/git-playground
cd git-playground
git config --global user.name "your-username"
git config --global user.email "your-email"
```

2. `feature1` という名前のブランチを作成して切り替え、`file.txt` という名前のファイルを作成してその中に `feature 1` を書き込み、ステージングエリアに追加して "Add feature 1" というメッセージでコミットします。

```shell
git checkout -b feature1
echo "Feature 1" >> file.txt
git add.
git commit -m "Add feature 1"
```

3. `master` ブランチに戻り、`feature1` ブランチをマージし、前方マージを無効にして、テキストを変更せずに保存して終了します。

```shell
git checkout master
git merge --no-ff feature1
```

4. マージコミットを除外したすべてのコミットの短い要約を表示します。

```shell
git log --oneline --no-merges
```

これにより、リポジトリに対して行われたすべてのコミットのリストが出力され、マージコミットは除外されます。出力は以下のようになります。

```shell
430b986 (feature1) Add feature 1
d22f46b (origin/master, origin/HEAD) Added file2.txt
cf80005 Added file1.txt
b00b937 Initial commit
```
