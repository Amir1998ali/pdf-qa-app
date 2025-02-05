from fastapi import FastAPI, File, UploadFile
import fitz  # PyMuPDF
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.chat_models import ChatOpenAI
from langchain.chains.question_answering import load_qa_chain
from langchain.docstore.document import Document
from dotenv import load_dotenv
import os

app = FastAPI()
load_dotenv()

# Load OpenAI model
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
llm = ChatOpenAI(model_name="gpt-4", openai_api_key=OPENAI_API_KEY)
qa_chain = load_qa_chain(llm, chain_type="stuff")

@app.post("/process_pdf/")  # ✅ Ensure this is POST
async def process_pdf(file: UploadFile = File(...), query: str = ""):
    pdf_reader = fitz.open(stream=await file.read(), filetype="pdf")
    text = "\n".join([page.get_text("text") for page in pdf_reader])

    # Split text into chunks
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    texts = text_splitter.split_text(text)
    documents = [Document(page_content=t) for t in texts]

    # Get AI answer
    answer = qa_chain.run(input_documents=documents, question=query)

    return {"answer": answer}
