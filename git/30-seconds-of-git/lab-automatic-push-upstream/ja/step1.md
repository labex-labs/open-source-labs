# 上流ブランチ作成の自動化

開発者として、プッシュ時に上流ブランチを作成するプロセスを自動化して、リモートリポジトリで手動でブランチを作成する面倒を避きたいと思います。

この実験では、`https://github.com/labex-labs/git-playground` リポジトリをあなたのアカウントにフォークし、アカウント内の `git-playground` リポジトリを使用して、プッシュ時に自動的に上流ブランチを作成します。

1. GitHub ウェブサイトで、あなたのアカウントにログインし、`https://github.com/labex-labs/git-playground` を見つけて、そのリポジトリをあなたのアカウントにフォークします。
2. 自分自身のフォークしたリポジトリのページで、`Code` ボタンをクリックして、リポジトリのURLをコピーします。
3. リポジトリをクローンし、ディレクトリに移動して、識別情報を設定します。

```shell
git clone https://github.com/your-username/git-playground.git
cd git-playground
git config --global user.name "your-username"
git config --global user.email "your-email"
```

4. 以下のコマンドを使用して、プッシュ時に自動的な上流ブランチ作成を有効にします。

```shell
git config --global push.default current
```

5. リモートリポジトリに存在しない `new-feature` という新しいブランチをプッシュします。

```shell
git checkout -b new-feature
git push
```

6. リモートリポジトリに新しいブランチが作成されたことを確認します。

```shell
git ls-remote --heads origin
```

これが実験を完了した後の結果です。

![automatic upstream branch result](../assets/challenge-automatic-push-upstream-step1-1.png)
