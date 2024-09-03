def parse_user_query(query):
    if "load data" in query:
        return "LOAD_DATA"
    elif "clean data" in query:
        return "CLEAN_DATA"
    elif "run analysis" in query:
        return "RUN_ANALYSIS"
    elif "generate report" in query:
        return "GENERATE_REPORT"
    else:
        return "UNKNOWN_COMMAND"

def command_line_interface():
    while True:
        user_input = input("Enter your command: ")
        command = parse_user_query(user_input)
        
        if command == "LOAD_DATA":
            file_path = input("Enter the file path: ")
            print(f"Loading data from {file_path}...")
        elif command == "CLEAN_DATA":
            print("Cleaning data...")
        elif command == "RUN_ANALYSIS":
            print("Running analysis...")
        elif command == "GENERATE_REPORT":
            print("Generating report...")
        else:
            print("Unknown command. Please try again.")
