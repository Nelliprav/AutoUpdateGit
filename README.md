#### AutoUpdateGit - Docs



- lang="ru" - Русский язык модуля
- lang="en" - English language module
- lang="ua" - Українська мова модуля
- lang="ar" - وحدة اللغة العربية
- lang="kz" - Қазақ тілі модулі

- requests - the module does not need to be imported.

```py
pip install AutoUpdateGit
```

import AutoUpdateGit
import requests

 # ссылка на raw файл

githubraw_url = "https://raw.githubusercontent.com/Nelliprav/NikkeBot/main/main.py"

def update_check(githubraw_url=githubraw_url, lang="ru"):
    r = requests.get(githubraw_url)
    with open(__file__, 'w') as f:
        f.write(r.text)

if __name__ == "__main__":
    update_check()
