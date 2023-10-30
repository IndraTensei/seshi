import requests

cookies = {
    'XSRF-TOKEN': 'eyJpdiI6InA2eXRoM3cwMUt1T0tvSW5rRVZyM3c9PSIsInZhbHVlIjoiRndzZWZ0Q21vYit5ekk5WWpPaW5PVTBWQ3IyTmxUUWJkc0VnaVNXOXBCcnh6TFJFU01pQnlEcWk2N1FFV0RIS0l5SHZtRjJ2Tm5iclNEc2JVK2hIdEdKRzRERHVpRzBGNnZqaHBaakJTejJ0RWVDa04zUXVnSUlHQ1V0TVhFVWgiLCJtYWMiOiI1NmUwN2FlMDYzZmVlYTJhYWFhODgxOWE0MGFmYTRmNTg0Mzk4ODdhMWFhZDNmNDJlNDlmZGE5Mjk0NGNkNTFkIiwidGFnIjoiIn0%3D',
    'gmailnator_session': 'eyJpdiI6Iml5K3k3VVJ5NzErSHMzSEY4Q294cVE9PSIsInZhbHVlIjoiak85cHNXQnhta3RPUjNIaVVmZ2I4UStLbVV5QlZsaXc5QktiL1RGcUhqRzVmNkdLWWErdXBUV2p3cFl1bUNFa0VrWHlkaVVMbmhJV0NnMUpxL2pya3Bhb0pTb2lVelZUOWR1R3d0Z1orVGJwOVd6bWNGYkJndjd6OVZNNDUvbkoiLCJtYWMiOiI1YjEzNDdlOWQ2MWMxZDAyMWIyOGYzODMzOTZlYzQzMjIwNzZkMTA1ZjcyMTA0OWVmYzYyZGZmMDcwZDdlZmM4IiwidGFnIjoiIn0%3D',
}

headers = {
    'authority': 'www.emailnator.com',
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'en-US,en;q=0.9',
    'content-type': 'application/json',
    # 'cookie': 'XSRF-TOKEN=eyJpdiI6InA2eXRoM3cwMUt1T0tvSW5rRVZyM3c9PSIsInZhbHVlIjoiRndzZWZ0Q21vYit5ekk5WWpPaW5PVTBWQ3IyTmxUUWJkc0VnaVNXOXBCcnh6TFJFU01pQnlEcWk2N1FFV0RIS0l5SHZtRjJ2Tm5iclNEc2JVK2hIdEdKRzRERHVpRzBGNnZqaHBaakJTejJ0RWVDa04zUXVnSUlHQ1V0TVhFVWgiLCJtYWMiOiI1NmUwN2FlMDYzZmVlYTJhYWFhODgxOWE0MGFmYTRmNTg0Mzk4ODdhMWFhZDNmNDJlNDlmZGE5Mjk0NGNkNTFkIiwidGFnIjoiIn0%3D; gmailnator_session=eyJpdiI6Iml5K3k3VVJ5NzErSHMzSEY4Q294cVE9PSIsInZhbHVlIjoiak85cHNXQnhta3RPUjNIaVVmZ2I4UStLbVV5QlZsaXc5QktiL1RGcUhqRzVmNkdLWWErdXBUV2p3cFl1bUNFa0VrWHlkaVVMbmhJV0NnMUpxL2pya3Bhb0pTb2lVelZUOWR1R3d0Z1orVGJwOVd6bWNGYkJndjd6OVZNNDUvbkoiLCJtYWMiOiI1YjEzNDdlOWQ2MWMxZDAyMWIyOGYzODMzOTZlYzQzMjIwNzZkMTA1ZjcyMTA0OWVmYzYyZGZmMDcwZDdlZmM4IiwidGFnIjoiIn0%3D',
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

json_data = {
    'email': 'du.r.ani.salbe.r.t@gmail.com',
}

response = requests.post('https://www.emailnator.com/message-list', cookies=cookies, headers=headers, json=json_data)