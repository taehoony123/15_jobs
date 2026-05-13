import csv
from scrapper import search_incruit
from scrapper import search_saramin

def save_to_csv(jobs):
    with open('download.csv', 'w', encoding='cp949') as file:
        csv_writer = csv.writer(file)
        csv_writer.writerow(['No','회사', '공고제목', '지역', '경력','링크'])

        for i, job in enumerate(jobs):
            csv_writer.writerow([i + 1, job['company'], job['title'], job['location'], job['career'], job['link']])
    