# クリーンアップ

この実験を完了すると、ホスト上に多数の実行中のコンテナが残ります。これらをクリーンアップしましょう。

まず、`docker container ls` を使用して実行中のコンテナの一覧を取得します。

```bash
$ docker container ls
CONTAINER ID IMAGE COMMAND CREATED STATUS PORTS NAMES
d6777df89fea nginx "nginx -g 'daemon..." 3 minutes ago Up 3 minutes 0.0.0.0:8080- nginx > 80/tcp
ead80a0db505 mongo "docker-entrypoint..." 3 minutes ago Up 3 minutes 0.0.0.0:8081- mongo > 27017/tcp
af549dccd5cf ubuntu "top" 8 minutes ago Up 8 minutes priceless_kepler
```

次に、リスト内の各コンテナに対して `docker container stop [コンテナ ID]` を実行します。事前に指定したコンテナの名前を使用することもできます。

```bash
$ docker container stop d67 ead af5
d67
ead
af5
```

**注**: ID の一意性を保つために必要な桁数だけを参照すればよいことに注意してください。ほとんどの場合、3 桁で十分です。

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
7872fd96ea4695795c41150a06067d605f69702dbcb9ce49492c9029f0e1b44b
60abd5ee65b1e2732ddc02b971a86e22de1c1c446dab165462a08b037ef7835c
31617fdd8e5f584c51ce182757e24a1c9620257027665c20be75aa3ab6591740

Total reclaimed space: 12B
```
