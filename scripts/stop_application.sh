ps auxw | grep runserver | awk '{print $2}' | xargs kill