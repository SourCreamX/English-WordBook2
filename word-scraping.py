import requests, csv
from bs4 import BeautifulSoup

url = 'https://englishlevelup.net/toeic-word-list/'
res = requests.get(url)
soup = BeautifulSoup(res.text, 'html.parser')

w = soup.find_all('td')

word = []
for i in range(0,4000, 2): 
    tmp = []
    tmp.append(w[i].get_text())
    tmp.append(w[i+1].get_text())
    word.append(tmp)

w1 = word[0:300]
w2 = word[300:600]
w3 = word[600:900]
w4 = word[900:1200]
w5 = word[1200:1500]
w6 = word[1500:1800]
w7 = word[1800:2000]

word_list = []
word_list += [w1,w2,w3,w4,w5,w6,w7]

for i,x in enumerate(word_list):
    filename = 'dict/chapter' + str(i+1) + '.csv'
    with open(filename,'w') as f:
        writer = csv.writer(f, lineterminator='\n')
        writer.writerows(x)
