import webbot
import time
driver = webbot.Browser();
yt_id = 'UCvgvktJEZQhPZMJWzF4tojg'
driver.go_to('https://mytoolstown.com/youtube/earn/');
driver.scrolly(400);
driver.type(yt_id, into='Channel Link / ID.');
driver.click('SEARCH CHANNEL');
driver.go_to('https://mytoolstown.com/youtube/earn/');
driver.scrolly(300);
driver.click(id='checkbox1');
driver.click(text='Like')
while True:
	time.sleep(0.001)