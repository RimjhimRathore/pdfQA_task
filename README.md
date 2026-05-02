<<<<<<< HEAD
📄 PDF Question Answering System

A lightweight and efficient Document Question Answering System that allows users to upload a PDF and ask questions based strictly on its content. The system retrieves relevant context and generates accurate answers without relying on external APIs — ensuring privacy, speed, and offline usability.

🚀 Features

📥 Upload PDF Documents
Easily upload any PDF file for processing
❓ Natural Language Queries
Ask questions in simple, human language
📚 Context-Based Answers
Responses are generated strictly from the document content
⚡ Fast Semantic Search
Uses embeddings for quick and relevant information retrieval
🔒 Fully Local Execution
No external APIs required — runs completely on your machine


🧠 How It Works

📄 PDF is uploaded and parsed
✂️ Text is split into smaller chunks
🔢 Each chunk is converted into embeddings
🗂️ Stored in a vector database (FAISS / ChromaDB)
❓ User asks a question
🔍 Relevant chunks are retrieved
🤖 Local LLM generates the final answer


🛠️ Tech Stack

Python
Sentence Transformers / Transformers
FAISS / ChromaDB
PyPDF / PDF Processing Libraries
CTransformers / LLaMA (for local LLM, optional)
=======
# pdfQA_task
A lightweight and efficient Document Question Answering system that allows users to upload a PDF and ask questions based strictly on its content. The system retrieves relevant context from the document and generates accurate answers without relying on external APIs.
>>>>>>> 48892a53e83a03b9240251eac12cebd72e23a510
