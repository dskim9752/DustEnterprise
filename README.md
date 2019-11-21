#### DustEnterprise

## 미세먼지 사업 아키택처

# 1.	장고

# 2.	Datas
Sample.csv
설명 : 정제 완료된 데이터 저장폴더
속성으로 id, STD_DD, MCT_CAT, SEX_CD, AGE_CD, USE_CNT, USE_AMT, PM10, PM25를 가짐

# 3.	섞는부분 

# 4.	미세먼지
4-1. callAPI_daily.py
설명 : API url reqeust를 csv 형식으로 받아오는 requests, pandas를 import 하여 서울 열린 데이터광장에서 받은 api로 url request한 후 필요한 부분만 걸러내어 실행한 경로의 하위폴더 dust에 미세먼지 데이터를 csv형태로 저장시킨다.


### **빌드 가이드**
1. 서울열린데이터광장 가입 후 서울시 일별 평균 대기오염도 정보 api 신청, 어디어디 가입 후 현재 미세먼지 api 신청
2. 매출 데이터 더미데이터 생성 혹은 다른 외부 데이터를 받아온 후 속성에 맞추어 저장
3. 웹서버에 Django , Python, sqlitestudio 설치
4. python pip install django-chartjs 설치
5. 데이터 클로닝을 통해 데이터 받아옴
6. callAPI_daily.py 있는 경로에 dust폴더를 생성한 후 소스 api 키 부분 입력, 정보 처리를 원하는 기간 선택하여 실행 
7. 매출 데이터와 dust 데이터를 섞음
8. sqlitestudio 실행하여 django\mysite\ 의 db.sqlite3 오픈
9. 이전 생성된 지역_성별_나이.csv 파일들을 import 기능을 이용하여 csv파일 업로드

### **실행 가이드**
1. \django\mysite\ 경로에 커맨드창 실행 후 python manage.py runserver 실행
2. 웹사이트 연 후 localhost:8000으로 접속
3. 접속확인 및 그래프 데이터 확인 가능

### **테스트 가이드**
1. 미세먼지 데이터 csv 저장 시 일부분 오류발생 -> 해당 날짜의 데이터가 존재하지 않는 오류이므로 날짜 범위 재설정후 재실행
2. 미세먼지 데이터 csv 저장 완전히 안됨 -> api키가 정확히 입력되었는지 확인
3. sqlitestudio를 이용한 csv import 문제 발생 -> 테이블의 속성과 csv의 속성 개수의 일치를 확인
4. sqlitestudio로 db.sqlite3 오픈 시 테이블 없음 -> . \django\mysite\ 경로에 커맨드창 실행 후 python manage.py makemigration , python manage.py migrate 실행
5. localhost 접속 시 오류 발생 -> 에러 로그에 따라 대처
6. localhost 접속 시 그래프 미출력 -> python pip install django-chartjs 설치여부 확인

