import requests

res = requests.get('https://automatetheboringstuff.com/files/rj.txt')

if res.status_code < 300:
    # wb -> write binary, maintain unicode encoding of the text
    rjFile = open('romeoAndJuliet.txt', 'wb')

    for chunk in res.iter_content(100000):
        rjFile.write(chunk)