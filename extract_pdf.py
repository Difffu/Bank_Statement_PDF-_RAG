from PyPDF2 import PdfReader
import pdfplumber
import pandas as pd

pdf_path = "Financial-Document-Samples_01.28.19.pdf"

def extract_text_from_pdf(pdf_path):
    reader = PdfReader(pdf_path)
    text = ""
    for page in reader.pages:
        text += page.extract_text()

    print(text)



def extract_tables_from_pdf(pdf_path):
    # Open the PDF file
    with pdfplumber.open(pdf_path) as pdf:
        # Initialize an empty list to store all tables
        all_tables = []
        
        # Iterate through each page
        for page in pdf.pages:
            # Extract tables from the current page
            tables = page.extract_tables()
            
            # Add tables to our list if any were found
            if tables:
                all_tables.extend(tables)
    
    # Convert tables to pandas DataFrames and store them
    dfs = []
    for i, table in enumerate(all_tables):
        df = pd.DataFrame(table[1:], columns=table[0])  # Assuming first row contains headers
        dfs.append(df)
        
        # Optionally save each table to CSV
        df.to_csv(f'table_{i+1}.csv', index=False)


# Extract tables
extract_text_from_pdf(pdf_path)

# # Print number of tables found
# print(f"Found {len(tables)} tables in the PDF")

# # Optionally display the first few rows of each table
# for i, df in enumerate(tables):
#     print(f"\nTable {i+1}:")
#     print(df.head())