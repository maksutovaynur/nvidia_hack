import json
import numpy as np
import pandas as pd


#1
def get_all_users_tags(person_skills_json_path='./person_skills.json'):
    with open(person_skills_json_path, 'r') as f:
        d = json.load(f)
        all_skills = []

        for lst in d.values():
            all_skills += lst

        all_skills = np.unique(all_skills)
    return list(all_skills)


#2
def get_all_projects_tags(person_skills_json_path='./person_skills.json'):
    with open(person_skills_json_path, 'r') as f:
        d = json.load(f)
        all_skills = []

        for lst in d.values():
            all_skills += lst

        all_skills = np.unique(all_skills)
    return list(all_skills)


#3
def find_users_by_tags(input_tags_lst, top_N = 6,
                       person_df_path='./person.csv',
                       person_skills_json_path='./person_skills.json'):
    df = pd.read_csv(person_df_path)
    with open(person_skills_json_path, 'r') as f:
                skills_dct = json.load(f)

    users_scores = np.zeros(df.shape[0])

    for user_id in df['person_id'].values:
            user_skills = skills_dct[str(user_id)]
            for skill in input_tags_lst:
                if skill in user_skills:
                    users_scores[user_id] += 1

    top_users_ids = np.argsort(-users_scores)[:top_N]
    
    if sum(users_scores) == 0:
        np.random.seed(ord(input_tags_lst[0][2]) + 42)
        top_users_ids = np.random.choice(np.arange(df.shape[0]), size=top_N)
    
    return top_users_ids


#7
def get_user_info_by_id(user_id,
                        person_df_path='./person.csv',
                        person_skills_json_path='./person_skills.json'):
    df = pd.read_csv(person_df_path)
    row = df.iloc[user_id].values

    with open(person_skills_json_path, 'r') as f:
            skills_dct = json.load(f)

    user_dct = {}
    user_dct['user_id'] = row[0]
    user_dct['full_name'] = row[1]
    user_dct['gender'] = row[2]
    user_dct['photo_path'] = row[3]
    user_dct['telegram_nickname'] = row[4]
    user_dct['position'] = row[5]
    user_dct['github_nickname'] = row[6]
    user_dct['email'] = row[7]
    user_dct['skills_tags'] = skills_dct[str(user_id)]
    return user_dct