import pandas as pd
data={
    "Product":["laptop","mouse","keyboard","monitor"],
      "Category":["Electronics","Accessories","Accessories","Electronics"],
      "Price":[1200,25,45,300],
      "Quantity":[2,10,5,3],
      "City":["Cairo","Alexandria","Giza","Cairo"]
}

df=pd.DataFrame(data)
df.to_csv("sales_data.csv",index=False)
print("Data generated and saved to sales_data.csv")

df=pd.read_csv("sales_data.csv")
df["Total_sales"]=df["Price"]*df["Quantity"]
print(f"Total sales calculated and added to the Dataframe:\n{df}")
total_revenue=df["Total_sales"].sum()
print(f"Total revenue from all products: {total_revenue}")