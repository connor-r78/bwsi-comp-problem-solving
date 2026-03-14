# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py:percent
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.18.1
#   kernelspec:
#     display_name: cps
#     language: python
#     name: python3
# ---

# %% [markdown]
# # Intermediate Python: Class Inheritance

# %% [markdown]
# ## Review of Object Oriented Programming

# %% [markdown]
# ### What is OOP?
#
# **Object-Oriented Programming (OOP)** is a programming paradigm that organizes code around **objects** — bundles of data (attributes) and behaviors (methods) that work together.
#
# ### Quick Refresher
#
# If you need a review, check out these resources from the BWSI Intro Python course:
# - [Introduction to OOP](https://github.com/kxgallant/bwsi-intro-python/blob/main/mod6_object_oriented_programming/1_intro_to_oop.ipynb)
# - [Writing Classes](https://github.com/kxgallant/bwsi-intro-python/blob/main/mod6_object_oriented_programming/2_writing_classes.ipynb)
# - [OOP vs Functions](https://github.com/kxgallant/bwsi-intro-python/blob/main/mod6_object_oriented_programming/3_oop_vs_functions.ipynb)
#
# ---
#
# ### Why Use OOP?
#
# OOP is particularly useful when:
# - **Modeling real-world entities:** Cars, students, bank accounts, etc.
# - **Managing complex state:** When data and behaviors are tightly coupled
# - **Building reusable code:** Create blueprints (classes) that can be instantiated many times
# - **Organizing large projects:** Group related functionality together
#
# ---
#
# ### OOP vs. Functional Programming
#
# | Aspect | OOP | Functional Programming |
# |--------|-----|------------------------|
# | **Focus** | Objects with state and behavior | Pure functions and transformations |
# | **Data** | Encapsulated in objects | Passed as function arguments |
# | **State** | Objects maintain internal state | Avoids mutable state |
# | **Best For** | Modeling systems, simulations, GUIs | Data transformations, parallel processing |
#
# **Key Insight:** Python supports both paradigms! You can use OOP when modeling entities and their relationships, and functional approaches when transforming data. Many real-world programs use both.
#
# ---

# %% [markdown]
# ## Inheritance

# %% [markdown]
# ### What is Inheritance?
#
# **Inheritance** is a fundamental concept in OOP that allows a class to **inherit attributes and methods** from another class. This creates a parent-child relationship between classes.
#
# - **Parent Class (Base/Super Class):** The class being inherited from
# - **Child Class (Derived/Sub Class):** The class that inherits from the parent
#
# ---
#
# ### Why Use Inheritance?
#
# | Benefit | Description |
# |---------|-------------|
# | **Code Reuse** | Avoid repeating code by inheriting common functionality |
# | **Logical Hierarchy** | Model real-world "is-a" relationships (e.g., a GoldenRetriever *is a* Dog) |
# | **Extensibility** | Add specialized behavior to child classes without modifying the parent |
# | **Maintainability** | Update shared functionality in one place (the parent class) |
#
# ---
#
# ### The Three-Level Hierarchy
#
# It's important to understand the distinction between:
#
# 1. **Parent Class:** The general blueprint (e.g., `Dog`)
# 2. **Child Class:** A specialized version (e.g., `GoldenRetriever`, `Poodle`)
# 3. **Instance:** An actual object created from a class (e.g., `my_dog = GoldenRetriever("Buddy")`)
#
# ---

# %% [markdown]
# ### Basic Syntax
#
# To create a child class that inherits from a parent class:
#
# ```python
# class ChildClass(ParentClass):
#     def __init__(self, child_params, parent_params):
#         super().__init__(parent_params)  # Call parent's __init__
#         self.child_attribute = child_params
#     
#     def child_method(self):
#         # New method specific to child class
#         pass
# ```
#
# **Key Points:**
# - Use `super().__init__()` to call the parent class's constructor
# - Child classes can add new attributes and methods
# - Child classes can **override** parent methods by redefining them
#
# ---
#

# %% [markdown]
# ## Example: Dog Breeds
#
# Let's model different dog breeds using inheritance!
#
# ### Step 1: Create the Parent Class
#
# First, we'll create a general `Dog` class with attributes and methods common to all dogs.
#

# %%
class Dog:
    """A general Dog class with common attributes and methods"""
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def bark(self):
        return f"{self.name} says: Woof!"
    
    def get_info(self):
        return f"{self.name} is {self.age} years old"



# %%
# Create an instance of Dog
generic_dog = Dog("Rex", 5)
print(generic_dog.bark())
print(generic_dog.get_info())


