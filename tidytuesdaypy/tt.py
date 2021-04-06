from datetime import datetime

REPO = "rfordatascience/tidytuesday"


class TidyTuesday:
    def __init__(self, date):
        if type(date) == str:
            self.date = datetime.fromisoformat(date).date()

        if self.date.weekday() != 1:
            raise ValueError(f'{self.date.strftime("%Y-%m-%d")} is not a Tuesday')

    def load_context(self):
        pass
