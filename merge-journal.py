import os
from datetime import datetime

# Paths
here = os.path.abspath(os.path.dirname(__file__))
input_dir = os.path.join(here, "journal")
out_dir = os.path.join(here, "weekly_summary")

# Process into weeks
journal_files = [f for f in os.listdir(os.path.join(here, "journal"))]
dates = [datetime.strptime(os.path.splitext(f)[0], "%Y-%m-%d") for f in journal_files]
weeks_dict = {}
for fname, d in zip(journal_files, dates):
    year, week, _ = d.isocalendar()
    if week not in weeks_dict.keys():
        weeks_dict[week] = []
    weeks_dict[week].append((year, fname))

# Write out the files
os.makedirs(out_dir, exist_ok=True)

# Get week summaries
summary_file = open(os.path.join(out_dir, "week_roundups.md"), "r")
summary_info = {}
key = None
info = []
for line in summary_file.readlines():
    if line == "\n" or line.startswith("[["):
        continue
    elif line.split()[0] == "##":
        if key is not None:
            summary_info[key] = "".join(info)[:-1]
        info = []
        key = "-".join(line[2:].split())
    else:
        info.append(line)
summary_info[key] = "".join(info)

for week, v in weeks_dict.items():
    year = v[0][0]
    with open(os.path.join(out_dir, f"{year}-{week}.md"), "w") as out_:
        out_.write(f"# {year} week {week}\n\n")

        out_.write(summary_info[f"{year}-{week}"] + "\n\n")

        for i, (_, fname) in enumerate(v):
            with open(os.path.join(input_dir, fname), "r") as in_:
                contents = in_.readlines()
                for line in contents:
                    if line.startswith("#"):
                        line = "#" + line
                    out_.write(line)
                if i != (len(v) - 1):
                    out_.write("\n\n")