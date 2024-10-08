### ER-диаграмма базы данных:
![QuickDBD-export](https://user-images.githubusercontent.com/94752140/199353265-5ec6bfeb-5a02-4142-b1f8-c2a86fd970f0.png)


### Как запустить проект в dev-режиме?
### 1) Создаём новый проект и клонируем этот репозиторий, прописывая в терминале:
#### <command>
    git clone https://github.com/LonelyColonel/Django_project.git
#### </command>

### 2) Переходим в папку склонированного проекта:
#### <command>
    cd Django_project
#### </command>

### 3) Устанавливаем зависимости:
#### <command>
    pip install -r requirements.txt
#### </command>

### 4) Настраиваем переменные окружения. Все нужные переменные можно посмотреть в файле ".env_example.txt":
#### <command>
    echo SECRET_KEY="your-secret-key" >> .env
#### </command>
#### <command>
    echo DEBUG=True >> .env
#### </command>

### 5) Применим миграции:
#### <command>
    python manage.py migrate
#### <command>

### 6) Переходим в папку с файлом manage.py:
#### <command>
    cd django_project
#### <command>

### 7) Прописываем следующую команду для запуска локального сервера:
#### <command>
    python manage.py runserver
#### </command>

### 8) Переходим на http://127.0.0.1:8000/
### Всё, проект запущен в dev-режиме

