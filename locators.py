
class Locators():
    # Регистрация
    personal_account = ".//p[text()='Личный Кабинет']" # Кнопка "Личный кабинет" на главной странице
    sign_up = ".//a[text()='Зарегистрироваться']" # Надпись "Зарегистрироваться"
    name = ".//label[text() = 'Имя']/following-sibling::input" # Поле имя в окне регистрации
    email_sign_up = ".//label[text() = 'Email']/following-sibling::input" # Поле емейл в окне регистрации"
    password_sign_up = ".//label[text() = 'Пароль']/following-sibling::input" # Поле пароль в окне регистрации"
    sign_up_button = ".//button[text()='Зарегистрироваться']" # Кнопка Зарегистрироваться"
    sign_up_fail = ".//p[text()='Некорректный пароль']" #Ошибка при некорректном пароле при регистрации"

#Вход
    log_in = ".//button[text()='Войти в аккаунт']" #Кнопка Войти в аккаунт
    log_in_sign_up = ".//a[text()='Войти']" #Кнопка входа в окне регистрации
    restore_password = ".//a[text()='Восстановить пароль']" #Кнопка восстановления пароля
    log_in_restore_password = ".//a[text()='Войти']" #Кнопка входа в окне восстановления пароля
    log_in_button = ".//button[text()='Войти']" #Кнопка "Войти" в форме входа
    emeil_log_in = ".//label[text() = 'Email']/following-sibling::input" #Поле емейл в окне входа
    password_log_in = ".//label[text() = 'Пароль']/following-sibling::input" #Поле пароль в окне входа
    order = ".//button[text()='Оформить заказ']" #Кнопка "Оформить заказ
    personal_info_chandge =  ".//p[text()='В этом разделе вы можете изменить свои персональные данные']" #Изменение персональных данных

    profile = ".//a[text()='Профиль']" #Элемент "Профиль" в личном кабинете
    log_off = ".//button[text()='Выход']" #Элемент "Выход" в личном кабинете
    constructor = ".//p[text()='Конструктор']" #Конструктор
    logo = ".//div/header/nav/div/a/*" #Логотип Stellar Burgers
    buns_non_active = ".//div[@class='tab_tab__1SPyG  pt-4 pr-10 pb-4 pl-10 noselect']/span[text()='Булки']" #неактивный раздел «Булки»
    buns_active = ".//div[contains(@class,'current')]/span[text()='Булки']" #активный раздел «Булки»
    sauces_non_active = ".//div[@class='tab_tab__1SPyG  pt-4 pr-10 pb-4 pl-10 noselect']/span[text()='Соусы']" #неактивный раздел "Соусы"
    sauces_active = ".//div[contains(@class,'current')]/span[text()='Соусы']" #активный раздел "Соусы"
    stuffing_non_active = ".//div[@class='tab_tab__1SPyG  pt-4 pr-10 pb-4 pl-10 noselect']/span[text()='Начинки']" #неактивный раздел "Начинки"
    stuffing_active = ".//div[contains(@class,'current')]/span[text()='Начинки']" #активный раздел "Начинки"