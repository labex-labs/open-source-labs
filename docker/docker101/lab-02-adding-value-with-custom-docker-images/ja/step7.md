# クリーンアップ

この実験を完了すると、ホスト上に多数の実行中のコンテナが残ります。これらをクリーンアップしましょう。

各実行中のコンテナに対して `docker container stop [コンテナ ID]` を実行する

まず、`docker container ls` を使用して実行中のコンテナの一覧を取得します。

```bash
$ docker container ls
```

次に、一覧に表示される各コンテナに対してコマンドを実行します。

```bash
$ docker container stop <コンテナID>
```

停止したコンテナを削除する

`docker system prune` は、システムをクリーンアップするための非常に便利なコマンドです。停止したコンテナ、未使用のボリュームとネットワーク、およびダングリング イメージを削除します。

```bash
$ docker system prune
WARNING! This will remove:
- all stopped containers
- all volumes not used by at least one container
- all networks not used by at least one container
- all dangling images
Are you sure you want to continue? [y/N] y
Deleted Containers:
0b2ba61df37fb4038d9ae5d145740c63c2c211ae2729fc27dc01b82b5aaafa26

Total reclaimed space: 300.3kB
```
