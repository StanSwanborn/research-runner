import sys
from pathlib import Path
from Controllers.SearchController import SearchController
from Procedures.OutputProcedure import OutputProcedure as output

def main(config_path):
    config_path = Path(config_path)
    search_controller = SearchController(config_path)
    search_controller.do_search()


if __name__ == "__main__":
    argv_count = len(sys.argv)
    if argv_count == 2 and sys.argv[1] == "--help":  # Help CLI
        output.console_log("usage: python3 %s [PATH_TO_CONFIG.JSON]" % __file__)
        # output.console_log_bold("optional: python3 %s --verbose [PATH_TO_CONFIG.JSON]" % __file__)
        sys.exit(0)
    elif argv_count == 2:
        main(sys.argv[1])
    # elif argv_count == 3 and sys.argv[1] == '--verbose':
    #     main(sys.argv[2], verbose=True)
    else:
        output.console_log("Incorrect usage, please run with --help to view possible arguments")
        sys.exit(0)