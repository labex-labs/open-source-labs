# `__init__.py` ファイル

これらのファイルの主な目的は、モジュールをまとめることです。

例：関数の統合

```python
# porty/__init__.py
from.pcost import portfolio_cost
from.report import portfolio_report
```

これにより、インポート時に名前が _トップレベル_ に表示されます。

```python
from porty import portfolio_cost
portfolio_cost('portfolio.csv')
```

階層的なインポートを使う代わりに。

```python
from porty import pcost
pcost.portfolio_cost('portfolio.csv')
```
