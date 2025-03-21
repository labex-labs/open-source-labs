# まとめ

この実験では、Python の関数から値を返すいくつかの重要なパターンを学びました。まず、Python の関数は複数の値をタプルにパックすることで返すことができ、これにより値の返却とアンパックがきれいで読みやすくなります。次に、常に有効な結果を生成できない関数の場合、値が存在しないことを示す一般的な方法は `None` を返すことであり、例外 (exception) を発生させる方法も紹介しました。

最後に、並行プログラミングでは、`Future` は将来の結果のプレースホルダーとして機能し、別のスレッドまたはプロセスで実行されている関数から戻り値を取得できるようにします。これらのパターンを理解することで、Python コードの堅牢性と柔軟性が向上します。さらなる練習として、異なるエラー処理戦略を試し、他の並行実行タイプで `Future` を使用し、`async`/`await` を使った非同期プログラミングでのそれらのアプリケーションを探索してみてください。
