class FakeFunctions:
    @classmethod
    def get_skill_tags(cls):
        return ["aws", "backend", "frontend", "ml", "cv", "RL"]

    @classmethod
    def get_people_by_skills(cls, skills):
        return ["Andrey", "Random", "Cluni"]

    @classmethod
    def get_projects_by_tags(cls, tags):
        return ["Project 1", "Project 2", "Project 3"]
