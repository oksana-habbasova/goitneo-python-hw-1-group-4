from datetime import datetime
from collections import defaultdict

def get_birthdays_per_week(users):

    next_week_birthdays = defaultdict(list)

    today = datetime.today().date()

    for user in users:
        name = user['name']
        birthday = user['birthday'].date()
        birthday_this_year = birthday.replace(year=today.year)

        if birthday_this_year < today:
            birthday_this_year = birthday_this_year.replace(year=today.year + 1)

        delta_days = (birthday_this_year - today).days

        if delta_days < 7:
            day = birthday_this_year.strftime('%A')

            if day == 'Saturday' or day == 'Sunday':
                day = 'Monday'

            next_week_birthdays[day].append(name)

    for day, names in next_week_birthdays.items():
        print(day + ': ' + ', '.join(names))
