# 소개

이 실험은 scikit-learn 을 사용하여 다중 레이블 문서 분류 문제를 보여줍니다. 데이터셋은 다음 과정을 기반으로 무작위로 생성됩니다.

- 레이블 수 선택: n ~ Poisson(n_labels)
- N 번 반복하여 클래스 c 선택: c ~ Multinomial(theta)
- 문서 길이 선택: k ~ Poisson(length)
- K 번 반복하여 단어 w 선택: w ~ Multinomial(theta_c)

이 과정에서 거부 샘플링 (rejection sampling) 을 사용하여 n 이 2 보다 크고 문서 길이가 0 이 되지 않도록 합니다. 마찬가지로 이미 선택된 클래스는 거부됩니다. 두 클래스 모두에 할당된 문서는 두 가지 색상의 원으로 둘러싸여 표시됩니다.

## VM 팁

VM 시작이 완료되면 왼쪽 상단 모서리를 클릭하여 **Notebook** 탭으로 전환하여 연습을 위한 [Jupyter Notebook](https://support.labex.io/en/labex-vm/jupyter)에 접근합니다.

때때로 Jupyter Notebook 이 완전히 로드되기까지 몇 초 정도 기다려야 할 수 있습니다. Jupyter Notebook 의 제한으로 인해 작업 검증은 자동화될 수 없습니다.

학습 중 문제가 발생하면 Labby 에 문의하십시오. 세션 후 피드백을 제공하면 문제를 신속하게 해결해 드리겠습니다.
