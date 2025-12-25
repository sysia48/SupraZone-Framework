#!/usr/bin/env python3
# =========================================================
#  SUPRAZONE FRAMEWORK — BASIC USAGE EXAMPLE
# =========================================================
#  Purpose: Simple example showing basic framework usage
# =========================================================

"""
Basic Usage Example for SupraZone Framework

This script demonstrates the minimal steps needed to:
- Generate a resonance signal
- Calculate energy
- Create a simple plot
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

# Add parent directory to path for imports
parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(parent_dir, 'suprazone'))

def basic_resonance_example():
    """
    Minimal example: Generate and plot a resonance signal.
    """
    print("🌀 SupraZone Framework — Basic Usage Example")
    print("-" * 50)
    
    # Step 1: Setup time array
    print("\n1. Setting up time domain...")
    t = np.linspace(0, 20, 5000)
    print(f"   Time range: {t[0]:.1f}s to {t[-1]:.1f}s ({len(t)} samples)")
    
    # Step 2: Define parameters
    print("\n2. Defining system parameters...")
    H = 1.25        # Harmonic tension
    A = 1.4         # Amplitude scaling
    ETH_gate = 0.92 # Entropic threshold
    print(f"   H={H}, A={A}, ETH_gate={ETH_gate}")
    
    # Step 3: Create signal components
    print("\n3. Computing signal components...")
    S = 0.05 * np.sin(0.4*t) + 0.1                              # Suppression
    Φg = np.sin(2*np.pi*0.25*t) + 0.2*np.cos(2*np.pi*0.4*t)    # Phase gradient
    X = 1 / (1 + np.exp(-3*(np.sin(t/2) - 0.5)))               # Tunneling
    print("   ✓ Components calculated")
    
    # Step 4: Compute Ω-resonance signal
    print("\n4. Computing Ω-resonance signal...")
    Ωq = H * A * Φg * (1 - S) * X * ETH_gate
    print(f"   ✓ Signal generated: Ωq(t)")
    
    # Step 5: Calculate total energy
    print("\n5. Calculating total energy...")
    E_total = simps(np.abs(Ωq)**2, t)
    print(f"   ⚡ Total resonance energy: {E_total:.6f}")
    
    # Step 6: Create visualization
    print("\n6. Creating plot...")
    plt.figure(figsize=(12, 5))
    plt.plot(t, Ωq, color='deepskyblue', linewidth=1.5, label='Ωq(t)')
    plt.title('SupraZone — Resonance Signal', fontsize=14, fontweight='bold')
    plt.xlabel('Time [s]')
    plt.ylabel('Amplitude')
    plt.grid(alpha=0.4)
    plt.legend()
    plt.tight_layout()
    print("   ✓ Plot created")
    
    print("\n" + "=" * 50)
    print("✅ Basic example completed!")
    print("=" * 50)
    print("\nTo display the plot, call plt.show() in an interactive environment.")
    
    # Uncomment to show plot:
    # plt.show()
    
    return Ωq, t, E_total

def custom_parameters_example():
    """
    Example showing how to experiment with different parameters.
    """
    print("\n\n🔬 Advanced Example — Parameter Exploration")
    print("-" * 50)
    
    t = np.linspace(0, 20, 5000)
    
    # Try different parameter sets
    parameter_sets = [
        {"name": "Low Energy", "H": 0.8, "A": 1.0, "ETH": 0.85},
        {"name": "Standard", "H": 1.25, "A": 1.4, "ETH": 0.92},
        {"name": "High Energy", "H": 1.5, "A": 1.8, "ETH": 0.95}
    ]
    
    plt.figure(figsize=(12, 6))
    
    for params in parameter_sets:
        # Generate signal with custom parameters
        H, A, ETH = params["H"], params["A"], params["ETH"]
        
        S = 0.05 * np.sin(0.4*t) + 0.1
        Φg = np.sin(2*np.pi*0.25*t) + 0.2*np.cos(2*np.pi*0.4*t)
        X = 1 / (1 + np.exp(-3*(np.sin(t/2) - 0.5)))
        
        Ωq = H * A * Φg * (1 - S) * X * ETH
        E_total = simps(np.abs(Ωq)**2, t)
        
        plt.plot(t, Ωq, linewidth=1.5, 
                label=f"{params['name']} (E={E_total:.3f})")
        
        print(f"\n{params['name']} Configuration:")
        print(f"  H={H}, A={A}, ETH={ETH}")
        print(f"  Energy: {E_total:.6f}")
    
    plt.title('Parameter Comparison — Resonance Signals', 
              fontsize=14, fontweight='bold')
    plt.xlabel('Time [s]')
    plt.ylabel('Amplitude Ωq(t)')
    plt.grid(alpha=0.4)
    plt.legend()
    plt.tight_layout()
    
    print("\n" + "=" * 50)
    print("✅ Parameter exploration completed!")
    print("=" * 50)
    
    # Uncomment to show plot:
    # plt.show()

def main():
    """Run all examples."""
    print("\n" + "=" * 60)
    print("  SUPRAZONE FRAMEWORK — BASIC USAGE EXAMPLES")
    print("=" * 60)
    
    # Run basic example
    Ωq, t, E_total = basic_resonance_example()
    
    # Run parameter exploration example
    custom_parameters_example()
    
    print("\n\n" + "=" * 60)
    print("  📚 For more advanced examples, see:")
    print("     • run_demo.py — Full demonstration")
    print("     • ../SupraZone_Framework_Sysia_EN.py — Complete framework")
    print("=" * 60 + "\n")
    
    return 0

if __name__ == "__main__":
    sys.exit(main())
