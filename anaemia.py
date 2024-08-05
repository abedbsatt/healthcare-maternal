# %%
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# %%
file_path = "C:\\Users\\hossc\\Downloads\\maternal_and_reproductive_health_indicators_lbn (1).csv"

# %% [markdown]
# Data Cleaning

# %%
data = pd.read_csv(file_path, skiprows=1)

# %%
data.columns = ['GHO_CODE', 'GHO_DISPLAY', 'GHO_URL', 'YEAR_DISPLAY', 'STARTYEAR', 
                'ENDYEAR', 'REGION_CODE', 'REGION_DISPLAY', 'COUNTRY_CODE', 
                'COUNTRY_DISPLAY', 'DIMENSION_TYPE', 'DIMENSION_CODE', 
                'DIMENSION_NAME', 'Numeric', 'Value', 'Low', 'High']


# %%
data['YEAR_DISPLAY'] = pd.to_numeric(data['YEAR_DISPLAY'], errors='coerce')
data['Numeric'] = pd.to_numeric(data['Numeric'], errors='coerce')
data['Low'] = pd.to_numeric(data['Low'], errors='coerce')
data['High'] = pd.to_numeric(data['High'], errors='coerce')


# %%
data.dropna(subset=['YEAR_DISPLAY', 'Numeric'], inplace=True)

# %%
indicator_code = 'NUTRITION_ANAEMIA_NONPREGNANT_NUM'
filtered_data = data[data['GHO_CODE'] == indicator_code]

# %%
unique_years = filtered_data[['YEAR_DISPLAY', 'Numeric']].drop_duplicates().sort_values(by='YEAR_DISPLAY')
unique_years

# %% [markdown]
# Anemia in Non-Pregnant Women

# %%
plt.figure(figsize=(12, 6))
sns.lineplot(x='YEAR_DISPLAY', y='Numeric', data=filtered_data, marker='o')

plt.xticks(ticks=filtered_data['YEAR_DISPLAY'].unique(), 
           labels=filtered_data['YEAR_DISPLAY'].unique().astype(int), 
           rotation=0, fontweight='bold')

plt.yticks(fontweight='bold')

plt.title('Trend of Number of Non-Pregnant Women with Anemia Over Years', fontweight='bold')
plt.xlabel('Year', fontweight='bold')
plt.ylabel('Number of Women', fontweight='bold')
plt.grid(False)

sns.set(style="whitegrid")
sns.despine(left=True, bottom=True)
plt.tight_layout()
plt.show()


# %% [markdown]
# Trend of Number of Pregnant Women (Aged 15-49 Years) with Anemia Over Years

# %%
indicator_code = 'NUTRITION_ANAEMIA_PREGNANT_NUM'
filtered_data = data[data['GHO_CODE'] == indicator_code]

# %%
plt.figure(figsize=(12, 6))
sns.lineplot(x='YEAR_DISPLAY', y='Numeric', data=filtered_data, marker='o')

plt.xticks(ticks=filtered_data['YEAR_DISPLAY'].unique(), 
           labels=filtered_data['YEAR_DISPLAY'].unique().astype(int), 
           rotation=0, fontweight='bold')

plt.yticks(fontweight='bold')

plt.title('Trend of Number of Pregnant Women (Aged 15-49 Years) with Anemia Over Years', fontweight='bold')
plt.xlabel('Year', fontweight='bold')
plt.ylabel('Number of Women', fontweight='bold')
plt.grid(False)

sns.set(style="whitegrid")
sns.despine(left=True, bottom=True)
plt.tight_layout()
plt.show()

# %%
indicator_code_1 = 'NUTRITION_ANAEMIA_NONPREGNANT_NUM'
indicator_code_2 = 'NUTRITION_ANAEMIA_PREGNANT_NUM'

filtered_data_1 = data[data['GHO_CODE'] == indicator_code_1]
filtered_data_2 = data[data['GHO_CODE'] == indicator_code_2]

# Merge the two datasets on 'YEAR_DISPLAY' to enable comparison
comparison_data = pd.merge(filtered_data_1[['YEAR_DISPLAY', 'Numeric']], 
                           filtered_data_2[['YEAR_DISPLAY', 'Numeric']], 
                           on='YEAR_DISPLAY', 
                           suffixes=('_non_pregnant', '_pregnant'))

# %%
fig, ax1 = plt.subplots(figsize=(12, 6))

# Plot for non-pregnant women
sns.lineplot(x='YEAR_DISPLAY', y='Numeric_non_pregnant', data=comparison_data, marker='o', ax=ax1, color='blue', label='Non-Pregnant Women')
ax1.set_xlabel('Year', fontweight='bold')
ax1.set_ylabel('Number of Non-Pregnant Women', fontweight='bold', color='blue')
ax1.tick_params(axis='y', labelcolor='blue')
ax1.set_xticks(comparison_data['YEAR_DISPLAY'].unique())
ax1.set_xticklabels(comparison_data['YEAR_DISPLAY'].unique().astype(int), fontweight='bold')
ax1.grid(False)

# Add a second y-axis for pregnant women
ax2 = ax1.twinx()
sns.lineplot(x='YEAR_DISPLAY', y='Numeric_pregnant', data=comparison_data, marker='o', ax=ax2, color='orange', label='Pregnant Women')
ax2.set_ylabel('Number of Pregnant Women', fontweight='bold', color='orange')
ax2.tick_params(axis='y', labelcolor='orange')
ax2.grid(False)

