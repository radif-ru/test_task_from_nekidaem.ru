# Запуск проекта:
## После запуска доступ на локальной машине по адресу и порту: http://127.0.0.1:3333
### Если пользователь не добавлен в группу docker:  
> sudo groupadd docker 
> 
> sudo usermod -aG docker username 
> 
> newgrp docker 

### Запуск prod версии:
#### Остановить контейнеры: 
> docker-compose -f docker-compose.prod.yml down -v
#### Выдать права на запуск данных скриптов: 
> chmod +x ./blog/entrypoint.sh && chmod +x ./blog/entrypoint.prod.sh
#### Создать образ и запустить контейнер в фоне:
> docker-compose -f docker-compose.prod.yml up -d --build
#### Выполнить миграции
> docker-compose -f docker-compose.prod.yml exec web python manage.py migrate --noinput
#### Сборка стандартных и подготовленных статических файлов 
> docker-compose -f docker-compose.prod.yml exec web python manage.py collectstatic --no-input --clear
#### Заполнить таблицы подготовленными данными
> docker-compose -f docker-compose.prod.yml exec web python manage.py fill_db

 При запуске `python manage.py fill_db` генерируются суперюзер `radif`, 
 обычные пользователи `Kolya`, `Alyosha`.
 Пароль у админа и пользователей `qwertytrewq`.
 Так же происходит автозаполнение таблицы постов с привязкой 
 к этим пользователям

### Запуск dev версии:
#### Выдать права на запуск данных скриптов: 
> chmod +x ./blog/entrypoint.sh && chmod +x ./blog/entrypoint.prod.sh
#### Собрать образ и запустить контейнер в фоне:
> docker-compose up -d --build 


# Полезные командны: 

#### Создать образ: 
> docker-compose build 
#### Запустить контейнер:
> docker-compose up
#### Посмотреть все образы/контейнеры/тома
> docker image ls && docker container ls && docker volume ls
#### Удалить неиспользуемые контейнеры/образы/тома
> docker container prune && docker image prune && docker volume prune
#### Удалить тома вместе с контейнерами 
> docker-compose down -v
#### Проверка наличия ошибок в журналах, просмотр логов
> docker-compose logs -f
#### Зайти в работающий контейнер 
> docker exec -it CONTAINER ID bash
#### Проверить, что том (volume) был создан: 
> docker volume inspect django-on-docker_postgres_data
#### Удалить образ 
> docker rmi CONTAINER ID `или` docker rmi -f CONTAINER ID
#### Удалить образы, контейнеры по названию или id
> docker image rm name_or_id `контейнер` docker container rm name_or_id
#### Приостановить контейнер 
> docker stop CONTAINER ID
#### Запустить ранее остановленный контейнер 
> docker start CONTAINER ID
#### Перегрузить контейнер 
> docker restart CONTAINER ID
#### Посмотреть работающие и все контейнеры 
> docker ps `и` docker ps -a
#### Посмотреть список всех образов
> docker images

### Работа с django, manage.py:
#### Очистка таблиц:
> docker-compose exec web python manage.py flush --no-input 
#### Создание и запуск миграций:
> python manage.py makemigrations --no-input
> 
> docker-compose exec web python manage.py migrate 

### Вход в postgres: 
> docker-compose exec db psql --username=admin --dbname=blog_db 
#### Внутри postgres: 
#### Показать базы данных: ` # \l `
#### Подключение к базе данных: ` # \c blog_db ` 
#### Список зависимостей:  ` # \dt ` 
#### Выход из postgres  ` # \q `


# Задание:

Реализовать бэкенд с минимальным фронтендом (можно на голом HTML):

Имеется база стандартных пользователей Django (добавляются через админку, регистрацию делать не надо).
У каждого пользователя есть персональный блог. Новые создавать он не может.
Пост в блоге — элементарная запись с заголовком, текстом и временем создания.
Пользователь может подписываться (отписываться) на блоги других пользователей (любое количество).
У пользователя есть персональная лента новостей, в которой в обратном хронологическом порядке выводятся посты из блогов, на которые он подписан.
Пользователь может помечать посты в ленте прочитанными.
При добавлении/удалении подписки содержание ленты меняется (при удалении подписки пометки о "прочитанности" сохранять не нужно).
При добавлении поста в ленту — подписчики получают почтовое уведомление со ссылкой на новый пост.
Изменение содержания лент подписчиков (и рассылка уведомлений) должно происходить как при стандартной публикации поста пользователем через интерфейс сайта, так при добавлении/удалении поста через админку.

Техника:
Python 3.x, Django > 3.х, Postgresql или SQLite. 
Проект должен быть на гитхабе и отражать процесс разработки.
Код максимально приближенный к боевому (насколько получится).
Реализовать на Class-based views.

Проект необходимо упаковать в докер. Запускать через docker-compose.

В проекте должно быть README с описанием запуска проекта.

Срок выполнения 1-2 дня.

Результат выложить на github или bitbucket и прислать ссылку на info@nekidaem.ru.

https://docs.google.com/document/d/1oS2m4lLskCUQCUpPqzwcS8mcPCAvlBLqUM6u-cHc_38/edit#heading=h.ynpjfxumehs
