# 내부 GridSpec 생성

이제 내부 gridspec 을 생성합니다. `GridSpecFromSubplotSpec` 메서드를 사용하여 외부 gridspec 의 서브플롯이 될 3x3 gridspec 을 생성합니다.

```python
gs00 = gridspec.GridSpecFromSubplotSpec(3, 3, subplot_spec=gs0[0])
```
