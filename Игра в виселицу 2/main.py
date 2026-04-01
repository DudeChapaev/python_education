import hangman_module

run = hangman_module.app_start()

while run:
    hangman_module.show_screen()
    guess = hangman_module.get_guess()
    hangman_module.process_guess(guess)

    if hangman_module.is_win():
        hangman_module.show_win_message()
        run = hangman_module.app_stop()
    elif hangman_module.is_lose():
        hangman_module.show_lose_message()
        run = hangman_module.app_stop()

hangman_module.show_end_message()