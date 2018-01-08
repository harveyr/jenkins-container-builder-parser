# jenkins-container-builder-parser

This is a fledgling script to parse timestamped Jenkins log output for
jobs that run [Google Container
Builder](https://cloud.google.com/container-builder/) builds.

It reports step durations.

Container Builder does not yet show which steps failed or how long steps take, so this is a stopgap.

Very much for my own haphazard use in optimizing our Jenkins jobs.
