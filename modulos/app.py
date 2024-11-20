import reports

#generar reportes de ventas y gastos usando funciones del módulo reports.py

sales_report = reports.generate_sales_report('October', 3000)
expenses_report = reports.generate_expenses_report('October', 40000)

print(sales_report)
print(expenses_report)