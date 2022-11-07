1) Запустить Docker
2) Проверить наличие всех файлов (posts.csv, requirements.txt) в корне проекта
3) ввести комманду docker-compose build
4) После успешного завершения предыдущей ввести комманду docker-compose up
5) Дождитесь окончания скачивания и запуска контейнеров !!! (Elastic может запускаться долго)
6) Зайти по адресу http://127.0.0.1:8000/docs#/
7) Заполнить базу данных mongodb и elastic
    1. Открываем функцию generate, нажимаем кнопку "Try it out"
    2. Далее нажимаем большую синюю кнопку Execute
    3. Ждем ответа ("message": "data in mongo and elastic generated") - окончания загрузки данных из файла posts.csv в базы

8) Все готово! Можно искать посты по адресу /search и удалять их по /delete_post
