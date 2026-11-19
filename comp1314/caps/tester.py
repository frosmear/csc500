#!/usr/bin/env python3
"""Run a dataset of test cases against a Python script."""

import subprocess
import sys
from pathlib import Path


def main():
    if len(sys.argv) != 3:
        print("Usage: python3 tester.py <script.py> <dataset.txt>")
        sys.exit(1)

    script = Path(sys.argv[1]).resolve()
    dataset = Path(sys.argv[2]).resolve()
    results_file = Path("results.txt")

    if not script.is_file():
        print(f"Error: Script not found: {script}")
        sys.exit(1)

    if not dataset.is_file():
        print(f"Error: Dataset not found: {dataset}")
        sys.exit(1)

    test_cases = [
        line.strip()
        for line in dataset.read_text().splitlines()
        if line.strip()
    ]

    total = len(test_cases)
    passed = 0
    failed = 0

    print(f"\nRunning {total} test cases...")
    print(f"Script:  {script.name}")
    print(f"Dataset: {dataset.name}")
    print(f"Results: {results_file.resolve()}\n")

    with results_file.open("w") as results:

        for number, test_case in enumerate(test_cases, start=1):

            results.write("=" * 60 + "\n")
            results.write(f"TEST #{number}: {test_case}\n")
            results.write("=" * 60 + "\n")

            # Split IP address and CIDR
            try:
                ip_address, cidr = test_case.split("/")
                if not ip_address or not cidr:
                    raise ValueError("Missing IP address or CIDR")
            except ValueError:
                failed += 1
                error = f"Invalid test case format: {test_case}"

                results.write(f"ERROR: {error}\n\n")
                print(f"ERROR #{number}: {error}")
                continue

            # Execute the target script
            try:
                print(f"\rTesting #{number} of {total}...", end="", flush=True)
                result = subprocess.run(
                    [sys.executable, str(script), ip_address, cidr],
                    capture_output=True,
                    text=True,
                    timeout=30
                )

                output = result.stdout
                error_output = result.stderr

                results.write(output)

                if error_output:
                    results.write("\nSTDERR:\n")
                    results.write(error_output)

                # Check for execution errors
                errors = []

                if result.returncode != 0:
                    errors.append(
                        f"Exit code: {result.returncode}"
                    )

                if error_output.strip():
                    errors.append(error_output.strip())

                if "Error:" in output:
                    errors.append(
                        "Script reported an error in its output."
                    )

                if errors:
                    failed += 1
                    print(f"\nERROR #{number}: {test_case}")

                    for error in errors:
                        print(error)

                    results.write("\nTEST STATUS: FAILED\n")
                else:
                    passed += 1
                    results.write("\nTEST STATUS: PASSED\n")

            except subprocess.TimeoutExpired:
                failed += 1
                error = "Test timed out after 30 seconds."
                results.write(f"\nERROR: {error}\n")
                print(f"\nERROR #{number}: {error}")

            except Exception as error:
                failed += 1
                results.write(f"\nERROR: {error}\n")
                print(f"\nERROR #{number}: {error}")

            results.write("\n\n")

    # Final summary
    print() 
    print("\n" + "=" * 45)
    print("TEST SUMMARY")
    print("=" * 45)
    print(f"Total tests: {total}")
    print(f"Passed:      {passed}")
    print(f"Failed:      {failed}")
    print(f"Results:     {results_file.resolve()}")
    print("=" * 45)


if __name__ == "__main__":
    main()

