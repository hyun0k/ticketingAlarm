import requests
from bs4 import BeautifulSoup
import telegram
from apscheduler.schedulers.blocking import BlockingScheduler

bot = telegram.Bot(token='') # 자신의 api 키 입력
url = 'http://www.cgv.co.kr/common/showtimes/iframeTheater.aspx?areacode=01&theatercode=0013&date=20190623'

def alarm():
    html = requests.get(url)
    soup = BeautifulSoup(html.text, 'html.parser')
    fordx = soup.select_one('span.forDX')

    if (fordx):
        fordx = fordx.find_parent('div', class_='col-times')
        title = fordx.select_one('div.info-movie > a > strong').text.strip()
        bot.send_message(chat_id=1234567, text=title + ' 4DX 예매가 열렸습니다.') # chat_id에 자신의 id입력
        sched.pause()

sched = BlockingScheduler()
sched.add_job(alarm, 'interval', seconds=30)
sched.start()
