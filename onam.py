import requests

# A program to translate into all languages
# Education use
# Thank you Google Translate

url = "https://translate.google.co.in/_/TranslateWebserverUi/data/batchexecute"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:91.0) Gecko/20100101 Firefox/91.0",  # Adjust the user agent as needed
    "Content-Type": "application/x-www-form-urlencoded;charset=UTF-8",
}
languages = {
    'Afrikaans': 'af',
    'Albanian': 'sq',
    'Amharic': 'am',
    'Arabic': 'ar',
    'Armenian': 'hy',
    'Assamese': 'as',
    'Azerbaijani': 'az',
    'Bangla': 'bn',
    'Basque': 'eu',
    'Belarusian': 'be',
    'Bosnian': 'bs',
    'Bulgarian': 'bg',
    'Burmese': 'my',
    'Cantonese': 'zh-yue',
    'Catalan': 'ca',
    'Cebuano': 'ceb',
    'Central Kurdish': 'ckb',
    'Chakma': 'ccp',
    'Cherokee': 'chr',
    'Chinese (Hong Kong)': 'zh-HK',
    'Chinese (Simplified, China)': 'zh-Hans',
    'Chinese (Simplified)': 'zh-CN',
    'Chinese (Traditional, Taiwan)': 'zh-Hant',
    'Chinese (Traditional)': 'zh-TW',
    'Corsican': 'co',
    'Croatian': 'hr',
    'Czech': 'cs',
    'Danish': 'da',
    'Dutch': 'nl',
    'Dzongkha': 'dz',
    'English': 'en',
    'Esperanto': 'eo',
    'Estonian': 'et',
    'Filipino': 'fil',
    'Finnish': 'fi',
    'French': 'fr',
    'Galician': 'gl',
    'Georgian': 'ka',
    'German': 'de',
    'Greek': 'el',
    'Gujarati': 'gu',
    'Haitian Creole': 'ht',
    'Hebrew': 'he',
    'Hindi': 'hi',
    'Hmong': 'hmn',
    'Hungarian': 'hu',
    'Icelandic': 'is',
    'Indonesian': 'id',
    'Inuktitut': 'iu',
    'Irish': 'ga',
    'Italian': 'it',
    'Japanese': 'ja',
    'Javanese': 'jv',
    'Kannada': 'kn',
    'Kazakh': 'kk',
    'Khmer': 'km',
    'Korean': 'ko',
    'Kurdish': 'ku',
    'Kyrgyz': 'ky',
    'Lao': 'lo',
    'Latin': 'la',
    'Latvian': 'lv',
    'Lithuanian': 'lt',
    'Luxembourgish': 'lb',
    'Māori': 'mi',
    'Macedonian': 'mk',
    'Malagasy': 'mg',
    'Malay': 'ms',
    'Malayalam': 'ml',
    'Maltese': 'mt',
    'Manipuri (Meitei Mayek)': 'mni-Mtei',
    'Marathi': 'mr',
    'Mongolian': 'mn',
    'Navajo': 'nv',
    'Nepali': 'ne',
    'Norwegian Nynorsk': 'nn',
    'Norwegian': 'nb',
    'Nyanja': 'ny',
    'Odia': 'or',
    'Ojibwa': 'oj',
    'Pashto': 'ps',
    'Persian': 'fa',
    'Plains Cree': 'crk',
    'Polish': 'pl',
    'Portuguese (Brazil)': 'pt-BR',
    'Portuguese (Portugal)': 'pt-PT',
    'Punjabi': 'pa',
    'Romanian': 'ro',
    'Russian': 'ru',
    'Samoan': 'sm',
    'Sanskrit': 'sa',
    'Scottish Gaelic': 'gd',
    'Serbian': 'sr',
    'Shona': 'sn',
    'Sindhi': 'sd',
    'Sinhala': 'si',
    'Slovak': 'sk',
    'Slovenian': 'sl',
    'Somali': 'so',
    'Spanish': 'es',
    'Swahili': 'sw',
    'Swedish': 'sv',
    'Tajik': 'tg',
    'Tamil': 'ta',
    'Telugu': 'te',
    'Thai': 'th',
    'Tibetan': 'bo',
    'Tigrinya': 'ti',
    'Turkish': 'tr',
    'Ukrainian': 'uk',
    'Urdu': 'ur',
    'Uyghur': 'ug',
    'Uzbek': 'uz',
    'Vietnamese': 'vi',
    'Welsh': 'cy',
    'Western Frisian': 'fy',
    'Xhosa': 'xh',
    'Yiddish': 'yi',
    'Yoruba': 'yo',
    'Zulu': 'zu',
}

def parse(count,unparse,lang):
    ind = unparse.index('"'+lang)
    need = unparse[ind:]
    need2 = need.split(",")[7]
    need3 = need2.split('"')[1]
    print(count," . ",lang," : ", need3[:-1])


text = input(" Enter your text: ")
# text = "happy onam to you"


payval = '[[["MkEWBc","[[\\"'+text+'\\",\\"auto\\",\\"lang\\",1],[]]","null","generic"]]]'

params = {
    "rpcids": "MkEWBc",
    "source-path": "/",
    "f.sid": "5646788640256968910",
    "bl": "boq_translate-webserver_20230823.07_p0",
    "hl": "en-US",
    "soc-app": "1",
    "soc-platform": "1",
    "soc-device": "1",
    "_reqid": "777465",
    "rt": "c",
}

count = 0
for lang in languages.values():
    v = payval.replace("lang",lang)
    payload = {"f.req": v}
    count += 1
    response = requests.post(url, headers=headers, data=payload, params=params)
    # print("irruku  ",count , "  ")
    try:
        parse(count,response.text,lang)  # Print the response content
    except:
        continue
