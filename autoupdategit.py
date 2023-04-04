import requests
import os
from tqdm import tqdm

def update_check(githubraw_url, lang="en"):
    messages = {
        "en": {
            "update_available": "New update available!",
            "update_not_required": "Update not required.",
            "failed_to_fetch": "Failed to fetch data from GitHub Raw.",
            "update_succes": "Update completed successfully!"
        },
        "ru": {
            "update_available": "Доступно новое обновление!",
            "update_not_required": "Обновление не требуется.",
            "failed_to_fetch": "Не удалось получить данные с GitHub Raw.",
            "update_succes": "Обновление успешно выполнено!"
        },
        "kz": {
            "update_available": "Жаңарту қолжетімді!",
            "update_not_required": "Жаңарту қажет емес.",
            "failed_to_fetch": "GitHub Raw жүйесінен деректерді алу мүмкін болмады.",
            "update_succes": "Жаңарту сәтті аяқталды!"
        },
        "ua": {
            "update_available": "Доступне оновлення!",
            "update_not_required": "Оновлення не потрібне.",
            "failed_to_fetch": "Не вдалося отримати дані із GitHub Raw.",
            "update_succes": "Оновлення успішно виконане!"
        },
        "ar": {
            "update_available": "التحديث متاح!",
            "update_not_required": "لا يوجد تحديث مطلوب.",
            "failed_to_fetch": "فشل إحضار البيانات من GitHub Raw.",
            "update_succes": "اكتمل التحديث بنجاح!"
        }
    }

    r = requests.get(githubraw_url)
    if r.status_code == 200:
        remote_code = r.text
        with open(__file__, 'r') as f:
            local_code = f.read()
        if remote_code != local_code:
            print(messages[lang]["update_available"])
            with tqdm(total=100) as pbar:
                for i in range(100):
                    pbar.update(1)
            print(messages[lang]["update_succes"])
            return True
        else:
            print(messages[lang]["update_not_required"])
            return False
    else:
        print(messages[lang]["failed_to_fetch"])
        return False
