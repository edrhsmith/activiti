import argparse


def main(args):
    stripped_lines = []
    with open(args.input_file) as f:
        for n, line in enumerate(f):
            stripped = line.strip()
            if stripped.startswith('<power>') and stripped.endswith('</power>'):
                continue
            stripped_lines.append(line)

    with open("new_morning_ride.gpx", "wt") as g:
        for line in stripped_lines:
            g.write(line)


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--input-file", type=str, required=True)
    args = parser.parse_args()
    if not args.input_file.endswith('.gpx'):
        raise ValueError("input file must be gpx")
    return args


if __name__ == "__main__":
    main(parse_args())
