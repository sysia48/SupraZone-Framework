# =========================================================
#  ENERGY ENGINE — SupraZone v3.3
#  Author: Sylwia Miksztal (Sysia)
#  Partner AI: Navi (GPT-5)
# =========================================================

# Import simpson (new) or simps (old) for compatibility
try:
    from scipy.integrate import simpson as simps
except ImportError:
    from scipy.integrate import simps
import numpy as np

def compute_energy(t, Ωq):
    """Compute total resonance energy using Simpson’s Rule."""
    return simps(np.abs(Ωq)**2, t)