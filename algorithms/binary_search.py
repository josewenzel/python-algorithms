def count_guesses_to_find_name(list_of_names: list[str], name_to_find: str) -> int:
    lower_end = 0
    high_end = len(list_of_names) - 1
    times_guessed = 0

    while lower_end <= high_end:
        middle_end = int((lower_end + high_end) / 2)
        guess = list_of_names[middle_end]

        if guess == name_to_find:
            times_guessed += 1
            return times_guessed

        if guess < name_to_find:
            times_guessed += 1
            lower_end = middle_end + 1
        else:
            times_guessed += 1
            high_end = middle_end - 1
