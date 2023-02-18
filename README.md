Запуск базы данных предполагается через docker-контейнер. Для этого выполните команду:

docker run --name <имя контейнера> -e POSTGRES_USER=<имя> -e POSTGRES_PASSWORD=<пароль> -e POSTGRES_DB=<имя базы данных> -p 5432:5432 -d postgres:latest <br>
(без <>)

Указанные в команде выше переменные должны быть перечислены в файле .env, пример которого размещён в корне проекта в файле .env.example
