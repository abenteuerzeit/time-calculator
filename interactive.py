"""
interactive.py
"""


def get_yes_no_input(prompt):
    while True:
        response = input(prompt).strip().lower()
        if response in ('y', 'yes'):
            return True
        elif response in ('n', 'no'):
            return False
        else:
            print('Please enter "yes" or "no" (or "y" or "n").')


def print_help():
    print('Time Calculator')
    print('Usage:')
    print('    python time_calculator.py [OPTIONS]')
    print('Options:')
    print('    -i, --interactive    Run in interactive mode')
    print('    -h, --help           Show this help message')
    print(
        '    -s, --start          Start time in the format hh:mm or hh:mm AM/PM'
    )
    print('    -d, --duration       Duration in the format hh:mm or minutes')
    print('    -w, --weekday        Starting weekday (e.g., Monday)')
    print('    -c, --current        Use current time as start time')


def parse_time_input(input_str, is_duration=False):
    """
    Parse user input for time in various formats (hh:mm or minutes).

    Args:
        input_str (str): User-provided input for time.
        is_duration (bool): Whether the input is a duration (default: False).

    Returns:
        str: Parsed time in the format hh:mm with AM/PM, or duration in minutes.

    Raises:
        ValueError: If the input format is not valid.
    """
    if ':' in input_str:
        parts = input_str.split(':')
        if len(parts) != 2 or not parts[0].isdigit():
            raise ValueError(
                'Invalid time format. Please use hh:mm or hh:mm AM/PM.')

        hours = int(parts[0])
        minutes_and_meridiem = parts[1].split()
        if len(minutes_and_meridiem) == 2:
            minutes, meridiem = minutes_and_meridiem
            if not minutes.isdigit() or meridiem not in ['AM', 'PM']:
                raise ValueError(
                    'Invalid time format. Please use hh:mm AM/PM.')
            minutes = int(minutes)
        elif len(minutes_and_meridiem) == 1:
            minutes = minutes_and_meridiem[0]
            if not minutes.isdigit():
                raise ValueError(
                    'Invalid time format. Please use hh:mm or minutes.')
            minutes = int(minutes)
            meridiem = None
        else:
            raise ValueError(
                'Invalid time format. Please use hh:mm or hh:mm AM/PM.')

        if is_duration:
            return f"{hours * 60 + minutes}"
        else:
            hours = hours % 12 or 12
            return f"{hours}:{minutes:02d} {meridiem}"

    elif input_str.isdigit():
        return input_str if is_duration else f"{int(input_str) // 60}:{int(input_str) % 60:02d} AM"
    else:
        raise ValueError(
            'Invalid time format. Please use hh:mm or hh:mm AM/PM.')
