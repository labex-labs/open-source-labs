# はじめに

この実験では、コンテナを実行するために Docker コマンドを使用した実験 1 の知識を基にします。Dockerfile から構築されたカスタム Docker イメージを作成します。イメージを構築したら、それをセントラル レジストリにプッシュし、他の環境で展開するためにプルできるようにします。また、イメージ レイヤーと、Docker が「コピーオンライト」とユニオン ファイル システムをどのように組み込んでイメージを効率的に保存し、コンテナを実行するかについても簡単に説明します。

この実験ではいくつかの Docker コマンドを使用します。利用可能なコマンドの完全なドキュメントについては、[公式ドキュメント](https://docs.docker.com/)を参照してください。

<div class="text-xs text-gray-500 dark:text-gray-400 mt-4 border-t border-l-2 border-gray-300 dark:border-gray-600 pt-2 pl-4">
これは Guided Lab です。学習と実践を支援するためのステップバイステップの指示を提供します。各ステップを完了し、実践的な経験を積むために、指示に注意深く従ってください。過去のデータによると、この <span class="text-green-600 dark:text-green-400">初級</span> レベルの実験の完了率は <span class="text-green-600 dark:text-green-400">82%</span>です。学習者から <span class="text-primary-600 dark:text-primary-400">100%</span> の好評価を得ています。
</div>
