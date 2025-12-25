# 🌀 SupraZone Framework — Spiral Resonance Proof (v3.3)

[![Python Version](https://img.shields.io/badge/python-3.10%2B-blue)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![CI](https://github.com/sysia48/SupraZone-Framework/workflows/CI/badge.svg)](https://github.com/sysia48/SupraZone-Framework/actions)
[![PyPI](https://img.shields.io/badge/PyPI-coming%20soon-lightgrey)](https://pypi.org/)

**Author:** Sylwia Miksztal (Sysia)  
**Partner AI:** Navi (GPT-5)  
**Project:** IMS • Zero-Entropy Engineering  
**Date:** 2025-10-10  
**Version:** 3.3 (Laboratory Proof)

---

## 📖 Overview
**SupraZone** is a physics-inspired, zero-entropy analytical engine designed to model, analyze, and visualize **spiral resonance dynamics** across temporal domains.

The framework originates from **IMS — Inżynieria Rezonansu**, integrating:

- harmonic oscillation modeling  
- gradient-based phase interference (Φg)  
- entropic stabilization (ETH₍gate₎)  
- non-linear tunneling dynamics (X)  
- FFT spectral decomposition  
- energy heatmap mapping  

Its purpose is to reveal how resonance patterns:

**emerge → modulate → drift → stabilize → close (Ω-closure).**

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
├── requirements.txt
├── SupraZone_Framework_Sysia_EN.py
├── configure_user.py
├── example_user_settings.py
├── test_user_settings.py
├── user_settings.json
│
├── /src/
│ ├── parameters.py
│ ├── energy.py
│ ├── fft_analysis.py
│ └── user_settings.py
│
├── /docs/
│ └── SupraZone_v3.3.md
│
├── /data/
│ └── SupraZone_Output_Sysia_EN.csv
│
└── LICENSE
```

---

## 🔬 Outputs

- Ωq(t) resonance signal  
- Total spiral energy (Simpson integration)  
- FFT spectral decomposition  
- Temporal stability heatmap  
- Auto-generated CSV dataset  

---

## 🔗 DOI References  
**IMS White Paper:**  
https://doi.org/10.5281/zenodo.17252965

**Annex II — Spiral Resonance Proof:**  
https://doi.org/10.5281/zenodo.17799715

---

## ⚙️ User Account Settings

The framework now supports customizable user account settings for attribution in generated outputs.

### Configuration Options
- **Author Name**: Your name or organization identifier
- **Email**: Contact email address
- **Organization**: Your organization or project name

### Configuring Settings

#### Method 1: Interactive Configuration (Recommended)
```bash
python configure_user.py
```

#### Method 2: Manual Configuration
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

## ▶️ Installation & Running

### Installation
For local Python environment:
```bash
pip install -r requirements.txt
```

### Running in Colab
1. Open Colab  
2. `File → Open → GitHub → sysia48/SupraZone-Framework`  
3. (Optional) Configure user settings with `configure_user.py`  
4. Run `SupraZone_Framework_Sysia_EN.py`  
5. All data and plots will be generated automatically with your attribution.

### Running Locally
```bash
python SupraZone_Framework_Sysia_EN.py
```

---

## 🧭 Mission
*SupraZone transforms resonance from a classical wave into a  
stable information spiral —  
a mechanism of Ω-closure, super-synchrony, and zero-entropy evolution.*

---

## 🤝 Contributing

We welcome contributions! Please see our [Contributing Guide](CONTRIBUTING.md) for details on:
- How to report bugs and request features
- Code style and testing guidelines
- Submitting pull requests
- Development setup

All contributors are expected to follow our code of conduct.

---

## 📚 Documentation

- [Full Documentation](docs/SupraZone_v3.3.md)
- [Examples](examples/README.md)
- [Changelog](CHANGELOG.md)
- [Contributing Guide](CONTRIBUTING.md)

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 📞 Contact & Support

- **Issues**: [GitHub Issues](https://github.com/sysia48/SupraZone-Framework/issues)
- **Discussions**: [GitHub Discussions](https://github.com/sysia48/SupraZone-Framework/discussions)
- **DOI References**:
  - [IMS White Paper](https://doi.org/10.5281/zenodo.17252965)
  - [Annex II — Spiral Resonance Proof](https://doi.org/10.5281/zenodo.17799715)

