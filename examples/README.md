# SupraZone Framework Examples

This directory contains example scripts and notebooks demonstrating how to use the SupraZone Framework.

## Basic Usage

### Running the Main Framework

The simplest way to get started is to run the main framework script:

```python
# Run the complete SupraZone analysis
python SupraZone_Framework_Sysia_EN.py
```

This will generate:
- Spiral resonance signal Ω(t)
- FFT spectral decomposition
- Temporal stability heatmap
- CSV output with complete dataset

### Importing Framework Components

You can also import and use specific components from the framework:

```python
from src.parameters import get_parameters
from src.energy import calculate_energy
from src.fft_analysis import perform_fft_analysis

# Get default parameters
params = get_parameters()

# Use individual components in your analysis
# (Add more specific examples as the API evolves)
```

### Configuring User Settings

Before running the framework, you may want to configure your user settings for proper attribution:

```bash
python configure_user.py
```

Or manually edit `user_settings.json`:

```json
{
  "author": "Your Name",
  "email": "your.email@example.com",
  "organization": "Your Organization"
}
```

## Additional Examples

More examples will be added here as the framework evolves. Contributions of example notebooks and scripts are welcome!

## Need Help?

- Check the main [README.md](../README.md) for installation instructions
- Review the [documentation](../docs/) for detailed information
- Open an [issue](https://github.com/sysia48/SupraZone-Framework/issues) if you encounter problems
