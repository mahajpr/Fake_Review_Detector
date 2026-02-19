
import streamlit as st
import pandas as pd
import requests

st.set_page_config(
    page_title="Fake Review Detection Dashboard",
    layout="wide"
)

API_URL = "http://localhost:8000/analyze"
API_STATS = "http://localhost:8000/stats"

if "page" not in st.session_state:
    st.session_state.page = "Dashboard"


st.sidebar.title("🔍 Fake Review Detection")

if st.sidebar.button("Dashboard"):
    st.session_state.page = "Dashboard"

if st.sidebar.button("All Reviews"):
    st.session_state.page = "All Reviews"

if st.sidebar.button("Flagged Reviews"):
    st.session_state.page = "Flagged Reviews"

if st.sidebar.button("Reports"):
    st.session_state.page = "Reports"


if st.session_state.page == "Dashboard":

    st.markdown("## Fake Review Detection Dashboard")

    stats_response = requests.get(API_STATS)
    if stats_response.status_code == 200:
        stats = stats_response.json()
    else:
        stats = {
            "total_reviews": 0,
            "detected_fake": 0,
            "flagged_reviews": 0,
            "monthly_reviews": 0
        }

    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Total Reviews", stats["total_reviews"])
    col2.metric("Detected as Fake", stats["detected_fake"])
    col3.metric("Flagged for Review", stats["flagged_reviews"])
    col4.metric("Monthly Stats", stats["monthly_reviews"])

    st.markdown("---")

    left, right = st.columns([2, 1])

    with left:
        st.subheader("Review Analysis")

        review_text = st.text_area(
            "Customer Review",
            height=120
        )

        if st.button("Analyze Review"):
            response = requests.post(API_URL, json={"review": review_text})

            if response.status_code == 200:
                st.session_state.result = response.json()
            else:
                st.error("Backend error")

        if "result" in st.session_state:
            r = st.session_state.result

            st.markdown("### Explanation & Similar Reviews")
            st.success(r["explanation"])

            st.markdown("#### 📚 Similar Historical Reviews")
            for sim in r["similar_reviews"]:
                st.warning(sim)


    with right:
        if "result" in st.session_state:
            r = st.session_state.result

            st.subheader("Detection Result")

            if r["prediction"] == "Fake":
                st.error(f"🚨 Fake Review — {int(r['confidence']*100)}% Confidence")
            else:
                st.success(f"✅ Genuine Review — {int(r['confidence']*100)}% Confidence")

            if r["suspicious_phrases"]:
                st.markdown("**⚠️ Suspicious Phrases Detected**")
                st.write(", ".join(r["suspicious_phrases"]))

        st.markdown("### Recent Review Trends")

        response = requests.get("http://localhost:8000/reviews")

        if response.status_code == 200:
            data = response.json()

            if data:
                df = pd.DataFrame(data)
                df["created_at"] = pd.to_datetime(df["created_at"])
                df["date"] = df["created_at"].dt.date

                grouped = df.groupby(["date", "prediction"]).size().unstack(fill_value=0)
                st.line_chart(grouped)
            else:
                st.info("No review data yet")
        else:
            st.error("Failed to load trends")

elif st.session_state.page == "All Reviews":

    st.markdown("## 📝 All Reviews")
    response = requests.get("http://localhost:8000/reviews")

    if response.status_code == 200:
        data = response.json()

        if len(data) == 0:
            st.info("No reviews yet")
        else:
            df = pd.DataFrame(data)
            df = df[["review_text", "prediction", "confidence"]]
            df.columns = ["Review", "Prediction", "Confidence"]
            st.dataframe(df, use_container_width=True)
    else:
        st.error("Failed to fetch reviews")

elif st.session_state.page == "Flagged Reviews":

    st.markdown("## 🚩 Flagged Reviews")

    response = requests.get("http://localhost:8000/flagged")

    if response.status_code == 200:
        data = response.json()

        if len(data) == 0:
            st.info("No flagged reviews yet")
        else:
            df = pd.DataFrame(data)
            df = df[["review_text", "reason", "confidence"]]
            df.columns = ["Review", "Reason", "Confidence"]
            st.dataframe(df, use_container_width=True)
    else:
        st.error("Failed to fetch flagged reviews")

elif st.session_state.page == "Reports":

    st.markdown("## 📊 Reports")

    report_data = pd.DataFrame({
        "Month": ["Jan", "Feb", "Mar", "Apr"],
        "Fake Reviews": [210, 320, 410, 530],
        "Genuine Reviews": [480, 450, 430, 390]
    }).set_index("Month")

    st.bar_chart(report_data)

    st.download_button(
        label="Download Report (CSV)",
        data=report_data.to_csv(),
        file_name="fake_review_report.csv",
        mime="text/csv"
    )

















