# はじめに

この実験では、React の `useComponentWillUnmount` フックを調べます。このフックを使うと、コンポーネントがアンマウントされ破棄される直前にコールバック関数を実行できます。このフックを使うことで、イベントリスナーの削除や保留中のリクエストのキャンセルなど、必要なクリーンアップタスクを行うことができます。この実験では、このフックの使い方と動作を理解するための実践的な経験を提供します。この動作は、クラスコンポーネントの `componentWillUnmount()` ライフサイクルメソッドと似ています。

<div class="text-xs text-gray-500 dark:text-gray-400 mt-4 border-t border-l-2 border-gray-300 dark:border-gray-600 pt-2 pl-4">
これは Guided Lab です。学習と実践を支援するためのステップバイステップの指示を提供します。各ステップを完了し、実践的な経験を積むために、指示に注意深く従ってください。過去のデータによると、この <span class="text-green-600 dark:text-green-400">初級</span> レベルの実験の完了率は <span class="text-green-600 dark:text-green-400">100%</span>です。学習者から <span class="text-primary-600 dark:text-primary-400">100%</span> の好評価を得ています。
</div>
