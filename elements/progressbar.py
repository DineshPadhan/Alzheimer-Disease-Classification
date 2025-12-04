import streamlit as st

def progress_bar(current_step, total_steps):
    # ───── Animated Stepper Styles ─────
    st.markdown("""
    <style>
    .stepper-wrapper {
        display: flex;
        align-items: center;
        justify-content: space-between;
        margin: 10px 0 25px 0;
        gap: 8px;
    }

    .step {
        width: 40px;
        height: 40px;
        border-radius: 50%;
        background: #d4d4d4;
        color: #333;
        display: flex;
        align-items: center;
        justify-content: center;
        font-weight: 600;
        font-size: 16px;
        position: relative;
        transition: background-color 0.35s ease,
                    color 0.35s ease,
                    transform 0.35s ease,
                    box-shadow 0.35s ease;
    }

    .step.active {
        background: #1f77b4;
        color: #fff;
        transform: scale(1.12);
        box-shadow: 0 0 12px rgba(31, 119, 180, 0.6);
    }

    .step.active::after {
        content: "";
        position: absolute;
        width: 58px;
        height: 58px;
        border-radius: 50%;
        border: 2px solid rgba(31, 119, 180, 0.35);
        animation: pulse-ring 1.4s ease-out infinite;
    }

    @keyframes pulse-ring {
        0% {
            transform: scale(0.75);
            opacity: 0.9;
        }
        70% {
            transform: scale(1.05);
            opacity: 0;
        }
        100% {
            transform: scale(1.05);
            opacity: 0;
        }
    }

    .line {
        flex: 1;
        height: 4px;
        background: #d4d4d4;
        border-radius: 999px;
        position: relative;
        overflow: hidden;
    }

    .line-inner {
        position: absolute;
        left: 0;
        top: 0;
        bottom: 0;
        width: 0%;
        background: linear-gradient(90deg, #1f77b4, #4fa3ff);
        border-radius: 999px;
        transition: width 0.5s ease;
    }

    .line-inner.active {
        width: 100%;
    }
    </style>
    """, unsafe_allow_html=True)

    # ───── Build Animated Stepper HTML ─────
    html = "<div class='stepper-wrapper'>"

    for i in range(total_steps):
        is_active = (i == current_step)
        html += f"<div class='step {'active' if is_active else ''}'>{i+1}</div>"

        if i < total_steps - 1:
            line_active_class = "active" if i < current_step else ""
            html += f"""
            <div class='line'>
                <div class='line-inner {line_active_class}'></div>
            </div>
            """

    html += "</div>"

    st.markdown(html, unsafe_allow_html=True)
