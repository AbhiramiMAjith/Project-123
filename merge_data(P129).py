import pandas as pd

planet_df = pd.read_csv('planet_data.csv')
dwarf_df = pd.read_csv('new_scraped_data.csv')

dwarf_df.dropna(inplace=True)

merge_planets_df = pd.merge(planet_df,dwarf_df)#, on = 'id')
merge_planets_df.to_csv('merge_planets.csv', index = True, index_label = 'id')