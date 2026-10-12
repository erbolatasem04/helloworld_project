actor1_name    = "Leonardo DiCaprio"
actor1_country = "США"
actor1_birth   = 1974

actor2_name    = "Brad Pitt"
actor2_country = "США"
actor2_birth   = 1963

actor3_name    = "Асель Садвакасова"
actor3_country = "Казахстан"
actor3_birth   = 1985

actor4_name    = "Санжар Мади"
actor4_country = "Казахстан"
actor4_birth   = 1986

years = [2026, 2000, 1990]

print("========== АНКЕТА АКТЕРОВ ===========")

print(f"{actor1_name} ({actor1_country})")
age1_in_2026 = 2026 - actor1_birth
print("Возраст в 2026:", age1_in_2026)
age1_in_2000 = 2000 - actor1_birth
print("Возраст в 2000:", age1_in_2000)
age1_in_1990 = 1990 - actor1_birth
print("Возраст в 1990:", age1_in_1990)
age1_in_month = age1_in_2026 * 12
print('Возраст в месяцах (на 2026):', age1_in_month)



print(f"{actor2_name} ({actor2_country})")
age2_in_2026 = 2026 - actor2_birth
print("Возраст в 2026:", age2_in_2026)
age2_in_2000 = 2000 - actor2_birth
print("Возраст в 2000:", age2_in_2000)
age2_in_1990 = 1990 - actor2_birth
print("Возраст в 1990:", age2_in_1990)
age2_in_month = age2_in_2026 * 12
print('Возраст в месяцах (на 2026):', age2_in_month)



print(f"{actor3_name} ({actor3_country})")
age3_in_2026 = 2026 - actor3_birth
print("Возраст в 2026:", age3_in_2026)
age3_in_2000 = 2000 - actor3_birth
print("Возраст в 2000:", age3_in_2000)
age3_in_1990 = 1990 - actor3_birth
print("Возраст в 1990:", age3_in_1990)
age3_in_month = age3_in_2026 * 12
print('Возраст в месяцах (на 2026):', age3_in_month)

print(f"{actor4_name} ({actor4_country})")
age4_in_2026 = 2026 - actor4_birth
print("Возраст в 2026:", age4_in_2026)
age4_in_2000 = 2000 - actor4_birth
print("Возраст в 2000:", age4_in_2000)
age4_in_1990 = 1990 - actor4_birth
print("Возраст в 1990:", age3_in_1990)
age4_in_month = age4_in_2026 * 12
print('Возраст в месяцах (на 2026):', age4_in_month)


print('=== ИТОГИ ===')
sum_in_2026 = age1_in_2026 + age2_in_2026 + age3_in_2026  + age4_in_2026
median_age_2026 = sum_in_2026 / 4
max_age = max(age1_in_2026 , age2_in_2026 , age3_in_2026, age4_in_2026,)
min_age = min(age1_in_2026 , age2_in_2026 , age3_in_2026, age4_in_2026,)
difference_in_2026 = max_age - min_age
print('Суммарный возраст в 2026:' , sum_in_2026)
print('Средний возраст в 2026:', median_age_2026)
if age1_in_2026 == max_age :
    print(f'Cамый старший : {actor1_name} ({max_age}')
elif age2_in_2026 == max_age :
    print(f'Самый старший : {actor2_name} ({max_age})')
elif age3_in_2026 == max_age :
    print(f'Самый старший : {actor3_name} ({max_age})')
else :
    print(f'Самый старший : {actor4_name} ({max_age})')


if age1_in_2026 == min_age :
    print(f'Cамый старший : {actor1_name} ({min_age}')
elif age2_in_2026 == min_age :
    print(f'Самый старший : {actor2_name} ({min_age})')
elif age3_in_2026 == min_age :
    print(f'Самый старший : {actor3_name} ({min_age})')
else :
    print(f'Самый старший : {actor4_name} ({min_age})')

print('=== ОТЧЕТ ===')
print(f'В 2026 году 4 актёра имеют средний возраст {median_age_2026}. Самый старший — Brad Pitt ({max_age}), самый младший — Санжар Мади ({min_age}).')