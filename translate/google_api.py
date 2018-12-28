from googletrans import Translator
import requests


def get_proxy():
    return requests.get('http://127.0.0.1:5010/get/', timeout=3).content


def delete_proxy(proxy):
    requests.get('http://127.0.0.1:5010/delete/?proxy=%s' % proxy.decode())
    # print("http://127.0.0.1:5010/delete/?proxy=%s" % proxy.decode(), '删除')


def google_tran(text_1, des_1='zh-cn', src_1='auto'):
    retry_count = 5
    try:
        proxy = get_proxy()
    except Exception:
        proxy = b''
    # print(proxy, 'gg')
    if proxy != b'':
        proxies = {'http': 'http://%s' % proxy.decode()}
        # print(proxies, 'gg')
        # return

    else:
        # print(proxy)
        proxies = None
    while retry_count > 0:
        try:
            # print(proxies, '代理地址')
            if proxies is not None:
                translator = Translator(service_urls=['translate.google.cn'], proxies=proxies, timeout=5)
                # print('使用代理')
            else:
                translator = Translator(service_urls=['translate.google.cn'], timeout=5)
                # print('没使用代理')
            translations = translator.translate(text_1, dest=des_1, src=src_1)
            return translations
        except Exception:
            retry_count -= 1
    delete_proxy(proxy)
    google_tran(text_1, des_1, src_1)
    return None


if __name__ == '__main__':
    p = google_tran('i love you, These will be removed in APScheduler 4.0.', 'zh-cn', 'auto')
    print(p.text)
