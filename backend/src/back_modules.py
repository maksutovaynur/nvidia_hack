import json
import os
import random
from time import time

import numpy as np
import pandas as pd

from . import settings as S

person_df = pd.read_csv(S.PERSON_DF_PATH)
person_skills_json = json.load(open(S.PERSON_SKILL_PATH, "r"))
all_skills = sorted(set(sum(person_skills_json.values(), [])))

project_df = pd.read_csv(S.PROJECT_DF_PATH).rename(columns={"Unnamed: 0": "project_id"})
project_tags_json = json.load(open(S.PROJECT_TAG_PATH, "r"))
all_tags = sorted(set(sum(project_tags_json.values(), [])))

contributors_json = json.load(open(S.CONTRIBUTORS_PATH, "r"))

img_file_names = [i.strip() for i in os.popen(f"find {S.IMG_DIR}").read().split("\n") if i.endswith("jpeg")]
imgs = {"." + i.rsplit("profile_avatars", 1)[-1]: open(i, "rb").read() for i in img_file_names}
imgs = {i: v for i, v in imgs.items()}


# 1
def get_all_users_tags(max_len=14):
    return sorted(np.random.permutation(all_skills)[:max_len])


# 2
def get_all_projects_tags(max_len=14):
    return sorted(np.random.permutation(all_tags)[:max_len])


# 3
def find_user_ids_by_tags(input_tags_lst, top_N=3):
    users_scores = np.zeros(person_df.shape[0])

    for user_id in person_df['person_id'].values:
        user_skills = person_skills_json[str(user_id)]
        for skill in input_tags_lst:
            if skill in user_skills:
                users_scores[user_id] += 1

    top_users_ids = np.argsort(-users_scores)[:top_N]

    if sum(users_scores) == 0:
        np.random.seed(int(time()) + 42)
        top_users_ids = np.random.choice(np.arange(person_df.shape[0]), size=top_N)

    return top_users_ids


# 4
def find_projects_through_tags(tag_lst, top_N=3):
    project_lst = np.zeros(26)

    for tag in tag_lst:
        for project_id in range(26):
            if tag in project_tags_json[str(project_id)]:
                project_lst[project_id] += 1
    return np.argsort(-project_lst)[:top_N]


# 7
def get_user_info_by_id(user_id):
    row = person_df.iloc[int(user_id)]
    user_dct = row.to_dict()
    user_dct['img'] = imgs[user_dct['photo_path']]
    user_dct['skills_tags'] = person_skills_json[str(user_id)]
    return user_dct


def serialize_user(user):
    if user["github_nick"][0] == '@':
        user["github_nick"] = user["github_nick"][1:]
    tags = user['skills_tags'][:3]
    tags_str = ", ".join([f"<i>{sk}</i>" for sk in tags])
    stri = "<b>{full_name}</b>\n" \
           "<code>{person_position}</code>\n" \
           "{skl_tags}\n" \
           "<a href='/{tg_nick}'>Telegram: {tg_nick}</a>\n" \
           "<a href='https://github.com/{github_nick}'>Github: {github_nick}</a>\n" \
           "Email: {email}\n" \
           "<a href='https://womenslunchplace.org/'>Have a lunch</a>\n" \
           "".format(**user, skl_tags=tags_str)
    return stri, user["img"]


def get_random_person_id():
    return random.choice(list(person_skills_json.keys()))


def get_random_project_id():
    return random.choice(list(project_tags_json.keys()))


def get_project_by_id(id):
    row = project_df.iloc[int(id)]
    project_dct = row.to_dict()
    project_dct['tags'] = project_tags_json[str(id)]
    project_dct['contrib'] = [p for p in map(get_user_info_by_id, contributors_json[str(id)])]
    return project_dct


def serialize_project(project):
    tags = project['tags'][:3]
    tags_str = ", ".join([f"<i>{t}</i>" for t in tags])
    contrib = project['contrib'][:5]
    contrib_str = ", ".join([f"<i><a href='email:{c['email']}'>{c['full_name']}</a></i>" for c in contrib])
    return "<b>{name}</b>\n" \
           "<i>{description}</i>\n" \
           "Contributors: {contr}\n" \
           "Tags: {tgs}\n" \
           "<a href='{link}'>Link</a>\n".format(
        **project, tgs=tags_str, contr=contrib_str)
