from flask import Blueprint, render_template

equipment_bp = Blueprint("equipment", __name__)

@equipment_bp.route("/equipment.html")
def equipment():
    return render_template("equipment.html")
