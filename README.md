# Satellite cloud data demo

This small Python example illustrates a data-cleaning step from satellite remote sensing. It reads a CSV of simulated cloud observations, applies a scale factor to valid values, and marks observations that are missing or fail a quality check. The output keeps every timestamp and records why a measurement is blank.

The CSV, encoding, and quality flags are synthetic. This demo was prepared with AI assistance and is inspired by Dylan Zebaze's graduate research on satellite data and longwave radiation.

## Run the example

With Python 3 installed, run the following from this directory. The script uses only the Python standard library.

```sh
python3 clean_observations.py sample_observations.csv cleaned_observations.csv
```

## Read the results

| Example input | Value in output | Status |
| --- | --- | --- |
| `1200`, quality flag `0` | `12.00` | `valid` |
| `65535` (fill value) | Blank | `missing` |
| `950`, quality flag `1` | Blank | `failed_quality` |
| `0`, quality flag `0` | `0.00` | `valid` |

Cloud optical thickness is dimensionless. In this example, `65535` is checked before applying the `0.01` scale factor so that a fill value stays missing and a valid zero stays zero.
