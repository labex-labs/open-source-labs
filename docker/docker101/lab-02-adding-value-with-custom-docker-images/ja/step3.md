# Docker イメージを実行する

イメージを構築したので、それが機能することを確認するために実行しましょう。

Docker イメージを実行する

```bash
docker run -p 5001:5000 -d python-hello-world
```

`-p` フラグは、コンテナ内で実行されているポートをホストにマップします。この場合、コンテナ内のポート 5000 で実行されている Python アプリを、ホストのポート 5001 にマップしています。ホスト上の別のアプリケーションが既にポート 5001 を使用している場合は、5001 を別の値、たとえば 5002 に置き換える必要がある場合があります。

ターミナル ウィンドウの **PORTS** タブに移動し、リンクをクリックして新しいブラウザ タブでアプリを開きます。

![Terminal ports tab link](../assets/20230829-13-59-19-e8dZe3aN.png)

ターミナルで `curl localhost:5001` を実行すると、`hello world!` が返されます。

コンテナのログ出力を確認する

アプリケーションのログを表示したい場合は、`docker container logs` コマンドを使用できます。既定では、`docker container logs` はアプリケーションから標準出力に送信される内容を表示します。実行中のコンテナの ID を取得するには、`docker container ls` を使用します。

```bash
labex:project/ $ docker container ls
CONTAINER ID   IMAGE                COMMAND           CREATED         STATUS         PORTS                                       NAMES
52df977e5541   python-hello-world   "python app.py"   2 minutes ago   Up 2 minutes   0.0.0.0:5001->5000/tcp, :::5001->5000/tcp   heuristic_lamport
labex:project/ $ docker container logs 52df977e5541
 * Serving Flask app 'app'
 * Debug mode: off
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on all addresses (0.0.0.0)
 * Running on http://127.0.0.1:5000
 * Running on http://172.17.0.2:5000
Press CTRL+C to quit
172.17.0.1 - - [23/Jan/2024 02:43:10] "GET / HTTP/1.1" 200 -
172.17.0.1 - - [23/Jan/2024 02:43:10] "GET /favicon.ico HTTP/1.1" 404 -
```

Dockerfile は、アプリケーションの再現可能なビルドを作成する方法です。一般的なワークフローは、CI/CD 自動化がビルド プロセスの一部として `docker image build` を実行することです。イメージが構築されると、それらはセントラル レジストリに送信され、そのアプリケーションのインスタンスを実行する必要があるすべての環境（たとえばテスト環境）でアクセスできるようになります。次の手順では、カスタム イメージをパブリック Docker レジストリである Docker Hub にプッシュし、他の開発者やオペレーターが利用できるようにします。
