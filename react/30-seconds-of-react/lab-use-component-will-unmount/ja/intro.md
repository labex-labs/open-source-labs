# はじめに

この実験では、React の `useComponentWillUnmount` フックを調べます。このフックを使うと、コンポーネントがアンマウントされ破棄される直前にコールバック関数を実行できます。このフックを使うことで、イベントリスナーの削除や保留中のリクエストのキャンセルなど、必要なクリーンアップタスクを行うことができます。この実験では、このフックの使い方と動作を理解するための実践的な経験を提供します。この動作は、クラスコンポーネントの `componentWillUnmount()` ライフサイクルメソッドと似ています。
