import re


def extract_primary_dependencies(requirements_txt):
    primary_deps = []
    with open(requirements_txt, "r") as f:
        for line in f:
            if re.match(r"^[a-zA-Z0-9\-_]+==", line):
                primary_deps.append(re.split(r"==", line)[0].strip())
    return primary_deps


def write_requirements_in(primary_deps, requirements_in):
    with open(requirements_in, "w") as f:
        for dep in primary_deps:
            f.write(f"{dep}\n")


requirements_txt = "requirements.txt"
requirements_in = "requirements.in"

primary_deps = extract_primary_dependencies(requirements_txt)
write_requirements_in(primary_deps, requirements_in)

print(f"Recreated {requirements_in} with primary dependencies from {requirements_txt}.")
