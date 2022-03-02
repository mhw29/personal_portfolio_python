#!/usr/bin/env bash
cd /var/www/personal_portfolio_python
source /www/personal_portfolio_python/env/bin/activate
python3 manage.py runserver 0.0.0.0:8000 &

