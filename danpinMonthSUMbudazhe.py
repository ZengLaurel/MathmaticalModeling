summ = 0

with open('database2all.txt', 'r', encoding='utf-8') as f:
    content = f.read()
    date = content.split()[0]
    dmbh = content.split()[1]
    month0 = 202010
    for line in content.split('\n'):
        if line.strip():
            if line.split()[4] == "否":
                date = line.split()[0]
                if "2020-07-01" <= date < "2020-08-01":
                    month = 202007
                elif "2020-08-01" <= date < "2020-09-01":
                    month = 202008
                elif "2020-09-01" <= date < "2020-10-01":
                    month = 202009
                elif "2020-10-01" <= date < "2020-11-01":
                    month = 202010
                elif "2020-11-01" <= date < "2020-12-01":
                    month = 202011
                elif "2020-12-01" <= date < "2021-01-01":
                    month = 202012
                elif "2021-01-01" <= date < "2021-02-01":
                    month = 202101
                elif "2021-02-01" <= date < "2021-03-01":
                    month = 202102
                elif "2021-03-01" <= date < "2021-04-01":
                    month = 202103
                elif "2021-04-01" <= date < "2021-05-01":
                    month = 202104
                elif "2021-05-01" <= date < "2021-06-01":
                    month = 202105
                elif "2021-06-01" <= date < "2021-07-01":
                    month = 202106
                elif "2021-07-01" <= date < "2021-08-01":
                    month = 202107
                elif "2021-08-01" <= date < "2021-09-01":
                    month = 202108
                elif "2021-09-01" <= date < "2021-10-01":
                    month = 202109
                elif "2021-10-01" <= date < "2021-11-01":
                    month = 202110
                elif "2021-11-01" <= date < "2021-12-01":
                    month = 202111
                elif "2021-12-01" <= date < "2022-01-01":
                    month = 202112
                elif "2022-01-01" <= date < "2022-02-01":
                    month = 202201
                elif "2022-02-01" <= date < "2022-03-01":
                    month = 202202
                elif "2022-03-01" <= date < "2022-04-01":
                    month = 202203
                elif "2022-04-01" <= date < "2022-05-01":
                    month = 202204
                elif "2022-05-01" <= date < "2022-06-01":
                    month = 202205
                elif "2022-06-01" <= date < "2022-07-01":
                    month = 202206
                elif "2022-07-01" <= date < "2022-08-01":
                    month = 202207
                elif "2022-08-01" <= date < "2022-09-01":
                    month = 202208
                elif "2022-09-01" <= date < "2022-10-01":
                    month = 202209
                elif "2022-10-01" <= date < "2022-11-01":
                    month = 202210
                elif "2022-11-01" <= date < "2022-12-01":
                    month = 202211
                elif "2022-12-01" <= date < "2023-01-01":
                    month = 202212
                elif "2023-01-01" <= date < "2023-02-01":
                    month = 202301
                elif "2023-02-01" <= date < "2023-03-01":
                    month = 202302
                elif "2023-03-01" <= date < "2023-04-01":
                    month = 202303
                elif "2023-04-01" <= date < "2023-05-01":
                    month = 202304
                elif "2023-05-01" <= date < "2023-06-01":
                    month = 202305
                elif "2023-06-01" <= date < "2023-07-01":
                    month = 202306
                if month0 != month:
                    with open('danpinMonthSUMbudazhe.txt', 'a', encoding='utf-8') as file:
                        file.write(str(dmbh) + '\n' + str(month0) + '\n' + str(summ) + '\n')
                        file.close()
                    summ = 0
                    dmbh = line.split()[1]
                month0 = month
                summ += float(line.split()[2])