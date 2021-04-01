import COVID19Py
covid19 = COVID19Py.COVID19(data_source="jhu")

location = covid19.getLocationByCountryCode("CH", timelines=True)
print(location)
location_d = location[0]
for k, v in location_d.items():
    print(k, v)

#time formate i have ot search: 2020-07-28T00:00:00Z
# I have to change the first part
time_format = "T00:00:00Z"
confirmed_data = location_d['timelines']['confirmed']['timeline']
for k, v in confirmed_data.items():
    print(k, v)
print("Test")