# %% [markdown]
# ### Step 2: Create Child Classes
#
# Now we'll create specialized breed classes that inherit from `Dog` and add breed-specific attributes and behaviors.
#

# %%
class GoldenRetriever(Dog):
    """A Golden Retriever - friendly and loves water"""
    
    def __init__(self, name, age, loves_swimming=True):
        super().__init__(name, age)  # Call parent class constructor
        self.loves_swimming = loves_swimming
    
    def fetch(self):
        return f"{self.name} retrieves the ball!"
    
    def bark(self):
        # Override parent method with breed-specific behavior
        return f"{self.name} says: Woof woof! (friendly bark)"


class Poodle(Dog):
    """A Poodle - intelligent and elegant"""
    
    def __init__(self, name, age, haircut_style="standard"):
        super().__init__(name, age)
        self.haircut_style = haircut_style
    
    def perform_trick(self):
        return f"{self.name} does a fancy trick!"
    
    def bark(self):
        # Override with a different breed-specific behavior
        return f"{self.name} says: Yip yip! (high-pitched bark)"



# %%
# Create instances of child classes
buddy = GoldenRetriever("Buddy", 3)
princess = Poodle("Princess", 2, haircut_style="teddy bear")

print("=== Golden Retriever ===")
print(buddy.bark())           # Uses overridden method
print(buddy.fetch())          # Uses unique method
print(buddy.get_info())       # Inherits from parent
print(f"Loves swimming: {buddy.loves_swimming}")

print("\n=== Poodle ===")
print(princess.bark())        # Uses overridden method
print(princess.perform_trick())  # Uses unique method
print(princess.get_info())    # Inherits from parent
print(f"Haircut style: {princess.haircut_style}")


# %% [markdown]
# ### Key Observations
#
# **What happened here?**
#
# 1. **Inheritance:** Both `GoldenRetriever` and `Poodle` inherit from `Dog`
#    - They get `name`, `age`, and `get_info()` automatically
#    
# 2. **Extension:** Child classes add new attributes and methods
#    - `GoldenRetriever` adds `loves_swimming` and `fetch()`
#    - `Poodle` adds `haircut_style` and `perform_trick()`
#    
# 3. **Overriding:** Child classes redefine `bark()` with breed-specific behavior
#    - Each breed has its own unique bark!
#    
# 4. **The `super()` function:** Calls the parent class's `__init__()` 
#    - Ensures proper initialization of inherited attributes
#
# ---
#

# %% [markdown]
# ### Understanding: Class vs. Instance
#
# Let's clarify the three levels with our dog example:
#
# | Level | Type | Example | Description |
# |-------|------|---------|-------------|
# | **Level 1** | Parent Class | `Dog` | The general blueprint for all dogs |
# | **Level 2** | Child Class | `GoldenRetriever`, `Poodle` | Specialized blueprints for specific breeds |
# | **Level 3** | Instance | `buddy`, `princess` | Actual dog objects with specific data |
#
# **Think of it this way:**
# - `Dog` is like saying "dogs in general"
# - `GoldenRetriever` is like saying "golden retrievers as a breed"
# - `buddy = GoldenRetriever("Buddy", 3)` is a **specific** golden retriever named Buddy
#
# ---
#

# %% [markdown]
# ## Your Turn: Cat Exercise
#
# Now it's your turn to practice inheritance! Below is a skeleton of a `Cat` class. Your task is to:
#
# 1. Create a `Tuxedo` child class that inherits from `Cat`
# 2. Add at least one new attribute specific to Tuxedo cats
# 3. Add at least one new method specific to Tuxedo cats
# 4. Override the `meow()` method with a Tuxedo-specific meow
# 5. Create instances of both `Cat` and `Tuxedo` to demonstrate the difference
#
# ---
#
# ### Cat Parent Class (Given)
#

# %%
class Cat:
    """A general Cat class"""
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def meow(self):
        return f"{self.name} says: Meow!"
    
    def get_info(self):
        return f"{self.name} is {self.age} years old"


# %% [markdown]
# ### Task 1: Create a Tuxedo Child Class
#
# **Hints:**
# - Tuxedo cats are known for their black and white coloring (like a tuxedo suit!)
# - You might add attributes like `has_bow_tie` or `white_chest`
# - You could add a method like `show_off_tuxedo()` or `look_fancy()`
# - Remember to use `super().__init__()` to initialize parent attributes
#
# Write your code in the cell below:
#

# %%
# TODO: Create your Tuxedo class here

class Tuxedo(Cat):

    def __init__(self, name, age, has_bow_tie, has_white_chest):
        super().__init__(name, age)
        self.has_bow_tie = has_bow_tie
        self.has_white_chest = has_white_chest

    def show_off_tuxedo(self):
        return f'{self.name} shows off tuxedo'
 
    def look_fancy(self):
        return f'{self.name} looks fancy'

