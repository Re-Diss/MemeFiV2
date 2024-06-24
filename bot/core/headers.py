from bot.core.agents import generate_random_user_agent

headers = {
    'Accept': 'application/json',
    'Accept-Language': 'ru-RU,ru;q=0.9',
    'Content-Type': 'application/json',
    'Origin': 'https://tg-app.memefi.club',
    'Referer': 'https://tg-app.memefi.club/',
    'Sec-Ch-Ua': '"Google Chrome";v="123", "Not:A-Brand";v="8", "Chromium";v="123"',
    'Sec-Ch-Ua-mobile': '?1',
    'Sec-Ch-Ua-platform': '"Android"',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-site',
    "User-Agent": generate_random_user_agent()
}
