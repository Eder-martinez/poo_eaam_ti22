from openpyxl import Workbook # importar un libro
wb = Workbook () # crear variable con el valor del libro
sheet = wb.active # activar las hojas de trabajo
sheet ["A1"] = 5
sheet ["A2"] = 10
wb.save ("prueba_escritura.xlsx")

