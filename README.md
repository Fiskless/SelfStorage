# СК Ладный
Сеть складов для частных лиц в Моске


*Сайт сети складов представляет удобное упорядоченное описание услуг и преимуществ. Основной функционал: пользователь сайта получает стоимость аренды площади или сезонного хранения вещей в зависимости от срока аренды и локации, оформляет заказ на аренду и оплачивает его. Дополнительный функционал заключается в нахождении ближайшего к пользователю склада и онлайн-консультации.*

![Скриншот приложения](selfstorage.png)

[Демо-версия](https://otbot.ru/)


## Установка

Приложение является свободным, ты можешь установить его и пользоваться. Для этого тебе понадобятся:
1. Python 3.9+ [см. как установить (англ.)](https://realpython.com/installing-python/), а [здесь для Debian-based (рус.)](http://userone.ru/?q=node/41).
2. Django 3.x [см. как установить (рус.)](https://developer.mozilla.org/ru/docs/Learn/Server-side/Django/development_environment).

Далее, скачай репозиторий к себе, установи и активируй виртуальное окружение: 

    python3 -m venv env
    source env/bin/activate

установи необходимые библиотеки для Django, указанные в файле requirements.txt:

    pip install -r requirements.txt

запусти сайт:

    ./manage.py runserver

и открой его в браузере, указав в адресной строке (главная страница или административная панель):

    http://127.0.0.1:8000
    http://127.0.0.1:8000/admin


Сайт для своей работы использует следующие ресурсы: 

* шаблон Carousel css-библиотеки [Bootstrap](https://getbootstrap.com/)

* [Яндекс.Карты](https://www.yandex.ru/maps)

* jQuery

* платёжную систему [Stripe](https://stripe.com/)

* фотографии с сервиса [Pixabay](https://pixabay.com/ru/)


## Переменные окружения

Для улучшения уровня безопасности, когда будешь размещать сайт в общем доступе, сделай файл .env и размести его в папке настроек проекта. В этом файле укажи:

* секретный ключ Django;
* [ключ](https://yandex.ru/dev/maps/jsapi/doc/2.1/quick-start/index.html#get-api-key) для работы с API Яндекс.карты;
* ключ API платёжной системы Stripe. Для его получения необходимо перейти в [мануал](https://stripe.com/docs/payments/accept-a-payment). Во 2 пункте этого мануала будет показан пример кода, где и будет ваш личный ключ `stripe.api_key`.
* данные для подключения к БД
* DEBUG и ALLOWED_HOSTS


Вот так должен выглядеть твой .env файл:

    SECRET_KEY='длинная строка символов'
    DEBUG=False
    ALLOWED_HOSTS=127.0.0.1,[::1]
    YANDEX_MAPS_API_KEY='ключ API Яндекса'
    POSTGRES_DB_URL=postgres://user_name:password@host:port/db_name
    STRIPE_PUBLISHABLE_KEY=<ключ платёжной системы Stripe>
    

Указывать эти ключи в файле настроек settings.py не нужно.

## Настройка геолокации

Для работы геолокации необходимо безопасное окружение. В противном случае, браузер не отдаёт координаты пользователя. Безопасным считается локальный хост (localhost, 127.0.0.1) и хосты, обмен данных с которыми происходит по протоколу HTTPS. Таким образом, при установке сайта на сервер также необходимо установить SSL-сертификат. 

В качестве временной обходной меры для настройки работы сайта можно применить [изменение настроек бразуера Chrome.](https://stackoverflow.com/a/55858436/14354180)

## Настройка платёжной системы

Подключение платежной системы к вашему сайту подробно представлено в [мануале](https://stripe.com/docs/payments/accept-a-payment)

## Настройка онлайн-консультации

Для настройки онлайн-консультации Jivosite, [зарегистрируйтесь](https://www.jivo.ru/?partner_id=14624), после чего [подключите](https://app.jivosite.com/settings/channels) онлайн-консультанта к вашему сайту  

## Роли

### Администратор сайта

Администратор сайта является суперпользователем, имеет все права в отношении контента. На демо-сайте авторизуйся со следующими данными:

    Логин: admin
    Пароль: admin

### Незарегистрированный пользователь

Может просматривать контент сайта, пользоваться калькулятором, регистрироваться на сайте.

### Зарегистрированный пользователь

Дополнительно к возможностям незарегистрированного пользователя может оформлять заказ, совершать оплату, просматривать историю заказов, восстанавливать пароль от своего аккаунта.

## Цели проекта

Код написан в учебных целях — это урок в курсе по Python и веб-разработке на сайте [Devman](https://dvmn.org).


