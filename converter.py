import pandas

# df = pandas.read_json("./data.json")
# df.to_excel("data.xlsx",index=False)

df = pandas.read_json("./colors.json")
df.to_excel("colors.xlsx",index=False)

