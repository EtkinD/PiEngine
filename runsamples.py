import os
import argparse as ap


def test_samples(samples: list[str]) -> None:
    """
        Run sample scripts
    """
    # ===== Print Info ===== #
    print("Selected samples:")
    for sample in samples:
        print(f"  ∟ {os.path.basename(sample)}")
    print()

    # ===== Run Samples ===== #
    for sample in samples:
        sample_name = f" {os.path.basename(sample)} "
        print(f"+{sample_name:-^60}+")

        os.chdir(sample)
        os.system(f"python \"{sample}/main.py\"")

        print(f"+{'':-^60}+")
        print()

    print("All samples are done")


def main():
    # ===== Parse Arguments ===== #
    parser = ap.ArgumentParser(description="Run all samples")
    parser.add_argument("-s", "--samples", action="store_true", help="Run all samples", default=False)
    parser.add_argument("-n", "--number", type=int, nargs="+", help="Run specific samples", default=None)
    args = parser.parse_args()

    # ===== Get Samples ===== #
    SAMPLES_DIR = os.path.join(os.path.dirname(__file__), 'samples')
    SAMPLES = [os.path.join(SAMPLES_DIR, f) for f in os.listdir(SAMPLES_DIR)]
    SAMPLES.sort(key=lambda x: int(x.split('-')[0].split(' ')[1]))

    # ===== Select Samples ===== #
    if args.samples:
        samples = SAMPLES
    elif args.number:
        samples = [SAMPLES[i - 1] for i in args.number]
    else:
        print("No samples selected")
        return

    # ===== Run Samples ===== #
    test_samples(samples)


if __name__ == "__main__":
    main()
