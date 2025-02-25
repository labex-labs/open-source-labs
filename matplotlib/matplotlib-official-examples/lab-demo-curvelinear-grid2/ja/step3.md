# GridHelperCurveLinearを定義する

3番目のステップは、GridHelperCurveLinearインスタンスを定義することです。2番目のステップで定義した変換関数を使ってグリッドを変換します。また、目盛りの密度を高めるために、`grid_locator1`と`grid_locator2`を`MaxNLocator(nbins=6)`に設定します。

```python
grid_helper = GridHelperCurveLinear(
    (tr, inv_tr),
    extreme_finder=ExtremeFinderSimple(20, 20),
    grid_locator1=MaxNLocator(nbins=6), grid_locator2=MaxNLocator(nbins=6))
```
