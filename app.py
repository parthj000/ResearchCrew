import json

import streamlit as st

from main_agent import kapa

st.set_page_config(page_title="AI Research Assistant", layout="wide")

st.title("🔎 AI Research Assistant")

topic = st.text_input("Research Topic")


if st.button("Run Research"):
    if topic:
        with st.spinner("Searching and analyzing..."):
            initial_state = kapa.generate_initial_state(query=topic)
            result = kapa.graph.invoke(initial_state)

        col1, col2 = st.columns(2)

        with col1:
            st.subheader("Summary")
            st.write(result.get("summary", ""))

        with col2:
            st.subheader("Deep Analysis")
            st.write(result.get("insights", ""))

        st.subheader("Sources")
        urls = []

        docs = result.get("documents", "[]")
        documents = json.loads(docs)

        for doc in documents:
            title = doc.get("title", "Source")
            url = doc.get("url")

            if url:
                st.markdown(f"- [{title}]({url})")
