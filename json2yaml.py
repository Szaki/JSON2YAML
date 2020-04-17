#!/usr/bin/env python3
import json
import yaml
import glob
import os
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-r", "--recursive", action='store_true', help="Look for files in subdirectories.")
parser.add_argument("-s", "--sort", action='store_true', help="Sort the key-value pairs during conversion.")
parser.add_argument("-d", "--delete", action='store_true', help="Delete file(s) after conversion.")
parser.add_argument("PATH", type=str, help="Path to a JSON file or directory containing JSON files.")
args = parser.parse_args()

def convert(path):
    with open(path, "r") as fj:
        with open(path.replace(".json", ".yml"), "w") as fy:
            yaml.safe_dump(json.load(fj), fy, sort_keys=args.sort)
    if args.delete:
        os.remove(path)
    print(f"Successfully converted {path}...")


if __name__ == "__main__":
    if args.PATH.endswith(".json"):
        convert(args.PATH)
    else:
        for path in glob.glob(args.PATH + "**/*.json", recursive=args.recursive):
            convert(path)
