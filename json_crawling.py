import requests
import json
import pandas as pd

def transform_theme_data(themes_data):
    transformed_list = []
    
    for theme in themes_data:
        # 각 테마의 코인 코드만 리스트로 추출
        coin_codes = [coin['code'] for coin in theme['coins']]
        
        # 원하는 형식으로 데이터 구조화
        theme_info = {
            'theme': theme['name'],
            'shortDescription': theme.get('shortDescription', ''),
            'coin': coin_codes
        }
        transformed_list.append(theme_info)
    
    return transformed_list

# API 요청 설정
headers = {
    "referer": "https://coinness.com/",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36"
}

# API 호출
url = requests.get("https://api.coinness.com/market/v3/themes?languageCode=ko", headers=headers)
themes_list = json.loads(url.content)

# 데이터 변환
transformed_data = transform_theme_data(themes_list)

# JSON 파일로 저장
with open('theme_data.json', 'w', encoding='utf-8') as f:
    json.dump(transformed_data, f, ensure_ascii=False, indent=4)

# 결과 출력
print(json.dumps(transformed_data, ensure_ascii=False, indent=4))

# theme_list = [
#     {
#         'theme': theme,
#         'shortDescription': desc,
#         'coin': coin_list
#     }
#     for theme, desc, coin_list in zip(themes, descriptions, coins)
# ]

