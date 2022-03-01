#!/usr/bin/env bash
chown ubuntu:ubuntu /var/www
virtualenv /var/www/personal_portfolio_python/mwilliamson_portfolio_python/env
chown ubuntu:ubuntu /var/www/personal_portfolio_python/mwilliamson_portfolio_python/env
chown ubuntu:ubuntu /var/www/personal_portfolio_python/mwilliamson_portfolio_python/env/*
source /var/www/personal_portfolio_python/mwilliamson_portfolio_python/env/bin/activate
pip install -r /var/www/personal_portfolio_python/requirements.txt