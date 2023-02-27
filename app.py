import os
import openai
import gradio as gr


openai.api_key = "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"

start_sequence = "\nAI:"
restart_sequence = "\nHuman: "

prompt = "Hold a conversation with an AI Chatbot. The Chatbot is based on gpt-3 and is helpful and very friendly.\n\nHuman: Hello, who are you?\nAI: I am Glow, a chatbot created by Enyi Gloria as a final year project. Let's Chat :D.\nHuman: "

def openai_create(prompt):

    response = openai.Completion.create(
    model="text-davinci-003",
    prompt=prompt,
    temperature=0.9,
    max_tokens=150,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0.6,
    stop=[" Human:", " AI:"]
    )

    return response.choices[0].text



def chatgpt_clone(input, history):
    history = history or []
    s = list(sum(history, ()))
    s.append(input)
    inp = ' '.join(s)
    output = openai_create(inp)
    history.append((input, output))
    return history, history


block = gr.Blocks()


with block: 
    gr.Markdown("""<h1><center>Chat with Glow</center></h1>\n<h6>your very own AI buddy</h6>
    """)
    chatbot = gr.Chatbot()
    message = gr.Textbox(placeholder=prompt)
    state = gr.State()
    submit = gr.Button("SEND")
    submit.click(chatgpt_clone, inputs=[message, state], outputs=[chatbot, state])

block.launch(debug = True, share = True)