#!/usr/bin/env python
import os
import sys


if __name__ == "__main__":
    path_variable = os.path.dirname(os.path.abspath(__file__))
    sys.path.insert(0, path_variable)
    sys.path.insert(1, path_variable + '/' + os.path.pardir)
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "hackathon2016.settings")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
