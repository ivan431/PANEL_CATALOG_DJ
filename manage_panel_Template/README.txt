
Выполнить по порядку
1.git clone https://github.com/ivan431/PANEL_CATALOG_DJ.git из гитхаба
2. Перейдите в папку склонированного репозитория с помощью команды
`cd имя_папки_репозитория`.
3.python -m venv venv - создаем вирт. окружение
4.Активируйте виртуальное окружение ->
    venv\Scripts\activate
5.Установите зависимости проекта из файла requirements.txt
    pip install -r requirements.txt
6.Запустите проект - python manage.py runserver (если порты все заняты как у меня,
 то напишите свободный порт -> cmd -> netstat -ano - посмотреть какие порты свободны)
