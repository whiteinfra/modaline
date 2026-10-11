# Release v{version} — {release-date}

> Коротко (1–2 речення): що головне в цьому релізі і для кого.

## Нове
- feat({scope}): Опис нової функції (#{issue})

## Покращено
- perf/refactor({scope}): Опис покращення

## Виправлено
- fix({scope}): Опис виправленої помилки (#{issue})

## Зламні зміни (BREAKING CHANGES)
- Лише для MAJOR-версій: що змінилося і як мігрувати

## Відомі проблеми
- Опис проблеми та тимчасове рішення (workaround)

## Встановлення / оновлення
```bash
git fetch --tags
git checkout v{version}
pip install -r requirements.txt
```

## Перевірка перед публікацією
- [ ] CI зелений для тегу `v{version}`
- [ ] Виконано ACCEPTANCE_CHECKLIST.md
- [ ] Оновлено CHANGELOG.md

**Повний перелік змін:** `git log --oneline v{previous}..v{version}`
