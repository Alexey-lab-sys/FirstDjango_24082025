# FirstDjango_24082025

## Инструкция по развертыванию проекта
1. Создать виртуальное окружение
```
python3 -m venv django_venv
```
2. Активировать виртуальное окружение
```
source django_venv/bin/activate
```
3. Установить нужные библиотеки в виртуальное окружение
```
pip install -r requirements.txt
```
4. Применить миграции
```
python manage.py migrate
```
5. Запуск сервера
```
python manage.py runserver
``` 

## Запуск `ipython` в контексте `django` приложений
```
python manage.py shell_plas --ipython
```

## Дополнительно
1. Полезное расширение для шаблонов `django`
```
exit install batisteo.vscode-django
```
2. Добавить в `settings.json`:
```
"emmet.includeLanguages": {"django-html": "html"},
"files.associations": {"*.html": "django-html"}
```