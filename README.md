# prob

## create database

```cmd
CREATE DATABASE prob DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;
```

```cmd
python manager.py db init
python manager.py db migrate
python manager.py db upgrade
```