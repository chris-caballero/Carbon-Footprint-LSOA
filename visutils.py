import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from zipfile import ZipFile

def get_avg_dfs(df, cols, grouped=False):
    avg_dfs = {}
    for col in cols:
        data = []
        for i in range(9):
            colname = col + f'_201{i}'
            if not grouped:
                data.append(df[colname].mean())
            else:
                data.append(df[colname].mean().iloc[0])
        avg_dfs[col] = pd.DataFrame(
            data=data,
            index=[f'201{i}' for i in range(9)],
            columns=[col + '_yearly'])
    return avg_dfs

def plot_yearly_distribution(df):
    # sns.set_style('white')
    sns.set(rc={'figure.facecolor':'#dcdcf2', 'axes.facecolor':'#f5f5f7'})
    axs = plt.subplots(2, 2, figsize=(10, 8))[1]
    for i, name in enumerate(df.keys()):
        for col in df[name].columns:
            ax = axs[i//2][i%2]
            ax.bar(df[name].index, df[name][col], color=sns.color_palette('pastel', 4)[i])

            # Customize the plot
            ax.set_xlabel('Year')
            ax.set_ylabel('kg CO2e per person')
            ax.set_title(f'Distribution of:\n{col}')

            # # Rotate the x-axis labels for better readability (optional)
            ax.set_xticklabels(ax.get_xticklabels(), rotation=45)
            
    plt.suptitle('Distribution of key attributes over the years (2010-2018)')
    plt.tight_layout(pad=2)
    plt.show()
    
def get_kgco2e_df(df, cols, grouped=False, idx=0):
    data = []
    kgco2e_cols = []
    
    for col in cols:
        if 'kgco2' in col:
            kgco2e_cols.append(col)
            
    kgco2e_cols.remove('total_kgco2e_percap')
    
    for col in kgco2e_cols:
        if not grouped:
            data.append(df[col].mean())
        else:
            mean = df[col].mean().iloc[idx]
            data.append(mean)
            
    if grouped:
        data.append(df[kgco2e_cols[0]].sum().index[idx])
    else:
        data.append(df['LA name (2018 boundaries)'].iloc[idx])
    
    kgco2e_cols.append('LA Name')
        
    avg_kgco2e_df = pd.DataFrame(
        data=[data],
        columns=kgco2e_cols)

    return avg_kgco2e_df, kgco2e_cols

def plot_stacked_kgco2e(df, cols, labels=['England']):
    # sns.set_style('white')
    sns.set(rc={'figure.facecolor':'#dcdcf2', 'axes.facecolor':'#f5f5f7'})
    
    ax = plt.subplots(figsize=(7, 5))[1]
    ax.set_title(df['LA Name'].iloc[0])
    df.plot(kind='bar', stacked=True, color=sns.color_palette('pastel'), ax=ax)

    plt.ylabel('kg CO2e per person')
    plt.legend(title='Categories')
    ax.set_xticklabels([f'{label} Average' for label in labels], rotation=0)

    handles, _ = ax.get_legend_handles_labels()

    labels = [col.replace('_kgco2e_percap', '') for col in cols]
    labels = [col.replace('_shelter', '') for col in labels]
    labels = [col.replace('_all', '') for col in labels]

    plt.legend(handles, labels, loc='upper center', ncol=4, columnspacing=3, bbox_to_anchor=(0.48, -0.1))
    plt.tight_layout()
    plt.show()