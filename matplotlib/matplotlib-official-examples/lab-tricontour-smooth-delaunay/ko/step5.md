# 일부 삼각형 마스크 처리

무효화된 데이터를 시뮬레이션하기 위해 메쉬 (mesh) 의 일부 삼각형을 마스크 처리합니다. `init_mask_frac` 매개변수를 기반으로 삼각형의 하위 집합을 무작위로 선택합니다.

```python
# Some invalid data are masked out
mask_init = np.zeros(ntri, dtype=bool)
masked_tri = random_gen.randint(0, ntri, int(ntri * init_mask_frac))
mask_init[masked_tri] = True
tri.set_mask(mask_init)
```
