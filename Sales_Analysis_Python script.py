# -*- coding: utf-8 -*-
"""
Created on Mon Apr  6 16:12:02 2026

@author: RAMYA KEERTHI
"""

import os
print("Current Working Directory:")
print(os.getcwd())
## Change working directory to correct folder
os.chdir(r"D:\Data Analysr Training\My projects\Sales_Analytics_Project_Python\data")

## Confirm change
print("\n New Working Directory:")
print(os.getcwd())

## Check files again
print("\nFiles after changing directory:")
print(os.listdir())


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import seaborn as sns

df = pd.read_csv("../data/sales_data.csv")


print("\n## First 5 rows")
print(df.head())

print("\n## Shape")
print(df.shape)

print("\n## Columns")
print(df.columns)

print("\n## Missing Values")
print(df.isnull().sum())


##  DATA CLEANING

## Convert 'date' column to proper datetime format
df["date"] = pd.to_datetime(df["date"])

## Fill missing price values with average price
df["price"] = df["price"].fillna(df["price"].mean())

## Fill missing region values with 'Unknown'
df["region"] = df["region"].fillna("Unknown")

## Verify cleaning
print("\n## Missing Values After Cleaning:")
print(df.isnull().sum())

## FEATURE ENGINEERING

## Create new column 'revenue'
## Revenue = quantity * price
df["revenue"] = df["quantity"] * df["price"]

print("\n## Revenue column created successfully")

## BASIC STATISTICS

## Get statistical summary of dataset
print("\n## Summary Statistics:")
print(df.describe())

##BUSINESS ANALYSIS

# Total Revenue
total_revenue = df["revenue"].sum()
print("\n## Total Revenue:")
print(total_revenue)

## Top Products by Revenue
top_products = df.groupby("product")["revenue"].sum().sort_values(ascending=False)

print("\n## Top Products:")
print(top_products.head(10))


## Region-wise Revenue
region_sales = df.groupby("region")["revenue"].sum().sort_values(ascending=False)

print("\n## Region-wise Sales:")
print(region_sales)

## Category-wise Revenue

category_sales = df.groupby("category")["revenue"].sum().sort_values(ascending=False)

print("\n## Category-wise Sales:")
print(category_sales)

## Monthly Revenue Trend

## Extract month from date
df["month"] = df["date"].dt.to_period("M")

monthly_sales = df.groupby("month")["revenue"].sum()

print("\n## Monthly Sales Trend:")
print(monthly_sales)


## Top Customers
top_customers = df.groupby("customer_id")["revenue"].sum().sort_values(ascending=False)

print("\n## Top Customers:")
print(top_customers.head(10))



print("\n===== KEY METRICS =====")
print("Total Revenue:", round(total_revenue, 2))
print("Top Product:", top_products.idxmax())
print("Top Region:", region_sales.idxmax())
print("Top Category:", category_sales.idxmax())


## VISUALIZATION

## IMPORTANT: Always create figure before plotting

## 1. BAR CHART → Top Products

plt.figure(figsize=(12,6))
## plt.figure() → create a new chart canvas
## figsize=(12,6) → width = 12, height = 6
## Because if you do not create a figure first, the chart may appear too small or messy.


## Plot the bar chart
top_products.head(10).plot(kind="bar", color="skyblue", edgecolor="black")

## Add title

plt.title("Top 10 Products by Revenue", fontsize=14, fontweight="bold")
##This gives the chart a heading.

##fontsize=14 → bigger title
##fontweight="bold" → bold text


### Add axis labels
plt.xlabel("Product", fontsize=12)
plt.ylabel("Revenue", fontsize=12)


# xlabel → label for horizontal axis
#ylabel → label for vertical axis -Without labels, a chart is incomplete.

#Rotate product names
plt.xticks(rotation=45)

# This rotates the product names on x-axis by 45 degrees.
#Why?
##Because product names may overlap if they are straight. Rotation makes them easier to read.
plt.gca().yaxis.set_major_formatter(mticker.StrMethodFormatter('{x:,.0f}'))
## This changes y-axis numbers from scientific notation like:
    ##1e7 to normal readable values like 10,000,000

#Breaking it simply
#plt.gca() → get current axis
#.yaxis → select y-axis
#.set_major_formatter(...) → change how numbers look

plt.tight_layout()
## This adjusts spacing automatically so:

#labels do not get cut
#title does not overlap
#chart looks neat

#Save the chart
plt.savefig("chart1_top_products.png")
## This saves your chart in your project folder as an image file.
#@# Why is this useful? Because later you can:
    
## add it to GitHub
#use it in LinkedIn posts
#keep it in project folder
#show it in interviews

plt.show()

## CHART 2: Monthly Revenue Trend
## ===============================

## Convert month to string (important)
monthly_sales.index = monthly_sales.index.astype(str)

monthly_sales = monthly_sales.sort_index() ## Ensures correct timeline

## Create figure
plt.figure(figsize=(12,6))

## Plot line chart
monthly_sales.plot(
    kind="line",
    marker="o",
    color="green"
)

## Titles and labels
plt.title("Monthly Revenue Trend", fontsize=14, fontweight="bold")
plt.xlabel("Month", fontsize=12)
plt.ylabel("Revenue", fontsize=12)

## Rotate labels
plt.xticks(rotation=45)

## Format numbers
plt.gca().yaxis.set_major_formatter(mticker.StrMethodFormatter('{x:,.0f}'))

## Grid for readability
plt.grid(True)

## Adjust layout
plt.tight_layout()

## Save chart
plt.savefig("chart2_monthly_trend.png")

## Show
plt.show()



## CHART 3: Region-wise Revenue
## ===============================

plt.figure(figsize=(12,6))

region_sales.plot(
    kind="bar",
    color="orange",
    edgecolor="black"
)

plt.title("Revenue by Region", fontsize=14, fontweight="bold")
plt.xlabel("Region", fontsize=12)
plt.ylabel("Revenue", fontsize=12)

plt.xticks(rotation=45)

plt.gca().yaxis.set_major_formatter(mticker.StrMethodFormatter('{x:,.0f}'))

plt.grid(axis="y")

plt.tight_layout()

plt.savefig("chart3_region_sales.png")

plt.show()


## CHART 4: Category-wise Distribution
## ===============================

plt.figure(figsize=(8,8))

category_sales.plot(
    kind="pie",
    autopct="%1.1f%%",
    startangle=90,
    colors=["#66b3ff", "#ff9999"]
)

plt.title("Revenue Contribution by Category", fontsize=14, fontweight="bold")

plt.ylabel("")

plt.tight_layout()

plt.savefig("chart4_category_distribution.png")

plt.show()

print("\n Analysis Completed Successfully!")
