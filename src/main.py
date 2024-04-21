from user_interface import run_user_interface
from performance_analysis import analyze_performance

def main():
    """
    Main entry point for the online hash algorithms project.
    """
    print("Welcome to the Online Hash Algorithms Project!")
    
    run_user_interface()
    
    # Perform performance analysis
    input_data = "This is a sample input data for performance analysis."
    analyze_performance(input_data)

if __name__ == "__main__":
    main()