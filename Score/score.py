import requests


def send_request(url, headers, payload):
    response = requests.put(url, headers=headers, json=payload)
    print(response.status_code)
    print(response.json())
    print('\n' + '=' * 50 + "\n")


id = '아이디'
pw = '비밀번호'

wantscore = 123456

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

    payload1 = {
        'cat1': 'DL03',
        'cat2': '1',
        'cat3': '1',
        'cat4': '1',
        'clear': 'Y',
        'gameTy': 63,
        'isRnkngMisn': True,
        'detailRecord': {
            'point': wantscore,
            'codeBotOpen': 0,
            'UHint': 0,
            'UKeyBlock': 0,
            'settingTime': 2.505,
            'runningTime': 59.997,
            'coin': 0
        }
    }
    print('도깨비왕국')
    send_request(url, headers, payload1)

    with open('long_content/MAK01-answerblock.txt', 'r',
              encoding='utf-8') as file:
        answer_block = file.read()

    payload2 = {
        'cat1': 'MAK01',
        'cat2': '1',
        'cat3': 'S',
        'cat4': '4',
        'clear': 'Y',
        'gameTy': 90,
        'isRnkngMisn': True,
        'detailRecord': {
            'point': wantscore,
            'codeBotOpen': 0,
            'UHint': 0,
            'UBlock': 43,
            'UKeyBlock': 0,
            'answerBlock': answer_block,
            'settingTime': 3.306,
            'runningTime': 123.456
        }
    }
    print('인트런')
    send_request(url, headers, payload2)

    with open('long_content/MAK04-answerblock.txt', 'r',
              encoding='utf-8') as file:
        answer_block_content = file.read()

    payload3 = {
        'cat1': 'MAK04',
        'cat2': '2',
        'cat3': 'S',
        'cat4': '4',
        'clear': 'Y',
        'gameTy': 55,
        'isRnkngMisn': True,
        'detailRecord': {
            'UObjectBlock': {
                'flapInt': 32,
                'gameover': 2,
                'pillar': 45,
                'monster': 18
            },
            'point': wantscore,
            'codeBotOpen': 0,
            'UHint': 0,
            'UBlock': 97,
            'UKeyBlock': 0,
            'answerBlock': {
                'flapInt': answer_block_content
            },
            'settingTime': 1.351,
            'runningTime': 5.19
        }
    }
    print('플랩인트')
    send_request(url, headers, payload3)

    with open('long_content/MAKM01-answerblock.txt', 'r',
              encoding='utf-8') as file:
        answer_block = file.read()

    payload4 = {
        'cat1': 'MAKM01',
        'cat2': '1',
        'cat3': 'S',
        'cat4': '1',
        'clear': 'Y',
        'gameTy': 58,
        'isRnkngMisn': True,
        'detailRecord': {
            'point': wantscore,
            'codeBotOpen': 1,
            'UHint': 0,
            'UBlock': 22,
            'UKeyBlock': 0,
            'answerBlock': answer_block,
            'settingTime': 3.306,
            'runningTime': 123.456
        }
    }
    print('구름콩콩')
    send_request(url, headers, payload4)
    print('끝')

else:
    print('엑세스 토큰을 가져오지 못했습니다.')
