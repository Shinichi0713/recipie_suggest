import requests
from bs4 import BeautifulSoup
import urllib.parse
import certifi
import ssl


def google_image_search(query, num_images=10):
    query = urllib.parse.quote_plus(query)
    url = f"https://www.google.com/search?tbm=isch&q={query}"

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }
    path_cert = r"C:\python\Lib\site-packages\certifi\cacert.pem"
    ssl_context = ssl.create_default_context(cafile=certifi.where())
    response = requests.get(url, headers=headers, verify=ssl_context)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, 'html.parser')
    image_elements = soup.find_all('img', {'class': 't0fcAb'}, limit=num_images)

    image_urls = [img['src'] for img in image_elements]
    return image_urls

if __name__ == "__main__":
    QUERY = '猫'  # 検索キーワード
    NUM_IMAGES = 10  # 取得する画像の数

    image_urls = google_image_search(QUERY, NUM_IMAGES)
    for idx, url in enumerate(image_urls):
        print(f"{idx + 1}: {url}")