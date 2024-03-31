from tabulate import tabulate
from flask import Flask, render_template, request, url_for

app = Flask(__name__)


def building(area):
    land = area
    labour = area
    cement = round(area * 0.45, 2)
    steel = round(area * 3.5, 2)
    sand = round(area * 1.8, 2)
    aggregate = round(area * 1.35, 2)
    bricks = int(area * 9)
    tiles = round(area * 0.75, 2)
    granites = round(area * 0.05, 2)
    pop = round(area * 5, 2)
    paint = round(area * 0.18, 2)
    plumbing = round(area, 2)
    electric = round(area, 2)
    door = round(area / 200, 2)
    window = round(area / 200, 2)

    land_cost = round(area * 35, 2)
    labour_cost = round(area * 275, 2)
    cement_cost = round(area * 0.4 * 400, 2)
    sand_cost = round(area * 1.8 * 55, 2)
    aggregate_cost = round(area * 1.35 * 68, 2)
    steel_cost = round(area * 3.5 * 75, 2)
    bricks_cost = round(area * 8.5 * 9, 2)
    tiles_cost = round(area * 0.75 * 42, 2)
    granites_cost = round(area * 0.05 * 90, 2)
    pop_cost = round(area * 5 * 10, 2)
    paint_cost = round(area * 0.18 * 500, 2)
    plumbing_cost = round(area * 135, 2)
    electric_cost = round(area * 90, 2)
    door_cost = round(area * 63, 2)
    window_cost = round(area * 23, 2)

    data = [
        ["Land Rate", land, "sq.ft", land_cost],
        ["Labour Cost", labour, "sq.ft", labour_cost],
        ["Cement", cement, "bag", cement_cost],
        ["Sand", sand, "sq.ft", sand_cost],
        ["Aggregate", aggregate, "sq.ft", aggregate_cost],
        ["Steel", steel, "kg", steel_cost],
        ["Bricks", bricks, "unit", bricks_cost],
        ["Tiles", tiles, "sqft", tiles_cost],
        ["Granites (for kitchen)", granites, "sqft", granites_cost],
        ["Plaster of Paris", pop, "sq.ft", pop_cost],
        ["Paint", paint, "ltr", paint_cost],
        ["Plumbing Cost", plumbing, "sq.ft", plumbing_cost],
        ["Electric Work", electric, "sq.ft", electric_cost],
        ["Door", door, "unit", door_cost],
        ["Window", window, "unit", window_cost],
    ]
    return data
    # print("Here is the value of the area given by you ")
    # print(tabulate(data, headers="firstrow", tablefmt="grid"))
    # print(" by Yash kartikey Dubey ")


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
