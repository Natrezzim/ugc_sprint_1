Performance test Vertica and Clickhouse

Для каждого хранилища поднимаются свои контейнеры
     docker-compose up --scale worker=4

Тесты которые были проведены:
1) Локальный тест на запись 10M строк чанками по 5К.
2) Локальный тест на получение рандомных данных в цикле 5К.
        Для запуска локального теста запускаем скрипт local_test_clickhouse.py и local_test_vertica.py.
        Результатом будет время выполнения 10М записей + время чтения.
4) Для тестирования нагрузки при записи/чтении данных в реальном времени использовалась либа Locust.
    После поднятия контейнеров заходим в http://localhost:8089/


VERTICA:

        Вставка батчами по 5К
        Query type INSERT, query_time 224.51499999999942 sec

        Получение данных в цикле 5К
        Query type SELECT, query_time 93.625 sec
        
   Запись чтение в реальном времени:
            
![total_requests_per_second_1653221606](https://user-images.githubusercontent.com/62523428/169695808-b41cefc5-77f9-4400-9f91-3d197f1f982d.png)
![response_times_(ms)_1653221606](https://user-images.githubusercontent.com/62523428/169695814-9a15247b-02aa-4cfe-bf98-229f9abaafe6.png)
![number_of_users_1653221606](https://user-images.githubusercontent.com/62523428/169695821-010a8e55-d706-4c61-9e57-f12b646ea7f6.png)
![Screenshot 2022-05-22 141342](https://user-images.githubusercontent.com/62523428/169695833-21847673-4728-47fe-8375-905083c77a94.png)
![Screenshot 2022-05-22 141558](https://user-images.githubusercontent.com/62523428/169695840-6db907b2-d10f-43a4-8b69-cb6eeff14918.png)


CLICKHOUSE:

        Вставка батчами по 5К
        Query type INSERT, query_time 209.65599999999995 sec

        Получение данных в цикле 5К
        Query type SELECT, query_time 364.21900000000005 sec
 
 Запись чтение в реальном времени:
![total_requests_per_second_1653222231](https://user-images.githubusercontent.com/62523428/169696159-204fb1c4-c268-495d-b077-1f00df757d77.png)
![response_times_(ms)_1653222231](https://user-images.githubusercontent.com/62523428/169696189-6dc10b4c-d8ca-4279-af75-65ef1cf4f06f.png)
![number_of_users_1653222231](https://user-images.githubusercontent.com/62523428/169696195-42ec1c9c-24b1-4b14-96bd-04cf752ad232.png)
![Screenshot 2022-05-22 142427](https://user-images.githubusercontent.com/62523428/169696206-91864ec7-326f-42b6-8aa4-e65d4f8a0ad0.png)
![Screenshot 2022-05-22 142213](https://user-images.githubusercontent.com/62523428/169696209-f2dc51c1-5414-46c0-926f-db733264c2b7.png)
