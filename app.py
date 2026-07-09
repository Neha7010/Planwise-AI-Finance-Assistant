import gradio
import os
from groq import Groq
client = Groq(api_key=os.getenv("GROQ_API_KEY"))
def initialize_messages():
    return [{"role": "system",
             "content": '''You are a personal finance advisor.
             Help users with budgeting, saving money,
             investment basics, insurance, and financial planning.
             Give educational guidance only.'''}]
messages_prmt = initialize_messages()
def customLLMBot(user_input, history):
    global messages_prmt
    messages_prmt.append({"role": "user", "content": user_input})
    response = client.chat.completions.create(
        messages=messages_prmt,
        model="llama-3.3-70b-versatile",
    )
    print(response)
    LLM_reply = response.choices[0].message.content
    messages_prmt.append({"role": "assistant", "content": LLM_reply})
    return LLM_reply                                                                  


custom_css = """
    .gradio-container h1 {
        text-align: center !important;
    }
"""

with gradio.Blocks(css=custom_css) as iface:
    gradio.ChatInterface(
        customLLMBot,
        chatbot=gradio.Chatbot(height=700),
        textbox=gradio.Textbox(
            placeholder="Ask me a question about personal finance"
        ),
        title="PlanWise📝",
        description="AI chatbot for budgeting, saving, investing, and financial planning",
        examples=[
        ]
    )

iface.launch(share=True)