# %% [markdown]
# ### Task 2: Create Instances
#
# Create instances to demonstrate the difference between `Cat` and `Tuxedo`:
#
# 1. Create a generic `Cat` instance
# 2. Create a `Tuxedo` instance
# 3. Call methods on both to show the differences
#

# %%
# TO DO: Create your instances here and demonstrate the differences

# Example structure:
# generic_cat = Cat("Whiskers", 4)
# tuxedo_cat = Tuxedo("Mr. Mittens", 3, ...)

# print(generic_cat.meow())
# print(tuxedo_cat.meow())
# ...


# %%
# Create instances
whiskers = Cat("Whiskers", 4)
bond = Tuxedo("Bond", 4, True, True);

print("=== Generic Cat ===")

print(whiskers.meow());
print(whiskers.get_info());

print("\n=== Tuxedo Cat ===")

print(bond.meow());
print(bond.get_info());
print(bond.look_fancy());
print(bond.show_off_tuxedo(), '\n')

# %% [markdown]
# ---
#
#
# ### Multiple Inheritance
#
# Python supports **multiple inheritance**, where a class can inherit from multiple parent classes:
#
# ```python
# class ChildClass(Parent1, Parent2):
#     pass
# ```
#
# **Note:** Multiple inheritance can get complex. Use it carefully and consider alternative design patterns when possible.
#
# ---
#
# ### The `isinstance()` Function
#
# You can check if an object is an instance of a class or its parent:
#

# %%
# Using isinstance() to check object types
print("buddy is a GoldenRetriever:", isinstance(buddy, GoldenRetriever))
print("buddy is a Dog:", isinstance(buddy, Dog))  # True! GoldenRetriever IS A Dog
print("buddy is a Cat:", isinstance(buddy, Cat))  # False

print("\ngeneric_dog is a Dog:", isinstance(generic_dog, Dog))
print("generic_dog is a GoldenRetriever:", isinstance(generic_dog, GoldenRetriever))  # False


# %% [markdown]
# ---
#
# ## Best Practices for Inheritance
#
# ### 1. Use the "Is-A" Test
# Only use inheritance when there's a true "is-a" relationship:
# - "A GoldenRetriever **is a** Dog" → Good use of inheritance
# - "A Car **has a** Engine" → Use composition instead (store engine as an attribute)
#
# ### 2. Keep Hierarchies Shallow
# Avoid deep inheritance chains (parent → child → grandchild → ...). They become hard to understand and maintain.
#
# ### 3. Don't Override Methods Unnecessarily
# Only override methods when you need different behavior. Inherit when possible!
#
# ### 4. Use `super()` Properly
# Always call `super().__init__()` in child class constructors to properly initialize parent attributes.
#
# ### 5. Document Your Classes
# Use docstrings to explain what each class does and how it relates to its parent.
#
# ---
#

# %% [markdown]
# ## Real-World Applications
#
# ### Where is Inheritance Used?
#
# | Domain | Example Hierarchy |
# |--------|------------------|
# | **Game Development** | `Character` → `Player`, `Enemy`, `NPC` |
# | **GUI Programming** | `Widget` → `Button`, `TextBox`, `Slider` |
# | **Web Development** | `HTTPRequest` → `GetRequest`, `PostRequest` |
# | **Scientific Computing** | `Model` → `LinearModel`, `NeuralNetwork` |
# | **Data Science** | `Estimator` → `Classifier`, `Regressor` (sklearn) |
#
# ### Example: sklearn Machine Learning
#
# Libraries like `scikit-learn` use inheritance extensively:
#
# ```python
# from sklearn.base import BaseEstimator
#
# class LinearRegression(BaseEstimator):
#     # Inherits fit(), predict(), etc.
#     pass
#
# class LogisticRegression(BaseEstimator):
#     # Inherits the same interface
#     pass
# ```
#
# This creates a **consistent interface** across different models!
#
# ---
#

# %% [markdown]
# ## Quick Review Questions
#
# **Discuss with a partner or think through:**
#
# 1. **What is the difference between a parent class, a child class, and an instance?**
#
# 2. **When should you use inheritance vs. composition?**
#    - Hint: Think about the "is-a" vs. "has-a" relationship
#
# 3. **What does `super().__init__()` do and why is it important?**
#
# 4. **Can you override any method in a child class? Should you?**
#
# 5. **Give an example of inheritance from your own interests** (sports, music, technology, etc.)
#
# ---
#
