FROM debian:11
FROM python:3.10.5-buster
FROM nikolaik/python-nodejs:python3.9-nodejs18

WORKDIR /Yumeko/

RUN /usr/local/bin/python -m pip install --upgrade pip
RUN pip3 install --upgrade pip setuptools
RUN apt-get -y install git
RUN apt-get update -y && apt-get upgrade -y \
    && apt-get install -y --no-install-recommends ffmpeg \
    emoji \
    tzlocal \
    lxml \
    wget \
    gtts \
    faker \
    beautifulsoup4 \
    requests \
    python-telegram-bot==12.8 \
    sqlalchemy==1.3.20 \
    ffmpeg-python \
    psycopg2-binary \
    feedparser \
    hachoir \
    pynewtonmath \
    spongemock \
    zalgo-text \
    geopy \
    nltk \
    psutil \
    aiohttp \
    Pillow \
    CurrencyConverter \
    googletrans \
    jikanpy \
    speedtest-cli \
    coffeehouse \
    regex \
    bleach \
    git+https://github.com/starry69/python-markdown2.git \
    wikipedia \
    telethon \
    telegraph \
    heroku3 \
    spamwatch \
    alphabet_detector \
    pybase64 \
    pySmartDL \
    validators \
    nekos.py \
    aiofiles \
    pyrate-limiter \
    cachetools \
    ujson \
    pretty_errors \
    TgCrypto \
    Pyrogram \
    yt-dlp \
    youtube_search_python \
    youtube_search \
    asyncio \
    dateparser \
    pymongo \
    dnspython \
    secureme \
    apscheduler \
    emoji-country-flag \
    countryinfo \
    html2text \
    bs4 \
    fontTools \
    bing_image_downloader \
    search_engine_parser \
    pytz \
    lyricsgenius \
    tswift \
    envparse \
    better_profanity \
    nudepy \
    motor \
    cloudscraper \ 
    pendulum \
    pykeyboard \
    aiohttp \
    youtube_dl \
    fuzzysearch \
    Python_ARQ \
    httpx[http2] \
    gpytranslate \
    google-trans-new \    
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*
RUN apt-get install libxml2-dev libxslt-dev python


COPY requirements.txt .

RUN pip3 install wheel
RUN pip3 install --no-cache-dir -U -r requirements.txt
COPY . .
CMD ["python3", "-m", "Yumeko"]
