#!/venv/bin/python3.6
"""
at2018 / this is the entry point of the 2K18 
"""
import sys
from fn.main import Main
# gather args list and pass to menu
Main(sys.argv[1:]).menu()

