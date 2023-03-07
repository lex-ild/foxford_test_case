Инструкция по запуску:  
    1. docker-compose build  
    2. docker-compose up  

Документация: http://127.0.0.1:8000/swagger-ui/

Для выполнения использовался фреймворк Django. В качестве БД используется postgresql. Таск расчёта зарплаты запускается через celery, celery_beat, redis.