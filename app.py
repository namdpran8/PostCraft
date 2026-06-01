# Design Language: Apple Liquid Glass — Earthy Burgundy & Sage
# ──────────────────────────────────────────
# LinkedIn Post Generator — Streamlit App
# Palette: #7F2020 · #869B7E · #C9CAAC · #F6F3EB
# Fonts: Sacramento (cursive) + Cormorant Garamond (serif) + Plus Jakarta Sans (body)
# ──────────────────────────────────────────

import re
import streamlit as st

# ── Page Config (MUST be first st.* call) ─────────────
st.set_page_config(
    page_title="PostCraft — LinkedIn Post Generator",
    page_icon="✦",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        'Get Help': None,
        'Report a bug': None,
        'About': None
    }
)

# ── Inject Styles (immediately after page config) ─────
from styles import get_styles
st.markdown(get_styles(), unsafe_allow_html=True)

# ── Imports ────────────────────────────────────────────
from config import get_model
from prompt_builder import generate_post
from components import (
    app_header, section_label, badge, glass_divider,
    toast, custom_spinner, empty_state, post_output,
    metric_card, linkedin_preview_frame
)
from user_inputs import VALID_TONES, VALID_LENGHTS, VALID_FRAMEWORKS

# ═══════════════════════════════════════════════════════
#  SIDEBAR — Input Controls (frosted glass)
# ═══════════════════════════════════════════════════════
with st.sidebar:
    # ── Brand Mark ──
    st.markdown(
        '<div style="display:flex;align-items:center;gap:14px;margin-bottom:0.2rem;'
        'animation:fadeUp 0.5s cubic-bezier(0.34,1.56,0.64,1) both;">'
        # Logo badge — burgundy to sage gradient
        '<div style="width:40px;height:40px;border-radius:12px;'
        'background:linear-gradient(135deg,#7F2020,#869B7E);'
        'display:flex;align-items:center;justify-content:center;'
        'font-size:1.15rem;color:#F6F3EB;'
        'box-shadow:0 4px 18px rgba(127,32,32,0.25),'
        'inset 0 1px 0 rgba(246,243,235,0.1);">✦</div>'
        '<div>'
        # App name in cursive
        '<div style="font-family:var(--font-cursive);font-weight:400;font-size:1.8rem;'
        'color:var(--text-primary);line-height:1.1;">PostCraft</div>'
        '<div style="font-family:var(--font-body);font-size:0.62rem;'
        'color:var(--text-quaternary);text-transform:uppercase;'
        'letter-spacing:0.14em;font-weight:600;">LinkedIn AI Writer</div>'
        '</div>'
        '</div>',
        unsafe_allow_html=True
    )

    glass_divider()

    # ── Topic ──
    section_label("✧ Topic")
    topic = st.text_area(
        "What's your post about?",
        placeholder="e.g. How AI is transforming healthcare in 2026…",
        height=90,
        label_visibility="collapsed"
    )

    st.markdown("<div style='height:0.5rem;'></div>", unsafe_allow_html=True)

    # ── Tone ──
    section_label("✧ Tone")
    tone = st.selectbox(
        "Select tone",
        options=VALID_TONES,
        index=0,
        label_visibility="collapsed"
    )

    st.markdown("<div style='height:0.5rem;'></div>", unsafe_allow_html=True)

    # ── Target Audience ──
    section_label("✧ Target Audience")
    audience = st.text_input(
        "Who is this for?",
        placeholder="e.g. Tech professionals, startup founders…",
        label_visibility="collapsed"
    )

    st.markdown("<div style='height:0.5rem;'></div>", unsafe_allow_html=True)

    # ── Post Length ──
    section_label("✧ Length")
    length = st.radio(
        "Post length",
        options=VALID_LENGHTS,
        index=1,
        label_visibility="collapsed"
    )

    st.markdown("<div style='height:0.5rem;'></div>", unsafe_allow_html=True)

    # ── Framework ──
    section_label("✧ Framework")
    framework = st.selectbox(
        "Framework",
        options=VALID_FRAMEWORKS,
        index=0,
        label_visibility="collapsed"
    )

    glass_divider()

    # ── Generate Button ──
    generate_clicked = st.button("✦  Generate Post", use_container_width=True, type="primary")

    # ── Sidebar footer ──
    st.markdown(
        '<div style="margin-top:1.5rem;padding-top:1rem;'
        'border-top:1px solid rgba(246,243,235,0.04);text-align:center;">'
        '<div style="font-family:var(--font-cursive);font-size:1.1rem;'
        'color:var(--text-quaternary);opacity:0.5;">craft with care</div>'
        '</div>',
        unsafe_allow_html=True
    )


# ═══════════════════════════════════════════════════════
#  MAIN CONTENT AREA
# ═══════════════════════════════════════════════════════

# ── Header ──
app_header(
    "PostCraft",
    "AI-powered LinkedIn posts that sound like you — not a machine."
)

# ── Active Settings Summary (glass metric cards) ──
if topic:
    cols = st.columns([1, 1, 1, 1])
    with cols[0]:
        metric_card("Tone", tone)
    with cols[1]:
        length_short = length.split("(")[0].strip() if "(" in length else length
        metric_card("Length", length_short)
    with cols[2]:
        fw_short = framework.split("(")[0].strip() if "(" in framework else framework
        metric_card("Framework", fw_short)
    with cols[3]:
        word_est = "100–150" if "Short" in length else "200–300" if "Medium" in length else "400–500"
        metric_card("Est. Words", word_est)

    st.markdown("<div style='height:1.2rem;'></div>", unsafe_allow_html=True)

