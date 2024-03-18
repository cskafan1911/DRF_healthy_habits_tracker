# «Атомные привычки» Джеймс Клир
### Backend Django для создания полезных привычек 
### После создания привычек, в указанное время приходит оповещение в телеграм, о времени начала выполнения привычки.

## Docker compose
1) Собрать образ и запустить контейнер с помощью команды: docker compose up --build
2) Для остановки и удаления контейнеров используйте Ctrl + C.

## Запуск (на Windows 10)
1) Установить зависимости: pip install -r requirements.txt
```
pip install -r requirements.txt
```
2) Создать базу данных postgres
```
CREATE DATABASE NAME_DB
```
3) Создать в корневой директории проекта файл .env и дописать в переменные окружения данные. (Шаблон можно посмотреть в файле .env.sample)
```
POSTGRES_USER=имя пользователя postgresql
POSTGRES_PASSWORD=пароль пользователя postgresql
POSTGRES_DB=имя базы данных для проекта
SECRET_KEY=секретный ключ Django
TELEGRAM_BOT = token для telegram
```
5) Применить миграции
```
python manage.py migrate
```
6) Для старта локального сервиса
```
python manage.py runserver
```
7) Для работы брокера Redis на Windows воспользуйтесь WSL
8) Для запуска периодических задач (отправки сообщений в telegram). Запускать в разных терминалах.
```
celery -A config beat -l info -S django
```
```
celery -A config worker -l info -P eventlet 
```

### Пользователь создает полезные привычки с полями:
* Место — место, в котором необходимо выполнять привычку.
* Время — время, когда необходимо выполнять привычку.
* Действие — действие, которое представляет собой привычка.
* Признак приятной привычки — привычка, которую можно привязать к выполнению полезной привычки.
* Связанная привычка - привычка, которая связана с другой привычкой, важно указывать для полезных привычек, но не для приятных
* Периодичность (по умолчанию ежедневная) - периодичность выполнения привычки, для напоминания в днях
* Вознаграждение - чем пользователь должен себя вознаградить после выполнения
* Время выполнения - время, которое предположительно потратит пользователь на выполнение привычки
* Признак публичности - привычки можно публиковать в общий доступ, чтобы другие пользователи могли брать в пример чужие привычки

Чем отличается полезная привычка от приятной и связанной?
Полезная привычка — это само действие, которое пользователь будет совершать и получать за его выполнение определенное вознаграждение (приятная привычка или любое другое вознаграждение).

Приятная привычка — это способ вознаградить себя за выполнение полезной привычки. Приятная привычка указывается в качестве связанной для полезной привычки (в поле «Связанная привычка»).

Например: в качестве полезной привычки вы будете выходить на прогулку вокруг квартала сразу же после ужина. Вашим вознаграждением за это будет приятная привычка — принять ванну с пеной. То есть такая полезная привычка будет иметь связанную привычку.

Рассмотрим другой пример: полезная привычка — «я буду не опаздывать на еженедельную встречу с друзьями в ресторан». В качестве вознаграждения вы заказываете себе десерт. В таком случае полезная привычка имеет вознаграждение, но не приятную привычку.

Признак приятной привычки — булево поле, которые указывает на то, что привычка является приятной, а не полезной.
