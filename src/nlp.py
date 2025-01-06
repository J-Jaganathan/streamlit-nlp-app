import PyPDF2
import re
import os

# Step 1: Extract text from the local PDF using PyPDF2
def extract_text_from_pdf(pdf_file):
    if not pdf_file:
        raise ValueError("No file uploaded.")
    
    reader = PyPDF2.PdfReader(pdf_file)
    text = ""
    for page in range(len(reader.pages)):
        text += reader.pages[page].extract_text()
    return text

# Step 2: Extract specific information using regex
def extract_data_from_text(text):
    # Define regex patterns for each field
    patterns = {
        #"Company": r"Company:\s*([^\n]+)",
        #"Project Name": r"Project Name:\s*([^\n]+)",
        #"Last Updated": r"Last Updated:\s*([^\n]+)",
        "Governance Score": r"Governance_Score:\s*([^\n]+)",
        "Social Score": r"Social_Score:\s*([^\n]+)",
        "Environmental Score": r"Environmental_Score:\s*([^\n]+)",
        "Emissions": r"Emissions:\s*([^\n]+)",
        "Water Usage": r"Water_Usage:\s*([^\n]+)",
        "Budget": r"Budget:\s*([^\n]+)",
        "Economic Impact": r"Economic_Impact:\s*([^\n]+)",
        "Historical Success Rate": r"Historical_Success_Rate:\s*([^\n]+)",
        "Climate Volatility Index": r"Climate_Volatility_Index:\s*([^\n]+)",
        "ROI": r"ROI:\s*([^\n]+)",
         # "ESG_Score": r"ESG_Score:\s*([^\n]+)",
         #"Risk_Level": r"Risk_Level:\s*([^\n]+)" 
    }
    extracted_data = {}
    for field, pattern in patterns.items():
        match = re.search(pattern, text)
        if match:
            extracted_data[field] = match.group(1).strip()
    return extracted_data