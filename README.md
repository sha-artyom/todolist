## Дипломный проект TODOLIST

В данном проекте представлено приложение для отслеживания выполнения задач и напоминаний.

### Deploy
Приложение доступно по адресу <http://skypro-ashagalov.ga>

Все необходимые docker-образы загружены на сервер.
Отслеживание изменений происходит автоматически при обновлении проекта на GitHub.

### Telegram-бот
В качестве мобильной версии приложения доступен Telegram-бот, позволяющий просматривать цели,
а также создавать новые в уже существующих категориях.

Бот: _@Artyom_diplom_bot_

### Доступный функционал:
* Пользователи:
  * Создание пользователя
  * Просмотр, редактирование, удаление профиля
  * Изменение пароля
* Цели:
  * Создание цели
  * Просмотр, редактирование, удаление цели
  * Просмотр списка целей
* Категории:
  * Создание категории
  * Просмотр, редактирование, удаление категории
  * Просмотр списка категорий
* Доски:
  * Создание доски
  * Просмотр, редактирование, удаление доски
  * Просмотр списка досок
* Комментарии:
  * Создание комментария
  * Просмотр, редактирование, удаление комментария
  * Просмотр списка комментариев

### Тесты
Разработаны автоматические тесты, покрывающие основной функционал приложения

Запуск тестов: `pytest`
___
### Стек:
- python 3.11.3
- Django 4.2
- PostgreSQL 12.4-alpine

___
Для запуска проекта на локальной машине следует выполнить в терминале следующие команды:
```
docker-compose up -d
python manage.py migrate

```
