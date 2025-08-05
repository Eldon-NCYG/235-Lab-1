class Category:

    def __init__(self, name: str, id: int):
        self.name = name

        self.id = id

        self.__recipes = []

    @property

    def name(self):

        return self.name

    @property

    def id(self):

        return self.id

    def add_recipe(self, recipe):

        if recipe in self.__recipes:

            raise ValueError("Recipe already added")

        self.__recipes.append(recipe)



    def __str__(self):

        return f"Category {self.id}: {self.name}"