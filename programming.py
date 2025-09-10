import requests
from bs4 import BeautifulSoup
import pandas as pd
import time
from datetime import datetime

def crawl_news_headlines():
    """
    뉴스 헤드라인 크롤링 함수
    (예시: 실제 사이트 구조에 맞게 수정 필요)
    """
    
    # 예시 URL (실제로는 허가된 뉴스 사이트 사용)
    base_url = "https://httpbin.org/html"  # 테스트용 URL
    
    news_data = []
    
    try:
        # 페이지 요청
        response = session.get(base_url)
        response.raise_for_status()  # HTTP 에러 발생 시 예외 처리
        
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # 실제 뉴스 사이트의 구조에 맞게 수정
        # 예시: headlines = soup.find_all('h2', class_='headline')
        
        # 테스트용 데이터 생성
        headlines = ["AI 기술 발전 가속화", "파이썬 인기 지속 상승", "데이터 분석 시장 확대"]
        
        for i, headline in enumerate(headlines, 1):
            news_item = {
                'title': headline,
                'url': f"https://example.com/news/{i}",
                'crawl_time': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            }
            news_data.append(news_item)
            
        print(f"✅ {len(news_data)}개의 뉴스 헤드라인 수집 완료!")
        
    except Exception as e:
        print(f"❌ 크롤링 중 오류 발생: {e}")
    
    return news_data

def save_news_data(news_data):
    """수집한 뉴스 데이터를 CSV 파일로 저장"""
    if news_data:
        df = pd.DataFrame(news_data)
        filename = f"news_headlines_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"
        df.to_csv(filename, index=False, encoding='utf-8-sig')
        print(f"✅ 데이터가 {filename}에 저장되었습니다.")
        return df
    else:
        print("❌ 저장할 데이터가 없습니다.")
        return None

# 실행
news_data = crawl_news_headlines()
df = save_news_data(news_data)
if df is not None:
    print("\n📊 수집된 데이터 미리보기:")
    print(df.head())