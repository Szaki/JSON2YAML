import json
import yaml
import glob
import sys

for f in glob.glob(sys.argv[1] + "**/*.json", recursive=True):
    with open(f, "r") as fj:
        with open(f.replace(".json", ".yml"), "w") as fy:
            yaml.dump(json.load(fj), fy, yaml.CDumper)

