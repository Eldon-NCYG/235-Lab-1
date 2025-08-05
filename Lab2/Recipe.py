import datetime
class Recipe:
    def __init__(self, id:str, name:str, author:str, date:str, category:str):
        self.name = name
        self.id = id
        self.author = author
        self.date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.category = category
        self.category = category

    @property
    def __name(self):
        return self.name
    def name(self, value:str):
        if not value:
            raise ValueError("Name cannot be empty")
        self.name = value


    @property
    def __author(self):
        return self.author


    def author(self, value):
        if not value:
            raise ValueError("Author cannot be empty")
        self.author = value


    def id(self):
        return self.id

    def __id(self, value:str):
        if not value:
            raise ValueError("ID cannot be empty")
        self.id = value



    def __str__(self):
        return f"<Recipe {self.name} with id {self.id} was created by {self.author} on {self.date}>"



recipe_test = Recipe("59", "Brian","Gordon Ramsay", "2025-08-05","Food")

print(recipe_test)

