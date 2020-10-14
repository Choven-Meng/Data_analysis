import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np
import scipy as sp
from scipy import stats
from matplotlib.ticker import PercentFormatter


def catPlot(df,feature,target, figsize=(14, 6), save=False, filename=None):
    feature_name = feature.capitalize()
    df_temp = df.copy()
    df_temp[feature] = df_temp[feature].fillna(-1)
    tmp = pd.crosstab(df_temp[feature], df_temp[target], normalize='index') * 100
    tmp = tmp.reset_index()
    tmp.rename(columns={0:'NoFraud', 1:'Fraud'}, inplace=True)

    plt.figure(figsize=figsize)
    plt.suptitle(f'{feature_name} Distributions', fontsize=22)
    
    # 柱形图：该特征下各类型占比
    plt.subplot(121)
    g = sns.countplot(x=feature, data=df_temp.sort_values(by=feature))
    plt.xticks(rotation=60)
    # plt.legend(title='Fraud', loc='upper center', labels=['No', 'Yes'])
    g.set_title(f"{feature_name} Distribution", fontsize=19)
    g.set_xlabel(feature_name, fontsize=17)
    g.set_ylabel("Count", fontsize=17)
    for p in g.patches:
        height = p.get_height()
        g.text(p.get_x()+p.get_width()/2.,
                height + 3,
                '{:1.2f}%'.format(height/df.shape[0]*100),
                ha="center", fontsize=14) 
    # 柱形图&折线图：目标值下该特征各类型数量&目标值为‘1’的占比(当折线图的点与柱形图差距高，认为欺诈风险高)
    plt.subplot(122)
    g1 = sns.countplot(x=feature, hue=target, data=df_temp.sort_values(by=feature))
    plt.xticks(rotation=60)
    plt.legend(title='Fraud', loc='best', labels=['No', 'Yes'])
    gt = g1.twinx()
    gt = sns.pointplot(x=feature, y='Fraud', data=tmp.sort_values(by=feature), 
                       color='black', scale=0.5,
                       legend=False)
    gt.set_ylabel("% of Fraud Transactions", fontsize=16)

    g1.set_title(f"{feature_name} by Target(isFraud)", fontsize=19)
    g1.set_xlabel(feature_name, fontsize=17)
    g1.set_ylabel("Count", fontsize=17)
    #plt.xticks(rotation=60)
    plt.subplots_adjust(hspace = 0.6, top = 0.85)
    if save:
        if filename:
            plt.savefig(f'../pics/{filename}.png', bbox_inches='tight', dpi=300)
        else:
            plt.savefig(f'../pics/{feature_name}.png', bbox_inches='tight', dpi=300)
    plt.show()

# 箱型图（查看特征值的分布情况，删除异常点）
def boxPlot(df,feature,target, save=False, filename=None):
    feature_name = feature.capitalize()
    df_temp = df.copy()
    df_temp[feature] = df_temp[feature].fillna(-1)
    fig, axs = plt.subplots(1, 2, tight_layout=True, figsize=(8, 4))
    axs[0].boxplot(df_temp.loc[df_temp[target] == 0, feature])
    axs[0].set_xlabel('NoFraud')
    axs[1].boxplot(df_temp.loc[df_temp[target] == 1, feature])
    axs[1].set_xlabel('Fraud')
    plt.suptitle(feature_name)
    if save:
        if filename:
            plt.savefig(f'../pics/{filename}.png', bbox_inches='tight', dpi=300)
        else:
            plt.savefig(f'../pics/{feature_name}.png', bbox_inches='tight', dpi=300)
    plt.show()
    
# 目标值在该特征下各类别的占比（如果target的两条曲线在该特征上的走势相似，说明该特征并没有很好的区分效果，可以考虑删除，一般配合箱型图）
def distPlot(df,feature,target, save=False, filename=None):
    feature_name = feature.capitalize()
    df_temp = df.copy()
    df_temp[feature] = df_temp[feature].fillna(-1)
    g = sns.distplot(df_temp[df_temp[target] == 1][feature], label='Fraud')
    g = sns.distplot(df_temp[df_temp[target] == 0][feature], label='NoFraud')
    g.legend()
    g.set_title(f"{feature_name} Distribution by Target", fontsize=20)
    g.set_xlabel(feature_name, fontsize=18)
    g.set_ylabel("Probability", fontsize=18)
    if save:
        if filename:
            plt.savefig(f'../pics/{filename}.png', bbox_inches='tight', dpi=300)
        else:
            plt.savefig(f'../pics/{feature_name}.png', bbox_inches='tight', dpi=300)
    plt.show()
