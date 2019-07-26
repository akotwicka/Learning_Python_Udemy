import datetime as dt

class Trip:
    def __init__(self, symbol, title, start, end):
        self.symbol = symbol
        self.title = title
        self.start = start
        self.end = end

    def check_data(self):
        assert len(self.title) > 0, "Title is empty!"
        assert self.start <= self.end, "Start date is later than end date!"

    @classmethod
    def publish_offer(cls, list_of_trips):

        list_of_errors = []

        for i in list_of_trips:
            try:
                i.check_data()
            except (ValueError, Exception) as e:
                list_of_errors.append("{}: {}".format(i.symbol, e))

        assert len(list_of_errors) == 0, "The list of trips has errors: {}".format(list_of_errors)
        print("The offer will be published")

trips = [
    Trip('IT-VNC', 'Italy-Venice', dt.date(2023, 6, 1), dt.date(2023, 6, 12)),
    Trip('SP-BRC', 'Spain-Barcelona', dt.date(2023, 6, 12), dt.date(2023, 5, 22)),
    Trip('IT-ROM', 'Italy-Rome', dt.date(2023, 6, 21), dt.date(2023, 6, 12))
]

try:
    print("Checking list of trips before publishing...")
    Trip.publish_offer(trips)
    print("Done")
except Exception as e:
    print('THERE ARE ERRORS')
    print(e)
    print('THE OFFER CANNOT BE PUBLISHED')
