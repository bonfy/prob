# prob

## create database

1. In mysql:
```cmd
CREATE DATABASE prob DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;
```

2. In command:
```cmd
python manager.py db init
python manager.py db migrate
python manager.py db upgrade
```

3. Start Python Flask Server:
```cmd
python app.py
```