glass_divider()

# ═══════════════════════════════════════════════════════
#  POST GENERATION LOGIC
# ═══════════════════════════════════════════════════════

# Initialize session state
if "generated_post" not in st.session_state:
    st.session_state.generated_post = None
if "post_topic" not in st.session_state:
    st.session_state.post_topic = None

if generate_clicked:
    # Validation
    if not topic.strip():
        toast("Please enter a topic before generating.", variant="info")
    elif not audience.strip():
        toast("Please specify your target audience.", variant="info")
    else:
        # Build inputs dict
        inputs = {
            "topic": topic.strip(),
            "tone": tone,
            "audience": audience.strip(),
            "length": length,
            "framework": framework
        }

        # Show custom spinner while generating
        spinner_placeholder = st.empty()
        with spinner_placeholder.container():
            custom_spinner("Crafting your LinkedIn post…")

        try:
            model = get_model()
            post = generate_post(model, inputs)
            st.session_state.generated_post = post
            st.session_state.post_topic = topic.strip()
            spinner_placeholder.empty()
        except Exception as e:
            spinner_placeholder.empty()
            st.markdown(
                '<div class="toast toast-info" style="background:var(--danger-tonal);'
                f'color:var(--danger-text);border-color:rgba(127,32,32,0.15);">⚠ {str(e)}</div>',
                unsafe_allow_html=True
            )

# ═══════════════════════════════════════════════════════
#  DISPLAY RESULTS or EMPTY STATE
# ═══════════════════════════════════════════════════════

if st.session_state.generated_post:
    post = st.session_state.generated_post

    # ── Success Toast ──
    toast("Post generated successfully")
    st.markdown("<div style='height:0.8rem;'></div>", unsafe_allow_html=True)

    # ── View Modes ──
    tab_raw, tab_preview = st.tabs(["✎  Raw Output", "◉  LinkedIn Preview"])

    with tab_raw:
        st.markdown("<div style='height:0.5rem;'></div>", unsafe_allow_html=True)
        section_label("Generated Post")
        post_output(post)

    with tab_preview:
        st.markdown("<div style='height:0.5rem;'></div>", unsafe_allow_html=True)
        section_label("Preview — How it looks on LinkedIn")
        linkedin_preview_frame(post, author_name="You")

    st.markdown("<div style='height:1rem;'></div>", unsafe_allow_html=True)

    # ── Actions Row ──
    act_cols = st.columns([1, 1, 3])

    with act_cols[0]:
        safe_name = re.sub(r'[^a-zA-Z0-9_]', '_', (st.session_state.post_topic or "post").strip())
        filename = f"LINKEDIN_POST_{safe_name}.txt"
        st.download_button(
            label="⤓  Save as .txt",
            data=post,
            file_name=filename,
            mime="text/plain",
            use_container_width=True
        )

    with act_cols[1]:
        st.markdown('<div class="secondary-btn">', unsafe_allow_html=True)
        if st.button("↻  Regenerate", use_container_width=True):
            inputs = {
                "topic": topic.strip(),
                "tone": tone,
                "audience": audience.strip(),
                "length": length,
                "framework": framework
            }
            regen_placeholder = st.empty()
            with regen_placeholder.container():
                custom_spinner("Regenerating…")
            try:
                model = get_model()
                new_post = generate_post(model, inputs)
                st.session_state.generated_post = new_post
                st.session_state.post_topic = topic.strip()
                regen_placeholder.empty()
                st.rerun()
            except Exception as e:
                regen_placeholder.empty()
                st.markdown(
                    '<div class="toast toast-info" style="background:var(--danger-tonal);'
                    f'color:var(--danger-text);border-color:rgba(127,32,32,0.15);">⚠ {str(e)}</div>',
                    unsafe_allow_html=True
                )
        st.markdown('</div>', unsafe_allow_html=True)

    # ── Word / Character Count ──
    st.markdown("<div style='height:1rem;'></div>", unsafe_allow_html=True)
    word_count = len(post.split())
    char_count = len(post)
    st.markdown(
        '<div style="display:flex;gap:12px;justify-content:flex-start;flex-wrap:wrap;">'
        f'<span class="badge badge-neutral">⌗ {word_count} words</span>'
        f'<span class="badge badge-neutral">⌘ {char_count} characters</span>'
        '<span class="badge badge-accent">✦ Powered by Gemini</span>'
        '</div>',
        unsafe_allow_html=True
    )

else:
    # ── Empty State ──
    empty_state(
        icon="◇",
        title="Your next great post starts here",
        subtitle="Fill in your topic, audience, and preferences in the sidebar — then hit Generate to craft a LinkedIn post with AI."
    )

# ── Footer ──
st.markdown("<div style='height:2rem;'></div>", unsafe_allow_html=True)
st.markdown(
    '<div style="text-align:center;padding:1rem 0 2rem 0;">'
    '<span style="font-family:var(--font-cursive);font-size:1.3rem;'
    'color:var(--text-quaternary);opacity:0.4;">PostCraft</span>'
    '<span style="font-family:var(--font-body);font-size:0.7rem;'
    'color:var(--text-quaternary);opacity:0.3;margin-left:12px;'
    'letter-spacing:0.05em;">Built with Streamlit & Gemini · 2026</span>'
    '</div>',
    unsafe_allow_html=True
)
