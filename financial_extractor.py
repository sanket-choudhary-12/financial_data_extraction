import streamlit as st
import google.generativeai as genai
import PyPDF2
import json
import os
import re  

# Configure Google Gemini API
GENAI_API_KEY = "AIzaSyChpvT-miHvwDxWxxkjgHJCGk4OL8Dcv5w"
genai.configure(api_key=GENAI_API_KEY)

# Function to extract text from PDF
def extract_text_from_pdf(pdf_file):
    reader = PyPDF2.PdfReader(pdf_file)
    text = "\n".join(page.extract_text() for page in reader.pages if page.extract_text())
    return text

# Function to process text with Gemini API
def get_financial_details(text):
    model = genai.GenerativeModel("gemini-pro")

    prompt = f"""
    Extract the following financial details from the document **in valid JSON format only**:
    
    - **Company Name**
    - **Report Date**
    - **Profit Before Tax**
    - **Any additional relevant financial details**

    **Response Format (Must be valid JSON):**
    ```json
    {{
      "company_name": "Company Name Here",
      "report_date": "YYYY-MM-DD",
      "profit_before_tax": "Amount Here",
      "additional_details": "Other financial details"
    }}
    ```

    **Important:**  
    - **Only return JSON** (no explanations, no extra text).  
    - **Ensure JSON is properly formatted**.  
    - **Do not include markdown formatting (` ```json `, ` ``` `)**.  

    ### **Document Text:**
    {text}
    """

    response = model.generate_content(prompt)

    try:
        # Extract raw response text
        raw_response = response.text.strip()

        # Use regex to extract valid JSON from the response
        json_match = re.search(r"\{.*\}", raw_response, re.DOTALL)
        if json_match:
            json_data = json_match.group(0)  # Extract JSON part
            extracted_data = json.loads(json_data)  # Convert to Python dictionary
        else:
            extracted_data = {"error": "Failed to extract valid JSON from AI response."}
    
    except json.JSONDecodeError:
        extracted_data = {"error": "Failed to parse JSON response from AI."}

    return extracted_data

# Streamlit UI
st.title("📊 Financial Data Extractor")
uploaded_file = st.file_uploader("📂 Upload a PDF file", type="pdf")

extracted_data = {}

if uploaded_file:
    with st.spinner("🔍 Extracting text from PDF..."):
        text = extract_text_from_pdf(uploaded_file)
    
    with st.spinner("🤖 Processing with Gemini AI..."):
        extracted_data = get_financial_details(text)

    st.subheader("📄 Extracted Financial Data:")
    st.json(extracted_data)  # Display extracted data as JSON

# Save Button - Appends data to JSON file
if extracted_data and "error" not in extracted_data:
    if st.button("💾 Save Data to JSON"):
        json_file = "extracted_financial_data.json"

        # Check if the file exists and load existing data
        if os.path.exists(json_file):
            try:
                with open(json_file, "r") as f:
                    existing_data = json.load(f)
                    if not isinstance(existing_data, list):  # Ensure it's a list
                        existing_data = []
            except json.JSONDecodeError:
                existing_data = []
        else:
            existing_data = []

        # Append new data
        existing_data.append(extracted_data)

        # Save updated data
        with open(json_file, "w") as f:
            json.dump(existing_data, f, indent=4)

        st.success("✅ Data successfully saved to **extracted_financial_data.json**")
