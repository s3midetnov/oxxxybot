from lyricsgenius import Genius
import random
import requests


genius = Genius(token)

where_to_go = open("/Users/artemsemidetnov/PycharmProjects/genius/names_of_songs", "r")

n = random.randint(0, 215)
sngs = where_to_go.readlines()
print(sngs[n])
def oper(w):
    u = w.split("/")
    u1 = u[2]
    le = len(u1)
    gg = u1[:le-1]
    return gg

id = oper(sngs[n])

gonogo = open("/Users/artemsemidetnov/PycharmProjects/genius/fornow.txt", "w")
gonogo.write(genius.lyrics(id))
gonogo = open("/Users/artemsemidetnov/PycharmProjects/genius/fornow.txt", "r")
lyroc = gonogo.readlines()

ans = ""

ind = 1
while ind:
    m = random.randint(2, len(lyroc)-1)
    if lyroc[m][0]!= '[':
        ind  = 0
        ans = lyroc[m]
def send_message(msg):

    requests.get(artem_url)
    requests.get(grisha_url)
    requests.get(petr_url)
    requests.get(zhenia_url)
    requests.get(katia_url)
send_message(ans)