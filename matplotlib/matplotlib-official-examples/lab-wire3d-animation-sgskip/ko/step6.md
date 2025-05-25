# 평균 FPS 표시

여섯 번째 단계는 애니메이션 실행에 걸린 총 시간을 사용하여 평균 초당 프레임 수 (FPS) 를 표시하는 것입니다.

```python
print('Average FPS: %f' % (100 / (time.time() - tstart)))
```
