# GridHelperCurveLinear 정의

세 번째 단계는 `GridHelperCurveLinear` 인스턴스를 정의하는 것입니다. 2 단계에서 정의한 변환 함수를 사용하여 그리드를 변환합니다. 또한 눈금 밀도를 높이기 위해 `grid_locator1`과 `grid_locator2`를 `MaxNLocator(nbins=6)`으로 설정합니다.

```python
grid_helper = GridHelperCurveLinear(
    (tr, inv_tr),
    extreme_finder=ExtremeFinderSimple(20, 20),
    grid_locator1=MaxNLocator(nbins=6), grid_locator2=MaxNLocator(nbins=6))
```
