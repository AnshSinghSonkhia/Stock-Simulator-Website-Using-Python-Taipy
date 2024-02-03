from taipy import Gui
import pandas as pd

Stock = "Stock Simulator by Ansh Singh Sonkhia"
StockSim = "YOur Simulation"
logo = "/img/logo.jpg"

letUsInput = "Tata Motors"
minp = 599

def button_pressed(state):
    print("Stock Purchase Successful")

# Data to make charts
data = {
    "Date": pd.date_range("2024-02-01", periods=4, freq="D"),
    "TataMotors": [-15,-12.9,7.2,10.2],
    "AsianPaints": [-22,-19.7,2.7,6.5],
    "Tesla": [-8.6,-8.2,12.,13.5]
}

# You can write HTML or Markdown to make websites
page = """
<h1> HEyyyyyyy This is MEeeeeeeeee.. </h1>

## H2 Using markdown

<|text-center |
<|{logo}|image|>

<|{Stock}|hover_text=This is hover text|>

Name of Stock:    <|{letUsInput}|input|>

Min Price:    <|{minp}|input|>

<|Purchase|button|on_action=button_pressed|>

<|{StockSim}|hover_text=Your Simulation|>

<|{data}|chart|mode=lines|x=Date|y[1]=TataMotors|y[2]=AsianPaints|y[3]=Tesla|line[1]=dash|color[2]=blue|color[3]=red|>

"""



if __name__ == "__main__":
    app = Gui(page)
    app.run(use_reloader=True)