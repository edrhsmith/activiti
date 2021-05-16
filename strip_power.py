import argparse


POWER_TAGS = {'gpx': 'power', 'tcx': 'ns3:Watts'}


def main(args):
    extension = get_extension(args.input_file)
    power_tag_name = get_power_tag(extension)
    stripped_lines = []
    with open(args.input_file) as f:
        for n, line in enumerate(f):
            stripped = line.strip()
            if stripped.startswith(get_start_tag(power_tag_name)) and stripped.endswith(get_end_tag(power_tag_name)):
                continue
            stripped_lines.append(line)

    with open("new_" + args.input_file, "wt") as g:
        for line in stripped_lines:
            g.write(line)


def get_start_tag(tag_name):
    return '<' + tag_name + '>'


def get_end_tag(tag_name):
    return '</' + tag_name + '>'


def get_extension(file_name):
    return file_name.split('.')[-1]


def get_power_tag(extension):
    return POWER_TAGS[extension]


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--input-file", type=str, required=True)
    args = parser.parse_args()
    if not get_extension(args.input_file) in POWER_TAGS:
        raise ValueError("input file must be gpx")
    return args


if __name__ == "__main__":
    main(parse_args())
