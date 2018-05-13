
import hashlib
import urllib.parse
import random
import json
import math
from urllib import request




def translate(original_text):
    #每次发送1500个汉字翻译，上限建议2000
    target_text = u''
    max_size = 1500
    times = int(math.floor((len(original_text) + max_size - 1) / max_size))
    for i in range(0, times-1):
        text = original_text[i*max_size: (i+1)*max_size-1]
        target_text += send(text)
    text = original_text[(times-1)*max_size: len(original_text)]
    target_text += send(text)
    return target_text


def send(query):
    q = query.replace('\n', '').replace('\r', '').replace(' ', '').replace('\t', '').replace(" ", '').replace('　', '')
    appid = '20180511000156980'
    secretKey = 'TFoUNgWt2rZY27oZXqtz'

    fromLang = 'zh'
    toLang = 'en'
    salt = random.randint(32768, 65536)

    sign = appid+q+str(salt)+secretKey
    m1 = hashlib.md5()
    m1.update(sign.encode("utf-8"))
    sign = m1.hexdigest()
    print(q)
    data = {
        'appid': appid,
        'q': q,
        'from': fromLang,
        'to': toLang,
        'salt': str(salt),
        'sign': sign
    }
    data_urlencode = urllib.parse.urlencode(data).encode('utf-8')
    print(data_urlencode)

    url='http://api.fanyi.baidu.com/api/trans/vip/translate'
    try:
        response = urllib.request.urlopen(url=url, data=data_urlencode)

        result = response.read()
        print(result)
        print("以下是翻译结果")
        data = json.loads(result)
        dst = data["trans_result"][0]["dst"]
        print(dst)
        return dst

    except Exception as e:
        print("错误：")
        print(e)



if __name__ == "__main__":
    input_path = r'C:\Code\Python\summarization\input\600340\758228292_业绩靓丽，成长延续_2018-05-02.txt'
    with open(input_path, 'r') as input_file:
        original_text = input_file.read()
    processed_text = translate(original_text)
    output_path = r'C:\Code\Python\summarization\output\600340\758228292_业绩靓丽，成长延续_2018-05-02.txt'
    with open(output_path, 'w') as output_file:
        output_file.write(processed_text)
    

