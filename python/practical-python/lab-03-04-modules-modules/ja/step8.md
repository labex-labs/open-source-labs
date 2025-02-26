# インポートに関するコメント

インポートのバリエーションは、モジュールの動作方法を _変更しません_。

```python
import math
# vs
import math as m
# vs
from math import cos, sin
...
```

具体的には、`import` は常に _ファイル全体を実行_ し、モジュールは依然として孤立した環境です。

`import module as` 文は、ローカルでの名前のみを変更しています。`from math import cos, sin` 文は、依然としてバックグラウンドで _math モジュール全体を読み込みます_。それは、完了後にモジュールから `cos` と `sin` の名前をローカル空間にコピーするだけです。
