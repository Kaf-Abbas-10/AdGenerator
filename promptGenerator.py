from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate

llm = ChatGroq(
    api_key="YOUR_GROQ_API_KEY",
    model="llama-3.3-70b-versatile"
)

template = PromptTemplate(
    input_variables=["product"],
    template="Write a catchy marketing ad for: {product}"
)

ad_text = llm.invoke(template.format(product="Organic Tea"))
print(ad_text.content) 