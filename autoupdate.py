import requests
import os

def update_check(githubraw_url, lang="en"):
    messages = {
        "en": {
            "update_available": "Update available!",
            "update_not_required": "Update not required.",
            "failed_to_fetch": "Failed to fetch data from GitHub Raw."
        },
        "ru": {
            "update_available": "Доступно обновление!",
            "update_not_required": "Обновление не требуется.",
            "failed_to_fetch": "Не удалось получить данные из GitHub Raw."
        }
    }

    r = requests.get(githubraw_url)
    if r.status_code == 200:
        remote_code = r.text
        with open(__file__, 'r') as f:
            local_code = f.read()
        if remote_code != local_code:
            print(messages[lang]["update_available"])
            return True
        else:
            print(messages[lang]["update_not_required"])
            return False
    else:
        print(messages[lang]["failed_to_fetch"])
        return False
