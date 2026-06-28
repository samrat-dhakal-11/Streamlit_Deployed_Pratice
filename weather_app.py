import streamlit as st
import requests

st.set_page_config(page_title="Free AI Chatbot", page_icon="💬", layout="centered")
st.title("The Great Samrat Dhakal \n\n\n\n")
st.title("💬 Free Open-Source AI Chatbot")
st.write("A fully functional chatbot running on a free open-source model without API keys.")

# 1. Initialize Chat History in Session State
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "Hello! I am a free AI model hosted on Hugging Face. How can I help you today?"}
    ]

# 2. Display Chat History from Session State
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

# 3. Handle User Input
if user_prompt := st.chat_input("Type your message here..."):
    
    # Display user message instantly
    with st.chat_message("user"):
        st.write(user_prompt)
    
    # Add user message to session state history
    st.session_state.messages.append({"role": "user", "content": user_prompt})
    
    # Display assistant placeholder with a spinner while fetching response
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            
            try:
                # Using a public, free-tier serverless endpoint for Microsoft's Phi-3 model
                API_URL = "https://api-inference.huggingface.co/models/microsoft/Phi-3-mini-4k-instruct"
                
                # Format the prompt context for the model
                payload = {"inputs": f"<|user|>\n{user_prompt}<|end|>\n<|assistant|>"}
                
                # Send request to Hugging Face
                response = requests.post(API_URL, json=payload, timeout=10)
                output = response.json()
                
                # Extract response text safely
                if isinstance(output, list) and len(output) > 0 and "generated_text" in output[0]:
                    raw_text = output[0]["generated_text"]
                    # Clean up the output to only show the assistant's final response
                    ai_response = raw_text.split("<|assistant|>")[-1].strip()
                else:
                    ai_response = "The free serverless API is currently busy or waking up. Please try again in a few seconds!"
                    
            except Exception as e:
                ai_response = f"Connection Error: Could not reach the free AI server right now."

            # Display the final AI response
            st.write(ai_response)
            
    # Add assistant response to session state history
    st.session_state.messages.append({"role": "assistant", "content": ai_response})
