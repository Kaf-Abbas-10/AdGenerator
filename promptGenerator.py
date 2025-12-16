from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate

llm = ChatGroq(
    api_key="GROQ_API_KEY",
    model="llama-3.3-70b-versatile"
)

template = PromptTemplate(
    input_variables=["product"],
    template="""You are an expert at creating image generation prompts for marketing advertisements.

For the product: {product}

Generate a detailed image generation prompt that includes:
- Visual composition and layout
- Color scheme and mood
- Key elements to include
- Style (photorealistic, illustration, modern, vintage, etc.)
- Lighting and atmosphere
- Text placement suggestions (if any)

Create a compelling prompt that will generate an eye-catching advertisement image.

Prompt:"""
)

def generate_image_prompt(product):
    """Generate an image ad prompt for the given product"""
    response = llm.invoke(template.format(product=product))
    return response.content

if __name__ == "__main__":
    product = "My software Company, ZAK"
    image_prompt = generate_image_prompt(product)
    print("Generated Image Prompt:")
    print("-" * 50)
    print(image_prompt)
    print("-" * 50)
    
    # Save to file for use by image generator
    with open("generated_prompt.txt", "w") as f:
        f.write(image_prompt)