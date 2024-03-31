from tabulate import tabulate
from flask import Flask, render_template, request, url_for

app = Flask(__name__)


def building():
    area = float(input("Enter the Area of building (in sqft): "))
    land = area
    labour = area
    cement = area * 0.45
    steel = round(area * 3.5, 2)
    sand = round(area * 1.8, 2)
    aggregate = round(area * 1.35, 2)
    bricks = int(area * 8.5)
    tiles = round(area *0.75, 2)
    granites = round(area * 0.05, 2)
    pop = round(area * 5, 2)
    paint = round(area * 2.5, 2)
    plumbing = round (area)
    electric = round (area)
    door = round (area/200)
    window = round (area/200)

    land_cost = round(land * 35, 2)
    labour_cost = round(labour * 275, 2)
    cement_cost = round(cement * 400, 2)
    sand_cost = round(sand * 55, 2)
    aggregate_cost = round(aggregate * 50, 2)
    steel_cost = round(steel * 75, 2)
    bricks_cost = round(bricks * 9, 2)
    tiles_cost = round(tiles * 42, 2)
    granites_cost = round(granites* 90, 2)
    pop_cost = round(pop * 10, 2)
    paint_cost = round(paint * 30, 2)
    plumbing_cost = round(plumbing * 135, 2)
    electric_cost = round(electric * 90, 2)
    door_cost = round (area * 63, 2)
    window_cost = round (area * 23, 2)

    total = land_cost + labour_cost + cement_cost + sand_cost + aggregate_cost + steel_cost + bricks_cost + tiles_cost + granites_cost + pop_cost + paint_cost + plumbing_cost + electric_cost + door_cost + window_cost
    cost = total/area
    data = [
        ["Name", "Quantity", "unit", "Cost", "Rate"],
        ["Land Rate", land, "sq.ft", f"₹{land_cost}", "35/sq.ft"],
        ["Labour Cost", labour, "sq.ft", f"₹{labour_cost}", "275/sq.ft"],
        ["Cement", cement, "bag", f"₹{cement_cost}","400/bag"],
        ["Sand", sand, "sq.ft", f"₹{sand_cost}","55/cu ft."],
        ["Aggregate", aggregate, "sq.ft", f"₹{aggregate_cost}","50/cu ft."],
        ["Steel", steel, "kg", f"₹{steel_cost}","75/Kg"],
        ["Bricks", bricks, "unit", f"₹{bricks_cost}","9/unit"],
        ["Tiles", tiles, "sqft", f"₹{tiles_cost}","42/sq.ft"],
        ["Granites (for kitchen)", granites, "sqft", f"₹{granites_cost}","90/sq.ft"],
        ["Plaster of Paris", pop, "sq.ft", f"₹{pop_cost}","10/sq.ft"],
        ["Paint", paint, "ltr", f"₹{paint_cost}","30/sq.ft"],
        ["Plumbing Cost", plumbing, "sq.ft", f"₹{plumbing_cost}","135/sq.ft"],
        ["Electric Work", electric, "sq.ft", f"₹{electric_cost}","90/sq.ft"],
        ["Door", door, "unit", f"₹{door_cost}","63/sq.ft"],
        ["Window", window, "unit", f"₹{window_cost}","23/sq.ft"],
        ["Total", "-", "-", f"₹{total}",f"₹{cost}/sq.ft"]
    ]
    print("Here the Estimation for", f"{area}","sq ft.")
    print(tabulate(data, headers="firstrow", tablefmt="grid"))
    print(" by Yash kartikey Dubey ")


building()


@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        a = int(request.form.get('area'))
        data = building(a)
        total = 0
        for ele in data:
            total += int(ele[3])
        return render_template('index.html', data=data, header=["Name", "Quantity", "unit", "Cost"],
                               total=["Total", "", "", f"₹{total}"])

    return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True)
