import streamlit as st
from pymongo import MongoClient
from nlp import extract_text_from_pdf, extract_data_from_text
import pandas as pd

# MongoDB connection details
client = MongoClient('mongodb+srv://Jaganathan:ccc@clusterbeginj.s7behpd.mongodb.net/?retryWrites=true&w=majority&appName=ClusterBeginJ&ssl=true',serverSelectionTimeoutMS=50000)
db = client['ESG_DATA']  # Replace with your database name
collection = db['Small_part']  # Replace with your collection name

def main():
    st.title("Data Updating Tool")
    
    pdf_file = st.file_uploader("Upload a PDF file", type=["pdf"])
    
    if pdf_file is not None:
        pdf_text = extract_text_from_pdf(pdf_file)
        extracted_data = extract_data_from_text(pdf_text)
        
        # Display the extracted data
        if extracted_data:
            st.subheader("Extracted Data:")
            df = pd.DataFrame(list(extracted_data.items()), columns=['Key', 'Value'])
            st.table(df)
            
            # Insert data into MongoDB
            collection.insert_one(extracted_data)
            st.success("Data successfully added to MongoDB!") 
        else:
            st.write("No data extracted. Please verify the PDF format and content.")

if __name__ == "__main__":
    main()