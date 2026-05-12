import streamlit as st

from pathlib import Path

from services.review_service import generate_code_review


# Page config
st.set_page_config(
    page_title="AI Code Reviewer",
    page_icon="💻",
    layout="wide"
)

# Load CSS
def load_css():

    css_path = Path("ui/styles.css")

    if css_path.exists():

        with open(css_path) as f:

            st.markdown(
                f"<style>{f.read()}</style>",
                unsafe_allow_html=True
            )

# Session state
def initialize_session():

    if "page" not in st.session_state:
        st.session_state.page = "input"

    if "review_result" not in st.session_state:
        st.session_state.review_result = ""

# Input page
def render_input_page():

    st.markdown(
        """
        <h1 class="main-title">
            AI CODE REVIEWER
        </h1>
        """,
        unsafe_allow_html=True
    )

    code_input = st.text_area(
        label="",
        placeholder="Enter code here...",
        height=350
    )

    col1, col2 = st.columns(2)

    with col1:

        language = st.selectbox(
            "Language",
            [
                "Python",
                "JavaScript",
                "Java",
                "C"
            ]
        )

    with col2:

        model = st.selectbox(
            "Model",
            [
                "qwen2.5:7b"
            ]
        )

    analyze_button = st.button(
        "Analyze Code",
        use_container_width=True
    )

    # Generate review
    if analyze_button:

        if not code_input.strip():

            st.warning("Please enter code first.")

            return

        with st.spinner("Analyzing code..."):

            review = generate_code_review(
            code=code_input,
            language=language,
            model=model
        )

        if review.startswith("Error:"):

            st.error(review)

            return

        st.session_state.review_result = review

        st.session_state.page = "result"

        st.rerun()

# Result page
def render_result_page():

    st.markdown(st.session_state.review_result)

    back_button = st.button(
        "Analyze Another Code",
        use_container_width=True
    )

    if back_button:

        st.session_state.page = "input"

        st.session_state.review_result = ""

        st.rerun()


# Main app
def main():

    load_css()

    initialize_session()

    if st.session_state.page == "input":

        render_input_page()

    elif st.session_state.page == "result":

        render_result_page()


if __name__ == "__main__":

    main()