# Titles and labels with bold font
plt.title('Comparison of Number of Women with Anemia Over Years', fontweight='bold')

# Combine legends from both plots
lines_1, labels_1 = ax1.get_legend_handles_labels()
lines_2, labels_2 = ax2.get_legend_handles_labels()
ax2.legend(lines_1 + lines_2, labels_1 + labels_2, loc='upper left', fontsize='large', title_fontsize='13')

fig.tight_layout()
plt.show()

# %% [markdown]
# Streamlit

# %%
def load_and_clean_data(file_path):
    data = pd.read_csv(file_path, skiprows=1)
    data.columns = ['GHO_CODE', 'GHO_DISPLAY', 'GHO_URL', 'YEAR_DISPLAY', 'STARTYEAR', 
                    'ENDYEAR', 'REGION_CODE', 'REGION_DISPLAY', 'COUNTRY_CODE', 
                    'COUNTRY_DISPLAY', 'DIMENSION_TYPE', 'DIMENSION_CODE', 
                    'DIMENSION_NAME', 'Numeric', 'Value', 'Low', 'High']

    data['YEAR_DISPLAY'] = pd.to_numeric(data['YEAR_DISPLAY'], errors='coerce')
    data['Numeric'] = pd.to_numeric(data['Numeric'], errors='coerce')
    data['Low'] = pd.to_numeric(data['Low'], errors='coerce')
    data['High'] = pd.to_numeric(data['High'], errors='coerce')

    data.dropna(subset=['YEAR_DISPLAY', 'Numeric'], inplace=True)
    return data

def plot_anemia_trends():
    file_path = "C:\\Users\\hossc\\Downloads\\maternal_and_reproductive_health_indicators_lbn (1).csv"
    data = load_and_clean_data(file_path)
    indicator_code = 'NUTRITION_ANAEMIA_NONPREGNANT_NUM'
    filtered_data = data[data['GHO_CODE'] == indicator_code]
    plt.figure(figsize=(12, 6))
    sns.lineplot(x='YEAR_DISPLAY', y='Numeric', data=filtered_data, marker='o')

    plt.xticks(ticks=filtered_data['YEAR_DISPLAY'].unique(), 
               labels=filtered_data['YEAR_DISPLAY'].unique().astype(int), 
               rotation=0, fontweight='bold')

    plt.yticks(fontweight='bold')

    plt.title('Trend of Number of Non-Pregnant Women with Anemia Over Years', fontweight='bold')
    plt.xlabel('Year', fontweight='bold')
    plt.ylabel('Number of Women', fontweight='bold')
    plt.grid(False)

    sns.set(style="whitegrid")
    sns.despine(left=True, bottom=True)
    plt.tight_layout()
    return plt

def plot_anemia_comparison():
    file_path = "C:\\Users\\hossc\\Downloads\\maternal_and_reproductive_health_indicators_lbn (1).csv"
    data = load_and_clean_data(file_path)
    
    indicator_code_1 = 'NUTRITION_ANAEMIA_NONPREGNANT_NUM'
    indicator_code_2 = 'NUTRITION_ANAEMIA_PREGNANT_NUM'

    filtered_data_1 = data[data['GHO_CODE'] == indicator_code_1]
    filtered_data_2 = data[data['GHO_CODE'] == indicator_code_2]

    comparison_data = pd.merge(filtered_data_1[['YEAR_DISPLAY', 'Numeric']], 
                               filtered_data_2[['YEAR_DISPLAY', 'Numeric']], 
                               on='YEAR_DISPLAY', 
                               suffixes=('_non_pregnant', '_pregnant'))
    
    fig, ax1 = plt.subplots(figsize=(12, 6))

    sns.lineplot(x='YEAR_DISPLAY', y='Numeric_non_pregnant', data=comparison_data, marker='o', ax=ax1, color='blue', label='Non-Pregnant Women')
    ax1.set_xlabel('Year', fontweight='bold')
    ax1.set_ylabel('Number of Non-Pregnant Women', fontweight='bold', color='blue')
    ax1.tick_params(axis='y', labelcolor='blue')
    ax1.set_xticks(comparison_data['YEAR_DISPLAY'].unique())
    ax1.set_xticklabels(comparison_data['YEAR_DISPLAY'].unique().astype(int), fontweight='bold')
    ax1.grid(False)

    ax2 = ax1.twinx()
    sns.lineplot(x='YEAR_DISPLAY', y='Numeric_pregnant', data=comparison_data, marker='o', ax=ax2, color='orange', label='Pregnant Women')
    ax2.set_ylabel('Number of Pregnant Women', fontweight='bold', color='orange')
    ax2.tick_params(axis='y', labelcolor='orange')
    ax2.grid(False)

    plt.title('Comparison of Number of Women with Anemia Over Years', fontweight='bold')

    # Combine legends from both plots
    lines_1, labels_1 = ax1.get_legend_handles_labels()
    lines_2, labels_2 = ax2.get_legend_handles_labels()
    ax2.legend(lines_1 + lines_2, labels_1 + labels_2, loc='upper left', fontsize='large', title_fontsize='13')

    fig.tight_layout()
    return plt


