# はじめに

この実験では、コンテナを実行するために Docker コマンドを使用した実験 1 の知識を基にします。Dockerfile から構築されたカスタム Docker イメージを作成します。イメージを構築したら、それをセントラル レジストリにプッシュし、他の環境で展開するためにプルできるようにします。また、イメージ レイヤーと、Docker が「コピーオンライト」とユニオン ファイル システムをどのように組み込んでイメージを効率的に保存し、コンテナを実行するかについても簡単に説明します。

この実験ではいくつかの Docker コマンドを使用します。利用可能なコマンドの完全なドキュメントについては、[公式ドキュメント](https://docs.docker.com/)を参照してください。
