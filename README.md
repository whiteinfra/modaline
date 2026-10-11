# ModaLine — інтернет-магазин одягу (лабораторна робота №1)

Репозиторій до лабораторної роботи №1 з дисципліни «Технології створення програмних продуктів»: технічне завдання, вибір моделі життєвого циклу, політика версіонування і шаблони командної роботи. Окрім документів, тут є мінімальний Flask API — на ньому показано роботу GitFlow і семантичного версіонування.

**Автор:** Білоус Владислав, група К-41.

## Структура

```
lab-bilous-vladyslav/
├─ ТЗ.md                    # технічне завдання на MVP
├─ LIFECYCLE.md             # обґрунтування моделі життєвого циклу (Scrum)
├─ VERSIONING.md            # SemVer + GitFlow, команди Git
├─ RELEASE_TEMPLATE.md      # шаблон release notes
├─ CHANGELOG.md             # історія змін (Keep a Changelog)
├─ ACCEPTANCE_CHECKLIST.md  # чекліст приймання фічі
├─ releases/                # заповнені release notes для кожного тегу
├─ app/                     # Flask API (catalog, auth)
├─ tests/                   # pytest-тести
├─ .github/workflows/       # CI (тести) і Release (артефакт на тег v*)
├─ VERSION                  # поточна версія (джерело істини)
└─ requirements.txt
```

## Модель життєвого циклу (коротко)

Обрано **Agile/Scrum** зі спринтами по 2 тижні. Вимоги до магазину часто змінюються, а Scrum дає працюючий інкремент і зворотний зв’язок від замовника кожні два тижні. Спринти поєднано з GitFlow: історія — гілка `feature/*`, інкремент — `develop`, реліз — тег у `main`. Детально — у [LIFECYCLE.md](LIFECYCLE.md).

## Як запустити й перевірити

```bash
python -m venv .venv && . .venv/bin/activate      # Windows: .venv\Scripts\activate
pip install -r requirements.txt
pytest -q                                          # запуск тестів
flask --app app:create_app run                     # http://127.0.0.1:5000/api/products
```

Перевірка версіонування:

```bash
git log --graph --oneline --decorate --all   # історія гілок і злиттів
git branch -a                                # гілки
git tag -n                                   # теги релізів з описом
git describe --tags                          # поточна версія з тегу
git show v1.0.0 --stat                       # що увійшло в реліз 1.0.0
```

## Ендпоінти API

| Метод | URL | Опис |
|---|---|---|
| GET | `/api/version` | Поточна версія застосунку |
| GET | `/api/products?category=&size=` | Каталог з фільтрами |
| GET | `/api/products/<id>` | Картка товару |
| POST | `/api/auth/login` | Вхід, повертає токен (тестовий користувач `student@modaline.ua` / `Passw0rd!`) |
