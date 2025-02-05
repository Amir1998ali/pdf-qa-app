from fastapi import FastAPI, File, UploadFile
import fitz  # PyMuPDF
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.chat_models import ChatOpenAI
from langchain.chains.question_answering import load_qa_chain
from langchain.docstore.document import Document
import os

app = FastAPI()

# ✅ Load API Key directly from Render's environment variables
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# ✅ Initialize LangChain Chat Model
if not OPENAI_API_KEY:
    raise ValueError("❌ OPENAI_API_KEY is missing! Add it in Render's environment variables.")

llm = ChatOpenAI(model_name="gpt-4", openai_api_key=OPENAI_API_KEY)
qa_chain = load_qa_chain(llm, chain_type="stuff")

@app.get("/")  # ✅ Simple root endpoint to check if the server is running
def home():
    return {"message": "🚀 FastAPI backend is running on Render!"}

@app.post("/process_pdf/")  # ✅ Ensure this is a POST request
async def process_pdf(file: UploadFile = File(...), query: str = ""):
    try:
        # ✅ Read PDF in-memory without storing files
        pdf_reader = fitz.open(stream=await file.read(), filetype="pdf")
        text = "\n".join([page.get_text("text") for page in pdf_reader])

        # ✅ Split text into smaller chunks for processing
        text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
        texts = text_splitter.split_text(text)
        documents = [Document(page_content=t) for t in texts]

        # ✅ Get AI-generated answer
        answer = qa_chain.run(input_documents=documents, question=query)

        return {"answer": answer}

    except Exception as e:
        return {"error": str(e)}

