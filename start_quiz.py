get_ipython().run_cell_magic('javascript', '', "$('div.input').hide()")

from IPython.display import display, Markdown, YouTubeVideo
from IPython.html import widgets
from traitlets import (
    Unicode,
    link
)

# radio buttons

q1 = widgets.Text(
    description='1',
    value='Choose your topping.',
    disabled=True
)

a1 = widgets.RadioButtons(
    description='Answer',
    options=['pepperoni', 'pineapple', 'anchovies']
)

container1 = widgets.HBox(children=[q1, a1], height='50mm')
display(container1)


# select

q2 = widgets.Text(
    description='2',
    value='Your operating system?',
    disabled=True
)

a2 = widgets.Select(
    description='Answer',
    options=['Linux', 'Windows', 'OSX'],
)

container2 = widgets.HBox(children=[q2, a2], height='50mm')
display(container2)

# Toggle Buttons

q3 = widgets.Text(
    description='3',
    value='Select speed.',
    disabled=True
)

a3 = widgets.ToggleButtons(
    description='Answer',
    options=['Slow', 'Regular', 'Fast'],
)

container3 = widgets.HBox(children=[q3, a3], height='50mm')
display(container3)

# select multiple

q4 = widgets.Text(
    description='4',
    value='Answer',
    disabled=True
)

a4 = widgets.SelectMultiple(
    description="Fruits",
    options=['Apples', 'Oranges', 'Pears']
)

container4 = widgets.HBox(children=[q4, a4], height='50mm')
display(container4)

# submit results

submit_button = widgets.Button(description="Submit answers!")
display(widgets.HBox(children=[submit_button], height='10mm'))

# YouTube video
vid = YouTubeVideo('J---aiyznGQ')

def on_button_clicked(b):
    display(vid)

submit_button.on_click(on_button_clicked)

# show YouTube 