
import pandas as pd 
import openpyxl
import xlsxwriter

xls_imp = pd.ExcelFile('India_Imports_2011-12_And_2012-13.xls')
xls_exp = pd.ExcelFile('India_Exports_2011-12_And_2012-13.xls')

df_imp = xls_imp.parse()
df_exp = xls_exp.parse()


top_imp =df_imp.groupby('Country').sum().sort_values(by ='Value-INR-2011-12',ascending=False).head().reset_index()
#print("\n1.a -----------------------------------------------")
#print("Top five importers:\n")

top_imp = top_imp[['Country']]

#print(top_imp.to_string(index=False))


writer = pd.ExcelWriter('173050046_solution.xlsx', engine='xlsxwriter')

# Convert the dataframe to an XlsxWriter Excel object.
top_imp.to_excel(writer, sheet_name='Q1_imports',index=False)
worksheet = writer.sheets['Q1_imports']
worksheet.set_column('A:A', 18)



top_exp =df_exp.groupby('Country').sum().sort_values(by ='Value-INR-2011-12',ascending=False).head()['Value-INR-2011-12'].reset_index()
#print("\n1.b -----------------------------------------------")
#print("Top five Exporters:\n")
top_exp = top_exp[['Country']]
#print(top_exp)

top_exp.to_excel(writer, sheet_name='Q1_exports',index=False)
worksheet = writer.sheets['Q1_exports']
worksheet.set_column('A:A', 18)


#2)Top five import and export commodities.

top_comm_imp =df_imp.groupby('Commodity').sum().sort_values(by ='Value-INR-2011-12',ascending=False).head()['Value-INR-2011-12'].reset_index()
#print("\n2.a -----------------------------------------------")
#print("Top five import commodities : \n")
top_comm_imp = top_comm_imp[['Commodity']]
#print(top_comm_imp);
top_comm_imp.to_excel(writer, sheet_name='Q2_imports',index=False)
worksheet = writer.sheets['Q2_imports']
worksheet.set_column('A:A', 30)

top_comm_exp =df_exp.groupby('Commodity').sum().sort_values(by ='Value-INR-2011-12',ascending=False).head()['Value-INR-2011-12'].reset_index()
#print("\n2.b -----------------------------------------------")
#print("Top five Export commodities : \n")
top_comm_exp = top_comm_exp[['Commodity']]
#print(top_comm_exp);
top_comm_exp.to_excel(writer, sheet_name='Q2_exports',index=False)
worksheet = writer.sheets['Q2_exports']
worksheet.set_column('A:A', 30)

#3)Total imports, total exports, export/import ratio, export-import for each country.

importers = df_imp.groupby('Country')['Value-INR-2011-12'].agg([pd.np.sum])
importers = importers.rename(columns={'sum': 'Total imports'})

exporters = df_exp.groupby('Country')['Value-INR-2011-12'].agg([pd.np.sum])
exporters = exporters.rename(columns={'sum': 'Total exports'})

imp_exp = pd.concat([importers,exporters],axis=1)
imp_exp=imp_exp.fillna(0)



#imp_exp = pd.merge(importers, exporters, on='Country', how='inner')

imp_exp['Export/import'] = imp_exp['Total exports'] / imp_exp['Total imports']
imp_exp['Expots-imports(Trade deficit)'] = imp_exp['Total exports'] - imp_exp['Total imports']
#imp_exp.reset_index()
imp_exp = imp_exp.reset_index()
imp_exp = imp_exp.rename(columns={'index':'Country'})
#print("\n3. -----------------------------------------------")
#print("Total imports, total exports, export/import ratio, export-import for each country: \n")
#print(imp_exp)
imp_exp.to_excel(writer, sheet_name='Q3',index=False)
worksheet = writer.sheets['Q3']
worksheet.set_column('A:E', 18)

imp_exp = imp_exp.rename(columns={'Total exports':'Total_exports'})

#4)All countries to whom our export is more than Rs 10,000 Cr.
big_exporter = imp_exp.query('Total_exports>1e+11')
#big_exporter = imp_exp[imp_exp['Total exports'] > 1e+11]
big_exporter = big_exporter.rename(columns={'Total_exports': 'Exports(INR)','Total imports':'Imports(INR)'})
big_exporter = big_exporter.reset_index()
#print("\n4. -----------------------------------------------")
#print("All countries to whom our export is more than Rs 10,000 Cr: \n")
big_exporter4= big_exporter[['Country']]
#print(big_exporter[['Country','Exports(INR)']])
big_exporter4.to_excel(writer, sheet_name='Q4',index=False)
worksheet = writer.sheets['Q4']
worksheet.set_column('A:B', 18)

#5) Save tCountry', 'Exports', 'Imports'he answer to 4 in a new table. Rename the columns of this table to: 
#Country', 'Exports', 'Imports'


#print("\n5. -----------------------------------------------")

big_exporter5= big_exporter[['Country','Imports(INR)','Exports(INR)']]
#print(big_exporter5)
big_exporter5.to_excel(writer, sheet_name='Q5',index=False)
worksheet = writer.sheets['Q5']
worksheet.set_column('A:C', 18)

#print("\n6. -----------------------------------------------")

big_exporter = pd.melt(big_exporter, id_vars=['Country'], value_vars=['Imports(INR)','Exports(INR)'],var_name='Transaction', value_name='Value(INR)')
big_exporter = big_exporter.sort_values(by = 'Value(INR)', ascending = False).head(10)
big_exporter = big_exporter.reset_index()
big_exporter6=big_exporter[['Country','Transaction','Value(INR)']]
#print(big_exporter[['Country','Transaction','Value(INR)']])
big_exporter6.to_excel(writer, sheet_name='Q6',index=False)
worksheet = writer.sheets['Q6']
worksheet.set_column('A:C', 18)

#print("\n7. -----------------------------------------------")

imp_cmd = df_imp.groupby('Commodity').sum().reset_index()
exp_cmd = df_exp.groupby('Commodity').sum().reset_index()

#print(imp_cmd.columns)
imp_cmd = imp_cmd[imp_cmd['Value-INR-2011-12'] > 0]
exp_cmd = exp_cmd[exp_cmd['Value-INR-2011-12'] > 0]

#print(imp_cmd[['Commodity']])
#print(exp_cmd[['Commodity']])
common_cmd = pd.merge(imp_cmd, exp_cmd, on='Commodity', how='inner')
#print("Commodities that we both export and import\n\n")
big_exporter7=common_cmd[['Commodity']]
#print(big_exporter7)
big_exporter7.to_excel(writer, sheet_name='Q7',index=False)
worksheet = writer.sheets['Q7']
worksheet.set_column('A:A',30)
print("All operations done!\nPlease check new created 173050046_solution.xlsx file.")

writer.save()


	
