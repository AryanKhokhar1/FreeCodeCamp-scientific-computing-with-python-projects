def add_time(start, duration, week=None):
    # Function that returns a specified time based on a start time, duration and optional weekday. Imports are not allowed. Assumes that the user enters valid strings, since no checks are in place.

    # Store the weekdays in a dict with corresponding numbers.
    weekdays = {'monday':0, 'tuesday':1, 'wednesday':2, 'thursday':3, 'friday':4, 'saturday':5, 'sunday':6}

    # Extract data from given start and duration strings.
    startArr = start.split(' ')
    startTime = startArr[0].split(':')
    ampm = 'AM'
    durationTime = duration.split(':')

    # Add the hours together from start and duration
    tmpEndHour = (int(startTime[0]) + int(durationTime[0]))

    # Add 12 hours to the temporary end hour in case 'PM' is given in the start time (so that we can work with a 24h format instead before reformatting back to 12h)
    if startArr[1] == 'PM':
        tmpEndHour += 12

    # Add the start and duration minutes together
    tmpEndMinute = (int(startTime[1]) + int(durationTime[1]))

    # If the sum of the minutes is rgeater than 59, add one hour to the end hour.
    if(tmpEndMinute > 59):
        tmpEndHour += 1
    
    # Count the number of days that will have passed after the duration.
    days = int(tmpEndHour//24) # Flooring the division, since rounding will give a wrong value.

    # Calculate the end hour using modulo in a 24h format.
    endHour = tmpEndHour % 24

    # Change the 'AM' to 'PM' if the 12th hours is passed.
    if endHour > 11:
        ampm = 'PM'

    # Convert back to 12h format ()
    if endHour > 12:
        endHour -= 12
    elif endHour == 0:
        endHour = 12

    # Calculate the ending minute using modulo.
    endMinute = tmpEndMinute % 60

    # Concatonate the first part of the string.
    endTime = str(endHour) + ':' + str(endMinute).zfill(2) + ' ' + ampm

    # If the weekday option was given, add the new weekday to the string.
    if week is not None:
        week = week.lower()
        weekdayNum = weekdays[week]
        newWeekdayNum = (days + weekdayNum) % 7
        # https://stackoverflow.com/questions/8023306/get-key-by-value-in-dictionary
        newWeek = list(weekdays.keys())[list(weekdays.values()).index(newWeekdayNum)]
        endTime += ', ' + newWeek.capitalize()
    
    # If the day has changed, add the correct string value
    if days > 1:
        endTime += ' (' + str(days) + ' days later)'
    elif days > 0:
        endTime += ' (next day)'

    return endTime