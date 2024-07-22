import streamlit as st
import openai 
st.title("تكلم مع الدكتور محمد")
""" 
مرحبا ومسهلا معك الدكتور محمد, استشاري في علم الانف الأذن والحنجرة, كيف اقدر اخدمك؟
"""
if "messages" not in st.session_state:
    st.session_state["messages"] = [
        {"role": "system", "content":"انت الدكتور محمد, طبيب استشاري في علم الانف والأذن والحنجرة, انت طبيب مميز وعبقري, تفقه الكثير في علم الطب, تعلم كيف تخاطب الناس بلباقة واحترام, ان سألك احد عن ماهي الادوية التي يستعملها لعلاج الامراض, التي يقولوها لك"
           }

    ]
user = st.chat_input()
if user:
    openai.api_key = st.secrets["api"]
    st.session_state.messages.append({"role": "user", "content": user})
    st.chat_message("user").write(user)
    response = openai.ChatCompletion.create(model="gpt-4o-mini", messages=st.session_state.messages)
    ai = response.choices[0].message
    st.session_state.messages.append(ai)
    st.chat_message("assistant").write(ai.content)