import pandas as pd
from langchain_core.documents import Document

# code for converting data
class data_converter:
    def __init__(self):
        print("data converter path has been intialize")
        self.product_data=pd.read_csv(r"C:\Users\SHILPA\customer_support_system\data\amazon_product_review.csv")
        print(self.product_data.head())


    def data_transformation(self):
        reuired_columns=self.product_data.columns
        required_columns=list(reuired_columns[1:])

        product_list=[]
        for index,row in self.product_data.iterrows():
            object={
                "product_name":row["product_title"],
                "product_rating":row["rating"],
                "product_summary":row["summary"],
                "product_review":row["review"]


            }
            product_list.append(object)
        print("******below is product list****")
        print(product_list)

        for entry in product_list:
            metadata={"product_name":entry["product_name","product_rating":entry["product_rating"]]}
            doc=Document(page_content=entry["product_name"],metadata=metadata)
            docs.append(doc)
        print(docs[0])


if __name__=='__main__':
    data_convert=data_converter()


        