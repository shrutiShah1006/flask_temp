from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():
    print("Visiting homepage!")
    return """
        <h1>Hello World!</h1>
        <h2>hgrkuhzge</h2>
        <a href="/Autobiographies"><button style="background-color: black; color: white; border-radius: 10px; padding: 10px;">Biographies</button></a>
        <a href="/Fiction"><button style="background-color: black; color: white; border-radius: 10px; padding: 10px;">Fiction</button></a>
        <a href="/History"><button style="background-color: black; color: white; border-radius: 10px; padding: 10px;">History</button></a>
    """


@app.route("/Autobiographies")
def Autobiographies():
    return """
        <h2>Somethings Autobiographies</h2>
        <img src="https://tse1.mm.bing.net/th?id=OIP.AdXYFlSm_J87fbDFvYYRtAHaLH&pid=Api&P=0&h=220" alt="Autobiographies 1"/>
        <h4>hgrkuhzge</h4>
        <img src="https://tse2.mm.bing.net/th?id=OIP.EMPi3vqplq1FfcgnKcIJHAHaLM&pid=Api&P=0&h=220" alt="Autobiographies 3"/>
        
"""


@app.route("/Fiction")
def Fiction():
    return """
        <h2>Fictions</h2>
        <img src="https://tse3.mm.bing.net/th?id=OIP.SMNHDGdZekxM-2Da8TTk_gHaKm&pid=Api&P=0&h=220"/>
        <img src="https://tse2.mm.bing.net/th?id=OIP.XosIXUQSb7WwdqxQJ7HoBAHaLX&pid=Api&P=0&h=220" alt="Fiction 2"/>
        <img src="https://tse1.mm.bing.net/th?id=OIP.3nMK2bWfEZRsBzfrfmKfEgHaF7&pid=Api&P=0&h=220" alt="Autobiographies 3"/>
        
"""


@app.route("/History")
def History():
    return """
        <h2>History!</h2>
        <img src="https://tse1.mm.bing.net/th?id=OIP.TFdmnnmV1tq6Xm_DUH4UwgHaI6&pid=Api&P=0&h=220" alt="History 1"/>
        <img src="https://www.austinmacauley.com/sites/default/files/styles/adaptive_general/public/9781528930109.jpg" alt="History 2"/>
        <img src="https://i.thenile.io/r1000/9780313320958.jpg?r=5c6ab19b775aa" alt="History 3"/>
        
"""


if __name__ == "__main__":
    app.run(debug=True, use_reloader=True)
