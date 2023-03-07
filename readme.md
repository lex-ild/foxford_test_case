Инструкция по запуску:  
    1. docker-compose build  
    2. docker-compose up  

Для выполнения использовался фреймворк Django. В качестве БД используется postgresql. Таск расчёта зарплаты запускается через celery, celery_beat, redis.