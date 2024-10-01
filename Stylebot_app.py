import streamlit as st


# Remove whitespace from the top of the page and sidebar
st.markdown(
        """
            <style>
                .appview-container .main .block-container {{
                    padding-top: {padding_top}rem;
                    padding-bottom: {padding_bottom}rem;
                    }}

            </style>""".format(
            padding_top= 1, padding_bottom= 1
        ),
        unsafe_allow_html= True,
    )


# custom main page header 
st.markdown("""
    <h3 style= 'text-align: left; color: black;
            padding-top: 35px; padding-bottom: 8px;
            border-bottom: 3px solid orange;'>
            AI Styling Recommendations 🧥👕
    </h3>
            """, unsafe_allow_html= True)


# custom the app sidebar 
side_bar_message = """
Hi! 👋 I'm here to help you with your fashion choices. What would you like to know or explore?
\nHere are some areas you might be interested in:
1. **Fashion Trends**
2. **Personal Styling Advice**
3. **Seasonal Wardrobe Selections**
4. **Accessory Recommendations**

Feel free to ask me anything about fashion!
"""

with st.sidebar:
    st.title('StyleBot: Your AI Style Assistant')
    st.markdown(side_bar_message)


# app kickoff
initial_message = """
    Hi there! I'm StyleBot. Here are some questions you might ask me:\n
    ❔ What are the top fashion trends this summer?\n
    ❔ Can you suggest an outfit for a summer wedding?\n
    ❔ What are some must-have accessories for winter season?\n
    ❔ What type of shoes should I wear with a cocktail dress?\n
    ❔ What's the best look for a professional photo shoot?
"""

# Store LLM generated responses
if "messages" not in st.session_state.keys():
    st.session_state.messages = [{"role": "assistant", "content": initial_message}]

# Display or clear chat messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

def clear_chat_history():
    st.session_state.messages = [{"role": "assistant", "content": initial_message}]
st.button('Clear Chat', on_click=clear_chat_history)

# User-provided prompt
if prompt := st.chat_input():
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)
