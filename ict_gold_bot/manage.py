#!/usr/bin/env python3
"""Management CLI for ICT Gold Bot."""

import argparse
import sys


def main():
    parser = argparse.ArgumentParser(description="ICT Gold Bot CLI")
    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    subparsers.add_parser("backtest", help="Run strategy backtest")
    subparsers.add_parser("test", help="Run test suite")
    subparsers.add_parser("dashboard", help="Launch analytics dashboard")

    args = parser.parse_args()

    if args.command == "backtest":
        print("Starting ICT Gold Bot backtest...")
    elif args.command == "test":
        import pytest
        sys.exit(pytest.main(["ict_gold_bot/tests"]))
    elif args.command == "dashboard":
        print("Launching dashboard...")
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
