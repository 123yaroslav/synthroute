---
name: new-adr
description: Create an Architecture Decision Record in docs/adr from the template with the next free number. Use when a significant technical or research decision is made or proposed.
argument-hint: "[краткое название решения]"
---
# Новый ADR

1. Найди следующий номер: `ls docs/adr` → `NNNN-<kebab-title>.md`.
2. Скопируй `docs/templates/adr.md` и заполни все разделы. Альтернатив должно быть минимум две, и у каждой нужна честная причина отказа.
3. Статус: `Предложено`. Статус `Принято` ставит человек после обсуждения.
4. Если решение отменяет прошлое, обнови статус старого ADR на `Заменено ADR-NNNN`.
5. Сошлись на ADR из затронутых правил или кода и покажи пользователю итог.
