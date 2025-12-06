# =========================================================
#  FFT ANALYSIS — SupraZone v3.3
#  Author: Sylwia Miksztal (Sysia)
#  Partner AI: Navi (GPT-5)
# =========================================================

from scipy.fftpack import fft, fftfreq

def compute_fft(t, Ωq):
    """Perform FFT spectral decomposition."""
    N = len(t)
    T = t[1] - t[0]
    freq = fftfreq(N, T)[:N//2]
    fft_vals = 2.0 / N * abs(fft(Ωq)[0:N//2])
    return freq, fft_vals