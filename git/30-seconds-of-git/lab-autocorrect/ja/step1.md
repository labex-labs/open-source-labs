# Git コマンドの自動修正

問題は、開発者がしばしば Git コマンドを間違えて入力することで、エラーが発生し、作業効率が低下することです。たとえば、開発者が偶然にも `git sttaus` と入力してしまい、代わりに `git status` を入力する場合、エラーメッセージが表示されます。これはイライラするだけでなく時間がかかります。特に、多くのファイルや共同作業者がいる大規模なプロジェクトで作業する場合にはそうです。

Git の自動修正機能をどのように使用するかを示すために、`https://github.com/labex-labs/git-playground` ディレクトリにある Git リポジトリを使用します。

1. ターミナルを開き、リポジトリをクローンしたいディレクトリに移動します。
2. 次のコマンドを使用してリポジトリをクローンします。

```
git clone https://github.com/labex-labs/git-playground.git
```

3. 次のコマンドを使用してクローンしたリポジトリに移動します。

```
cd git-playground
```

4. 次のコマンドを使用して Git の自動修正機能を有効にします。

```
git config --global help.autocorrect 1
```

5. `git sttaus` のように Git コマンドを間違えて入力してみます。Git は自動的にコマンドを修正し、代わりに `git status` を実行します。

これが実験を完了した後の結果です。

![Git autocorrect command result](../assets/challenge-autocorrect-step1-1.jpg)
