import requests

header = {}

header['Accept'] = 'application/json, text/plain, */*'
header['Accept-Language'] = 'zh - CN'
header['appkey'] = '8dc7959eeee2792ac2eebb490e60deed'
header['Cache-Control'] = 'no - cache'
header['Connection'] = 'Keep-Alive'
#header['Cookie'] = 'userKey=LxrmhTTY4ph8lZ1mhvHKh5TVQTZTJNrdx7d134dHYRvsxHMFLLVx!336910670!1510886968803; userKey=pSGnhTJFTT4gTKJlhYfZ4S4jnC5V2n1KHx1C8JkChQyJQFpj8z0w!1427213981!1510885861233; JSESSIONID=LxrmhTTY4ph8lZ1mhvHKh5TVQTZTJNrdx7d134dHYRvsxHMFLLVx!336910670'
cookies = 'userKey=LxrmhTTY4ph8lZ1mhvHKh5TVQTZTJNrdx7d134dHYRvsxHMFLLVx!336910670!1510886968803; userKey=pSGnhTJFTT4gTKJlhYfZ4S4jnC5V2n1KHx1C8JkChQyJQFpj8z0w!1427213981!1510885861233; JSESSIONID=LxrmhTTY4ph8lZ1mhvHKh5TVQTZTJNrdx7d134dHYRvsxHMFLLVx!336910670'
header['Host'] = 'gsxt.cqgs.gov.cn'
header['Pragma'] = 'no - cache'
header['Referer'] = 'http://gsxt.cqgs.gov.cn/xxgg/xxggView.html?noticeid=LR5002341201711164025006&1'
header['User-Agent'] = 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 10.0; WOW64; Trident/7.0; .NET4.0C; .NET4.0E; Tablet PC 2.0)'
header['X-Requested-With'] = 'XMLHttpRequest'
         #'http://gsxt.cqgs.gov.cn/xxgg/xxggView.html?noticeid=LR5002341201711164025006&1'
url = 'http://gsxt.cqgs.gov.cn/gsxt/api/affichebase/queryForm/LR5002341201711164025006/0?currentpage=1&pagesize=5&t=1510888070017'

req = requests.get(url , headers=header)
print req.content

