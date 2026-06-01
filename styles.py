# Design Language: Apple Liquid Glass — Earthy Burgundy & Sage
# ──────────────────────────────────────────
# Palette: #7F2020 · #869B7E · #C9CAAC · #F6F3EB
# Fonts: Sacramento (cursive hero) + Cormorant Garamond (serif headings) + Plus Jakarta Sans (body)
# ──────────────────────────────────────────

def get_styles() -> str:
    """Return the complete CSS design system."""
    return """
    <style>
    /* ═══════════════════════════════════════════
       FONTS — Cursive + Serif + Sans Triple
       Hero:     Sacramento (elegant script cursive)
       Heading:  Cormorant Garamond (refined serif)
       Body:     Plus Jakarta Sans (modern geometric)
       ═══════════════════════════════════════════ */
    @import url('https://fonts.googleapis.com/css2?family=Sacramento&family=Cormorant+Garamond:ital,wght@0,400;0,500;0,600;0,700;1,400;1,500;1,600&family=Plus+Jakarta+Sans:ital,wght@0,300;0,400;0,500;0,600;0,700;0,800;1,400&display=swap');

    /* ═══════════════════════════════════════════
       CSS CUSTOM PROPERTIES
       ═══════════════════════════════════════════ */
    :root {
        /* Palette */
        --burgundy: #7F2020;
        --burgundy-light: #A03030;
        --burgundy-dim: #5E1818;
        --burgundy-soft: rgba(127, 32, 32, 0.15);
        --burgundy-glow: rgba(127, 32, 32, 0.25);
        --burgundy-glow-strong: rgba(160, 48, 48, 0.35);

        --sage: #869B7E;
        --sage-light: #A0B598;
        --sage-dim: #6A7E63;
        --sage-soft: rgba(134, 155, 126, 0.15);

        --khaki: #C9CAAC;
        --khaki-dim: #A8A98E;

        --cream: #F6F3EB;
        --cream-dim: #E8E4DA;

        /* Dark backgrounds — warm-tinted */
        --bg-deep: #0C0A09;
        --bg-primary: #131110;
        --bg-elevated: #1C1917;
        --bg-surface: #242120;
        --bg-surface-hover: #2E2A28;

        /* Glassmorphism */
        --glass-bg: rgba(20, 18, 16, 0.5);
        --glass-bg-hover: rgba(30, 27, 24, 0.65);
        --glass-border: rgba(246, 243, 235, 0.06);
        --glass-border-hover: rgba(246, 243, 235, 0.1);
        --glass-border-active: rgba(134, 155, 126, 0.2);
        --glass-shadow: 0 8px 32px rgba(0, 0, 0, 0.4);
        --glass-shadow-hover: 0 16px 52px rgba(0, 0, 0, 0.55);
        --glass-shadow-glow: 0 8px 40px rgba(127, 32, 32, 0.08);
        --glass-blur: blur(28px) saturate(160%);
        --glass-blur-heavy: blur(48px) saturate(200%);
        --glass-inner-glow: inset 0 1px 0 rgba(246, 243, 235, 0.04);
        --glass-inner-glow-strong: inset 0 1px 1px rgba(246, 243, 235, 0.06), inset 0 -1px 1px rgba(0, 0, 0, 0.15);
        --glass-highlight: linear-gradient(135deg, rgba(246, 243, 235, 0.03) 0%, transparent 50%, rgba(134, 155, 126, 0.02) 100%);

        /* Text — warm cream scale */
        --text-primary: #F6F3EB;
        --text-secondary: #C9CAAC;
        --text-tertiary: #918D82;
        --text-quaternary: #6B675E;
        --text-on-accent: #F6F3EB;

        /* Semantic */
        --success-tonal: rgba(134, 155, 126, 0.15);
        --success-text: #A0B598;
        --danger-tonal: rgba(127, 32, 32, 0.15);
        --danger-text: #C05050;

        /* Radii */
        --radius-sm: 10px;
        --radius-md: 14px;
        --radius-lg: 20px;
        --radius-xl: 24px;
        --radius-2xl: 32px;

        /* Motion */
        --spring: cubic-bezier(0.34, 1.56, 0.64, 1);
        --ease-out: cubic-bezier(0.25, 0.46, 0.45, 0.94);
        --ease-smooth: cubic-bezier(0.4, 0, 0.2, 1);
        --ease-expressive: cubic-bezier(0.2, 0, 0, 1.0);

        /* Fonts */
        --font-cursive: 'Sacramento', cursive;
        --font-serif: 'Cormorant Garamond', Georgia, serif;
        --font-body: 'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, sans-serif;
    }

    /* ═══════════════════════════════════════════
       GLOBAL RESETS
       ═══════════════════════════════════════════ */
    *, *::before, *::after { color-scheme: dark !important; }

    /* ═══════════════════════════════════════════
       KEYFRAME ANIMATIONS
       ═══════════════════════════════════════════ */
    @keyframes fadeUp {
        0%   { transform: translateY(24px); opacity: 0; }
        100% { transform: translateY(0); opacity: 1; }
    }
    @keyframes fadeUpSlow {
        0%   { transform: translateY(36px); opacity: 0; }
        100% { transform: translateY(0); opacity: 1; }
    }
    @keyframes fadeIn {
        0%   { opacity: 0; }
        100% { opacity: 1; }
    }
    @keyframes slideRight {
        0%   { transform: translateX(-20px); opacity: 0; }
        100% { transform: translateX(0); opacity: 1; }
    }
    @keyframes slideLeft {
        0%   { transform: translateX(20px); opacity: 0; }
        100% { transform: translateX(0); opacity: 1; }
    }
    @keyframes float {
        0%, 100% { transform: translateY(0px); }
        50%      { transform: translateY(-10px); }
    }
    @keyframes floatSlow {
        0%, 100% { transform: translateY(0) rotate(0deg); }
        25%      { transform: translateY(-6px) rotate(0.5deg); }
        50%      { transform: translateY(-4px) rotate(-0.3deg); }
        75%      { transform: translateY(-8px) rotate(0.2deg); }
    }
    @keyframes breathe {
        0%, 100% { opacity: 0.12; transform: scale(1); }
        50%      { opacity: 0.2; transform: scale(1.08); }
    }
    @keyframes breatheSage {
        0%, 100% { opacity: 0.08; transform: scale(1) translate(0, 0); }
        50%      { opacity: 0.15; transform: scale(1.05) translate(5px, -5px); }
    }
    @keyframes glowPulse {
        0%, 100% { box-shadow: 0 0 20px rgba(127, 32, 32, 0.04); }
        50%      { box-shadow: 0 0 45px rgba(127, 32, 32, 0.1); }
    }
    @keyframes borderGlow {
        0%, 100% { border-color: rgba(246, 243, 235, 0.05); }
        50%      { border-color: rgba(134, 155, 126, 0.12); }
    }
    @keyframes shimmer {
        0%   { background-position: -200% 0; }
        100% { background-position: 200% 0; }
    }
    @keyframes spin {
        0%   { transform: rotate(0deg); }
        100% { transform: rotate(360deg); }
    }
    @keyframes pulse {
        0%, 100% { opacity: 0.35; }
        50%      { opacity: 1; }
    }
    @keyframes toastIn {
        0%   { transform: translateY(14px) scale(0.92); opacity: 0; }
        100% { transform: translateY(0) scale(1); opacity: 1; }
    }
    @keyframes scaleIn {
        0%   { transform: scale(0.9); opacity: 0; }
        100% { transform: scale(1); opacity: 1; }
    }
    @keyframes wobble {
        0%, 100% { transform: rotate(0deg); }
        25%      { transform: rotate(1deg); }
        75%      { transform: rotate(-1deg); }
    }
    @keyframes gradientShift {
        0%   { background-position: 0% 50%; }
        50%  { background-position: 100% 50%; }
        100% { background-position: 0% 50%; }
    }

    /* ═══════════════════════════════════════════
       ROOT APP
       ═══════════════════════════════════════════ */
    .stApp {
        background: var(--bg-deep) !important;
        font-family: var(--font-body) !important;
        color: var(--text-primary) !important;
    }

    /* Three ambient glow orbs — burgundy, sage, and warm */
    .stApp::before {
        content: '';
        position: fixed;
        top: -18%;
        right: -12%;
        width: 700px;
        height: 700px;
        background: radial-gradient(ellipse, rgba(127, 32, 32, 0.06) 0%, transparent 55%);
        border-radius: 50%;
        pointer-events: none;
        z-index: 0;
        animation: breathe 10s ease-in-out infinite;
    }
    .stApp::after {
        content: '';
        position: fixed;
        bottom: -12%;
        left: -8%;
        width: 600px;
        height: 600px;
        background: radial-gradient(ellipse, rgba(134, 155, 126, 0.05) 0%, transparent 55%);
        border-radius: 50%;
        pointer-events: none;
        z-index: 0;
        animation: breatheSage 12s ease-in-out 3s infinite;
    }

    /* ═══════════════════════════════════════════
       TEXT COLORS — Global
       ═══════════════════════════════════════════ */
    .stApp p, .stApp span, .stApp li, .stApp div, .stApp label {
        color: var(--text-primary) !important;
        font-family: var(--font-body) !important;
    }
    .stMarkdown p { color: var(--text-primary) !important; }

    /* ═══════════════════════════════════════════
       HIDE "keyboard_double_arrow" COLLAPSE TEXT
       Nuclear approach — hide ALL sidebar collapse UI text
       ═══════════════════════════════════════════ */
    /* Hide the expand button when sidebar is collapsed */
    [data-testid="collapsedControl"] {
        background: var(--bg-elevated) !important;
        border: 1px solid var(--glass-border) !important;
        border-radius: 0 10px 10px 0 !important;
        overflow: hidden !important;
    }
    [data-testid="collapsedControl"] span,
    [data-testid="collapsedControl"] button span {
        font-size: 0 !important;
        color: transparent !important;
        width: 0 !important;
        overflow: hidden !important;
    }

    /* Hide the collapse arrow inside sidebar */
    section[data-testid="stSidebar"] [data-testid="stSidebarCollapseButton"],
    section[data-testid="stSidebar"] button[kind="header"],
    section[data-testid="stSidebar"] button[kind="headerNoPadding"] {
        position: absolute !important;
        top: 8px !important;
        right: 8px !important;
        width: 32px !important;
        height: 32px !important;
        min-height: 0 !important;
        padding: 0 !important;
        font-size: 0 !important;
        color: transparent !important;
        background: rgba(246, 243, 235, 0.04) !important;
        border: 1px solid rgba(246, 243, 235, 0.06) !important;
        border-radius: 8px !important;
        backdrop-filter: blur(12px) !important;
        overflow: hidden !important;
        z-index: 100 !important;
        opacity: 0.4 !important;
        transition: opacity 0.3s ease !important;
    }
    section[data-testid="stSidebar"] [data-testid="stSidebarCollapseButton"]:hover,
    section[data-testid="stSidebar"] button[kind="header"]:hover,
    section[data-testid="stSidebar"] button[kind="headerNoPadding"]:hover {
        opacity: 0.7 !important;
    }
    /* Hide ALL text children of the collapse button */
    section[data-testid="stSidebar"] [data-testid="stSidebarCollapseButton"] *,
    section[data-testid="stSidebar"] button[kind="header"] *,
    section[data-testid="stSidebar"] button[kind="headerNoPadding"] * {
        font-size: 0 !important;
        color: transparent !important;
        line-height: 0 !important;
    }
    /* But show SVG icons at normal size */
    section[data-testid="stSidebar"] [data-testid="stSidebarCollapseButton"] svg,
    section[data-testid="stSidebar"] button[kind="header"] svg,
    section[data-testid="stSidebar"] button[kind="headerNoPadding"] svg {
        width: 16px !important;
        height: 16px !important;
        color: var(--text-tertiary) !important;
        opacity: 0.7 !important;
    }

    /* ═══════════════════════════════════════════
       SIDEBAR — Deep frosted glass
       ═══════════════════════════════════════════ */
    section[data-testid="stSidebar"] {
        background: rgba(16, 14, 13, 0.88) !important;
        backdrop-filter: var(--glass-blur-heavy) !important;
        -webkit-backdrop-filter: var(--glass-blur-heavy) !important;
        border-right: 1px solid rgba(246, 243, 235, 0.04) !important;
        box-shadow: 2px 0 40px rgba(0, 0, 0, 0.5) !important;
    }
    section[data-testid="stSidebar"] > div {
        padding-top: 2.5rem !important;
        background: transparent !important;
    }
    section[data-testid="stSidebar"] > div > div {
        background: transparent !important;
    }
    section[data-testid="stSidebar"] p,
    section[data-testid="stSidebar"] span,
    section[data-testid="stSidebar"] label,
    section[data-testid="stSidebar"] div {
        color: var(--text-primary) !important;
    }
    section[data-testid="stSidebar"] h1,
    section[data-testid="stSidebar"] h2,
    section[data-testid="stSidebar"] h3 {
        font-family: var(--font-serif) !important;
        color: var(--text-primary) !important;
    }
    section[data-testid="stSidebar"] .stRadio > label,
    section[data-testid="stSidebar"] .stSelectbox > label,
    section[data-testid="stSidebar"] .stTextInput > label,
    section[data-testid="stSidebar"] .stTextArea > label {
        font-family: var(--font-body) !important;
        font-weight: 600 !important;
        font-size: 0.7rem !important;
        color: var(--text-tertiary) !important;
        text-transform: uppercase !important;
        letter-spacing: 0.1em !important;
    }

    /* ═══════════════════════════════════════════
       TYPOGRAPHY
       ═══════════════════════════════════════════ */
    h1 {
        font-family: var(--font-cursive) !important;
        font-weight: 400 !important;
        font-size: 4rem !important;
        color: var(--text-primary) !important;
        letter-spacing: 0.01em !important;
        line-height: 1.1 !important;
    }
    h2 {
        font-family: var(--font-serif) !important;
        font-weight: 600 !important;
        font-size: 1.6rem !important;
        color: var(--text-primary) !important;
        letter-spacing: -0.015em !important;
        font-style: italic !important;
    }
    h3 {
        font-family: var(--font-serif) !important;
        font-weight: 500 !important;
        font-size: 1.15rem !important;
        color: var(--text-secondary) !important;
        font-style: italic !important;
    }

    /* ═══════════════════════════════════════════
       BUTTONS — Burgundy with glass
       ═══════════════════════════════════════════ */
    .stButton > button {
        font-family: var(--font-body) !important;
        font-weight: 600 !important;
        font-size: 0.85rem !important;
        letter-spacing: 0.03em !important;
        min-height: 44px !important;
        padding: 10px 28px !important;
        border-radius: 50px !important;
        border: none !important;
        background: linear-gradient(135deg, var(--burgundy) 0%, var(--burgundy-light) 100%) !important;
        color: var(--text-on-accent) !important;
        box-shadow: 0 4px 20px var(--burgundy-glow), var(--glass-inner-glow) !important;
        transition: all 0.4s var(--spring) !important;
        cursor: pointer !important;
        position: relative !important;
        overflow: hidden !important;
    }
    /* Shimmer sweep on hover */
    .stButton > button::before {
        content: '';
        position: absolute;
        top: 0; left: -100%; width: 100%; height: 100%;
        background: linear-gradient(90deg, transparent, rgba(246,243,235,0.18), transparent);
        transition: left 0.6s var(--ease-smooth);
    }
    .stButton > button:hover::before { left: 100%; }
    .stButton > button:hover {
        background: linear-gradient(135deg, var(--burgundy-light) 0%, var(--burgundy) 100%) !important;
        transform: scale(1.04) translateY(-2px) !important;
        box-shadow: 0 10px 35px var(--burgundy-glow-strong), var(--glass-inner-glow) !important;
        color: var(--text-on-accent) !important;
    }
    .stButton > button:active {
        transform: scale(0.97) !important;
        transition-duration: 0.1s !important;
    }

    /* Secondary */
    .secondary-btn .stButton > button {
        background: transparent !important;
        color: var(--burgundy-light) !important;
        border: 1.5px solid rgba(127, 32, 32, 0.4) !important;
        box-shadow: none !important;
    }
    .secondary-btn .stButton > button::before { display: none; }
    .secondary-btn .stButton > button:hover {
        background: var(--burgundy-soft) !important;
        color: var(--cream) !important;
        border-color: var(--burgundy) !important;
        box-shadow: 0 0 25px rgba(127, 32, 32, 0.1) !important;
        transform: scale(1.02) translateY(-1px) !important;
    }

    /* Download */
    .stDownloadButton > button {
        font-family: var(--font-body) !important;
        font-weight: 600 !important;
        font-size: 0.82rem !important;
        min-height: 44px !important;
        padding: 10px 24px !important;
        border-radius: 50px !important;
        border: 1.5px solid rgba(134, 155, 126, 0.35) !important;
        background: var(--sage-soft) !important;
        color: var(--sage-light) !important;
        transition: all 0.4s var(--spring) !important;
        backdrop-filter: blur(12px) !important;
    }
    .stDownloadButton > button:hover {
        background: rgba(134, 155, 126, 0.22) !important;
        color: var(--cream) !important;
        transform: scale(1.03) translateY(-1px) !important;
        box-shadow: 0 4px 22px rgba(134, 155, 126, 0.15) !important;
    }

    /* ═══════════════════════════════════════════
       TEXT INPUTS — Frosted glass
       ═══════════════════════════════════════════ */
    .stTextInput > div > div > input,
    .stTextArea textarea {
        font-family: var(--font-body) !important;
        font-size: 0.92rem !important;
        color: var(--text-primary) !important;
        background: rgba(246, 243, 235, 0.03) !important;
        backdrop-filter: blur(16px) saturate(140%) !important;
        -webkit-backdrop-filter: blur(16px) saturate(140%) !important;
        border: 1.5px solid rgba(246, 243, 235, 0.07) !important;
        border-radius: 14px !important;
        padding: 12px 16px !important;
        transition: all 0.35s var(--ease-smooth) !important;
        caret-color: var(--sage) !important;
    }
    .stTextInput > div > div > input:focus,
    .stTextArea textarea:focus {
        border-color: rgba(134, 155, 126, 0.35) !important;
        box-shadow: 0 0 0 3px rgba(134, 155, 126, 0.12), 0 0 25px rgba(134, 155, 126, 0.05) !important;
        background: rgba(246, 243, 235, 0.05) !important;
    }
    .stTextInput > div > div > input::placeholder,
    .stTextArea textarea::placeholder {
        color: var(--text-quaternary) !important;
        opacity: 0.75 !important;
    }
    .stTextInput > label, .stTextArea > label {
        font-family: var(--font-body) !important;
        font-weight: 600 !important;
        font-size: 0.7rem !important;
        color: var(--text-tertiary) !important;
        text-transform: uppercase !important;
        letter-spacing: 0.1em !important;
    }

    /* ═══════════════════════════════════════════
       SELECTS — Frosted glass dropdown
       ═══════════════════════════════════════════ */
    .stSelectbox > label {
        font-family: var(--font-body) !important;
        font-weight: 600 !important;
        font-size: 0.7rem !important;
        color: var(--text-tertiary) !important;
        text-transform: uppercase !important;
        letter-spacing: 0.1em !important;
    }
    .stSelectbox [data-baseweb="select"] { background: transparent !important; }
    .stSelectbox > div > div,
    .stSelectbox [data-baseweb="select"] > div {
        background: rgba(246, 243, 235, 0.03) !important;
        backdrop-filter: blur(16px) !important;
        border: 1.5px solid rgba(246, 243, 235, 0.07) !important;
        border-radius: 14px !important;
        color: var(--text-primary) !important;
        font-family: var(--font-body) !important;
        transition: all 0.35s var(--ease-smooth) !important;
    }
    .stSelectbox > div > div:hover,
    .stSelectbox > div > div:focus-within {
        border-color: rgba(134, 155, 126, 0.3) !important;
        box-shadow: 0 0 0 3px rgba(134, 155, 126, 0.1) !important;
    }
    .stSelectbox [data-baseweb="select"] span,
    .stSelectbox [data-baseweb="select"] div { color: var(--text-primary) !important; }

    /* Popover menu — heavy frosted glass */
    [data-baseweb="popover"], [data-baseweb="menu"], ul[role="listbox"] {
        background: rgba(18, 16, 15, 0.9) !important;
        backdrop-filter: blur(50px) saturate(200%) !important;
        -webkit-backdrop-filter: blur(50px) saturate(200%) !important;
        border: 1px solid rgba(246, 243, 235, 0.07) !important;
        border-radius: 18px !important;
        box-shadow: 0 24px 64px rgba(0, 0, 0, 0.65), inset 0 1px 0 rgba(246, 243, 235, 0.03) !important;
        padding: 6px !important;
    }
    [data-baseweb="menu"] li, ul[role="listbox"] li {
        color: var(--text-primary) !important;
        font-family: var(--font-body) !important;
        background: transparent !important;
        border-radius: 12px !important;
        margin: 2px 0 !important;
        transition: all 0.25s ease !important;
    }
    [data-baseweb="menu"] li:hover, ul[role="listbox"] li:hover {
        background: var(--sage-soft) !important;
        color: var(--sage-light) !important;
    }
    [data-baseweb="menu"] li[aria-selected="true"], ul[role="listbox"] li[aria-selected="true"] {
        background: var(--sage-soft) !important;
        color: var(--sage) !important;
    }

    /* ═══════════════════════════════════════════
       RADIO BUTTONS
       ═══════════════════════════════════════════ */
    .stRadio > label {
        font-family: var(--font-body) !important;
        font-weight: 600 !important;
        font-size: 0.7rem !important;
        color: var(--text-tertiary) !important;
        text-transform: uppercase !important;
        letter-spacing: 0.1em !important;
    }
    .stRadio > div { gap: 0.2rem !important; }
    .stRadio > div > label {
        font-family: var(--font-body) !important;
        font-weight: 400 !important;
        font-size: 0.88rem !important;
        color: var(--text-secondary) !important;
        padding: 9px 14px !important;
        border-radius: 12px !important;
        transition: all 0.3s var(--ease-smooth) !important;
        text-transform: none !important;
        letter-spacing: 0 !important;
        background: transparent !important;
        border: 1px solid transparent !important;
    }
    .stRadio > div > label:hover {
        background: rgba(134, 155, 126, 0.06) !important;
        color: var(--text-primary) !important;
        border-color: rgba(246, 243, 235, 0.04) !important;
    }
    .stRadio > div > label > div[data-testid="stMarkdownContainer"] {
        color: var(--text-secondary) !important;
    }
    .stRadio input[type="radio"]:checked + div,
    .stRadio > div > label[data-checked="true"],
    .stRadio > div > label[aria-checked="true"] {
        background: var(--sage-soft) !important;
        color: var(--sage-light) !important;
        font-weight: 500 !important;
        border-color: rgba(134, 155, 126, 0.2) !important;
        box-shadow: 0 0 16px rgba(134, 155, 126, 0.06) !important;
    }
    .stRadio [role="radiogroup"] label div:first-child {
        border-color: var(--text-quaternary) !important;
    }

    /* ═══════════════════════════════════════════
       TABS
       ═══════════════════════════════════════════ */
    .stTabs [data-baseweb="tab-list"] {
        background: transparent !important;
        border-bottom: 1px solid rgba(246, 243, 235, 0.05) !important;
    }
    .stTabs [data-baseweb="tab"] {
        font-family: var(--font-serif) !important;
        font-weight: 500 !important;
        font-size: 0.92rem !important;
        font-style: italic !important;
        color: var(--text-tertiary) !important;
        background: transparent !important;
        border-bottom: 2px solid transparent !important;
        padding: 10px 24px !important;
        transition: all 0.3s var(--ease-smooth) !important;
    }
    .stTabs [data-baseweb="tab"]:hover {
        color: var(--text-primary) !important;
        background: rgba(246, 243, 235, 0.02) !important;
    }
    .stTabs [aria-selected="true"] {
        color: var(--sage) !important;
        border-bottom-color: var(--sage) !important;
        font-weight: 600 !important;
    }
    .stTabs [data-baseweb="tab-highlight"] { background-color: var(--sage) !important; }
    .stTabs [data-baseweb="tab-panel"] { background: transparent !important; }

    /* ═══════════════════════════════════════════
       GLASS CARD — Liquid glass with warm tint
       ═══════════════════════════════════════════ */
    .glass-card {
        background: var(--glass-bg);
        backdrop-filter: var(--glass-blur);
        -webkit-backdrop-filter: var(--glass-blur);
        border: 1px solid var(--glass-border);
        border-radius: var(--radius-2xl);
        padding: 2rem 2.2rem;
        box-shadow: var(--glass-shadow), var(--glass-inner-glow-strong);
        transition: all 0.45s var(--spring);
        position: relative;
        overflow: hidden;
        animation: glowPulse 8s ease-in-out infinite, borderGlow 6s ease-in-out infinite;
    }
    /* Top edge shine */
    .glass-card::before {
        content: '';
        position: absolute;
        top: 0; left: 0; right: 0;
        height: 1px;
        background: linear-gradient(90deg, transparent 5%, rgba(134, 155, 126, 0.15) 30%, rgba(246, 243, 235, 0.08) 50%, rgba(127, 32, 32, 0.12) 70%, transparent 95%);
    }
    /* Internal gradient overlay */
    .glass-card::after {
        content: '';
        position: absolute;
        top: 0; left: 0;
        width: 100%; height: 100%;
        background: var(--glass-highlight);
        pointer-events: none;
        border-radius: inherit;
    }
    .glass-card:hover {
        box-shadow: var(--glass-shadow-hover), var(--glass-shadow-glow), var(--glass-inner-glow-strong);
        border-color: var(--glass-border-hover);
        background: var(--glass-bg-hover);
        transform: translateY(-3px);
    }

    /* Compact */
    .glass-card-compact {
        background: var(--glass-bg);
        backdrop-filter: var(--glass-blur);
        -webkit-backdrop-filter: var(--glass-blur);
        border: 1px solid var(--glass-border);
        border-radius: var(--radius-xl);
        padding: 1.4rem 1.6rem;
        box-shadow: var(--glass-shadow), var(--glass-inner-glow);
        transition: all 0.45s var(--spring);
        position: relative;
        overflow: hidden;
        animation: borderGlow 7s ease-in-out 1s infinite;
    }
    .glass-card-compact::before {
        content: '';
        position: absolute;
        top: 0; left: 0; right: 0;
        height: 1px;
        background: linear-gradient(90deg, transparent, rgba(246, 243, 235, 0.05), transparent);
    }
    .glass-card-compact::after {
        content: '';
        position: absolute;
        top: 0; left: 0;
        width: 100%; height: 100%;
        background: var(--glass-highlight);
        pointer-events: none;
        border-radius: inherit;
    }
    .glass-card-compact:hover {
        transform: translateY(-3px);
        border-color: var(--glass-border-hover);
        box-shadow: var(--glass-shadow-hover), var(--glass-inner-glow-strong);
    }

    /* ═══════════════════════════════════════════
       METRICS
       ═══════════════════════════════════════════ */
    div[data-testid="stMetricValue"] {
        font-family: var(--font-serif) !important;
        font-weight: 700 !important;
        font-size: 2.2rem !important;
        color: var(--text-primary) !important;
    }
    div[data-testid="stMetricLabel"] {
        font-family: var(--font-body) !important;
        font-weight: 600 !important;
        font-size: 0.68rem !important;
        text-transform: uppercase !important;
        letter-spacing: 0.12em !important;
        color: var(--text-quaternary) !important;
    }

    /* ═══════════════════════════════════════════
       CUSTOM SPINNER
       ═══════════════════════════════════════════ */
    .custom-spinner-overlay {
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        padding: 4rem 2rem;
        gap: 1.5rem;
    }
    .custom-spinner-ring {
        width: 50px; height: 50px;
        border: 3px solid rgba(246, 243, 235, 0.05);
        border-top-color: var(--burgundy);
        border-right-color: var(--sage-dim);
        border-radius: 50%;
        animation: spin 0.85s ease-in-out infinite;
        box-shadow: 0 0 25px rgba(127, 32, 32, 0.1);
    }
    .custom-spinner-text {
        font-family: var(--font-serif);
        font-size: 0.92rem;
        font-weight: 500;
        font-style: italic;
        color: var(--text-tertiary);
        letter-spacing: 0.02em;
        animation: pulse 2s ease-in-out infinite;
    }

    /* ═══════════════════════════════════════════
       EMPTY STATE (base classes for the iframe)
       ═══════════════════════════════════════════ */
    .empty-state-container {
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        padding: 5rem 2rem;
        text-align: center;
    }

    /* ═══════════════════════════════════════════
       POST OUTPUT — Liquid glass
       ═══════════════════════════════════════════ */
    .post-output-container {
        background: rgba(20, 18, 16, 0.55);
        backdrop-filter: var(--glass-blur);
        -webkit-backdrop-filter: var(--glass-blur);
        border: 1px solid rgba(246, 243, 235, 0.06);
        border-radius: var(--radius-2xl);
        padding: 2.2rem 2.6rem;
        font-family: var(--font-body);
        font-size: 0.95rem;
        line-height: 1.85;
        color: var(--text-primary);
        white-space: pre-wrap;
        box-shadow: var(--glass-shadow), var(--glass-inner-glow-strong);
        position: relative;
        overflow: hidden;
        animation: fadeUp 0.5s var(--spring) 0.1s both;
    }
    .post-output-container::before {
        content: '';
        position: absolute;
        top: 0; left: 0; right: 0;
        height: 1px;
        background: linear-gradient(90deg, transparent, rgba(134, 155, 126, 0.12), rgba(127, 32, 32, 0.08), transparent);
    }
    .post-output-container::after {
        content: '';
        position: absolute;
        bottom: 0; left: 0; right: 0;
        height: 1px;
        background: linear-gradient(90deg, transparent, rgba(246, 243, 235, 0.03), transparent);
    }

    /* ═══════════════════════════════════════════
       BADGES — Glassmorphic
       ═══════════════════════════════════════════ */
    .badge {
        display: inline-flex;
        align-items: center;
        gap: 5px;
        padding: 5px 14px;
        border-radius: 50px;
        font-family: var(--font-body);
        font-size: 0.72rem;
        font-weight: 600;
        letter-spacing: 0.03em;
        backdrop-filter: blur(12px);
        transition: all 0.3s ease;
    }
    .badge-accent {
        background: var(--burgundy-soft);
        color: var(--burgundy-light);
        border: 1px solid rgba(127, 32, 32, 0.12);
    }
    .badge-success {
        background: var(--success-tonal);
        color: var(--success-text);
        border: 1px solid rgba(134, 155, 126, 0.08);
    }
    .badge-neutral {
        background: rgba(246, 243, 235, 0.04);
        color: var(--text-tertiary);
        border: 1px solid rgba(246, 243, 235, 0.04);
    }

    /* ═══════════════════════════════════════════
       DIVIDER
       ═══════════════════════════════════════════ */
    .glass-divider {
        height: 1px;
        background: linear-gradient(90deg, transparent, rgba(134, 155, 126, 0.1), rgba(127, 32, 32, 0.06), transparent);
        margin: 1.5rem 0;
        border: none;
    }

    /* ═══════════════════════════════════════════
       APP HEADER
       ═══════════════════════════════════════════ */
    .app-header {
        padding: 2rem 0 1rem 0;
        margin-bottom: 0.5rem;
        animation: fadeUp 0.6s var(--spring) both;
    }
    .app-header h1 {
        background: linear-gradient(135deg, var(--cream) 0%, var(--sage-light) 40%, var(--khaki) 70%, var(--cream-dim) 100%);
        background-size: 300% 300%;
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        animation: gradientShift 8s ease-in-out infinite;
    }
    .app-header-subtitle {
        font-family: var(--font-serif);
        font-size: 1.05rem;
        font-weight: 400;
        font-style: italic;
        color: var(--text-tertiary);
        margin-top: 0.35rem;
        letter-spacing: 0.01em;
        animation: fadeIn 1s ease 0.4s both;
    }

    /* ═══════════════════════════════════════════
       TOAST
       ═══════════════════════════════════════════ */
    .toast {
        display: inline-flex;
        align-items: center;
        gap: 8px;
        padding: 10px 22px;
        border-radius: 50px;
        font-family: var(--font-body);
        font-size: 0.82rem;
        font-weight: 500;
        letter-spacing: 0.01em;
        animation: toastIn 0.5s var(--spring);
        backdrop-filter: blur(20px);
    }
    .toast-success {
        background: var(--success-tonal);
        color: var(--success-text);
        border: 1px solid rgba(134, 155, 126, 0.1);
    }
    .toast-info {
        background: var(--burgundy-soft);
        color: var(--burgundy-light);
        border: 1px solid rgba(127, 32, 32, 0.1);
    }

    /* ═══════════════════════════════════════════
       SECTION LABEL
       ═══════════════════════════════════════════ */
    .section-label {
        font-family: var(--font-body);
        font-size: 0.66rem;
        font-weight: 700;
        text-transform: uppercase;
        letter-spacing: 0.14em;
        color: var(--text-quaternary);
        margin-bottom: 0.8rem;
        padding-left: 2px;
        animation: slideRight 0.4s var(--ease-smooth) both;
    }

    /* ═══════════════════════════════════════════
       HIDE STREAMLIT CHROME
       ═══════════════════════════════════════════ */
    #MainMenu { visibility: hidden; }
    header[data-testid="stHeader"] {
        background: rgba(12, 10, 9, 0.7) !important;
        backdrop-filter: blur(28px) saturate(160%) !important;
        border-bottom: 1px solid rgba(246, 243, 235, 0.03) !important;
    }
    footer { visibility: hidden; }
    .stDeployButton { visibility: hidden; }
    div[data-testid="stAppViewBlockContainer"] { background: transparent !important; }
    .stSpinner > div { border-color: var(--burgundy) transparent transparent transparent !important; }

    /* ═══════════════════════════════════════════
       SCROLLBAR
       ═══════════════════════════════════════════ */
    ::-webkit-scrollbar { width: 4px; height: 4px; }
    ::-webkit-scrollbar-track { background: transparent; }
    ::-webkit-scrollbar-thumb {
        background: rgba(246, 243, 235, 0.07);
        border-radius: 10px;
    }
    ::-webkit-scrollbar-thumb:hover { background: rgba(246, 243, 235, 0.13); }

    /* ═══════════════════════════════════════════
       EXPANDER
       ═══════════════════════════════════════════ */
    .streamlit-expanderHeader {
        font-family: var(--font-serif) !important;
        font-weight: 600 !important;
        font-style: italic !important;
        color: var(--text-secondary) !important;
        background: transparent !important;
    }
    details {
        border: 1px solid rgba(246, 243, 235, 0.04) !important;
        border-radius: var(--radius-md) !important;
        background: var(--bg-elevated) !important;
    }

    /* ═══════════════════════════════════════════
       ANIMATION UTILITY CLASSES
       ═══════════════════════════════════════════ */
    .animate-in { animation: fadeUp 0.5s var(--spring) both; }
    .animate-in-d1 { animation: fadeUp 0.5s var(--spring) 0.1s both; }
    .animate-in-d2 { animation: fadeUp 0.5s var(--spring) 0.2s both; }
    .animate-in-d3 { animation: fadeUp 0.5s var(--spring) 0.3s both; }
    .animate-in-d4 { animation: fadeUp 0.5s var(--spring) 0.4s both; }
    .animate-float { animation: float 5s ease-in-out infinite; }
    .animate-scale { animation: scaleIn 0.4s var(--spring) both; }
    .animate-wobble { animation: wobble 3s ease-in-out infinite; }

    /* ═══════════════════════════════════════════
       RESPONSIVE
       ═══════════════════════════════════════════ */
    @media (max-width: 768px) {
        h1 { font-size: 2.8rem !important; }
        .glass-card { padding: 1.5rem 1.3rem; border-radius: var(--radius-xl); }
        .post-output-container { padding: 1.5rem 1.3rem; }
    }

    </style>
    """
