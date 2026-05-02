import os
import sys
from pdf_processor import extract_text, chunk_text
from retriever import Retriever
from qa_engine import load_model, get_answer

# ── Path to your downloaded model ──────────────────────────
MODEL_PATH = "models/phi-2.Q4_K_M.gguf"

def main():
    print("=" * 55)
    print("   📄 Local Document Q&A System (100% Offline)")
    print("=" * 55)

    # ── Validate model exists ───────────────────────────────
    if not os.path.exists(MODEL_PATH):
        print(f"❌ Model not found at: {MODEL_PATH}")
        print("   Download phi-2.Q4_K_M.gguf from:")
        print("   https://huggingface.co/TheBloke/phi-2-GGUF")
        sys.exit(1)

    # ── Step 1: Load model ──────────────────────────────────
    llm = load_model(MODEL_PATH)

    # ── Step 2: Get PDF from user ───────────────────────────
    print()
    pdf_path = input("📂 Enter path to your PDF: ").strip().strip('"')

    if not os.path.exists(pdf_path):
        print("❌ File not found. Check the path and try again.")
        sys.exit(1)

    # ── Step 3: Extract and chunk text ──────────────────────
    print("\n⏳ Reading PDF...")
    text = extract_text(pdf_path)

    if not text.strip():
        print("❌ No text extracted. PDF might be a scanned image.")
        print("   This system only works with text-based PDFs.")
        sys.exit(1)

    print("⏳ Splitting into chunks...")
    chunks = chunk_text(text, chunk_size=300, overlap=50)
    print(f"✅ Created {len(chunks)} chunks from the document.")

    # ── Step 4: Build TF-IDF index ──────────────────────────
    print("⏳ Building search index...")
    retriever = Retriever()
    retriever.index(chunks)

    # ── Step 5: Q&A Loop ────────────────────────────────────
    print("\n" + "=" * 55)
    print("✅ Ready! Ask questions about your document.")
    print("   Type 'quit' to exit.")
    print("=" * 55)

    while True:
        print()
        question = input("❓ Question: ").strip()

        if question.lower() in ("quit", "exit", "q"):
            print("\n👋 Goodbye!")
            break

        if not question:
            print("⚠️  Please enter a question.")
            continue

        # Retrieve relevant chunks
        print("🔍 Searching document...")
        top_chunks = retriever.get_top_chunks(question, top_k=3)

        if not top_chunks:
            print("⚠️  No relevant content found for that question.")
            continue

        # Generate answer locally
        print("🤖 Generating answer (may take 20-40 sec on CPU)...")
        answer = get_answer(llm, question, top_chunks)

        print("\n💬 Answer:")
        print("-" * 55)
        print(answer)
        print("-" * 55)

if __name__ == "__main__":
    main()