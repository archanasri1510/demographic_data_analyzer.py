import pandas as pd

def calculate_demographic_data(print_data=True):
    df = pd.read_csv("adult.data.csv")

    race_count = df['race'].value_counts()
    average_age_men = round(df[df['sex'] == 'Male']['age'].mean(), 1)
    percentage_bachelors = round((df['education'] == 'Bachelors').mean() * 100, 1)

    higher_edu = df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])
    lower_edu = ~higher_edu

    higher_edu_rich = round((df[higher_edu]['salary'] == '>50K').mean() * 100, 1)
    lower_edu_rich = round((df[lower_edu]['salary'] == '>50K').mean() * 100, 1)

    min_hours = df['hours-per-week'].min()
    rich_min_workers = df[(df['hours-per-week'] == min_hours) & (df['salary'] == '>50K')]
    rich_percentage = round(len(rich_min_workers) / len(df[df['hours-per-week'] == min_hours]) * 100, 1)

    country_rich_pct = df[df['salary'] == '>50K']['native-country'].value_counts(normalize=True) * 100
    highest_earning_country = country_rich_pct.idxmax()
    highest_earning_country_percentage = round(country_rich_pct.max(), 1)

    top_IN_occupation = df[(df['native-country'] == 'India') & (df['salary'] == '>50K')]['occupation'].mode()[0]

    if print_data:
        print("Race count:\n", race_count)
        print("Average age of men:", average_age_men)
        print("Percentage with Bachelors degrees:", percentage_bachelors)
        print("Percentage with higher education that earn >50K:", higher_edu_rich)
        print("Percentage without higher education that earn >50K:", lower_edu_rich)
        print("Min work hours:", min_hours)
        print("Rich percentage among those who work fewest hours:", rich_percentage)
        print("Country with highest % of rich:", highest_earning_country)
        print("Highest country rich %:", highest_earning_country_percentage)
        print("Top occupation in India for those who earn >50K:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_edu_rich,
        'lower_education_rich': lower_edu_rich,
        'min_work_hours': min_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage': highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }
