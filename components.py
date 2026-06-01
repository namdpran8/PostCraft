# Design Language: Apple Liquid Glass — Earthy Burgundy & Sage
# ──────────────────────────────────────────
# Reusable UI components
# Uses st.components.v1.html for the empty state to avoid parser bugs
# ──────────────────────────────────────────

import streamlit as st
import streamlit.components.v1 as stc


def glass_card(content_fn, extra_class=""):
    """Wrap content in a frosted glass card container."""
    cls = f"glass-card {extra_class}".strip()
    st.markdown(f'<div class="{cls}">', unsafe_allow_html=True)
    content_fn()
    st.markdown('</div>', unsafe_allow_html=True)


def glass_card_compact(content_fn, extra_class=""):
    """Wrap content in a compact glass card."""
    cls = f"glass-card-compact {extra_class}".strip()
    st.markdown(f'<div class="{cls}">', unsafe_allow_html=True)
    content_fn()
    st.markdown('</div>', unsafe_allow_html=True)


def app_header(title: str, subtitle: str):
    """Render the main app header with animated gradient cursive title."""
    st.markdown(
        '<div class="app-header animate-in">'
        f'<h1>{title}</h1>'
        f'<div class="app-header-subtitle">{subtitle}</div>'
        '</div>',
        unsafe_allow_html=True
    )


def section_label(text: str):
    """Render a small uppercase section label."""
    st.markdown(f'<div class="section-label">{text}</div>', unsafe_allow_html=True)


def badge(text: str, variant: str = "accent"):
    """Render an inline badge. variant: 'accent' | 'success' | 'neutral'"""
    st.markdown(
        f'<span class="badge badge-{variant}">{text}</span>',
        unsafe_allow_html=True
    )


def glass_divider():
    """Render a soft gradient divider with sage and burgundy tints."""
    st.markdown('<div class="glass-divider"></div>', unsafe_allow_html=True)


def toast(message: str, variant: str = "success"):
    """Render a notification toast. variant: 'success' | 'info'"""
    icon = "✓" if variant == "success" else "ℹ"
    st.markdown(
        f'<div class="toast toast-{variant}">{icon}&ensp;{message}</div>',
        unsafe_allow_html=True
    )


def custom_spinner(message: str = "Generating your post…"):
    """Render a custom spinner overlay with burgundy/sage ring."""
    st.markdown(
        '<div class="custom-spinner-overlay">'
        '<div class="custom-spinner-ring"></div>'
        f'<div class="custom-spinner-text">{message}</div>'
        '</div>',
        unsafe_allow_html=True
    )


