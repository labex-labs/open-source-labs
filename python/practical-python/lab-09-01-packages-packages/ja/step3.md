# パッケージの使用

パッケージはインポートの名前空間として機能します。

これは、今では階層的なインポートが可能になることを意味します。

```python
import porty.report
port = porty.report.read_portfolio('portfolio.csv')
```

インポート文には他にもバリエーションがあります。

```python
from porty import report
port = report.read_portfolio('portfolio.csv')

from porty.report import read_portfolio
port = read_portfolio('portfolio.csv')
```
