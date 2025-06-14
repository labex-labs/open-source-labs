# 요약

이 실습에서는 Lasso 회귀 모델에 대한 최적의 하이퍼파라미터 alpha 를 선택하는 방법을 배웠습니다. 두 가지 접근 방식을 논의했습니다: (1) 훈련 세트와 일부 정보 기준만을 사용하여 alpha 의 최적값을 선택하는 방법, 그리고 (2) 교차 검증을 사용하여 최적의 하이퍼파라미터를 선택하는 방법입니다. 이 예제에서는 당뇨병 데이터 세트를 사용했습니다. 두 가지 접근 방식 모두 유사하게 작동할 수 있지만, 샘플 내 하이퍼파라미터 선택은 계산 성능 측면에서 효과가 있습니다. 그러나 특징의 수에 비해 샘플의 수가 충분히 많을 때만 사용할 수 있습니다. 교차 검증을 통한 하이퍼파라미터 최적화는 다양한 환경에서 안전한 전략입니다.
