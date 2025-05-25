# 소개

이 실습에서는 Python 의 scikit-learn 라이브러리를 사용하여 out-of-bag (OOB) 추정치를 사용한 Gradient Boosting 분류기를 구현하는 방법을 안내합니다. OOB 추정치는 교차 검증 추정치의 대안이며, 반복적인 모델 적합 없이 실시간으로 계산할 수 있습니다. 이 실습에서는 다음 단계를 다룰 것입니다.

1. 데이터 생성
2. OOB 추정치를 사용한 분류기 적합
3. 교차 검증을 사용한 반복 횟수 추정
4. 테스트 데이터에 대한 최적 반복 횟수 계산
5. 결과 플롯

## VM 팁

VM 시작이 완료되면 왼쪽 상단 모서리를 클릭하여 **Notebook** 탭으로 전환하여 연습을 위한 [Jupyter Notebook](https://support.labex.io/en/labex-vm/jupyter)에 접근할 수 있습니다.

때때로 Jupyter Notebook 이 완전히 로드되기까지 몇 초 정도 기다려야 할 수 있습니다. Jupyter Notebook 의 제한으로 인해 작업 검증을 자동화할 수 없습니다.

학습 중 문제가 발생하면 Labby 에 문의하십시오. 세션 후 피드백을 제공하면 문제를 신속하게 해결해 드리겠습니다.
