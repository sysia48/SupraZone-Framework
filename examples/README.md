# 📚 SupraZone Framework — Examples

This directory contains practical examples demonstrating the features and capabilities of the SupraZone Framework.

## Available Examples

### 1. `run_demo.py` — Complete Demonstration

A comprehensive demonstration of all framework features:

- ✅ Signal generation using the Ω-resonance equation
- ✅ Energy calculation with Simpson's rule integration
- ✅ FFT spectral decomposition and analysis
- ✅ Temporal stability heatmap visualization
- ✅ CSV data export with user attribution

**Run the demo:**
```bash
python examples/run_demo.py
```

**What you'll learn:**
- Complete workflow from signal generation to data export
- How each component of the framework works
- Understanding the energy calculation process
- Interpreting FFT results and frequency spectra
- Creating comprehensive visualizations

### 2. `basic_usage.py` — Quick Start Guide

A minimal example showing the essential steps:

- Basic resonance signal generation
- Energy calculation
- Simple plotting
- Parameter experimentation

**Run the example:**
```bash
python examples/basic_usage.py
```

**What you'll learn:**
- Minimal code needed to generate resonance signals
- How to adjust system parameters (H, A, ETH_gate)
- Comparing different parameter configurations
- Creating basic visualizations

## Prerequisites

Ensure you have all dependencies installed:

```bash
pip install -r ../requirements.txt
```

## Understanding the Output

### Time-Domain Signal (Ωq(t))

The resonance signal shows how the system evolves over time. Key observations:

- **Oscillations**: Represent harmonic energy flow
- **Envelope**: Shows the modulation by suppression and tunneling factors
- **Amplitude**: Related to energy concentration

### Frequency Spectrum

FFT analysis reveals:

- **Dominant frequencies**: Primary resonance modes
- **Harmonic structure**: Related resonance patterns
- **Spectral distribution**: Energy spread across frequencies

### Energy Heatmap

Temporal stability visualization showing:

- **Color intensity**: Energy concentration at different time windows
- **Patterns**: Emergence and evolution of resonance structures
- **Stability regions**: Areas of consistent energy distribution

## Customization

### Modifying Parameters

Edit the parameter values in the scripts:

```python
# Core parameters
H = 1.25        # Harmonic tension (0.5 to 2.0 recommended)
A = 1.4         # Amplitude scaling (0.8 to 2.0 recommended)
ETH_gate = 0.92 # Entropic threshold (0.8 to 0.98 recommended)
```

### Adjusting Time Domain

Change the time range and resolution:

```python
# Increase resolution
t = np.linspace(0, 20, 10000)  # More samples

# Extend duration
t = np.linspace(0, 50, 5000)   # Longer time span
```

### Custom Signal Components

Experiment with different mathematical functions:

```python
# Alternative suppression drift
S = 0.08 * np.sin(0.5*t) + 0.15

# Modified gradient field
Φg = np.sin(2*np.pi*0.3*t) + 0.3*np.cos(2*np.pi*0.5*t)

# Different tunneling behavior
X = 1 / (1 + np.exp(-5*(np.sin(t/3) - 0.3)))
```

## User Attribution

To set your own attribution in the outputs:

```bash
# Interactive configuration
python ../configure_user.py

# Or edit user_settings.json directly
```

Your information will be included in all CSV exports from the examples.

## Jupyter Notebook Usage

These examples can also be run in Jupyter notebooks:

```python
# In a Jupyter cell
%run examples/run_demo.py

# Or import as a module
import sys
sys.path.insert(0, 'examples')
from run_demo import generate_resonance_signal, perform_fft_analysis

# Use the functions
import numpy as np
t = np.linspace(0, 20, 5000)
Ωq, components = generate_resonance_signal(t)
```

## Additional Resources

- **Main Framework**: `../SupraZone_Framework_Sysia_EN.py`
- **Documentation**: `../docs/SupraZone_v3.3.md`
- **Theoretical Background**: See DOI references in main README
- **User Settings**: `../suprazone/user_settings.py`

## Troubleshooting

### Import Errors

If you get import errors, ensure you're running from the correct directory:

```bash
# From repository root
python examples/run_demo.py

# Or with explicit Python path
PYTHONPATH=. python examples/run_demo.py
```

### Missing Dependencies

Install all required packages:

```bash
pip install scipy numpy matplotlib pandas
```

### Plot Not Showing

In non-interactive environments, plots won't display automatically. Uncomment the `plt.show()` lines or save to file:

```python
# Save figure instead of showing
plt.savefig('output_plot.png', dpi=300, bbox_inches='tight')
```

## Contributing Examples

Have an interesting use case? We welcome contributions!

1. Create a new example script in this directory
2. Add clear comments and documentation
3. Update this README with a description
4. Submit a pull request

---

**Questions or Issues?**

Open an issue on GitHub: https://github.com/sysia48/SupraZone-Framework/issues
