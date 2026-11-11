"""Decode cloud optical thickness in the demo's synthetic CSV format."""

import argparse
import csv
from pathlib import Path


FILL_VALUE = 65535
SCALE_FACTOR = 0.01
PASSING_QUALITY_FLAG = "0"


def clean_observation(row: dict[str, str]) -> dict[str, str]:
    raw_value = int(row["raw_cloud_optical_thickness"])
    result = {
        "observation_utc": row["observation_utc"],
        "cloud_optical_thickness": "",
        "status": "missing",
    }
    if raw_value == FILL_VALUE:
        return result
    if row["quality_flag"] != PASSING_QUALITY_FLAG:
        result["status"] = "failed_quality"
        return result

    result["cloud_optical_thickness"] = f"{raw_value * SCALE_FACTOR:.2f}"
    result["status"] = "valid"
    return result


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input_csv", type=Path)
    parser.add_argument("output_csv", type=Path)
    args = parser.parse_args()
    if args.input_csv.resolve() == args.output_csv.resolve():
        parser.error("Choose a different file for the output CSV.")

    columns = ["observation_utc", "cloud_optical_thickness", "status"]
    with (
        args.input_csv.open(encoding="utf-8", newline="") as source,
        args.output_csv.open("w", encoding="utf-8", newline="") as destination,
    ):
        observations = csv.DictReader(source)
        writer = csv.DictWriter(destination, fieldnames=columns)
        writer.writeheader()
        writer.writerows(clean_observation(row) for row in observations)


if __name__ == "__main__":
    main()
