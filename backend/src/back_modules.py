import json
import numpy as np
import pandas as pd
from random import choice
from . import settings as S


person_df = pd.read_csv(S.PERSON_DF_PATH)
person_skills_json = json.load(open(S.PERSON_SKILL_PATH, "r"))
all_skills = sorted(set(sum(person_skills_json.values(), [])))

project_df = pd.read_csv(S.PROJECT_DF_PATH).rename(columns={"Unnamed: 0": "project_id"})
project_tags_json = json.load(open(S.PROJECT_TAG_PATH, "r"))
all_tags = sorted(set(sum(project_tags_json.values(), [])))

print(person_df.columns)
print(project_df.columns)

#1
def get_all_users_tags(max_len=20):
    return sorted(np.random.permutation(all_skills)[:max_len])


#2
def get_all_projects_tags():
    return all_tags


#3
def find_user_ids_by_tags(input_tags_lst, top_N = 6):
    users_scores = np.zeros(person_df.shape[0])

    for user_id in person_df['person_id'].values:
            user_skills = project_tags_json[str(user_id)]
            for skill in input_tags_lst:
                if skill in user_skills:
                    users_scores[user_id] += 1

    top_users_ids = np.argsort(-users_scores)[:top_N]
    
    if sum(users_scores) == 0:
        np.random.seed(ord(input_tags_lst[0][2]) + 42)
        top_users_ids = np.random.choice(np.arange(person_df.shape[0]), size=top_N)
    
    return top_users_ids


#4
def find_projects_through_tags(tag_lst, top_N):
    project_lst  = np.zeros(26)

    for tag in tag_lst:
        for project_id in range(26):
            if tag in project_tags_json[str(project_id)]:
                project_lst[project_id] += 1
    return np.argsort(-project_lst)[:top_N]


#7
def get_user_info_by_id(user_id):
    row = person_df.iloc[user_id].values
    user_dct = row.to_dict() #{}
    # user_dct['user_id'] = row[0]
    # user_dct['full_name'] = row[1]
    # user_dct['gender'] = row[2]
    # user_dct['photo_path'] = row[3]
    # user_dct['telegram_nickname'] = row[4]
    # user_dct['position'] = row[5]
    # user_dct['github_nickname'] = row[6]
    # user_dct['email'] = row[7]
    user_dct['skills_tags'] = person_skills_json[str(user_id)]
    return user_dct



def get_project_by_id(id):
    # projects = pd.read_csv(project_csv_file)
    # projects = projects
    pass

