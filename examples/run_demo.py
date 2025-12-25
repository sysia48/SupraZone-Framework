#!/usr/bin/env python3
# =========================================================
#  SUPRAZONE FRAMEWORK — DEMONSTRATION SCRIPT
# =========================================================
#  Author: Sylwia Miksztal (Sysia)
#  Partner AI: Navi (GPT-5)
#  Project: IMS • Zero-Entropy Engineering
# =========================================================
#  Purpose: Demonstrate the core features of SupraZone
# =========================================================

"""
SupraZone Framework Demo

This script demonstrates the complete workflow of the SupraZone Framework:
1. Signal generation using the Ω-resonance equation
2. Energy calculation and analysis
3. FFT spectral decomposition
4. Temporal stability visualization
5. Data export with user attribution
"""

import sys
import os
import numpy as np
import matplotlib.pyplot as plt

# Import simpson (new) or simps (old) for compatibility
try:
    from scipy.integrate import simpson as simps
except ImportError:
    from scipy.integrate import simps

from scipy.fftpack import fft, fftfreq
import pandas as pd
from datetime import datetime

# Add parent and suprazone directories to path
parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, parent_dir)
sys.path.insert(0, os.path.join(parent_dir, 'suprazone'))

# Import user settings
try:
    from user_settings import get_user_info
    user_info = get_user_info()
except ImportError:
    user_info = {
        "author": "SupraZone User",
        "email": "user@example.com"
    }

