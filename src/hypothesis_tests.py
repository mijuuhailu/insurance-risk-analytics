# Add T-Test Function
from scipy.stats import ttest_ind
from scipy.stats import chi2_contingency

def run_ttest(group_a, group_b):
    
    stat, p_value = ttest_ind(
        group_a,
        group_b,
        equal_var=False
    )
    
    return {
        "t_statistic": stat,
        "p_value": p_value
    }
#Add Chi-Square Function
def run_chi_square(contingency_table):
    
    chi2, p, dof, expected = chi2_contingency(
        contingency_table
    )
    
    return {
        "chi2": chi2,
        "p_value": p
    }