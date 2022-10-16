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
    echo > .env 'SECRET_KEY="your_secret_key"\nDEBUG=True'
#### </command>

### 5) Переходим в папку с файлом manage.py:
#### <command>
    cd django_project
#### <command>

### 6) Прописываем следующую команду для запуска локального сервера:
#### <command>
    python manage.py runserver
#### </command>
### 7) Переходим на http://127.0.0.1:8000/

### Всё, проект запущен в dev-режиме