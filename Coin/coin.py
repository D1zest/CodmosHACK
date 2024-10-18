import requests

id = '아이디'
pw = '비밀번호'

wantcoin = 123456
login_url = 'https://api.codmos.io/user/sign'
login_payload = {
    'userId': id,
    'userPw': pw,
    'deviceTy': 1,
    'svcTy': 1,
    'accesAplctn': 1,
    'prtnrTkn': None
}

response = requests.post(login_url, json=login_payload)
response_json = response.json()
acces_tkn = response_json.get('result', {}).get('accesTkn')

if acces_tkn:
    headers = {
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7',
        'authorization': acces_tkn,
        'content-language': 'ko',
        'content-type': 'application/json;charset=UTF-8',
        'if-none-match': 'W/"24a-WR932oJcWTgYyq8bKx4iRWZQzMY"',
        'priority': 'u=1, i',
        'sec-ch-ua':
        '"Chromium";v="128", "Not;A=Brand";v="24", "Google Chrome";v="128"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site'
    }

    url = 'https://api.codmos.io/study/rcord'
    payload = {
        "cat1": "GROW01",
        "cat2": "1",
        "cat3": "1",
        "cat4": "3",
        "clear": "Y",
        "gameTy": 50,
        "coin": wantcoin,
        "detailRecord": {
            "score": 1867,
            "runningTime": 198.922,
            "lastStage": 12,
            "blckMoveCnt": 89
        }
    }

    response = requests.put(url, headers=headers, json=payload)
    print(response.status_code)
    print(response.json())
else:
    print('엑세스 토큰을 가져오지 못했습니다.')
