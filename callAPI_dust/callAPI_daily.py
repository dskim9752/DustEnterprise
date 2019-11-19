## callAPI.py
import requests
import pandas as pd

from time import sleep

def call_api(api_name, start_date, end_date, dir_name):
    api_key = 'You need api key' #api 키 입력 : 서울열린데이터광장에서 신청해서 받음 깃허브 업로드시 이부분 키값을 지워야함
    url_format = 'http://openAPI.seoul.go.kr:8088/{api_key}/json/{api_name}/1/{end_index}/{date}' #데이터를 받아오는 url 포맷 입력
    headers = {'content-type': 'application/json;charset=utf-8'}

    for date in pd.date_range(start_date, end_date).strftime("%Y%m%d"):
        # 최초 1회 Call은 해당 일자의 데이터 수를 확인한다.
        url = url_format.format(api_name=api_name, api_key=api_key, end_index=1, date=date)
        response = requests.get(url, headers=headers)
        end_index = response.json()[api_name]["list_total_count"]
        print("Max Count(%s): %s" % (date, end_index)) #해당일자의 데이터수 출력

        # 해당 일자의 모든 데이터를 불러온다.
        url = url_format.format(api_name=api_name, api_key=api_key, end_index=end_index, date=date) #앞의 해당일자 데이터수를 end_index에 사용
        response = requests.get(url, headers=headers)
        temp1 = pd.DataFrame(response.json()[api_name]["row"]) #temp1에 모든 추출값 입력
        temp2 = temp1[["MSRDT_DE","MSRSTE_NM","PM10","PM25"]] #모든 추출값에서 날짜,주소,미세먼지농도만 추출
        result = temp2.loc[temp2['MSRSTE_NM'].isin(['노원구','종로구'])] #지역 중 노원구 종로구만 추출
        result.to_csv("./%s/dust_%s.csv" % (dir_name, date), index=False, encoding="utf-8-sig") #csv파일로 저장

        # API 부하 관리를 위해 0.5초 정도 쉬어 줌
        sleep(0.5)


if __name__ == '__main__':
    call_api("DailyAverageAirQuality", "2018-04-03", "2018-04-09", "dust") #api이름 , 시작날짜, 끝날짜, 디렉토리이름 입력
