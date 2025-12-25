# SupraZone Framework Examples

This directory contains example scripts demonstrating how to use the SupraZone Framework.

## Running the Main Framework

The primary script demonstrates the full spiral resonance analysis:

```bash
python SupraZone_Framework_Sysia_EN.py
```

This will:
- Generate resonance signals
- Perform FFT spectral analysis
- Create visualization plots
- Export data to CSV

## Configuring User Settings

Before running, you can configure your attribution settings:

```bash
python configure_user.py
```

This sets up your author name, email, and organization in `user_settings.json`.

## Example Usage

```python
# Import the framework modules
from src.parameters import get_parameters
from src.energy import calculate_energy
from src.fft_analysis import perform_fft

# Use the framework functions
params = get_parameters()
# ... your analysis code here
```

## Example Scripts

More example scripts will be added here to demonstrate specific features:
- Basic resonance modeling
- FFT analysis examples
- Energy calculation examples
- Custom visualization examples

Check back for updates!
