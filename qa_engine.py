from llama_cpp import Llama

# Global model instance (load once, reuse)
_llm = None

def load_model(model_path: str):
    """
    Load Phi-2 model with CPU-only settings.
    n_ctx=2048     → context window size
    n_threads=4    → use 4 CPU threads (good for i5 12th gen)
    n_gpu_layers=0 → no GPU, pure CPU inference
    """
    global _llm
    if _llm is None:
        print("⏳ Loading local AI model (first time takes ~30 seconds)...")
        _llm = Llama(
            model_path=model_path,
            n_ctx=2048,
            n_threads=4,
            n_gpu_layers=0,
            verbose=False
        )
        print("✅ Model loaded!")
    return _llm

def get_answer(llm, question: str, context_chunks: list) -> str:
    """
    Build a RAG prompt and run local inference.
    Temperature 0.1 = factual, deterministic answers.
    """
    if not context_chunks:
        return "No relevant content found in the document for your question."

    context = "\n\n".join(context_chunks)

    # Phi-2 works best with this Instruct-style prompt format
    prompt = f"""Instruct: You are a helpful assistant. Read the context below and answer the question.
Use ONLY the information in the context. If the answer is not there, say "Not found in document."

Context:
{context}

Question: {question}

Output:"""

    response = _llm(
        prompt,
        max_tokens=300,
        temperature=0.1,
        stop=["Instruct:", "Question:", "\n\n\n"]
    )

    return response["choices"][0]["text"].strip()