import requests

cookies = {
    '__cf_bm': 'khJmahrhypkQ41IiTU0jL4jOXoUjP1ZavYkE_1rWJsg-1698645612-0-AfDMTqcQv0HGZJfyJ094aJI7Aote+jwIWd9pMooy/Vh5p1f/EF8ay4OszmfnImP70QBhsgTXuX8KfTO+TBu4ErM=',
    'next-auth.csrf-token': 'c7fce17d9ab676c261acacf4799d03381504fe826a8a8c28889b3d513c85dcb7%7C0314bf69e6a06957c0c991ecc94e5d6d37e94bed3084aa19e44da442ffa2cb9f',
    'g_state': '{"i_p":1698652818272,"i_l":1}',
    '__Secure-next-auth.callback-url': 'https%3A%2F%2Fwww.perplexity.ai%2Fapi%2Fauth%2Fsignin-callback%3Fredirect%3Dhttps%253A%252F%252Fwww.perplexity.ai',
    '__cflb': '02DiuDyvFMmK5p9jVbWbam6CcSLCt41haw3efCACkzfLg',
    'AWSALB': 'BxutSOSNca4c88qzRkflwCPlBZbsUZ/aViIfmS+I1Kf2aA/YieS3CWNaLRbbKDHIerQKdREeDtJxkQEORTChnHiEcurVBv3eL130xQ0vuF1qrlJk3Ta597R6pETe',
    'AWSALBCORS': 'BxutSOSNca4c88qzRkflwCPlBZbsUZ/aViIfmS+I1Kf2aA/YieS3CWNaLRbbKDHIerQKdREeDtJxkQEORTChnHiEcurVBv3eL130xQ0vuF1qrlJk3Ta597R6pETe',
}

headers = {
    'authority': 'www.perplexity.ai',
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9',
    'baggage': 'sentry-environment=production,sentry-release=0xtkVeTrmnpDahoxo4THU,sentry-public_key=bb45aa7ca2dc43b6a7b6518e7c91e13d,sentry-trace_id=55abe6249983457b88d905d0b75ef778',
    'content-type': 'application/x-www-form-urlencoded',
    # 'cookie': '__cf_bm=khJmahrhypkQ41IiTU0jL4jOXoUjP1ZavYkE_1rWJsg-1698645612-0-AfDMTqcQv0HGZJfyJ094aJI7Aote+jwIWd9pMooy/Vh5p1f/EF8ay4OszmfnImP70QBhsgTXuX8KfTO+TBu4ErM=; next-auth.csrf-token=c7fce17d9ab676c261acacf4799d03381504fe826a8a8c28889b3d513c85dcb7%7C0314bf69e6a06957c0c991ecc94e5d6d37e94bed3084aa19e44da442ffa2cb9f; g_state={"i_p":1698652818272,"i_l":1}; __Secure-next-auth.callback-url=https%3A%2F%2Fwww.perplexity.ai%2Fapi%2Fauth%2Fsignin-callback%3Fredirect%3Dhttps%253A%252F%252Fwww.perplexity.ai; __cflb=02DiuDyvFMmK5p9jVbWbam6CcSLCt41haw3efCACkzfLg; AWSALB=BxutSOSNca4c88qzRkflwCPlBZbsUZ/aViIfmS+I1Kf2aA/YieS3CWNaLRbbKDHIerQKdREeDtJxkQEORTChnHiEcurVBv3eL130xQ0vuF1qrlJk3Ta597R6pETe; AWSALBCORS=BxutSOSNca4c88qzRkflwCPlBZbsUZ/aViIfmS+I1Kf2aA/YieS3CWNaLRbbKDHIerQKdREeDtJxkQEORTChnHiEcurVBv3eL130xQ0vuF1qrlJk3Ta597R6pETe',
    'origin': 'https://www.perplexity.ai',
    'referer': 'https://www.perplexity.ai/',
    'sec-ch-ua': '"Chromium";v="118", "Google Chrome";v="118", "Not=A?Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'sentry-trace': '55abe6249983457b88d905d0b75ef778-9be34d7c706d2299-0',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36',
}

params = ''

data = {
    'email': 'bri.ti.i.alr.ey.a@gmail.com',
    'callbackUrl': '',
    'csrfToken': 'c7fce17d9ab676c261acacf4799d03381504fe826a8a8c28889b3d513c85dcb7',
    'json': 'true',
}

response = requests.post(
    'https://www.perplexity.ai/api/auth/signin/email',
    params=params,
    cookies=cookies,
    headers=headers,
    data=data,
)
