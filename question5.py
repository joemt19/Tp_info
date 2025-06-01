# MBANGA TSHIBANDA ---PREPOLYTECHNIQUE UNIKIN---
# TRAVAIL PRATIQUE D'INFORMATIQUE N°1
# QUESTION 5

import pandas as pd
import matplotlib.pyplot as plt
from fpdf import FPDF

# Lire les données CSV
df = pd.read_csv("Category_Sales_for_1997.csv")

# Générer un histogramme groupé (bar chart)
plt.figure(figsize=(10,6))
plt.bar(df['CategoryName'], df['CategorySales'], color='skyblue')
plt.title("Ventes par catégorie - 1997")
plt.xlabel("Catégorie")
plt.ylabel("Ventes ($)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("graphique.png")
plt.close()

# Générer un rapport PDF
class PDF(FPDF):
    def header(self):
        self.set_font("Arial", 'B', 14)
        self.cell(0, 10, "Rapport de Ventes - Northwind 1997", ln=True, align='C')

    def footer(self):
        self.set_y(-15)
        self.set_font("Arial", 'I', 8)
        self.cell(0, 10, f"Page {self.page_no()}", align='C')

pdf = PDF()
pdf.add_page()

# Ajout du graphique
pdf.set_font("Arial", '', 12)
pdf.cell(0, 10, "Histogramme des ventes par catégorie :", ln=True)
pdf.image("graphique.png", x=10, y=40, w=190)
pdf.ln(110)

# Ajout du tableau
pdf.set_font("Arial", 'B', 12)
pdf.cell(95, 10, "Catégorie", border=1)
pdf.cell(95, 10, "Ventes ($)", border=1)
pdf.ln()

pdf.set_font("Arial", '', 12)
for index, row in df.iterrows():
    pdf.cell(95, 10, row['CategoryName'], border=1)
    pdf.cell(95, 10, str(row['CategorySales']), border=1)
    pdf.ln()

# Sauvegarder le rapport
pdf.output("rapport_ventes.pdf")

print("✅ Rapport PDF généré avec succès !")

