# はじめに

**目的:**

- マネージドジェネレータについて学ぶ

**作成されたファイル:** `multitask.py`, `server.py`

ジェネレータまたはコルーチン関数は、他のコードによって駆動されない限り決して実行できません。たとえば、反復処理に使用されるジェネレータは、forループを使用して実際に反復処理が行われない限り何もしません。同様に、コルーチンのコレクションは、その`send()`メソッドが何らかの方法で呼び出されない限り実行されません。

ジェネレータの高度なアプリケーションでは、様々な異常な方法でジェネレータを駆動することが可能です。このチャレンジでは、いくつかの例を見てみましょう。
