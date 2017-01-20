"""
File      : progresstracker.py
Date      : January, 2017
Author(s) : Andela Cohort14 A-Team
Desc      : progresstracker commandline program


Usage:
    python progresstracker.py command optional-argument


Options:
    -h --help       show help message
"""
# ============================================================================
# make necessary imports
# ============================================================================
import json
import argparse

from addskill import add_skill
from progress import show_progress
from checkcompletedskill import check_skill_completed
from viewstatus import view_skills, view_studied, view_not_studied

# ============================================================================
# useful constants
# ============================================================================
EPILOG = 'Created by A Team'
DESC = """progress tracker desc."""
DATA_FILE = 'skills.json'
MISSING_SKILLNAME_ERROR = "ERROR: no skill name provided"
MISSING_COMMAND_ERROR = "ERROR: invalid command"
INVALID_SKILLNAME_ERROR = "ERROR: skill not found"
# ============================================================================
# utility functions
# ============================================================================
def cli_parser():
    """Command Line Arguments parser

    """
    parser = argparse.ArgumentParser(description=DESC, epilog=EPILOG)
    parser.add_argument('command', type=str, help='command name')
    parser.add_argument('-s', '--skillname', type=str, help='skill name')

    args = vars(parser.parse_args())

    return args

def main():
    # ========================================================================
    # commands -functions mapping dictionary
    # ========================================================================
    commands_dict = {'viewall': view_skills,
                     'viewstudied': view_studied,
                     'viewnotstudied': view_not_studied,
                     'progress': show_progress}
    # ========================================================================
    # create database dictionary from json file
    # ========================================================================
    try:
        file_obj = open(DATA_FILE, 'r')
    except FileNotFoundError:
        data_dict = {}
    else:
        try:
            data_dict = json.load(file_obj)
        except json.decoder.JSONDecodeError:
            data_dict = {}

    # ========================================================================
    # fetch user input
    # ========================================================================
    args = cli_parser()
    updated_dict = None

    if args['command'] == 'addskill' and args['skillname']:
        try:
            updated_dict = add_skill(args['skillname'], data_dict)
        except ValueError:
            pass

    elif args['command'] == 'addskill' and not args['skillname']:
        print(MISSING_SKILLNAME_ERROR)
    elif args['command'] == 'checkoff' and args['skillname']:
        try:
            updated_dict = check_skill_completed(args['skillname'], data_dict)
        except ValueError:
            print(INVALID_SKILLNAME_ERROR)
    elif args['command'] == 'checkoff' and not args['skillname']:
        print(MISSING_SKILLNAME_ERROR)
    elif args['command'] in commands_dict:
        commands_dict[args['command']](data_dict)
    else:
        print(MISSING_COMMAND_ERROR)

    # ====================================================================
    # updated database
    #=========================================================================
    if updated_dict:
        file_obj = open(DATA_FILE, 'w')
        json.dump(updated_dict, file_obj, indent=4)




if __name__ == '__main__':
    main()
