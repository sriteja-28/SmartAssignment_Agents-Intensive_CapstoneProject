import argparse
from app.ui_cli import run_cli

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--demo", action="store_true", help="run demo flow")
    args = parser.parse_args()

    if args.demo:
        run_cli()
    else:
        print("run with --demo to run the sample workflow")

if __name__ == "__main__":
    main()
