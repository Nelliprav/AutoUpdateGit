- lang="ru" - Русский язык модуля
- lang="en" - English language module

- requests - the module does not need to be imported.


```py
from autoupdate import *

githubraw_url="https://raw.githubusercontent.com/username/repo/main/file.py" # url raw file


#module usage example
if update_check(githubraw_url, lang="ru"):
    r = requests.get(githubraw_url)
    with open(__file__, 'w') as f:
        f.write(r.text)
```
