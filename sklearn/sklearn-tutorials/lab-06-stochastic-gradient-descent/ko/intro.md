# 소개

확률적 경사 하강법 (SGD) 은 머신 러닝에서 널리 사용되는 최적화 알고리즘입니다. 경사 하강법의 변형으로, 각 반복에서 훈련 데이터의 임의로 선택된 부분 집합을 사용합니다. 이로 인해 계산 효율이 높아지고 대규모 데이터셋을 처리하기에 적합합니다. 이 실습에서는 scikit-learn 을 사용하여 파이썬에서 SGD 를 구현하는 단계를 살펴볼 것입니다.

## VM 팁

VM 시작이 완료되면 왼쪽 상단 모서리를 클릭하여 **Notebook** 탭으로 전환하여 연습용 [Jupyter Notebook](https://support.labex.io/en/labex-vm/jupyter)에 접근할 수 있습니다.

때때로 Jupyter Notebook 이 완전히 로드되기까지 몇 초 정도 기다려야 할 수 있습니다. Jupyter Notebook 의 제한으로 인해 작업의 유효성 검사를 자동화할 수 없습니다.

학습 중 문제가 발생하면 Labby 에게 문의하십시오. 세션 후 피드백을 제공하면 문제를 신속하게 해결해 드리겠습니다.

<div class="text-xs text-gray-500 dark:text-gray-400 mt-4 border-t border-l-2 border-gray-300 dark:border-gray-600 pt-2 pl-4">
이것은 가이드 실험입니다. 학습과 실습을 돕기 위한 단계별 지침을 제공합니다.각 단계를 완료하고 실무 경험을 쌓기 위해 지침을 주의 깊게 따르세요. 과거 데이터에 따르면, 이것은 <span class="text-green-600 dark:text-green-400">초급</span> 레벨의 실험이며 완료율은 <span class="text-green-600 dark:text-green-400">82%</span>입니다.학습자들로부터 <span class="text-primary-600 dark:text-primary-400">100%</span>의 긍정적인 리뷰율을 받았습니다.
</div>
