import perplexity

perplexity_headers = {
    'authority': 'www.perplexity.ai',
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9',
    'baggage': 'sentry-environment=production,sentry-release=0xtkVeTrmnpDahoxo4THU,sentry-public_key=bb45aa7ca2dc43b6a7b6518e7c91e13d,sentry-trace_id=55abe6249983457b88d905d0b75ef778',
    'content-type': 'application/x-www-form-urlencoded',
    'cookie': '__cf_bm=khJmahrhypkQ41IiTU0jL4jOXoUjP1ZavYkE_1rWJsg-1698645612-0-AfDMTqcQv0HGZJfyJ094aJI7Aote+jwIWd9pMooy/Vh5p1f/EF8ay4OszmfnImP70QBhsgTXuX8KfTO+TBu4ErM=; next-auth.csrf-token=c7fce17d9ab676c261acacf4799d03381504fe826a8a8c28889b3d513c85dcb7%7C0314bf69e6a06957c0c991ecc94e5d6d37e94bed3084aa19e44da442ffa2cb9f; g_state={"i_p":1698652818272,"i_l":1}; __Secure-next-auth.callback-url=https%3A%2F%2Fwww.perplexity.ai%2Fapi%2Fauth%2Fsignin-callback%3Fredirect%3Dhttps%253A%252F%252Fwww.perplexity.ai; __cflb=02DiuDyvFMmK5p9jVbWbam6CcSLCt41haw3efCACkzfLg; AWSALB=BxutSOSNca4c88qzRkflwCPlBZbsUZ/aViIfmS+I1Kf2aA/YieS3CWNaLRbbKDHIerQKdREeDtJxkQEORTChnHiEcurVBv3eL130xQ0vuF1qrlJk3Ta597R6pETe; AWSALBCORS=BxutSOSNca4c88qzRkflwCPlBZbsUZ/aViIfmS+I1Kf2aA/YieS3CWNaLRbbKDHIerQKdREeDtJxkQEORTChnHiEcurVBv3eL130xQ0vuF1qrlJk3Ta597R6pETe',
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

perplexity_cookies = {
    '__cf_bm': 'khJmahrhypkQ41IiTU0jL4jOXoUjP1ZavYkE_1rWJsg-1698645612-0-AfDMTqcQv0HGZJfyJ094aJI7Aote+jwIWd9pMooy/Vh5p1f/EF8ay4OszmfnImP70QBhsgTXuX8KfTO+TBu4ErM=',
    'next-auth.csrf-token': 'c7fce17d9ab676c261acacf4799d03381504fe826a8a8c28889b3d513c85dcb7%7C0314bf69e6a06957c0c991ecc94e5d6d37e94bed3084aa19e44da442ffa2cb9f',
    'g_state': '{"i_p":1698652818272,"i_l":1}',
    '__Secure-next-auth.callback-url': 'https%3A%2F%2Fwww.perplexity.ai%2Fapi%2Fauth%2Fsignin-callback%3Fredirect%3Dhttps%253A%252F%252Fwww.perplexity.ai',
    '__cflb': '02DiuDyvFMmK5p9jVbWbam6CcSLCt41haw3efCACkzfLg',
    'AWSALB': 'BxutSOSNca4c88qzRkflwCPlBZbsUZ/aViIfmS+I1Kf2aA/YieS3CWNaLRbbKDHIerQKdREeDtJxkQEORTChnHiEcurVBv3eL130xQ0vuF1qrlJk3Ta597R6pETe',
    'AWSALBCORS': 'BxutSOSNca4c88qzRkflwCPlBZbsUZ/aViIfmS+I1Kf2aA/YieS3CWNaLRbbKDHIerQKdREeDtJxkQEORTChnHiEcurVBv3eL130xQ0vuF1qrlJk3Ta597R6pETe',
}


emailnator_headers = { 
    headers = {
    'authority': 'www.emailnator.com',
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'en-US,en;q=0.9',
    'content-type': 'application/json',
    'cookie': 'XSRF-TOKEN=eyJpdiI6InA2eXRoM3cwMUt1T0tvSW5rRVZyM3c9PSIsInZhbHVlIjoiRndzZWZ0Q21vYit5ekk5WWpPaW5PVTBWQ3IyTmxUUWJkc0VnaVNXOXBCcnh6TFJFU01pQnlEcWk2N1FFV0RIS0l5SHZtRjJ2Tm5iclNEc2JVK2hIdEdKRzRERHVpRzBGNnZqaHBaakJTejJ0RWVDa04zUXVnSUlHQ1V0TVhFVWgiLCJtYWMiOiI1NmUwN2FlMDYzZmVlYTJhYWFhODgxOWE0MGFmYTRmNTg0Mzk4ODdhMWFhZDNmNDJlNDlmZGE5Mjk0NGNkNTFkIiwidGFnIjoiIn0%3D; gmailnator_session=eyJpdiI6Iml5K3k3VVJ5NzErSHMzSEY4Q294cVE9PSIsInZhbHVlIjoiak85cHNXQnhta3RPUjNIaVVmZ2I4UStLbVV5QlZsaXc5QktiL1RGcUhqRzVmNkdLWWErdXBUV2p3cFl1bUNFa0VrWHlkaVVMbmhJV0NnMUpxL2pya3Bhb0pTb2lVelZUOWR1R3d0Z1orVGJwOVd6bWNGYkJndjd6OVZNNDUvbkoiLCJtYWMiOiI1YjEzNDdlOWQ2MWMxZDAyMWIyOGYzODMzOTZlYzQzMjIwNzZkMTA1ZjcyMTA0OWVmYzYyZGZmMDcwZDdlZmM4IiwidGFnIjoiIn0%3D',
    'origin': 'https://www.emailnator.com',
    'referer': 'https://www.emailnator.com/inbox/',
    'sec-ch-ua': '"Chromium";v="118", "Google Chrome";v="118", "Not=A?Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36',
    'x-requested-with': 'XMLHttpRequest',
    'x-xsrf-token': 'eyJpdiI6InA2eXRoM3cwMUt1T0tvSW5rRVZyM3c9PSIsInZhbHVlIjoiRndzZWZ0Q21vYit5ekk5WWpPaW5PVTBWQ3IyTmxUUWJkc0VnaVNXOXBCcnh6TFJFU01pQnlEcWk2N1FFV0RIS0l5SHZtRjJ2Tm5iclNEc2JVK2hIdEdKRzRERHVpRzBGNnZqaHBaakJTejJ0RWVDa04zUXVnSUlHQ1V0TVhFVWgiLCJtYWMiOiI1NmUwN2FlMDYzZmVlYTJhYWFhODgxOWE0MGFmYTRmNTg0Mzk4ODdhMWFhZDNmNDJlNDlmZGE5Mjk0NGNkNTFkIiwidGFnIjoiIn0=',
}

}

emailnator_cookies = { 
    'XSRF-TOKEN': 'eyJpdiI6InA2eXRoM3cwMUt1T0tvSW5rRVZyM3c9PSIsInZhbHVlIjoiRndzZWZ0Q21vYit5ekk5WWpPaW5PVTBWQ3IyTmxUUWJkc0VnaVNXOXBCcnh6TFJFU01pQnlEcWk2N1FFV0RIS0l5SHZtRjJ2Tm5iclNEc2JVK2hIdEdKRzRERHVpRzBGNnZqaHBaakJTejJ0RWVDa04zUXVnSUlHQ1V0TVhFVWgiLCJtYWMiOiI1NmUwN2FlMDYzZmVlYTJhYWFhODgxOWE0MGFmYTRmNTg0Mzk4ODdhMWFhZDNmNDJlNDlmZGE5Mjk0NGNkNTFkIiwidGFnIjoiIn0%3D',
    'gmailnator_session': 'eyJpdiI6Iml5K3k3VVJ5NzErSHMzSEY4Q294cVE9PSIsInZhbHVlIjoiak85cHNXQnhta3RPUjNIaVVmZ2I4UStLbVV5QlZsaXc5QktiL1RGcUhqRzVmNkdLWWErdXBUV2p3cFl1bUNFa0VrWHlkaVVMbmhJV0NnMUpxL2pya3Bhb0pTb2lVelZUOWR1R3d0Z1orVGJwOVd6bWNGYkJndjd6OVZNNDUvbkoiLCJtYWMiOiI1YjEzNDdlOWQ2MWMxZDAyMWIyOGYzODMzOTZlYzQzMjIwNzZkMTA1ZjcyMTA0OWVmYzYyZGZmMDcwZDdlZmM4IiwidGFnIjoiIn0%3D',
}


perplexity_cli = perplexity.Client(perplexity_headers, perplexity_cookies)
perplexity_cli.create_account(emailnator_headers, emailnator_cookies) # Creates a new gmail, so your 5 copilots will be renewed. You can pass this one if you are not going to use "copilot" mode


# takes a string as query, and returns a string as answer.
def my_text_prompt_solver(query):
    return input(f'{query}: ')

# takes a string as description and a dictionary as options. Dictionary consists of ids and values. Example: {1: "Orange", 2: "Banana"}
# returns a list of integers which are ids of selected options. Let's say you selected "Banana", function should return [2]
def my_checkbox_prompt_solver(description, options):
    print(description + '\n' + '\n'.join([str(x) + ' - ' + options[x] for x in options]))
    return [int(input('--> '))]


# modes = ['concise', 'copilot']
# focus = ['internet', 'scholar', 'writing', 'wolfram', 'youtube', 'reddit']
# files = file list, each element of list is tuple like this: (data, filetype) perplexity supports two file types, txt and pdf
# follow_up = last query info for follow-up queries, you can directly pass response json from a query, look at second example below.
# solvers, list of functions to answer questions of ai while using copilot, there are 2 type of solvers, text and checkbox. If you do not define function for a solver, questions in that solver type will be skipped
resp = perplexity_cli.search('Your query here', mode='copilot', focus='internet', files=[(open('myfile.txt', 'rb').read(), 'txt'), (open('myfile2.pdf', 'rb').read(), 'pdf')], solvers={
    'text': my_text_prompt_solver,
    'checkbox': my_checkbox_prompt_solver
    })
print(resp)

# second example to show how to use follow-up queries
# you can't use file uploads on follow-up queries
# you can pass response json from a query directly like below
resp2 = perplexity_cli.search('Your query here', mode='copilot', focus='internet', follow_up=resp, solvers={
    'text': my_text_prompt_solver,
    'checkbox': my_checkbox_prompt_solver
    })
print(resp2)

# perplexity_cli.create_account(emailnator_headers, emailnator_cookies) # Call this function again when you run out of copilots