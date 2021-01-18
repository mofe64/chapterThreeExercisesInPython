class Date:

    def __init__(self, day, month, year):
        valid_month_range = 0 < month < 13
        valid_year_range = 1899 < year < 2100
        month_is_30_day_month = month == 4 or month == 6 or month == 9 or month == 11
        year_is_leap_year = year % 4 == 0
        valid_day_range_for_leap_year_february = 0 < day < 29
        valid_day_range_for_non_leap_year_february = 0 < day < 28
        month_is_february = month == 2
        valid_day_range_for_30_day_month = 0 < day < 31
        valid_day_range_for_31_day_month = 0 < day < 32
        if valid_month_range:
            self._month = month
        else:
            raise ValueError("Month must be between 1 and 12")
        if valid_year_range:
            self._year = year
        else:
            raise ValueError("Year must be between 1900 and 2099")
        if month_is_30_day_month:
            if valid_day_range_for_30_day_month:
                self._day = day
            else:
                raise ValueError(f"month no {month} is a 30 day month and day must be within 1 and 30")
        if month_is_february:
            if year_is_leap_year:
                if valid_day_range_for_leap_year_february:
                    self._day = day
                else:
                    raise ValueError(f"Year is a leap year and february days must be between 1 and 29")
            if not year_is_leap_year:
                if valid_day_range_for_non_leap_year_february:
                    self._day = day
                else:
                    raise ValueError(f"Year is not a leap year and february days must be between 1 and 28")

        if not month_is_30_day_month and not month_is_february:
            if valid_day_range_for_31_day_month:
                self._day = day
            else:
                raise ValueError(f"month no {month} is a 31 day month and day must be within 1 and 31")

    def get_day(self):
        return self._day

    def get_month(self):
        return self._month

    def get_year(self):
        return self._year

    def set_day(self, day):
        month_is_30_day_month = self._month == 4 or self._month == 6 or self._month == 9 or self._month == 11
        year_is_leap_year = self._year % 4 == 0
        valid_day_range_for_leap_year_february = 0 < day < 29
        valid_day_range_for_non_leap_year_february = 0 < day < 28
        month_is_february = self._month == 2
        valid_day_range_for_30_day_month = 0 < day < 31
        valid_day_range_for_31_day_month = 0 < day < 32
        if month_is_30_day_month:
            if valid_day_range_for_30_day_month:
                self._day = day
            else:
                raise ValueError(f"month no {self._month} is a 30 day month and day must be within 1 and 30")
        if month_is_february:
            if year_is_leap_year:
                if valid_day_range_for_leap_year_february:
                    self._day = day
                else:
                    raise ValueError(f"Year is a leap year and february days must be between 1 and 29")
            if not year_is_leap_year:
                if valid_day_range_for_non_leap_year_february:
                    self._day = day
                else:
                    raise ValueError(f"Year is not a leap year and february days must be between 1 and 28")

        if not month_is_30_day_month and not month_is_february:
            if valid_day_range_for_31_day_month:
                self._day = day
            else:
                raise ValueError(f"month no {self._month} is a 31 day month and day must be within 1 and 31")

    def set_month(self, month):
        valid_month_range = 0 < month < 13
        if valid_month_range:
            self._month = month
        else:
            raise ValueError("Month must be between 1 and 12")

    def set_year(self, year):
        valid_year_range = 1899 < year < 2100
        if valid_year_range:
            self._year = year
        else:
            raise ValueError("Year must be between 1900 and 2099")

    def display_date(self):
        print(f"{self._month}/{self._day}/{self._year}")

    def __str__(self):
        return f"{self._month}/{self._day}/{self._year}"
