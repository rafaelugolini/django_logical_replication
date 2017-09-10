#!/bin/bash

check_db() {
  psql -U postgres -h db collector -c 'select current_database()' > /dev/null 2>&1
  echo $?
}

while [[ $(check_db) != 0 ]]; do
  echo waiting for database to come up
  sleep 1
done

python manage.py runserver 0.0.0.0:8000
