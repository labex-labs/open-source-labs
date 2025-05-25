# 요약

이 실험에서는 Scikit-Learn 의 `VotingClassifier`를 사용하여 두 가지 특징을 기반으로 아이리스 꽃의 종류를 예측했습니다. `DecisionTreeClassifier`, `KNeighborsClassifier`, 그리고 `SVC` 세 가지 분류기를 학습시켰습니다. 그런 다음 `VotingClassifier`를 사용하여 이들의 예측 결과를 결합하고 결정 경계를 시각화했습니다. 그 결과 `VotingClassifier`의 결정 경계는 `SVC`의 결정 경계와 유사하지만 일부 영역에서는 복잡성이 덜하다는 것을 확인했습니다.
