# セントラル レジストリにプッシュする

まだ持っていない場合は、[Docker Hub](https://hub.docker.com) に移動してアカウントを作成します。あるいは、例えば [https://quay.io](https://quay.io) を使用することもできます。

この実験では、Docker Hub をセントラル レジストリとして使用します。Docker Hub は、公開可能なイメージを保存する無料サービスであり、プライベート イメージを保存する場合は有料です。[Docker Hub](https://hub.docker.com) ウェブサイトに移動して、無料アカウントを作成します。

Docker を大量に使用するほとんどの組織は、内部で独自のレジストリをセットアップします。簡単にするために、Docker Hub を使用しますが、以下の概念は任意のレジストリにも適用されます。

ログイン

ターミナルで `docker login` と入力するか、podman を使用している場合は `podman login` と入力することで、イメージ レジストリ アカウントにログインできます。

```bash
labex:project/ $ export DOCKERHUB_USERNAME=<your_docker_username>
labex:project/ $ docker login docker.io -u $DOCKERHUB_USERNAME
Password:
WARNING! Your password will be stored unencrypted in /home/labex/.docker/config.json.
Configure a credential helper to remove this warning. See
https://docs.docker.com/engine/reference/commandline/login/#credentials-store

Login Succeeded
```

イメージにユーザー名を付ける

Docker Hub の命名規則は、イメージに [dockerhub ユーザー名]/[イメージ名] を付けることです。これを行うために、先ほど作成したイメージ `python-hello-world` にこの形式に合うようにタグを付けます。

```bash
docker tag python-hello-world $DOCKERHUB_USERNAME/python-hello-world
```

イメージをレジストリにプッシュする

適切にタグ付けされたイメージがあれば、`docker push` コマンドを使用してイメージを Docker Hub レジストリにプッシュできます。

```bash
docker push $DOCKERHUB_USERNAME/python-hello-world
```

ブラウザで Docker Hub のイメージを確認する

[Docker Hub](https://hub.docker.com) に移動し、プロフィールに移動して、`https://hub.docker.com/repository/docker/<dockerhub-username>/python-hello-world` に新しくアップロードされたイメージを確認します。

イメージが Docker Hub にあるので、他の開発者やオペレーターは `docker pull` コマンドを使用して、イメージを他の環境に展開できます。

**注**：Docker イメージには、イメージ内でアプリケーションを実行するために必要なすべての依存関係が含まれています。これは便利です。なぜなら、展開するすべての環境にインストールされている依存関係に依存する場合、環境のドリフト（バージョンの違い）を処理する必要がなくなるからです。また、これらの環境をプロビジョニングするための追加の手順も必要ありません。1 つの手順：Docker をインストールするだけで、準備完了です。
