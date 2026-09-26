class Weather:
    def __init__(self, date, day, weather):
        self.date = date
        self.day = day
        self.weather = weather


n = int(input())

earliest = None

for _ in range(n):
    date, day, weather = input().split()

    w = Weather(date, day, weather)

    if w.weather == "Rain":
        if earliest is None or w.date < earliest.date:
            earliest = w

print(earliest.date, earliest.day, earliest.weather)