# Read the data
import pandas as pd
recipes_df = pd.read_json('https://s3-eu-west-1.amazonaws.com/dwh-test-resources/recipes.json', lines=True)
recipes_df.head()

# Get the ingredients column
ingredients = recipes_df['ingredients']

# Filter the recipes containing chilies 
df = recipes_df['ingredients'].apply(lambda x: 'chilies' in x.lower())

# Get the indexes of the recipes containing chilies
list_chilies = df[df].index.tolist()

# Creating a dataframe containing the recipies from the indexes
recipes_chilies = pd.DataFrame()
recipe_chilies = (recipes_df.loc[list_chilies])

# Save the recipes to csv
recipe_chilies.to_csv(r'~/recipes_chilies.csv', index=False)