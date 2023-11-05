"""
time_calculator.py

A module to add time durations to a start time, with weekday support.
"""


def add_time(start, duration, weekday=None):
    """
    Adds duration to start time, including the weekday if specified.

    Args:
        start (str): The start time in the 12-hour format (e.g., '3:00 PM').
        duration (str): The duration time to add (e.g., '2:12' or '135' for minutes).
        weekday (Optional[str]): The starting day of the week.

    Returns:
        str: The new time with the day of the week and optionally how many days passed.
    """
    # Setup
    days = [
        'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday',
        'Sunday'
    ]
    enum_days = {day: i for i, day in enumerate(days)}
    MINUTES_IN_HOUR = 60
    HOURS_IN_DAY = 24
    NOON = 12

    # Error checking
    try:
        parts = start.split()
        if len(parts) != 2 or parts[1] not in ['AM', 'PM']:
            raise ValueError("Start time must be in the format 'HH:MM AM/PM'.")

        start_hours, start_minutes = [int(x) for x in parts[0].split(':')]
        if start_hours < 1 or start_hours > 12 or start_minutes < 0 or start_minutes >= 60:
            raise ValueError("Invalid time in start time.")

        if ':' in duration:
            # Duration is given in "hh:mm" format
            duration_hours, duration_minutes = [
                int(x) for x in duration.split(':')
            ]
            if duration_hours < 0 or duration_minutes < 0 or duration_minutes >= 60:
                raise ValueError("Invalid duration time.")
        else:
            # Duration is given in minutes
            if not duration.isdigit():
                raise ValueError(
                    "Duration must be in minutes or 'hh:mm' format.")
            duration_minutes = int(duration)
            duration_hours = duration_minutes // 60
            duration_minutes %= 60

        if weekday and weekday.capitalize() not in enum_days:
            raise ValueError(
                f"Invalid weekday: {weekday}. Must be a full name of the day of the week."
            )

    except ValueError as e:
        raise e
    except Exception as e:
        raise ValueError("Invalid input format.") from e

    # Parse
    parts = start.split()
    start_hours, start_minutes = [int(x) for x in parts[0].split(':')]
    start_hours += NOON if parts[1] == 'PM' else 0

    # Calculate
    total_minutes = (start_hours * MINUTES_IN_HOUR + start_minutes +
                     duration_hours * MINUTES_IN_HOUR + duration_minutes)
    new_minutes = total_minutes % MINUTES_IN_HOUR
    total_hours = total_minutes // MINUTES_IN_HOUR
    new_hours = total_hours % HOURS_IN_DAY
    days_passed = total_hours // HOURS_IN_DAY

    # Format
    meridiem = 'AM' if new_hours < NOON else 'PM'
    new_hours = NOON if new_hours % NOON == 0 else new_hours % NOON
    next_day_str = '' if days_passed == 0 else \
                   ' (next day)' if days_passed == 1 else \
                   f' ({days_passed} days later)'

    # Optional: Calculate new weekday
    weekday_str = (
        f", {days[(enum_days[weekday.capitalize()] + days_passed) % len(days)]}"
        if weekday else '')

    return (f"{new_hours}:{str(new_minutes).zfill(2)} {meridiem}"
            f"{weekday_str}{next_day_str}")


if __name__ == "__main__":
    from interactive import parse_time_input, get_yes_no_input, print_help
    import sys
    import time

    def print_color(text, color_code):
        print(f"\x1b[{color_code}m{text}\x1b[0m")

    print_color(" ".join(sys.argv) + "\n", "33")

    use_current_time = '-c' in sys.argv or '--current' in sys.argv
    start_time_str = None
    duration = None
    weekday = None

    if len(sys.argv) == 1 or '-i' in sys.argv or '--interactive' in sys.argv:
        print('Interactive Mode:')
        print('Example:')
        print('Add 3 hours and 30 minutes to 10:30 PM.')
        print('>>> 2:00 AM (next day)')

        while True:
            try:
                print('\nPlease enter the following information:')
                use_current_time = get_yes_no_input(
                    'Use current time as the start time? (yes/no): ')
                if use_current_time:
                    current_time = time.localtime()
                    meridiem = 'AM' if current_time.tm_hour < 12 else 'PM'
                    hour = current_time.tm_hour % 12
                    hour = 12 if hour == 0 else hour
                    start_time_str = f"{hour:02}:{current_time.tm_min:02} {meridiem}"
                else:
                    start_time_str = input(
                        'Start time (hh:mm AM/PM) or type "exit" to quit: ')
                    if start_time_str.lower() in ('exit', 'quit'):
                        print('Exiting...')
                        break

                duration_str = input('Duration (hh:mm or minutes): ')
                duration = parse_time_input(duration_str, is_duration=True)

                result = add_time(start_time_str, duration)
                print(f'>>> {result}')
            except KeyboardInterrupt:
                print('Exiting...')
                break
    elif '-h' in sys.argv or '--help' in sys.argv:
        print_help()
    else:
        i = 1
        while i < len(sys.argv):
            arg = sys.argv[i]
            if arg in ['-c', '--current']:
                use_current_time = True
            elif arg in ['-s', '--start'] and not use_current_time:
                start_time_str = parse_time_input(sys.argv[i + 1])
                i += 1
            elif arg in ['-d', '--duration']:
                duration = parse_time_input(sys.argv[i + 1], is_duration=True)
                i += 1
            elif arg in ['-w', '--weekday']:
                weekday = sys.argv[i + 1]
                i += 1
            else:
                print(f"Unknown argument: {arg}")
            i += 1

        if use_current_time:
            current_time = time.localtime()
            meridiem = 'AM' if current_time.tm_hour < 12 else 'PM'
            hour = current_time.tm_hour % 12
            hour = 12 if hour == 0 else hour
            start_time_str = f"{hour:02d}:{current_time.tm_min:02d} {meridiem}"

        if start_time_str and duration:
            try:
                result = add_time(start_time_str, duration, weekday)
                print(f">>> {result}")
            except Exception as e:
                print(f"Error: {e}")
        else:
            print(
                'Please provide both start time and duration. Use the -h or --help flag for usage information.'
            )
