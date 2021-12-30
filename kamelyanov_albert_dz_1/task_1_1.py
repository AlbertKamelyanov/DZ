duration = int(input("Введите промежуток времени в секундах-"))
days = duration // 3600 // 24
hours = duration // 3600 - days * 24
minutes = duration // 60 % 60
seconds = duration % 60
print(days, "Дней" ",", hours, "часов"",", minutes, "минут" ",", seconds, "секунд" ".")