def empty_state(icon: str = "◇", title: str = "Nothing here yet",
                subtitle: str = "Configure your post settings and hit Generate."):
    """
    Render a designed empty state with animated SVG illustration.
    Uses st.components.v1.html to guarantee SVG renders correctly.
    """
    html_content = f"""
    <!DOCTYPE html>
    <html>
    <head>
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Sacramento&family=Cormorant+Garamond:ital,wght@0,500;1,500&family=Plus+Jakarta+Sans:wght@400&display=swap');

        * {{ margin: 0; padding: 0; box-sizing: border-box; }}

        body {{
            background: transparent;
            display: flex;
            justify-content: center;
            align-items: center;
            min-height: 100%;
            overflow: hidden;
        }}

        .container {{
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            padding: 2.5rem 2rem 2rem;
            text-align: center;
            animation: fadeUp 0.8s cubic-bezier(0.34, 1.56, 0.64, 1) both;
        }}

        @keyframes fadeUp {{
            0%   {{ transform: translateY(30px); opacity: 0; }}
            100% {{ transform: translateY(0); opacity: 1; }}
        }}
        @keyframes floatY {{
            0%, 100% {{ transform: translateY(0); }}
            50%      {{ transform: translateY(-12px); }}
        }}
        @keyframes glowPulse {{
            0%, 100% {{ filter: drop-shadow(0 0 8px rgba(127, 32, 32, 0.05)); }}
            50%      {{ filter: drop-shadow(0 0 24px rgba(127, 32, 32, 0.12)); }}
        }}
        @keyframes drawLine {{
            0%   {{ stroke-dashoffset: 80; }}
            100% {{ stroke-dashoffset: 0; }}
        }}
        @keyframes pop {{
            0%   {{ transform: scale(0); opacity: 0; }}
            60%  {{ transform: scale(1.15); opacity: 1; }}
            100% {{ transform: scale(1); opacity: 1; }}
        }}
        @keyframes shimmer {{
            0%   {{ opacity: 0.3; }}
            50%  {{ opacity: 0.7; }}
            100% {{ opacity: 0.3; }}
        }}

        .illustration {{
            margin-bottom: 1.8rem;
            animation: floatY 5s ease-in-out infinite, glowPulse 4s ease-in-out infinite;
        }}

        .illustration svg .line1 {{ stroke-dasharray: 50; animation: drawLine 1.2s ease 0.3s both; }}
        .illustration svg .line2 {{ stroke-dasharray: 70; animation: drawLine 1.4s ease 0.5s both; }}
        .illustration svg .line3 {{ stroke-dasharray: 60; animation: drawLine 1.3s ease 0.7s both; }}
        .illustration svg .line4 {{ stroke-dasharray: 40; animation: drawLine 1.1s ease 0.9s both; }}
        .illustration svg .check-circle {{ animation: pop 0.5s cubic-bezier(0.34, 1.56, 0.64, 1) 1.1s both; }}
        .illustration svg .check-mark {{ stroke-dasharray: 20; animation: drawLine 0.6s ease 1.4s both; }}
        .illustration svg .dot1 {{ animation: shimmer 3s ease-in-out infinite; }}
        .illustration svg .dot2 {{ animation: shimmer 3s ease-in-out 1s infinite; }}
        .illustration svg .dot3 {{ animation: shimmer 3s ease-in-out 2s infinite; }}

        .title {{
            font-family: 'Sacramento', cursive;
            font-size: 2.2rem;
            font-weight: 400;
            color: #C9CAAC;
            margin-bottom: 0.6rem;
        }}

        .subtitle {{
            font-family: 'Plus Jakarta Sans', sans-serif;
            font-size: 0.85rem;
            font-weight: 400;
            color: #6B675E;
            max-width: 380px;
            line-height: 1.65;
        }}
    </style>
    </head>
    <body>
        <div class="container">
            <div class="illustration">
                <svg width="140" height="140" viewBox="0 0 140 140" fill="none" xmlns="http://www.w3.org/2000/svg">
                    <!-- Document frame -->
                    <rect x="24" y="22" width="92" height="76" rx="12" stroke="rgba(134,155,126,0.22)" stroke-width="1.5" fill="rgba(134,155,126,0.03)"/>
                    <rect x="30" y="28" width="80" height="64" rx="8" stroke="rgba(134,155,126,0.1)" stroke-width="0.7" fill="none"/>

                    <!-- Text lines with draw animation -->
                    <line class="line1" x1="38" y1="48" x2="78" y2="48" stroke="rgba(201,202,172,0.2)" stroke-width="2.5" stroke-linecap="round"/>
                    <line class="line2" x1="38" y1="58" x2="100" y2="58" stroke="rgba(201,202,172,0.15)" stroke-width="2" stroke-linecap="round"/>
                    <line class="line3" x1="38" y1="67" x2="92" y2="67" stroke="rgba(201,202,172,0.12)" stroke-width="2" stroke-linecap="round"/>
                    <line class="line4" x1="38" y1="76" x2="64" y2="76" stroke="rgba(201,202,172,0.08)" stroke-width="2" stroke-linecap="round"/>

                    <!-- Checkmark badge -->
                    <circle class="check-circle" cx="104" cy="34" r="16" stroke="rgba(127,32,32,0.3)" stroke-width="1.5" fill="rgba(127,32,32,0.06)"/>
                    <path class="check-mark" d="M98 34L102 38L110 30" stroke="rgba(134,155,126,0.45)" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>

                    <!-- Floating dots -->
                    <circle class="dot1" cx="18" cy="55" r="4" fill="rgba(127,32,32,0.06)"/>
                    <circle class="dot2" cx="126" cy="75" r="3" fill="rgba(134,155,126,0.05)"/>
                    <circle class="dot3" cx="22" cy="95" r="2.5" fill="rgba(201,202,172,0.05)"/>
                </svg>
            </div>
            <div class="title">{title}</div>
            <div class="subtitle">{subtitle}</div>
        </div>
    </body>
    </html>
    """
    stc.html(html_content, height=400, scrolling=False)


