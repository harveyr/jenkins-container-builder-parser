import csv
from io import StringIO
import re

import click

# timestamp path suffix: /timestamps/?elapsed=HH:mm:ss&appendLog

STEP_BOUNDARY_REX = re.compile(
    r'^(\d{2}:\d{2}:\d{2})\s+(Starting|Finished) Step #(\d+) - \"(\S+)\"$'
)

data = {}


@click.command()
@click.option('--file', 'fpath', type=str, default=None)
def main(fpath: str):
    raw_logs = None

    if fpath:
        with open(fpath) as f:
            raw_logs = f.read()

    for line in raw_logs.splitlines():
        match = STEP_BOUNDARY_REX.search(line)
        if match:
            record_step_boundary(*match.groups())

    csv_file = build_csv()
    print(csv_file.getvalue())


def build_csv():
    f = StringIO()
    writer = csv.writer(f)
    writer.writerow(['Step', 'Name', 'Started', 'Finished', 'Duration'])

    for step_num, step_data in data.items():
        started = step_data['starting']
        finished = step_data.get('finished')
        writer.writerow([
            step_num,
            step_data['name'],
            started,
            finished,
            finished - started if finished else None,
        ])

    f.seek(0)

    return f


def record_step_boundary(time_str: str, action: str, step_str: str, name: str):
    time_parts = [int(p) for p in time_str.split(':')]
    if len(time_parts) != 3:
        raise ValueError('Invalid time string: {}'.format(time_str))

    seconds = 60 * 60 * time_parts[0] + 60 * time_parts[1] + time_parts[2]

    step_num = int(step_str)

    step_data = data.setdefault(step_num, {'name': name})
    step_data[action.lower()] = seconds


if __name__ == '__main__':
    main()