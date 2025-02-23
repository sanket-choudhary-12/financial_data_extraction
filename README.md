# Financial Data Extraction Using Open-Source LLMs

## 📌 Project Overview
This project is a **Financial Data Extractor** built using **Python, Streamlit, and Google Gemini API**. It extracts key financial details from **PDF documents** and stores the extracted data in a structured JSON format.

## 🎯 Features
- 📂 **Upload PDF** – Users can upload financial reports or statements.
- 🔍 **Extract Financial Data** – Extracts the following:
  - **Company Name**
  - **Report Date**
  - **Profit Before Tax**
  - **Additional Financial Details**
- 🤖 **AI Processing** – Uses **Google Gemini API** to extract structured data.
- 📄 **JSON Output** – Displays the extracted data in a structured JSON format.
- 💾 **Save Data** – Users can save extracted results to a JSON file.

---

## 🏗️ Tech Stack
- **Python** – Core programming language
- **Streamlit** – Web UI for user interaction
- **Google Gemini API** – AI-powered financial data extraction
- **PyPDF2** – PDF text extraction
- **JSON** – Data storage format

---

## 🚀 Installation Guide

### **1️⃣ Prerequisites**
Ensure you have the following installed:
- Python 3.8+
- Virtual environment (optional but recommended)

### **2️⃣ Clone the Repository**
```sh
git clone https://github.com/your-repo/financial-data-extractor.git
cd financial-data-extractor
```

### **3️⃣ Install Dependencies**
```sh
pip install -r requirements.txt
```

### **4️⃣ Configure API Key**
Replace `GENAI_API_KEY` in `app.py` with your **Google Gemini API Key**:
```python
GENAI_API_KEY = "YOUR_GOOGLE_GEMINI_API_KEY"
```

### **5️⃣ Run the Application**
```sh
streamlit run app.py
```

---

## 🛠️ Usage Guide

### **1️⃣ Upload a PDF File**
- Click **"Upload a PDF file"** button.
- Select a financial document (PDF format).

### **2️⃣ Extract Financial Data**
- The AI model will process the document.
- Extracted details will be displayed in JSON format.

### **3️⃣ Save Extracted Data**
- Click the **"Save Data"** button.
- JSON file will be saved locally with the extracted details.

---

## 📝 Example Output
```json
{
  "company_name": "TechCorp Ltd.",
  "report_date": "2024-01-15",
  "profit_before_tax": "$5,000,000",
  "additional_details": "Revenue growth of 10% YoY."
}
```

---

## ⚡ Future Enhancements
🔹 **Vector Database Integration** – Store & retrieve extracted data efficiently.  
🔹 **Multi-PDF Processing** – Allow bulk PDF uploads.  
🔹 **Advanced Data Validation** – Improve accuracy of extracted information.

---


