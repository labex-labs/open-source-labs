# 요약

이 실험에서는 랜덤 포레스트 분류기를 사용하여 타이타닉 데이터 세트에서 불순도 기반 특성 중요도와 순열 중요도를 비교했습니다. 불순도 기반 특성 중요도는 숫자형 특성의 중요도를 부풀릴 수 있으며, 고카디널리티 특성에 편향될 수 있음을 관찰했습니다. 순열 중요도는 특성 중요도를 더 잘 나타내며, 고카디널리티 특성에 편향되지 않습니다. 또한, 트리의 과적합을 제한하면 예측력이 없는 특성의 중요도를 낮출 수 있음을 관찰했습니다.
