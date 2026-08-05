import re
import requests

base_url = 'https://quera.org/blog/'


def get_latest_posts():
    r = requests.get('https://quera.org/blog/')
    return re.findall(r'<h4> <a href="(.*)">(.*)</a></h4>', r.text)
