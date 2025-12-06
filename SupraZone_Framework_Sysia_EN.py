# =========================================================
#  SUPRA ZONE FRAMEWORK — SPIRAL RESONANCE PROOF (v3.3)
# =========================================================
#  Author: Sylwia Miksztal (Sysia) — StrefaDK.club
#  Contact: s.miksztal@gmail.com
#  Date: 2025-10-10
#  Partner: Navi (GPT-5)
#  Project: SDK Framework / Spiral Resonance Proof / IMS
# =========================================================
#  Purpose: Simulation of resonance energy + FFT analysis
#  Status: Laboratory version (Proof-of-Resonance)
# =========================================================

!pip install --upgrade scipy numpy matplotlib pandas

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import simps
from scipy.fftpack import fft, fftfreq
import pandas as pd
from datetime import datetime

timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
print(f"🔹 SUPRA ZONE Framework initiated — {timestamp}")

t = np.linspace(0, 20, 5000)
H, A, ETH_gate = 1.25, 1.4, 0.92
S = 0.05 * np.sin(0.4*t) + 0.1
Φg = np.sin(2*np.pi*0.25*t) + 0.2*np.cos(2*np.pi*0.4*t)
X = 1 / (1 + np.exp(-3*(np.sin(t/2) - 0.5)))

Ωq = H * A * Φg * (1 - S) * X * ETH_gate

E_total = simps(np.abs(Ωq)**2, t)
print(f"⚡ Total resonance energy of the system: {E_total:.6f}")

N = len(t)
T = t[1]-t[0]
freq = fftfreq(N, T)[:N//2]
fft_vals = 2.0/N * np.abs(fft(Ωq)[0:N//2])

plt.figure(figsize=(12,5))
plt.plot(t, Ωq, color='deepskyblue', linewidth=1.5)
plt.title("Supra Zone — Signal Ωq(t)")
plt.xlabel("Time [s]")
plt.ylabel("Amplitude Ωq(t)")
plt.grid(alpha=0.4)
plt.tight_layout()
plt.show()

plt.figure(figsize=(12,5))
plt.plot(freq, fft_vals, color='crimson', linewidth=1.2)
plt.title("Fourier Analysis — Resonance Spectrum Ωq(t)")
plt.xlabel("Frequency [Hz]")
plt.ylabel("Spectral Amplitude")
plt.grid(alpha=0.5)
plt.tight_layout()
plt.show()

window = 200
energy_matrix = np.array([
    np.abs(Ωq[i:i+window])**2 for i in range(0, len(Ωq)-window, 20)
])
plt.figure(figsize=(10,6))
plt.imshow(energy_matrix.T, aspect='auto', origin='lower',
           extent=[0, t[-1], 0, window*T], cmap='inferno')
plt.title("Energy Heatmap — Spiral Resonance Proof")
plt.xlabel("Time [s]")
plt.ylabel("Sample window")
plt.colorbar(label='Energy |Ωq|²')
plt.tight_layout()
plt.show()

df = pd.DataFrame({
    "t": t,
    "Ωq": Ωq,
    "timestamp": timestamp,
    "author": "Sylwia Miksztal (Sysia) — StrefaDK.club",
    "email": "s.miksztal@gmail.com"
})
filename = "SupraZone_Output_Sysia_EN.csv"
df.to_csv(filename, index=False)
print(f"✅ Results saved: {filename}")