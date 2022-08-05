# Selenium을 이용하여 웹피이지 크롤링
# 패키지로드
from logging import exception
from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as  pd
import time

def getCoffeeBeanStoreInfo(result):
    
    
    # chrome webdriver 객체 생성
    wd = webdriver.Chrome('./day03/chromedriver.exe')

    for i in range(1,10+1):
        wd.get('https://www.coffeebeankorea.com/store/store.asp')
        time.sleep(1)
       
        try:
            wd.execute_script(f"storePop2('{i}')")
            time.sleep(0.5) #팝업 표시 후에 크롤링이 안되므로 브라우저가 닫히는 걸 방지
            html = wd.page_source
            soup = BeautifulSoup(html, 'html.parser')
            store_name = soup.select('div.store_txt > h2')[0].string
            print(store_name)
            store_info = soup.select(' table.store_table > tbody > tr > td ')
            store_address_list = list(store_info[2])
            store_address = store_address_list[0].strip()
            store_contact = store_info[3].string
            result.append([store_name]+[store_address]+[store_contact])
        
        except Exception as e:
            print(e)
            continue



def main( ):
    result = []
    print('할리스 매장 크롤링 >>>')
    getCoffeeBeanStoreInfo(result)

    #판다스 데이터프레임 생성
    columns = ['store','address','contact']
    coffeebean_df = pd.DataFrame(result, columns=columns)
    # csv 저장
    coffeebean_df.to_csv('./coffebean_shop_info.csv', index=True, encoding='utf-8')
    print('저장완료')

if __name__ == '__main__':
    main()
