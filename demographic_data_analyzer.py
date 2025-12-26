import pandas as pd

def calculate_demographic_data(print_data=True):
    column_names = [
        'age', 'workclass', 'fnlwgt', 'education', 'education-num',
        'marital-status', 'occupation', 'relationship', 'race', 'sex',
        'capital-gain', 'capital-loss', 'hours-per-week',
        'native-country', 'salary'
    ]

    df = pd.read_csv(
        "adult.data.csv",
        names=column_names,
        skipinitialspace=True
    )

    # 1. How many people of each race
    race_count = df['race'].value_counts()

    # 2. Average age of men
    average_age_men = round(
        df[df['sex'] == 'Male']['age'].mean(), 1
    )

    # 3. Percentage with Bachelor's degree
    percentage_bachelors = round(
        (df['education'] == 'Bachelors').mean() * 100, 1
    )

    advanced_education = df['education'].isin(
        ['Bachelors', 'Masters', 'Doctorate']
    )

    higher_education = df[advanced_education]
    lower_education = df[~advanced_education]

    higher_education_rich = round(
        (higher_education['salary'] == '>50K').mean() * 100, 1
    )

    lower_education_rich = round(
        (lower_education['salary'] == '>50K').mean() * 100, 1
    )

    min_work_hours = df['hours-per-week'].min()

    min_workers = df[df['hours-per-week'] == min_work_hours]
    rich_percentage = round(
        (min_workers['salary'] == '>50K').mean() * 100, 1
    )

    country_salary = (
        df[df['salary'] == '>50K']['native-country']
        .value_counts()
        /
        df['native-country'].value_counts()
    ) * 100

    highest_earning_country = country_salary.idxmax()
    highest_earning_country_percentage = round(
        country_salary.max(), 1
    )

    top_IN_occupation = (
        df[
            (df['native-country'] == 'India') &
            (df['salary'] == '>50K')
        ]['occupation']
        .value_counts()
        .idxmax()
    )

    if print_data:
        print("Race count:\n", race_count)
        print("Average age of men:", average_age_men)
        print("Percentage with Bachelors:", percentage_bachelors)
        print("Higher education rich:", higher_education_rich)
        print("Lower education rich:", lower_education_rich)
        print("Min work hours:", min_work_hours)
        print("Rich percentage:", rich_percentage)
        print("Highest earning country:", highest_earning_country)
        print("Highest earning country percentage:",
              highest_earning_country_percentage)
        print("Top occupation in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage':
            highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }
