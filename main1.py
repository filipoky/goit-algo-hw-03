from datetime import datetime, date, timedelta


def string_to_date(date_string):
    return datetime.strptime(date_string, "%Y.%m.%d").date()


def date_to_string(date):
    return date.strftime("%Y.%m.%d")


def prepare_user_list(user_data):
    prepared_list = []
    for user in user_data:
        prepared_list.append({"name": user["name"], "birthday": string_to_date(user["birthday"])})
    return prepared_list


def find_next_weekday(start_date, weekday):
    days_ahead = weekday - start_date.weekday()
    if days_ahead <= 0:
        days_ahead += 7
    return start_date + timedelta(days=days_ahead)


def adjust_for_weekend(birthday):
    if birthday.weekday() >= 5:
        return find_next_weekday(birthday, 0)
    return birthday


def get_upcoming_birthdays(users, days=7):
    upcoming_birthdays = []
    today = date.today()
       
    for user in users:
        birthday_this_year = user["birthday"].replace(year=today.year)

        if birthday_this_year < today:
            birthday_this_year = birthday_this_year.replace(year=today.year + 1)

        congratulation_date = adjust_for_weekend(birthday_this_year)

        if 0 <= (congratulation_date - today).days <= days:
            upcoming_birthdays.append({
                "name": user["name"],
                "congratulation_date": date_to_string(congratulation_date)
            })

    return upcoming_birthdays


# Test
users = [
    {"name": "Bill Gates", "birthday": "1955.03.29"},  
    {"name": "Steve Jobs", "birthday": "1955.03.31"},  
    {"name": "Jinny Lee", "birthday": "1956.03.22"},   
    {"name": "Sarah Lee", "birthday": "1957.03.24"},   
    {"name": "Jonny Lee", "birthday": "1958.03.26"},  
]

prepared_users = prepare_user_list(users)
print(get_upcoming_birthdays(prepared_users, 7))


