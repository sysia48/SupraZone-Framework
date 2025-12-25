# 🌀 SupraZone Framework — Spiral Resonance Proof (v3.3)

**Author:** Sylwia Miksztal (Sysia)  
**Partner AI:** Navi (GPT-5)  
**Project:** IMS • Zero-Entropy Engineering  
**Date:** 2025-10-10  
**Version:** 3.3 (Laboratory Proof)

[![Python Version](https://img.shields.io/badge/python-3.7%2B-blue.svg)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)

---

## 📖 Overview

**SupraZone** is a physics-inspired, zero-entropy analytical engine designed to model, analyze, and visualize **spiral resonance dynamics** across temporal domains.

The framework originates from **IMS — Inżynieria Rezonansu** (Resonance Engineering), integrating advanced mathematical concepts with practical computational physics.

### 🎯 Key Benefits

- **Zero-Entropy Engineering**: Models stable resonance patterns without energy dissipation
- **Multi-Domain Analysis**: Combines time-domain signals with frequency-domain analysis (FFT)
- **Visual Insights**: Generates intuitive plots and heatmaps for resonance patterns
- **Reproducible Research**: Automated CSV exports with complete attribution metadata
- **Extensible Architecture**: Modular design for easy integration and customization
- **Open Science**: Full transparency with DOI-referenced theoretical foundations

### ✨ Features

The framework integrates multiple analytical components:

- **Harmonic Oscillation Modeling** — Internal resonance potential calculation  
- **Gradient-Based Phase Interference (Φg)** — Cross-state phase analysis  
- **Entropic Stabilization (ETH₍gate₎)** — Stability limiting mechanism  
- **Non-Linear Tunneling Dynamics (X)** — Cross-temporal flow modeling  
- **FFT Spectral Decomposition** — Frequency-domain analysis  
- **Energy Heatmap Mapping** — Temporal stability visualization  
- **Configurable Attribution** — User account settings for output attribution

### 🔬 How It Works

SupraZone reveals how resonance patterns evolve through distinct phases:

**emerge → modulate → drift → stabilize → close (Ω-closure)**

This progression represents a complete resonance cycle, from initial excitation to stable Ω-closure, enabling the study of complex dynamical systems.

---

## ⚙️ Core Equation

\[
\Omega^\varphi(t)=
F_e(H_t,A_t)\times
\Phi_g(\sigma_t,\sigma_{ret})\times
(1-S_t)\times
X(\sigma_{t-1},\sigma_t)\times
ETH_{gate}
\]

Full theoretical breakdown →  
📄 `docs/SupraZone_v3.3.md`

---

## 🧩 Architecture

```
/SupraZone-Framework
│
├── README.md
├── LICENSE
├── requirements.txt
├── setup.py
├── pyproject.toml
├── MANIFEST.in
├── SupraZone_Framework_Sysia_EN.py
├── configure_user.py
├── example_user_settings.py
├── test_user_settings.py
├── user_settings.json
│
├── /suprazone/
│ ├── __init__.py
│ ├── configure_user.py
│ ├── parameters.py
│ ├── energy.py
│ ├── fft_analysis.py
│ └── user_settings.py
│
├── /examples/
│ ├── README.md
│ ├── run_demo.py
│ └── basic_usage.py
│
├── /docs/
│ └── SupraZone_v3.3.md
│
├── /.github/
│ └── /workflows/
│   └── ci.yml
│
└── /data/
  └── SupraZone_Output_Sysia_EN.csv
```

---

## 🔬 Outputs

The framework generates comprehensive analytical outputs:

- **Ωq(t) resonance signal** — Time-domain visualization of spiral dynamics  
- **Total spiral energy** — Integrated energy calculation using Simpson's rule  
- **FFT spectral decomposition** — Frequency-domain resonance spectrum  
- **Temporal stability heatmap** — Energy distribution visualization over time  
- **Auto-generated CSV dataset** — Complete data export with attribution metadata  

---

## 📦 Installation

### Prerequisites

- Python 3.7 or higher
- pip package manager

### Quick Install

```bash
# Clone the repository
git clone https://github.com/sysia48/SupraZone-Framework.git
cd SupraZone-Framework

# Install dependencies
pip install -r requirements.txt
```

### Installation via pip (PyPI)

Once published to PyPI, you can install directly:

```bash
pip install suprazone-framework
```

---

## 🚀 Usage

### Basic Usage

Run the main framework script:

```bash
python SupraZone_Framework_Sysia_EN.py
```

This will:
1. Generate resonance signals using the core Ω-equation
2. Perform FFT spectral analysis
3. Create visualization plots
4. Export results to CSV

### Using in Jupyter/Colab

1. Open [Google Colab](https://colab.research.google.com)
2. Navigate to `File → Open → GitHub`
3. Enter: `sysia48/SupraZone-Framework`
4. Select and run `SupraZone_Framework_Sysia_EN.py`

### Code Examples

#### Example 1: Basic Framework Execution

```python
import numpy as np
from scipy.integrate import simps
from scipy.fftpack import fft, fftfreq
import matplotlib.pyplot as plt

# Time domain setup
t = np.linspace(0, 20, 5000)

# Core parameters
H, A, ETH_gate = 1.25, 1.4, 0.92

# Signal components
S = 0.05 * np.sin(0.4*t) + 0.1
Φg = np.sin(2*np.pi*0.25*t) + 0.2*np.cos(2*np.pi*0.4*t)
X = 1 / (1 + np.exp(-3*(np.sin(t/2) - 0.5)))

# Compute Ω-resonance signal
Ωq = H * A * Φg * (1 - S) * X * ETH_gate

# Calculate total energy
E_total = simps(np.abs(Ωq)**2, t)
print(f"Total resonance energy: {E_total:.6f}")

# Plot the signal
plt.figure(figsize=(12,5))
plt.plot(t, Ωq, color='deepskyblue', linewidth=1.5)
plt.title("SupraZone — Signal Ωq(t)")
plt.xlabel("Time [s]")
plt.ylabel("Amplitude Ωq(t)")
plt.grid(alpha=0.4)
plt.show()
```

#### Example 2: Using Custom User Settings

```python
import sys
import os

# Add suprazone directory to path
sys.path.insert(0, 'suprazone')

from user_settings import get_user_info, update_user_settings

# Update user attribution
update_user_settings(
    author="Your Name",
    email="your.email@example.com",
    organization="Your Organization"
)

# Retrieve settings
user_info = get_user_info()
print(f"Author: {user_info['author']}")
print(f"Email: {user_info['email']}")
print(f"Organization: {user_info['organization']}")
```

#### Example 3: FFT Analysis

```python
from scipy.fftpack import fft, fftfreq
import numpy as np
import matplotlib.pyplot as plt

# Assuming Ωq and t are already computed
N = len(t)
T = t[1] - t[0]
freq = fftfreq(N, T)[:N//2]
fft_vals = 2.0/N * np.abs(fft(Ωq)[0:N//2])

# Plot frequency spectrum
plt.figure(figsize=(12,5))
plt.plot(freq, fft_vals, color='crimson', linewidth=1.2)
plt.title("Fourier Analysis — Resonance Spectrum")
plt.xlabel("Frequency [Hz]")
plt.ylabel("Spectral Amplitude")
plt.grid(alpha=0.5)
plt.show()
```

For more examples, see the [`examples/`](examples/) directory.

---

## 🔗 DOI References  
**IMS White Paper:**  
https://doi.org/10.5281/zenodo.17252965

**Annex II — Spiral Resonance Proof:**  
https://doi.org/10.5281/zenodo.17799715

---

## ⚙️ User Account Settings

The framework supports customizable user account settings for attribution in generated outputs.

### Configuration Options

- **Author Name**: Your name or organization identifier
- **Email**: Contact email address
- **Organization**: Your organization or project name

### Configuring Settings

#### Method 1: Interactive Configuration (Recommended)

```bash
python -m suprazone.configure_user
```

This will launch an interactive prompt to update your settings.

#### Method 2: Programmatic Configuration

```python
from suprazone.user_settings import update_user_settings

update_user_settings(
    author="Your Name",
    email="your.email@example.com",
    organization="Your Organization"
)
```

#### Method 3: Manual Configuration

Edit `user_settings.json` in the root directory:

```json
{
  "author": "Your Name",
  "email": "your.email@example.com",
  "organization": "Your Organization"
}
```

### Default Settings

If no configuration is provided, the framework uses default settings from the original author.

---

## 🤝 Contributing

We welcome contributions to SupraZone Framework! Here's how you can help:

### Getting Started

1. **Fork the repository** on GitHub
2. **Clone your fork** locally:
   ```bash
   git clone https://github.com/YOUR_USERNAME/SupraZone-Framework.git
   cd SupraZone-Framework
   ```
3. **Create a feature branch**:
   ```bash
   git checkout -b feature/your-feature-name
   ```

### Development Guidelines

- **Code Style**: Follow PEP 8 guidelines for Python code
- **Documentation**: Add docstrings to new functions and classes
- **Testing**: Add tests for new features in the appropriate test files
- **Commits**: Write clear, descriptive commit messages

### Submitting Changes

1. **Test your changes**:
   ```bash
   python test_user_settings.py
   # Add and run any new tests
   ```

2. **Commit your changes**:
   ```bash
   git add .
   git commit -m "Add feature: description of your changes"
   ```

3. **Push to your fork**:
   ```bash
   git push origin feature/your-feature-name
   ```

4. **Open a Pull Request** on GitHub with a clear description of your changes

### Areas for Contribution

- 🐛 Bug fixes and error handling improvements
- 📚 Documentation enhancements
- ✨ New analytical features
- 🧪 Additional test coverage
- 🎨 Visualization improvements
- 🔧 Performance optimizations

### Code Review Process

All submissions require review. We use GitHub pull requests for this purpose. The maintainers will review your PR and may request changes or improvements.

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 🧭 Mission

*SupraZone transforms resonance from a classical wave into a  
stable information spiral —  
a mechanism of Ω-closure, super-synchrony, and zero-entropy evolution.*

---

## 📧 Contact

**Author:** Sylwia Miksztal (Sysia)  
**Email:** s.miksztal@gmail.com  
**Project:** IMS — Zero-Entropy Engineering

For questions, suggestions, or collaboration opportunities, please open an issue on GitHub or contact via email.
