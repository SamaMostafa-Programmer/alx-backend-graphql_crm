## CRM Celery Setup

1. Install Redis
2. pip install -r requirements.txt
3. python manage.py migrate
4. python manage.py crontab add
5. celery -A crm worker -l info
6. celery -A crm beat -l info
7. Check logs in /tmp/crm_report_log.txt
