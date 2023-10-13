from datetime import datetime, date
from collections import defaultdict


def get_birthdays_per_week(users):
    current_date = datetime.today().date()
    list_birthdays_next_week = defaultdict(list)
    for user in users:
        name = user["name"]
        birthday = user["birthday"].date()  # Конвертуємо до типу date*
        birthday_this_year = birthday.replace(
            year=current_date.year
        )  # замінюємо рік на актуальний в датах народження
        delta_days = (
            birthday_this_year - current_date
        ).days  # визначаємо різницю у кількостів днів між сьогодні та датою народження
        if delta_days < 7:
            day_of_week = user["birthday"].strftime(
                "%A"
            )  # присвоюємо зміній day_of_week день тижня
            if (
                day_of_week == "Saturday" or day_of_week == "Sunday"
            ):  # по суботах та неділях переносимо на понеділок
                list_birthdays_next_week["Monday"].append(
                    name
                )  # переносимо name, з вихідних на понеділок
            else:
                list_birthdays_next_week[day_of_week].append(
                    name
                )  # решта днів крім вихідних та записуємо туди імя
    finish_list = "\n".join(
        f"{day}: {', '.join(names)}" for day, names in list_birthdays_next_week.items()
    )  # переводимо словник у рядки: день тижня та додаємо name

    # повертаємо результат
    return finish_list


# Author Volodymyr Chub
