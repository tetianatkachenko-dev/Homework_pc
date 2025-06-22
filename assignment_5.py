import requests
import pandas as pd

params = {
    'latitude': 50.4547,
    'longitude': 30.5238,
    'start_date': '2025-06-22',
    'end_date': '2025-06-29',
    'hourly': ['temperature_2m', 'wind_speed_10m']
}

data_json = requests.get('https://api.open-meteo.com/v1/forecast', params=params).json()

df = pd.DataFrame({
    'time': data_json['hourly']['time'],
    'temperature': data_json['hourly']['temperature_2m'],
    'windspeed': data_json['hourly']['wind_speed_10m']
})

df_first_3_days = df[(df['time'] >= '2025-06-22') & (df['time'] <= '2025-06-25')]

min_temp = df_first_3_days['temperature'].min()
max_temp = df_first_3_days['temperature'].max()
mean_temp = df_first_3_days['temperature'].mean()

print(f'Мінімальна температура за найближчі 3 дні {min_temp}. \nМаксимальна температура за найближчі 3 дні {max_temp}. \nСередня температура за найближчі 3 дні {mean_temp}.')

mean_windspeed = df_first_3_days['windspeed'].mean()
hours = (df_first_3_days['windspeed'] > mean_windspeed).sum()

print(f'Середня швидкість вітру за 3 дні {mean_windspeed}. {hours} годин, під час яких швидкість вітру була більша за середню.')
