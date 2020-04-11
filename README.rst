CatBot
======

CatBot - это бот для Telegram, созданный с целью делать вашу жихнь лучше, присылая котиков.

Установка
---------

Создайте виртуальное окружение и активируйте его:

.. code-block:: text

    python -m venv env
    env/Scripts/activate

Потом в виртуальном окружении выполните:

.. code-block:: text

    pip install -r requirements.txt

Положите картинки с котиками в папку Images. Название файлов должно начинаться с "cat".

Настройка
---------

Создайте файл settings.py и добавьте туда следующие настройки:

.. code-block:: python

    API_KEY="API ключ, который вы получили у BotFather"

    USER_EMOJI=[':smiley_cat:',':smiling_imp:',':panda_face:',':dog:']

Запуск
------

В активированом виртуальном окружении выполните:

.. code-block: text

    python3 bot.py