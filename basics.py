from taipy import Gui

# You can write HTML or Markdown to make websites

page = """
<h1> HEyyyyyyy This is MEeeeeeeeee.. </h1>

## H2 Using markdown
"""



if __name__ == "__main__":
    app = Gui(page)
    app.run()