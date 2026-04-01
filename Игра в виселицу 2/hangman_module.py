import random

# Глобальные переменные конфигурации
CONFIG = {
    "words_file": "words.txt",
    "hangman_prefix": "hangman_",
    "hangman_ext": ".txt",
    "max_errors": 6
}

# Глобальное состояние игры
GAME_STATE = {
    "word": "",
    "hint": "",
    "guessed_letters": [],
    "errors": 0,
    "game_over": False,
    "win": False
}


def load_word_list():
    """Загружает список слов из файла."""
    words = []
    try:
        with open(CONFIG["words_file"], "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if line:
                    parts = line.split(":")
                    if len(parts) >= 2:
                        words.append({"word": parts[0], "hint": parts[1]})
    except FileNotFoundError:
        # Если файл не найден, используем запасное слово
        words.append({"word": "ТЕСТ", "hint": "Отладка"})
    return words


def init_game():
    """Инициализирует новую игру."""
    data = load_word_list()
    if data:
        selected = random.choice(data)
        GAME_STATE["word"] = selected["word"].upper()
        GAME_STATE["hint"] = selected["hint"]
    else:
        GAME_STATE["word"] = "ERROR"
        GAME_STATE["hint"] = "Нет слов"

    GAME_STATE["guessed_letters"] = []
    GAME_STATE["errors"] = 0
    GAME_STATE["game_over"] = False
    GAME_STATE["win"] = False


def get_hangman_art():
    """Загружает текущий этап виселицы из файла."""
    stage = GAME_STATE["errors"]
    if stage > CONFIG["max_errors"]:
        stage = CONFIG["max_errors"]

    filename = CONFIG["hangman_prefix"] + str(stage) + CONFIG["hangman_ext"]
    try:
        with open(filename, "r", encoding="utf-8") as f:
            return f.read()
    except FileNotFoundError:
        return "Ошибка отрисовки виселицы"


def get_masked_word():
    """Возвращает слово с закрытыми буквами."""
    res = []
    for char in GAME_STATE["word"]:
        if char in GAME_STATE["guessed_letters"]:
            res.append(char)
        else:
            res.append("*")
    return "".join(res)


def show_screen():
    """Выводит текущее состояние игры в консоль."""
    print(get_hangman_art())
    print("Категория: " + GAME_STATE["hint"])
    print("Слово: " + get_masked_word())
    print("Угаданные буквы: " + ", ".join(GAME_STATE["guessed_letters"]))
    print("Ошибок: " + str(GAME_STATE["errors"]) + " из " + str(CONFIG["max_errors"]))


def get_user_input():
    """Запрашивает букву у пользователя."""
    while True:
        try:
            val = input("Введите букву или слово целиком: ").strip().upper()
            if val and val.isalpha():
                return val
            print("Пожалуйста, вводите только буквы.")
        except EOFError:
            return ""


def check_guess(guess):
    """Проверяет введенную букву или слово."""
    # Если введено целиком
    if len(guess) > 1:
        if guess == GAME_STATE["word"]:
            GAME_STATE["win"] = True
            GAME_STATE["game_over"] = True
            # Открываем все буквы
            for char in GAME_STATE["word"]:
                if char not in GAME_STATE["guessed_letters"]:
                    GAME_STATE["guessed_letters"].append(char)
        else:
            GAME_STATE["errors"] += 1
        return

    # Введена буква
    if guess in GAME_STATE["guessed_letters"]:
        print("Вы уже вводили эту букву!")
        return

    GAME_STATE["guessed_letters"].append(guess)

    if guess not in GAME_STATE["word"]:
        GAME_STATE["errors"] += 1
    else:
        # Проверка на победу по буквам
        win = True
        for char in GAME_STATE["word"]:
            if char not in GAME_STATE["guessed_letters"]:
                win = False
                break
        if win:
            GAME_STATE["win"] = True
            GAME_STATE["game_over"] = True

    # Проверка на проигрыш
    if GAME_STATE["errors"] >= CONFIG["max_errors"]:
        GAME_STATE["game_over"] = True
        GAME_STATE["win"] = False


def run_game():
    """Основной цикл игры."""
    init_game()

    while not GAME_STATE["game_over"]:
        show_screen()
        user_input = get_user_input()
        if user_input:
            check_guess(user_input)

    show_screen()
    if GAME_STATE["win"]:
        print("ВЫ ПОБЕДИЛИ!")
    else:
        print("ВЫ ПРОИГРАЛИ!")
        print("Загаданное слово: " + GAME_STATE["word"])

    print("Игра окончена.")