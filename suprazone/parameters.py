# =========================================================
#  PARAMETERS — SupraZone v3.3
#  Author: Sylwia Miksztal (Sysia)
#  Partner AI: Navi (GPT-5)
# =========================================================

import numpy as np

def get_parameters():
    t = np.linspace(0, 20, 5000)

    H = 1.25       # Harmonic tension
    A = 1.40       # Amplitude scaling
    ETH_gate = 0.92

    S = 0.05 * np.sin(0.4 * t) + 0.10
    Φg = np.sin(2*np.pi*0.25*t) + 0.2*np.cos(2*np.pi*0.4*t)
    X = 1 / (1 + np.exp(-3*(np.sin(t/2) - 0.5)))

    return t, H, A, ETH_gate, S, Φg, X