#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'apiproject.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()


# API --Application Programming Interface

# Client Side ----      API    ------Server Side
# Zomato, Swiggy,Uber 
# Google Maps Api

# Restaurant
# Customer  ----      Waiter           ----- Chef 
# Client        ---       API ---          Server

# API is an set of rules which communicates between two systems,
# softwares or between client and server

# Django
# API

# REST API
# REST API provides you method like GET,POST,PUT,DELETE