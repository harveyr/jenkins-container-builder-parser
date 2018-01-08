# jenkins-container-builder-parser

This is a fledgling script to parse timestamped Jenkins log output for
jobs that run [Google Container
Builder](https://cloud.google.com/container-builder/) builds.

It outputs a CSV of step names, start and end times, and durations.

Container Builder does not yet show which steps failed or how long steps take, so this is a stopgap.

This is very much for my own haphazard use in optimizing our Jenkins jobs.

To use it, append `/timestamps/?elapsed=HH:mm:ss&appendLog` to the end
of your job URL, download the resulting logs, and run:

```bash
python main.py --file /path/to/logs.txt
```

I'm piping the output to the wonderful [visidata](https://github.com/saulpw/visidata):

```bash
python main.py --file /path/to/logs.txt | vd -f csv
```
