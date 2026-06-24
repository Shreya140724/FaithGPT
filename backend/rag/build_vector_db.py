import os
import pandas as pd

from langchain_core.documents import Document

from langchain_community.vectorstores import FAISS

from langchain_huggingface import (
    HuggingFaceEmbeddings
)

CSV_PATH = "data/bible.csv"

VECTOR_STORE_PATH = "vector_store"

print("Loading Bible Dataset...")

df = pd.read_csv(CSV_PATH)

documents = []

for _, row in df.iterrows():

    reference = (
        f"{row['book_name']} "
        f"{row['chapter_number']}:"
        f"{row['verse_number']}"
    )

    text = str(
        row["verse_text"]
    )

    documents.append(

        Document(

            page_content=text,

            metadata={
                "reference": reference,
                "book": row["book_name"]
            }
        )
    )

print(
    f"Loaded {len(documents)} verses"
)

embeddings = HuggingFaceEmbeddings(

    model_name=
    "BAAI/bge-small-en-v1.5"
)

db = FAISS.from_documents(

    documents,
    embeddings
)

os.makedirs(
    VECTOR_STORE_PATH,
    exist_ok=True
)

db.save_local(
    VECTOR_STORE_PATH
)

print(
    "Vector Store Created"
)