### 리뷰의 진정성 평가 모델 구현
****
#### 1. 크롤러 제작(Google Maps Crawler)

- 동적 크롤링이 요구되어 Selenium 패키지 사용
- DOM 구조 파악 및 패키지 인스톨(21.10.23)
- 로직 작성, 크롤러 구현(21.10.24)
- Selenium 사용하지 않고 구현 방법 존재(api 이용, 정말 획기적인 방법!!)
- 개발자 탭>Network>찾고자 하는 docs 검색>해당 file의 curl copy 후 정규식 처리 or json변환(21.10.25)
- 가게 ID와 해당 가게 review를 연결하는 로직 생성(21.10.26)
- 전 코드 함수화(21.10.28)
- store_info.csv 빈 컬럼 채우는 코드 작성(21.10.28)
- store_info_1.csv 구동 확인(본 파일)(21.10.29)
****
#### 2. 리뷰 전처리(Preprocessing)

- gpu 환경설정 : CUDA driver, CUDA toolkit, cuDNN, tensorflow-gpu(21.11.01)
- 전처리 패키지 인스톨, 구동 확인