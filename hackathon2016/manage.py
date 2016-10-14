#!/usr/bin/env python
import os
import sys
sys.path.insert(0, '/home/ashmeet/hackathon/goibibo-hackathon2016/hackathon2016')

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "hackathon2016.settings")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