def post_output(content: str):
    """Render the generated post in a liquid glass container."""
    import html as html_mod
    safe = html_mod.escape(content).replace("\n", "<br>")
    st.markdown(
        '<div class="post-output-container">'
        f'{safe}'
        '</div>',
        unsafe_allow_html=True
    )


def metric_card(label: str, value: str, trend: str = "", trend_positive: bool = True):
    """Render a KPI metric card with glass effect and optional trend."""
    trend_html = ""
    if trend:
        color = "var(--success-text)" if trend_positive else "var(--danger-text)"
        bg = "var(--success-tonal)" if trend_positive else "var(--danger-tonal)"
        arrow = "↑" if trend_positive else "↓"
        trend_html = (
            f'<span style="display:inline-flex;align-items:center;gap:3px;'
            f'padding:2px 8px;border-radius:50px;background:{bg};color:{color};'
            f'font-size:0.72rem;font-weight:600;font-family:var(--font-body);">'
            f'{arrow} {trend}</span>'
        )

    st.markdown(
        '<div class="glass-card-compact" style="text-align:center;">'
        '<div style="font-family:var(--font-body);font-size:0.64rem;font-weight:700;'
        'text-transform:uppercase;letter-spacing:0.14em;color:var(--text-quaternary);'
        f'margin-bottom:0.5rem;">{label}</div>'
        '<div style="font-family:var(--font-serif);font-size:1.6rem;font-weight:700;'
        'color:var(--text-primary);line-height:1.2;margin-bottom:0.2rem;'
        f'font-style:italic;">{value}</div>'
        f'{trend_html}'
        '</div>',
        unsafe_allow_html=True
    )


def linkedin_preview_frame(content: str, author_name: str = "You"):
    """Render a mini LinkedIn-style post preview card with glass effect."""
    import html as html_mod
    safe = html_mod.escape(content).replace("\n", "<br>")

    html_str = (
        '<div class="glass-card" style="max-width:600px;">'
        # Author row
        '<div style="display:flex;align-items:center;gap:14px;margin-bottom:1.2rem;">'
        '<div style="width:48px;height:48px;border-radius:50%;'
        'background:linear-gradient(135deg,var(--burgundy),var(--sage-dim));'
        'display:flex;align-items:center;justify-content:center;'
        'color:var(--cream);font-weight:400;font-size:1.5rem;'
        'font-family:var(--font-cursive);'
        f'box-shadow:0 4px 16px rgba(127,32,32,0.2);">{author_name[0].upper()}</div>'
        '<div>'
        f'<div style="font-family:var(--font-serif);font-weight:600;font-size:0.95rem;'
        f'color:var(--text-primary);font-style:italic;">{author_name}</div>'
        '<div style="font-family:var(--font-body);font-size:0.74rem;'
        'color:var(--text-quaternary);">Just now · 🌐</div>'
        '</div>'
        '</div>'
        # Post body
        f'<div style="font-family:var(--font-body);font-size:0.9rem;line-height:1.8;'
        f'color:var(--text-secondary);">{safe}</div>'
        # Action bar
        '<div style="margin-top:1.4rem;padding-top:1rem;'
        'border-top:1px solid rgba(246,243,235,0.04);'
        'display:flex;gap:2rem;font-family:var(--font-body);'
        'font-size:0.76rem;color:var(--text-quaternary);letter-spacing:0.01em;">'
        '<span style="transition:color 0.2s ease;cursor:pointer;">👍 Like</span>'
        '<span style="transition:color 0.2s ease;cursor:pointer;">💬 Comment</span>'
        '<span style="transition:color 0.2s ease;cursor:pointer;">🔄 Repost</span>'
        '<span style="transition:color 0.2s ease;cursor:pointer;">📨 Send</span>'
        '</div>'
        '</div>'
    )
    st.markdown(html_str, unsafe_allow_html=True)
