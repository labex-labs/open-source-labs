# 요약

이 실험에서 `sklearn.model_selection`의 `permutation_test_score` 함수를 사용하여 교차 검증된 점수의 유의성을 퍼뮤테이션을 통해 평가하는 방법을 배웠습니다. 데이터셋의 1000 개 다른 퍼뮤테이션에 대한 분류기의 정확도를 계산하여 널 분포를 생성했으며, 원본 데이터를 사용하여 얻은 점수보다 큰 점수를 얻은 퍼뮤테이션의 백분율로 경험적 p-값을 계산했습니다. 또한 결과를 플롯하여 널 분포와 원본 데이터에서 얻은 점수를 시각적으로 보여주었습니다.
