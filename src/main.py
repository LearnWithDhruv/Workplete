# src/main.py
from data_ingestion import load_data
from data_preprocessing import clean_data
from analysis_engine import run_analysis
from report_generation import generate_report
from nlp_interface import command_line_interface

def main():
    data = load_data('data/sample_data.csv')
    cleaned_data = clean_data(data)
    analysis_results = run_analysis(cleaned_data)
    generate_report(cleaned_data, analysis_results)
    command_line_interface()

if __name__ == '__main__':
    main()
