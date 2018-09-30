import pandas as pd
app_train = pd.read_csv('public.train.csv')  # 读取训练数据
app_test = pd.read_csv('public.test.csv')  # 读取测试数据

power_a = app_train[u'电流A']*app_train[u'电压A']
power_a[0], app_train[u'功率A'][0]