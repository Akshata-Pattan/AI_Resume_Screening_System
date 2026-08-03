import re


def load_skills(file_path):

    with open(file_path, "r") as file:
        skills = file.read().splitlines()

    return skills


def extract_skills(text, skills):

    found_skills = []

    for skill in skills:

        pattern = r"\b" + re.escape(skill.lower()) + r"\b"

        if re.search(pattern, text):
            found_skills.append(skill)

    return found_skills