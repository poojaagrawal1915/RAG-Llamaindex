from llama_index.core import VectorStoreIndex
from llama_index.core import SimpleDirectoryReader
from llama_index.core import StorageContext,load_index_from_storage
import os
from dotenv import load_dotenv,find_dotenv
load_dotenv(find_dotenv())
os.environ["OPENAI_API_KEY"]=os.getenv("openai_api_key")

class RAG:
    def __init__(self,file_path):
        self.file_path=file_path

    def ouput(questions):
        documents=SimpleDirectoryReader(r"{self.file_path}").load_data()
        index=VectorStoreIndex(documents,show_progress=True)
        #Store data in local disk
        index.storage_context.persist(persist_dir="Path to store index")
        storage_context=Storage_Context.from_defaults(persist_dir="Path to store index")
        index=load_index_from_storage(storage_context)
        query_engine=index.as_query_engine()
        response=query_engine.query(f"{questions}")
        return response.response

    
obj=RAG(r'Path for my data corpus')
print(obj.output("list down skills of candidate?"))