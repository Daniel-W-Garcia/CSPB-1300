import turtle
t = turtle.Turtle()
wn = turtle.Screen()
t.speed(0)

country_name = ['Philippines', 'Costa Rica', 'Ghana', 'Vietnam', 'Honduras', 'Kenya', 'Guatemala', 'Togo', 'Peru', 'Lebanon', 'Bolivia', 'Kenya', 'Philippines', 'Kyrgyzstan', 'Vietnam', 'Colombia', 'Peru', 'Guatemala', 'El Salvador', 'Tanzania', 'Cambodia', 'Cambodia', 'Ghana', 'Philippines', 'Philippines', 'Colombia', 'Sierra Leone', 'Nicaragua', 'Lebanon', 'Kenya', 'Tajikistan', 'Kenya', 'Bolivia', 'Kenya', 'Uganda', 'Benin', 'Ghana', 'Cambodia', 'Peru', 'Palestine', 'Vietnam', 'Ecuador', 'Kyrgyzstan', 'Philippines', 'Samoa', 'Philippines', 'Philippines', 'Philippines', 'Honduras', 'Philippines', 'Philippines', 'Philippines', 'Philippines', 'Nigeria', 'India', 'Philippines', 'Philippines', 'Guatemala', 'Zimbabwe', 'Jordan', 'Togo', 'Bolivia', 'Cambodia', 'Philippines', 'Colombia', 'Philippines', 'Kosovo', 'Philippines', 'India', 'Bolivia', 'Vietnam', 'Peru', 'Paraguay', 'Ghana', 'Sierra Leone', 'Ecuador', 'Kenya', 'Nicaragua', 'Nigeria', 'Kenya', 'Philippines', 'Cambodia', 'Mongolia', 'Kenya', 'Paraguay', 'Kenya', 'Vietnam', 'Sierra Leone', 'Kenya', 'Peru', 'Nigeria', 'Philippines', 'Palestine', 'Nicaragua', 'Togo', 'Ecuador', 'Philippines', 'El Salvador', 'Togo', 'Cambodia']
unique_countries = ['India', 'Costa Rica', 'Cambodia', 'Tanzania', 'Peru', 'Palestine', 'Nigeria', 'Bolivia', 'Ecuador', 'Benin', 'Ghana', 'El Salvador', 'Togo', 'Guatemala', 'Zimbabwe', 'Jordan', 'Sierra Leone', 'Kyrgyzstan', 'Uganda', 'Philippines', 'Vietnam', 'Mongolia', 'Samoa', 'Honduras', 'Kosovo', 'Nicaragua', 'Lebanon', 'Colombia', 'Paraguay', 'Kenya', 'Tajikistan']

wn.title("Turtle Graphs")


x = -500
y = -250
# create the x and y axis
t.pensize(2)
t.up()
t.setx(x)
t.sety(y)
t.down()
t.forward(1100)
t.up()
t.setx(x)
t.left(90)
t.down()
t.forward(520)
t.up()

# create the tick marks up y-axis

y_axis = ["20", "19", "18", "17", "16", "15", "14", "13", "12", "11", "10", "9", "8", "7", "6", "5", "4", "3", "2", "1"]


loans_per_country = []
for country in unique_countries:
    country_loans = country_name.count(country)
    country_loan_count = (country, country_loans)
    loans_per_country.append(country_loan_count)

most_to_least_loans = sorted(loans_per_country, key=lambda x: x[1], reverse=True)
print(most_to_least_loans)


# create the y-axis labels
t.left(90)
t.forward(20)
t.left(90)
t.forward(20)
for i in range(20):
    t.write(y_axis[i], align="center", font=("Arial", 10, "normal"))
    t.forward(25)

t.left(90)
t.setx(x)

i = 0
for pair in most_to_least_loans:
    bar_height = pair[1] * 26
    t.hideturtle()
    t.pensize(1)
    t.forward(25)
    t.left(90)
    t.down()
    t.begin_fill()
    t.fillcolor("red")
    t.forward(bar_height)
    t.write(pair[0], align="center", font=("Arial", 10, "bold"))
    t.right(90)
    t.forward(10)
    t.right(90)
    t.forward(bar_height)
    t.end_fill()
    t.left(90)
    t.up()
    t.sety(y)
    i += 1

wn.exitonclick()