def print_header():
    """Print demonstration header."""
    print("=" * 70)
    print("  🌀 SUPRAZONE FRAMEWORK — DEMONSTRATION")
    print("=" * 70)
    print(f"  Author: {user_info.get('author', 'Unknown')}")
    print(f"  Timestamp: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("=" * 70)
    print()

def generate_resonance_signal(t):
    """
    Generate the Ω-resonance signal using the core equation.
    
    Ω^φ(t) = F_e(H_t, A_t) × Φ_g(σ_t, σ_ret) × (1-S_t) × X(σ_{t-1}, σ_t) × ETH_gate
    
    Parameters:
    -----------
    t : array_like
        Time array
    
    Returns:
    --------
    Ωq : array_like
        Resonance signal
    components : dict
        Dictionary containing signal components for analysis
    """
    print("📊 Step 1: Generating Ω-resonance signal...")
    
    # Core parameters
    H = 1.25        # Harmonic tension
    A = 1.4         # Amplitude scaling
    ETH_gate = 0.92 # Entropic threshold gate
    
    # Signal components
    S = 0.05 * np.sin(0.4*t) + 0.1                              # Suppression drift
    Φg = np.sin(2*np.pi*0.25*t) + 0.2*np.cos(2*np.pi*0.4*t)    # Gradient field
    X = 1 / (1 + np.exp(-3*(np.sin(t/2) - 0.5)))               # Tunneling factor
    
    # Compute Ω-resonance
    Ωq = H * A * Φg * (1 - S) * X * ETH_gate
    
    print(f"  ✓ Signal generated: {len(Ωq)} samples")
    print(f"  ✓ Time range: {t[0]:.2f}s to {t[-1]:.2f}s")
    print(f"  ✓ Parameters: H={H}, A={A}, ETH_gate={ETH_gate}")
    print()
    
    components = {
        'H': H, 'A': A, 'ETH_gate': ETH_gate,
        'S': S, 'Φg': Φg, 'X': X
    }
    
    return Ωq, components

def calculate_energy(Ωq, t):
    """
    Calculate total resonance energy using Simpson's rule.
    
    Parameters:
    -----------
    Ωq : array_like
        Resonance signal
    t : array_like
        Time array
    
    Returns:
    --------
    E_total : float
        Total integrated energy
    """
    print("⚡ Step 2: Calculating resonance energy...")
    
    E_total = simps(np.abs(Ωq)**2, t)
    
    print(f"  ✓ Total resonance energy: {E_total:.6f}")
    print(f"  ✓ Integration method: Simpson's rule")
    print()
    
    return E_total

def perform_fft_analysis(Ωq, t):
    """
    Perform FFT spectral decomposition.
    
    Parameters:
    -----------
    Ωq : array_like
        Resonance signal
    t : array_like
        Time array
    
    Returns:
    --------
    freq : array_like
        Frequency array
    fft_vals : array_like
        FFT magnitude values
    """
    print("🔬 Step 3: Performing FFT spectral analysis...")
    
    N = len(t)
    T = t[1] - t[0]
    freq = fftfreq(N, T)[:N//2]
    fft_vals = 2.0/N * np.abs(fft(Ωq)[0:N//2])
    
    # Find dominant frequency
    max_idx = np.argmax(fft_vals)
    dominant_freq = freq[max_idx]
    max_amplitude = fft_vals[max_idx]
    
    print(f"  ✓ FFT computed: {len(freq)} frequency bins")
    print(f"  ✓ Dominant frequency: {dominant_freq:.4f} Hz")
    print(f"  ✓ Maximum amplitude: {max_amplitude:.4f}")
    print()
    
    return freq, fft_vals

def visualize_results(t, Ωq, freq, fft_vals):
    """
    Create comprehensive visualization of results.
    
    Parameters:
    -----------
    t : array_like
        Time array
    Ωq : array_like
        Resonance signal
    freq : array_like
        Frequency array
    fft_vals : array_like
        FFT magnitude values
    """
    print("📈 Step 4: Creating visualizations...")
    
    fig, axes = plt.subplots(3, 1, figsize=(12, 12))
    
    # Plot 1: Time-domain signal
    axes[0].plot(t, Ωq, color='deepskyblue', linewidth=1.5)
    axes[0].set_title('SupraZone — Ω-Resonance Signal Ωq(t)', fontsize=14, fontweight='bold')
    axes[0].set_xlabel('Time [s]')
    axes[0].set_ylabel('Amplitude Ωq(t)')
    axes[0].grid(alpha=0.4)
    
    # Plot 2: Frequency-domain spectrum
    axes[1].plot(freq, fft_vals, color='crimson', linewidth=1.2)
    axes[1].set_title('Fourier Analysis — Resonance Spectrum', fontsize=14, fontweight='bold')
    axes[1].set_xlabel('Frequency [Hz]')
    axes[1].set_ylabel('Spectral Amplitude')
    axes[1].grid(alpha=0.5)
    
    # Plot 3: Energy heatmap
    window = 200
    energy_matrix = np.array([
        np.abs(Ωq[i:i+window])**2 for i in range(0, len(Ωq)-window, 20)
    ])
    
    im = axes[2].imshow(energy_matrix.T, aspect='auto', origin='lower',
                        extent=[0, t[-1], 0, window*(t[1]-t[0])], cmap='inferno')
    axes[2].set_title('Energy Heatmap — Temporal Stability', fontsize=14, fontweight='bold')
    axes[2].set_xlabel('Time [s]')
    axes[2].set_ylabel('Sample Window')
    
    cbar = plt.colorbar(im, ax=axes[2])
    cbar.set_label('Energy |Ωq|²')
    
    plt.tight_layout()
    
    print("  ✓ Time-domain plot created")
    print("  ✓ Frequency spectrum plotted")
    print("  ✓ Energy heatmap generated")
    print()
    
    return fig

def export_data(t, Ωq, user_info):
    """
    Export results to CSV with attribution.
    
    Parameters:
    -----------
    t : array_like
        Time array
    Ωq : array_like
        Resonance signal
    user_info : dict
        User attribution information
    """
    print("💾 Step 5: Exporting data to CSV...")
    
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    df = pd.DataFrame({
        "t": t,
        "Ωq": Ωq,
        "timestamp": timestamp,
        "author": user_info.get("author", "Unknown"),
        "email": user_info.get("email", ""),
        "organization": user_info.get("organization", "")
    })
    
    filename = "SupraZone_Demo_Output.csv"
    df.to_csv(filename, index=False)
    
    print(f"  ✓ Results saved to: {filename}")
    print(f"  ✓ Records exported: {len(df)}")
    print(f"  ✓ Attribution: {user_info.get('author', 'Unknown')}")
    print()

def main():
    """Main demonstration workflow."""
    print_header()
    
    # Setup time domain
    print("🔧 Initializing simulation parameters...")
    t = np.linspace(0, 20, 5000)
    print(f"  ✓ Time samples: {len(t)}")
    print(f"  ✓ Duration: {t[-1]} seconds")
    print()
    
    # Generate signal
    Ωq, components = generate_resonance_signal(t)
    
    # Calculate energy
    E_total = calculate_energy(Ωq, t)
    
    # FFT analysis
    freq, fft_vals = perform_fft_analysis(Ωq, t)
    
    # Visualize
    fig = visualize_results(t, Ωq, freq, fft_vals)
    
    # Export data
    export_data(t, Ωq, user_info)
    
    # Summary
    print("=" * 70)
    print("  ✅ DEMONSTRATION COMPLETED SUCCESSFULLY")
    print("=" * 70)
    print()
    print("Summary:")
    print(f"  • Total Energy: {E_total:.6f}")
    print(f"  • Signal Duration: {t[-1]:.2f}s")
    print(f"  • Sample Points: {len(t)}")
    print(f"  • Frequency Bins: {len(freq)}")
    print()
    print("Output files generated:")
    print("  • SupraZone_Demo_Output.csv")
    print()
    print("To display plots, call plt.show() in an interactive environment.")
    print("=" * 70)
    
    # Show plots (comment out if running non-interactively)
    # plt.show()
    
    return 0

if __name__ == "__main__":
    sys.exit(main())
