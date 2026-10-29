from langchain_ollama import ChatOllama
from dotenv import load_dotenv
from typing import TypedDict, Annotated, Optional

load_dotenv()

model = ChatOllama(model="gemma3:1b")

#Schema 
class review(TypedDict):
    summary : str
    sentiment : str
    pros : str
    cons : str
    author : Optional[str]

Structured_output = model.with_structured_output(review)

result = Structured_output.invoke(""" The iPhone 16 Pro offers a premium design, excellent camera quality, and powerful performance with its A18 Pro chip. The display is smooth and vibrant, making it suitable for gaming, streaming, and everyday use. However, its price is relatively high, and the upgrades over previous iPhone Pro models may not be significant enough for everyone. Battery life is generally good, although charging speeds could be better. Overall, the iPhone 16 Pro is a capable flagship smartphone with several strengths and a few drawbacks, making it a good option for users who value performance, camera quality, and the iOS ecosystem.

by Suyash Dabare """)

print(result)