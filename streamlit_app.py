import streamlit as st
import pandas as pd

st.set_page_config("Regeneration Generation", layout="wide")

st.title("🌱 Regeneration Generation")
st.subheader("What Can You Do in 30 Years?")
st.markdown("""
This interactive app is your guide to transforming small towns into regenerative eco-centers.
Use it to explore the movement, simulate impact, and help grow the future.
""")

# Tabs for sections
tabs = st.tabs(["🌍 Vision", "📊 Impact Simulator", "📚 Education Campaign", "🗺️ Policy Map (Coming Soon)", "📥 Downloads"])

# --- Vision Tab ---
with tabs[0]:
    st.header("The Regenerative Nation Vision")
    st.markdown("""
    **A 30-Year Plan (2025–2055)** to:
    - Turn underused rural land into regenerative assets
    - Create enterprise zones for food, energy, and fiber
    - Embed soil-based education in every school
    - Restore biodiversity and community health
    - Launch eco-hubs powered by circular economies
    """)

    st.markdown("""
    **Strategic Objectives**:
    - 🟢 Local food & soil restoration
    - ⚡ Tech-powered clean infrastructure
    - 👩‍🌾 Purpose-driven livelihoods
    - 🧒 Intergenerational learning & land literacy
    """)

# --- Impact Simulator Tab ---
with tabs[1]:
    st.header("Simulate Your Impact")
    acres = st.slider("Acres Regenerated", 1, 1000, 20)
    carbon = acres * 4.5
    income = acres * 2000
    toolkit_cost = acres * 18

    col1, col2, col3 = st.columns(3)
    col1.metric("Annual CO₂ Sequestered", f"{carbon:.0f} tons")
    col2.metric("Community Income Potential", f"${income:,.0f}/year")
    col3.metric("Education Investment (Est)", f"${toolkit_cost:,.0f}")

    st.markdown("""
    _Each acre supports food, carbon drawdown, and education. Now imagine a town, a county, or a country._
    """)

# --- Education Tab ---
with tabs[2]:
    st.header("📚 What Can You Grow? Education Campaign")
    st.markdown("""
    - Reach 50 million children
    - Distribute 1 million regenerative toolkits
    - Train 5,000 regional coordinators
    - Launch school gardens and soil storytelling events
    """)

    students = st.slider("Children Reached", 0, 50_000_000, 1_000_000, step=500_000)
    total_cost = students * 18
    st.metric("Estimated Toolkit Rollout Budget", f"${total_cost/1e6:.1f}M")

    st.info("Toolkits include storybooks, garden starter kits, soil science wheels, and parent guides.")

# --- Map Placeholder ---
with tabs[3]:
    st.header("🗺️ Regenerative Policy Map (Coming Soon)")
    st.markdown("Map-based exploration of land availability, town readiness, and regenerative funding zones.")
    st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/f/f8/Oklahoma_county_map.png/800px-Oklahoma_county_map.png")

# --- Downloads Tab ---
with tabs[4]:
    st.header("📥 Downloads")
    st.markdown("Download toolkits, charters, and presentation decks to share or present.")
    st.download_button("📄 Download Policy Toolkit PDF", data=open("Policy_Toolkit.pdf", "rb").read(), file_name="PolicyToolkit.pdf")
    st.download_button("📄 Download UN Proposal PDF", data=open("un_resolution.pdf", "rb").read(), file_name="UNResolution.pdf")
    st.download_button("📄 Download 30-Year Charter", data=open("30_year_charter.pdf", "rb").read(), file_name="30YearCharter.pdf")
