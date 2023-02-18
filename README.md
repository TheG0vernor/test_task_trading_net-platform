Тестовое задание 1. Платформа для онлайн-торговли.

<b>Project Stacks</b>: Python, Django, DRF, Postgres.

Запуск базы данных предполагается через docker-контейнер. Для этого выполните команду:

docker run --name <имя контейнера> -e POSTGRES_USER=<имя> -e POSTGRES_PASSWORD=<пароль> -e POSTGRES_DB=<имя базы данных> -p 5432:5432 -d postgres:latest <br>
(без <>)

Указанные в команде выше переменные должны быть перечислены в файле .env, пример которого размещён в корне проекта в файле .env.example.

Структура проекта:

- commercial_network - package с настройками проекта;
- employee - приложение сотрудников;
- factory - приложение заводов;
- retail_network - приложение розничных сетей;
- sole_trader - приложение индивидуальных предпринимателей.
<br><br>
- Модели размещены в файле models.py приложения;
- Абстрактные модели размещены в файле models.py приложения factory;
- Вью размещены в файле views.py приложения;
- Сериалайзеры размещены в файле serializers.py приложения.

Перед запуском установите библиотеки командой:<br>
<i>pip install requirements.txt</i>

Примените миграции командами:<br>
<i>python manage.py makemigrations<br></i>
<i>python manage.py migrate</i>

Запускайте приложение командой:
<i>python manage.py runserver</i>

или настройте run в своей среде разработки.