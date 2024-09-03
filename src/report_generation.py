# src/report_generation.py
import matplotlib.pyplot as plt
from fpdf import FPDF

def generate_visualizations(data, results):
    """
    Create visualizations such as charts and graphs.
    """
    plt.figure(figsize=(10, 6))
    plt.plot(data.index, results[0], label='Linear Regression')
    plt.title('Linear Regression Results')
    plt.legend()
    plt.savefig('results/visualizations/linear_regression.png')
    
    # Add more visualizations as needed
    plt.close()

def generate_report(data, results, file_name='report_example.pdf'):
    """
    Generate a PDF report with analysis results and visualizations.
    """
    pdf = FPDF()
    pdf.add_page()
    
    # Title
    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, txt="AI Employee Data Analysis Report", ln=True, align='C')
    
    # Summary
    pdf.set_font("Arial", size=10)
    pdf.multi_cell(0, 10, txt="This report summarizes the findings from the data analysis conducted by the AI employee...")
    
    # Add visualizations
    generate_visualizations(data, results)
    pdf.image('results/visualizations/linear_regression.png', x=10, y=60, w=180)
    
    pdf.output(f"results/{file_name}")
