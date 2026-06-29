import streamlit as st
import google.generativeai as genai

# 1. Page Configuration
st.set_page_config(page_title="Gemini Chatbot", page_icon="🤖")
st.title("🤖 Gemini AI Chatbot")

# 2. Configure API Key
# We use st.secrets for security. See "How to deploy" below.
try:
    genai.configure(api_key=st.secrets["GEMINI_API_KEY"])
    model = genai.GenerativeModel('gemini-2.5-flash')
except Exception as e:
    st.error("Error: Could not configure Gemini API. Check your Streamlit Secrets.")
    st.stop()

# 3. Initialize Chat History
if "messages" not in st.session_state:
    st.session_state.messages = []

# 4. Display History
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# 5. Handle Chat Input
if prompt := st.chat_input("Ask me anything..."):
    # Display and Save User Message
    st.chat_message("user").markdown(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})

    # Generate AI Response
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            try:
                # Use model.start_chat if you want to keep context
                chat = model.start_chat(history=[])
                response = model.generate_content(prompt)
                st.markdown(response.text)
                st.session_state.messages.append({"role": "assistant", "content": response.text})
            except Exception as e:
                st.error(f"An error occurred: {e}")                
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
