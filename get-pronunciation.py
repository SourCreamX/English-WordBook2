import requests, csv, time
from bs4 import BeautifulSoup

base_url = 'https://ejje.weblio.jp/content/'

for i in range(1,8):
    filename = 'dict/chapter' + str(i) + '.csv'
    with open(filename) as f:
        reader = csv.reader(f)
        wordlist = [row for row in reader]


    for w in wordlist:
        url = base_url + w[0]

        res = requests.get(url)
        soup = BeautifulSoup(res.text, 'html.parser')
        
        try:
            mp3_dl_url = soup.find('source')['src']
            print(w[0])
            
            response = requests.get(mp3_dl_url)
            mp3 = response.content

            save_file = './pronunciation/' + w[0] + '.mp3'
            
            with open(save_file,'wb') as f:
                f.write(mp3)

        except:
            print('error:{}'.format(w[0]))
        
        time.sleep(5)


