# Changelog

Усі помітні зміни проєкту документуються в цьому файлі.
Формат базується на [Keep a Changelog](https://keepachangelog.com/uk/1.1.0/),
проєкт дотримується [семантичного версіонування](https://semver.org/lang/uk/).

## [Unreleased]

## [1.0.1] - 2026-10-11

### Fixed
- Вхід не залежить від регістру та пробілів в email.
- Запит на вхід без email або пароля повертає 400 замість 500.

## [1.0.0] - 2026-10-11

### Added
- Технічне завдання (ТЗ.md) та обґрунтування моделі життєвого циклу (LIFECYCLE.md).
- Політика версіонування SemVer + GitFlow (VERSIONING.md).
- Шаблони: RELEASE_TEMPLATE.md, CHANGELOG.md, ACCEPTANCE_CHECKLIST.md.
- Каталог товарів: `GET /api/products` з фільтрами `category`, `size`; `GET /api/products/<id>`.
- CI: запуск pytest у GitHub Actions на кожен push і pull request.
- Вхід користувача: `POST /api/auth/login` (повертає токен).
- Release-конвеєр: збірка zip-артефакту і GitHub Release на тег `v*`.

