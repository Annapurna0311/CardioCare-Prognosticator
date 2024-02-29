from taipy import Gui
# from taipy import Core
# Previous configuration of scenario

title = "Heart failure Prediction"
path ="background.jpg"
page = """
<|text-center|>
#Heart.i.o
<|{path}|image|>
Name: <|{input_name}|input|>
<|text-center|
Age: <input_age}|input|>
<text-center|
Cholestrol: <|{input_name}|input|>
<|text-center|
Blood Pressure: <|{input_name}|input|>
<|text-center|
Thalasseima: <|{input_name}|input|>
<|text-center|
Coronary Artery: <|{input_name}|input|>
<|text-center|
<|submit|button|on_action=submit_scenario|>

"""
input_name = ""
message = None
def submit_scenario(state):
    scenario.input_name.write(state.input_name)
    scenario.submit()
    state.message = scenario.message.read()

if __name__ == "__main__":
    app = Gui(page)
    app.run(use_reloader=True)
