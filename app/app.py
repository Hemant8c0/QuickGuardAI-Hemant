import streamlit as st
import google.generativeai as genai
import warnings

warnings.filterwarnings("ignore")

# Page Layout & Theme
st.set_page_config(page_title="QuickGuard AI | Hemant", page_icon="🛡️", layout="wide")

# --- PREMIUM CYBER-SPRING UI (CSS) ---
st.markdown("""
    <style>
    /* Gradient Background */
    .stApp {
        background: radial-gradient(circle at 20% 30%, #0d1b11 0%, #05070a 100%);
        color: #e6f1ff;
    }

    /* Glassmorphism Main Card */
    .main-card {
        background: rgba(255, 255, 255, 0.02);
        backdrop-filter: blur(20px);
        border-radius: 25px;
        padding: 40px;
        border: 1px solid rgba(0, 255, 136, 0.1);
        box-shadow: 0 20px 50px rgba(0, 0, 0, 0.5);
    }

    /* Animated Neon Title */
    .hero-title {
        background: linear-gradient(90deg, #b0ffab, #00ff88, #6effff);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-size: 55px;
        font-weight: 900;
        text-align: center;
        letter-spacing: -2px;
        filter: drop-shadow(0 0 15px rgba(0, 255, 136, 0.3));
    }

    /* Developer Spotlight */
    .dev-tag {
        background: rgba(0, 255, 136, 0.1);
        color: #00ff88;
        padding: 5px 20px;
        border-radius: 50px;
        border: 1px solid #00ff88;
        font-size: 14px;
        font-weight: 700;
        text-transform: uppercase;
        display: block;
        width: fit-content;
        margin: 0 auto 15px;
        letter-spacing: 2px;
    }

    /* Action Button - High Contrast */
    .stButton>button {
        background: linear-gradient(45deg, #00ff88, #00d4ff) !important;
        color: #000 !important;
        font-size: 18px !important;
        font-weight: 800 !important;
        border-radius: 15px !important;
        padding: 15px !important;
        border: none !important;
        transition: 0.3s all ease !important;
        box-shadow: 0 0 20px rgba(0, 255, 136, 0.2);
    }

    .stButton>button:hover {
        transform: translateY(-3px);
        box-shadow: 0 10px 30px rgba(0, 255, 136, 0.4);
    }

    /* Sidebar Professionalism */
    [data-testid="stSidebar"] {
        background-color: #0a0c10;
        border-right: 1px solid rgba(0, 255, 136, 0.1);
    }

    /* Scanned Result Box */
    .result-box {
        background: rgba(0, 0, 0, 0.4);
        border-left: 5px solid #00ff88;
        padding: 25px;
        border-radius: 15px;
        margin-top: 20px;
    }
    </style>
    """, unsafe_allow_html=True)

# --- HEADER SECTION ---
st.markdown('<div class="dev-tag">Hemant\'s Innovation Lab</div>', unsafe_allow_html=True)
st.markdown('<h1 class="hero-title">QuickGuard AI</h1>', unsafe_allow_html=True)
st.markdown("<p style='text-align:center; color:#8892b0; margin-top:-15px;'>Where Advanced Security Blooms into Innovation 🌿</p>", unsafe_allow_html=True)

# --- SIDEBAR (JUDGE-READY) ---
with st.sidebar:
    st.markdown("### 🏆 Hackathon Dashboard")
    st.write("**Event:** CodeSpring 2026")
    st.write("**Track:** Cybersecurity / AI")
    st.success("Status: Ready to Audit")
    
    api_key = st.text_input("🔑 Enter Gemini API Key", type="password")
    st.markdown("---")
    st.info("💡 **Judge Note:** QuickGuard AI uses LLM heuristic analysis to identify real-time zero-day phishing threats.")

# --- MAIN INTERFACE ---
st.markdown('<div class="main-card">', unsafe_allow_html=True)

content = st.text_area("🔍 Hemant, Paste your URL or Code Snippet here:", 
                       placeholder="Enter any link or code to verify its safety score...", 
                       height=180)

if st.button("RUN SECURITY AUDIT 🚀"):
    if not api_key:
        st.error("⚠️ Hemant, please provide your API Key in the sidebar!")
    elif content:
        try:
            # Fixing the Error by using a safer model call and REST
            genai.configure(api_key=api_key, transport='rest')
            
            # Auto-selection of available models
            models = [m.name for m in genai.list_models() if 'generateContent' in m.supported_generation_methods]
            model_name = 'models/gemini-1.5-flash' if 'models/gemini-1.5-flash' in models else models[0]
            
            model = genai.GenerativeModel(model_name)
            
            with st.spinner(f'🌱 AI is scanning threat vectors using {model_name}...'):
                prompt = f"""
                You are a senior Cyber Security Analyst. 
                Perform a deep audit on this: {content}
                Provide:
                - RISK LEVEL (Low/Medium/High/Critical)
                - RISK SCORE (out of 10)
                - THREAT ANALYSIS
                - ACTIONABLE ADVICE FOR HEMANT
                """
                response = model.generate_content(prompt)
                
                st.success("✅ Audit Successfully Completed!")
                st.markdown('<div class="result-box">', unsafe_allow_html=True)
                st.markdown("### 📋 Final Security Report")
                st.write(response.text)
                st.markdown('</div>', unsafe_allow_html=True)
        except Exception as e:
            st.error(f"Execution Error: {str(e)}")
    else:
        st.warning("Please input some content to analyze, Hemant.")

st.markdown('</div>', unsafe_allow_html=True)

# --- FOOTER ---
st.markdown("""
    <br><br>
    <div style="text-align: center; color: #4b5563; font-size: 13px;">
        QuickGuard AI © 2026 | Built with ❤️ by <b>Hemant</b> for CodeSpring Hackathon
    </div>
""", unsafe_allow_html=True
