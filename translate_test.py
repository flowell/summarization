from urllib import parse
from urllib import request
import json
if __name__ == "__main__":
    url = "http://fanyi.baidu.com/v2transapi"
    Form_Data = {
        "from": "en",
        "to": "zn",
        "query": "apple",
        "transtype": "translang",
        "simple_means_flag": 3,
        "token": "dba977c37dec231310dbe9f6c65fd8e8",
        "sign": 704513.926512
    }
    data = parse.urlencode(Form_Data).encode('utf-8')
    response = request.urlopen(url, data)
    result = response.read().decode('utf-8')
    print(result)
    # 使用JSON
    translate_results = json.loads(result)
    # 找到翻译结果
    #translate_results = translate_results['translateResult'][0][0]['tgt']
