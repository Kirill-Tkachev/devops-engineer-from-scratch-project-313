### Hexlet tests and linter status

[![Actions Status](https://github.com/Kirill-Tkachev/devops-engineer-from-scratch-project-313/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/Kirill-Tkachev/devops-engineer-from-scratch-project-313/actions)

[![CI](https://github.com/Kirill-Tkachev/devops-engineer-from-scratch-project-313/actions/workflows/ci.yml/badge.svg)](https://github.com/Kirill-Tkachev/devops-engineer-from-scratch-project-313/actions/workflows/ci.yml)

# Проект "Деплой приложения на PaaS"

## Требования

- Python 3.12 или выше
- uv
- GNU Make

## Установка зависимостей

```bash
uv sync
```

## Запуск приложения

```bash
make run
```

После запуска приложение будет доступно по адресу:

```
http://localhost:8080/ping
```

Маршрут `/ping` возвращает:

```
pong
```

## Развернутое приложение

Основной адрес:

https://devops-engineer-from-scratch-project-313-nnw6.onrender.com

Проверка работоспособности:

https://devops-engineer-from-scratch-project-313-nnw6.onrender.com/ping