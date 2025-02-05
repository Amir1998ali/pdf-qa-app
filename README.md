# 📄 AI-Powered PDF Q&A App 🚀  
### **Instantly Ask Questions About Any PDF Using AI**  

![PDF Q&A Banner](https://user-images.githubusercontent.com/1234567/example-banner.png) <!-- Add a relevant image or remove this line -->  

## 📝 **About This Project**  
This app allows users to **upload a PDF** and ask AI-powered questions about its content. The **backend (FastAPI)** processes the document, and the **frontend (Streamlit)** provides an easy-to-use interface.  

### 🌟 **Key Features:**  
✅ **Upload any PDF & ask questions**  
✅ **AI-powered responses (GPT-4)**  
✅ **No document storage, fully in-memory processing**  
✅ **Fast & lightweight (LangChain + FastAPI + Streamlit)**  
✅ **Publicly accessible via Render & Streamlit Cloud**  

---  

## 🚀 **Live Demo**  
🔹 **Frontend (Streamlit App):** [View Live](https://your-streamlit-app-url.streamlit.app/)  
🔹 **Backend (FastAPI Docs):** [View API Docs](https://your-app.onrender.com/docs)  

---  

## 🛠 **Tech Stack**  
🔹 **Frontend:** Streamlit (Python)  
🔹 **Backend:** FastAPI (Python)  
🔹 **AI Model:** OpenAI GPT-4 (via LangChain)  
🔹 **File Processing:** PyMuPDF  
🔹 **Hosting:** Render (backend) & Streamlit Cloud (frontend)  

---  

## 🏗 **Setup & Installation**  
### **1️⃣ Clone the Repository**  
```bash  
git clone https://github.com/your-username/pdf-qa-app.git  
cd pdf-qa-app  
```

### **2️⃣ Setup Virtual Environment & Install Dependencies**  
```bash  
python -m venv env  
source env/bin/activate  # For macOS/Linux  
# OR  
env\Scripts\activate    # For Windows  

pip install -r requirements.txt  
```

### **3️⃣ Set Up Environment Variables**  
Create a `.env` file in the root directory:  
```bash  
OPENAI_API_KEY=your-secret-api-key  
```

### **4️⃣ Run the Backend (FastAPI)**  
```bash  
uvicorn backend:app --host 0.0.0.0 --port 8000 --reload  
```
✅ Now visit: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)  

### **5️⃣ Run the Frontend (Streamlit)**  
```bash  
streamlit run app.py  
```
✅ Open your browser at: [http://localhost:8501](http://localhost:8501)  

---  

## 📌 **API Endpoints**  
| **Method** | **Endpoint** | **Description** |  
|-----------|------------|---------------|  
| `POST` | `/process_pdf/` | Upload a PDF and ask a question |  
| `GET` | `/` | Check if the backend is running |  

---  

## 🌍 **Deployment**  
### ✅ **Backend (FastAPI) on Render**  
- Hosted at: [https://your-app.onrender.com](https://your-app.onrender.com)  
- Set environment variables in **Render Dashboard**  

### ✅ **Frontend (Streamlit) on Streamlit Cloud**  
- Hosted at: [https://your-streamlit-app-url.streamlit.app/](https://your-streamlit-app-url.streamlit.app/)  
- Connect repo to Streamlit Cloud & deploy  

---  

## 📜 **License**  
This project is licensed under the **MIT License**.  

---  

## ✨ **Contributing**  
Contributions are welcome! Feel free to open an issue or submit a pull request.  

---  

## 🙌 **Acknowledgments**  
- OpenAI for GPT-4  
- LangChain for AI-powered document processing  
- Streamlit for easy frontend development  
- FastAPI for efficient backend architecture  

🎉 **Enjoy using the AI-Powered PDF Q&A App!** 🚀

