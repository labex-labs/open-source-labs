# 커널 하이퍼파라미터 해석

이제 커널의 하이퍼파라미터를 살펴볼 수 있습니다.

```python
gaussian_process.kernel_
```

따라서, 평균을 뺀 대부분의 목표 신호는 약 45 ppm 의 장기적인 상승 추세와 약 52 년의 길이 스케일로 설명됩니다. 주기적 성분은 약 2.6ppm 의 진폭, 약 90 년의 감쇠 시간 및 약 1.5 의 길이 스케일을 갖습니다. 긴 감쇠 시간은 계절적 주기성에 매우 가까운 성분임을 나타냅니다. 상관된 노이즈는 약 0.2 ppm 의 진폭, 약 0.12 년의 길이 스케일 및 약 0.04 ppm 의 백색 노이즈 기여도를 갖습니다. 따라서 전체적인 노이즈 수준은 매우 작아서 데이터가 모델로 매우 잘 설명될 수 있음을 나타냅니다.
