# はじめに

この実験では、マネージドジェネレーターについて学び、通常とは異なる方法でジェネレーターを駆動する方法を理解します。また、簡単なタスクスケジューラーを構築し、ジェネレーターを使用してネットワークサーバーを作成します。

Python のジェネレーター関数は、外部コードによって実行される必要があります。たとえば、イテレーションジェネレーターは `for` ループで反復処理されるときにのみ実行され、コルーチンは `send()` メソッドが呼び出される必要があります。この実験では、高度なアプリケーションでジェネレーターを駆動する実用的な例を探ります。この実験中に作成されるファイルは `multitask.py` と `server.py` です。

<div class="text-xs text-gray-500 dark:text-gray-400 mt-4 border-t border-l-2 border-gray-300 dark:border-gray-600 pt-2 pl-4">
これは Guided Lab です。学習と実践を支援するためのステップバイステップの指示を提供します。各ステップを完了し、実践的な経験を積むために、指示に注意深く従ってください。過去のデータによると、この <span class="text-green-600 dark:text-green-400">初級</span> レベルの実験の完了率は <span class="text-green-600 dark:text-green-400">84.21%</span>です。学習者から <span class="text-primary-600 dark:text-primary-400">80%</span> の好評価を得ています。
</div>
