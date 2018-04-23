#Problem 19 - Sundays 1st of the month from 1901 to 2000

def sundays_first_of_month():
  non_leap_months = [31,28,31,30,31,30,31,31,30,31,30,31]
  leap_months = [31,29,31,30,31,30,31,31,30,31,30,31]
  sundays = 0
  day = 1

  for year in xrange(1900,2001):
    if year % 100 == 0 and year % 400 == 0:
      list_of_days = leap_months
    elif year % 4 == 0 and year % 100 != 0:
      list_of_days = leap_months
    else:
      list_of_days = non_leap_months

    for days in list_of_days:
      day += days
      if day % 7 == 0 and year != 1900:
        sundays += 1

  return sundays

def main():
  print sundays_first_of_month()

if __name__ == '__main__':
  main()
