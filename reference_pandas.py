import pandas

#### References
######################
######################
# https://pandas.pydata.org/pandas-docs/stable/comparison_with_sql.html
# https://pandas.pydata.org/pandas-docs/stable/comparison_with_r.html

#### Data types
######################
######################
# The datatype of a DataFrame column is a panas Series.
# Internally, a Series is a numpy array.
# Adding ,values to a Series returns the numpy array


#### Overview of a dataset
######################
######################
df.describe() # means, std, percentiles for all numeric cols
df.shape # equivalent to R's dim()
df.head()

#### Grouping and aggregating
######################
######################
df.groupby('col1').agg({'col1': 'mean'}) # removes NAs by default
df.groupby('col1').sum() # Sum of a numeric col

#### IO
######################
#####################
df.to_csv('foo.csv')
pd.read_csv('foo.csv')

#### Filtering
######################
######################
df.query('col1 == 1 & col2 == 1') # equivalent to dplyr filter()
df[['col1', 'col2']] # equivalent to dplyr select()

#### Sampling
######################
######################
df.sample(frac=0.01) # equivalent to dplyr sample_frac()

#### Sorting
######################
######################
df.sort_values('col1', ascending=False) # equiv to dplyr arrange()

#### Rename
######################
######################
df.rename(columns={'col1': 'col_one'})

#### Creating a new col from existing col
######################
######################
df.assign(c=df.a-df.b) # equiv to dplyr mutate()
