def time(XX, HH, MM):
    # Перетворюємо час лягання спати Каті та час прокидання в хвилинах
    sleep_time = HH * 60 + MM
    wake_up_time = sleep_time + XX

    if wake_up_time >= 1440:
        wake_up_time -= 1440

    wake_up_hour = wake_up_time // 60
    wake_up_minute = wake_up_time % 60

    return wake_up_hour, wake_up_minute

XX = int(input("Кількість хвилин для сну: "))
HH = int(input("Годину лягання спати: "))
MM = int(input("Хвилини лягання спати: "))

hour, minute = time(XX, HH, MM)
print("Години, на які треба поставити будильник:", hour)
print("Хвилини, на які треба поставити будильник:", minute)