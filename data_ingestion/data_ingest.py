from langchain_astradb import AstraDBVectorStore
from dotenv import load_dotenv
import os
import pandas as pd
from data_ingestion.data_transform import data_converter
from langchain_google_genai import GoogleGenerativeAIEmbeddings

load_dotenv()



os.environ["GEMINI_API_KEY"]="AIzaSyCxczsBSI1ydYmdXfPZoQMnPuURA6RBRaE"
os.environ["ASTRA_DB_API_ENDPOINT"]="https://c43bb6b1-8dd1-4c48-b9fe-d78a90594b6e-us-east-2.apps.astra.datastax.com"
os.environ["ASTRA_DB_APPLICATION_TOKEN"]="AstraCS:PjuJqXrnuhIOlkqjIrQzGHiz:1813b04b2c2a747fa20940cc27e09850ecabcc3ee61e84ad3deeb44ca4c62862"
os.environ["ASTRA_DB_KEYSPACE"]="default_keyspace"

GEMINI_API_KEY=os.getenv("GEMINI_API_KEY")
ASTRA_DB_API_ENDPOINT=os.getenv("ASTRA_DB_API_ENDPOINT")
ASTRA_DB_APPLICATION_TOKEN=os.getenv("ASTRA_DB_APPLICATION_TOKEN")
ASTRA_DB_KEYSPACE=os.getenv("ASTRA_DB_KEYSPACE")

class ingest_data:
    def __init__(self):
        print("data ingestion class has been intialize")
        self.embeddings = GoogleGenerativeAIEmbeddings(model="models/text-embedding-004")
        self.data_conveter=data_converter()

    def data_ingestion(self,status):
        vstore=AstraDBVectorStore(
            embedding=self.embeddings,
            collection_name="customer_support",
            api_endpoint=ASTRA_DB_API_ENDPOINT,
            token=ASTRA_DB_APPLICATION_TOKEN,
            namespace=ASTRA_DB_KEYSPACE,
        )
        storage=status
        
        if storage==None:
            docs=self.data_conveter.data_transformation()
            inserted_ids=vstore.add_documents(docs)
            #print(inserted_ids)
        else:
            return vstore
        
        return vstore,inserted_ids

if __name__=='__main__':
    ingest=ingest_data()
    vstore,inserted_id=ingest.data_ingestion(None)
    print(f"inserted Id:{inserted_id}")
    #result = vstore.similarity_search("can you provide me the low budget headphone")
    #for res in result:
     #   print(f"result is {res.page_content}, {res.metadata})
    
