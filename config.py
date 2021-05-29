class Config:
    # Адрес API
    api_host = ''
    api_port = 5000
    api_url = f"http://{api_host}:{api_port}"

    # Подключение к БД
    db_host = ""
    db_name = ""
    db_user = ""
    db_pass = ""

    # Соль для генерации хэша
    SECRET_KEY = ''
    salt = ""

    # Разрешенные адреса для подключения к API
    CORS_ALLOWED_ORIGINS = ['IP']
	
