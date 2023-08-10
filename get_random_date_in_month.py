def get_random_date_in_month(year, month):
    first_day = datetime(year, month, 1)
    next_month = (first_day.replace(day=28) + timedelta(days=4)).replace(day=1)
    last_day = next_month - timedelta(days=1)
    random_date = first_day + timedelta(days=random.randint(0, (last_day - first_day).days))
    date_string = random_date.strftime("%Y-%m-%d")
    return date_string