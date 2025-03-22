import requests
from bs4 import BeautifulSoup
import json


def get_image_urls(keyword):
    extension_allowance = ["jpg", "jpeg", "png"]
    # インスタンスを作成
    url_query = f"https://www.bing.com/images/search?q={keyword}&form=HDRSC3&first=1&cw=1177&ch=844"
    # ページの内容を取得
    response = requests.get(url_query, verify=False)
    html_content = response.text

    # BeautifulSoupを使用してHTMLを解析
    soup = BeautifulSoup(html_content, "html.parser")

    # class="iusc"を持つ<a>タグを全て見つける
    a_tags = soup.find_all("a", class_="iusc")

    # 見つけた<a>タグを表示
    image_url = None
    for a_tag in a_tags:
        # print(a_tag)
        try:
            m_data = json.loads(a_tag['m'])
            image_url = m_data['murl']
            extension = image_url.split('.')[-1]
            if extension not in extension_allowance:
                image_url = None
            else:
                break
            # print(image_url)
        except:
            pass
    return image_url


if __name__ == "__main__":
    print(get_image_urls("pizza"))