import gurobipy as gp

import subprocess
import os

def export_model_to_porta(model: gp.Model, filename):
    variables = model.getVars()
    constraints = model.getConstrs()
    n_vars = len(variables)

    var_names = [f"x{i+1}: {var.VarName}" for i, var in enumerate(variables)]
    index_map = {var.VarName: i for i, var in enumerate(variables)}

    def format_expr(coeffs):
        terms = []
        for i, coef in enumerate(coeffs):
            if coef == 0:
                continue
            # Solo el xN (sin el =original) en las expresiones
            name = f"x{i+1}"
            if coef == 1:
                terms.append(f"{name}")
            elif coef == -1:
                terms.append(f"-{name}")
            else:
                terms.append(f"{coef} {name}")
        return " + ".join(terms).replace("+ -", "- ")

    lines = []

    # DIM, bounds
    lines.append(f"DIM = {n_vars}\n")
    lines.append("LOWER_BOUNDS")
    lines.append(" ".join(["0"] * n_vars))
    lines.append("UPPER_BOUNDS")
    lines.append(" ".join(["1"] * n_vars))
    lines.append("")  # blank line
    lines.append("")  # blank line

    eq_lines = []
    ineq_lines = []
    count = 1
    count_equalities = 1
    lines.append("INEQUALITIES_SECTION")
    for constr in constraints:
        expr = model.getRow(constr)
        coeffs = [0] * n_vars
        for j in range(expr.size()):
            var = expr.getVar(j)
            coef = expr.getCoeff(j)
            coeffs[index_map[var.VarName]] = coef

        rhs = int(constr.RHS)
        expr_str = format_expr(coeffs)

        if constr.Sense == '=':
            eq_lines.append(f"({count_equalities}) {expr_str} = {rhs}")
            count_equalities += 1
        elif constr.Sense == '<':
            ineq_lines.append(f"({count}) {expr_str} <= {rhs}")
        elif constr.Sense == '>':
            ineq_lines.append(f"({count}) {expr_str} >= {rhs}")
        else:
            ineq_lines.append(f"({count}) {expr_str} ? {rhs}")  # fallback

        count += 1

    # Equalities first
    lines.extend(eq_lines)
    # Inequalities after
    lines.extend(ineq_lines)
    lines.append("")
    lines.append("END")
    lines.append("")

    # Mapping variable names to indices
    lines.append(" ".join(var_names))

    with open(filename, "w") as f:
        for line in lines:
            f.write(line + "\n")

    print(f"Model exported to {filename}.")

def process_ieq_file(ieq_file_path, porta_bin_path="./porta-1.4.1/gnu-make/bin"):
    """
    Process a .ieq file to validate points and get facets using PORTA commands.

    :param ieq_file_path: Path to the .ieq file.
    :return: None
    """
    # Ensure the file exists
    if not os.path.isfile(ieq_file_path):
        raise FileNotFoundError(f"The file {ieq_file_path} does not exist.")

    # Define the commands
    valid_command = [porta_bin_path + "/valid", "-V", ieq_file_path]
    xporta_command = [porta_bin_path + "/xporta", "-T", ieq_file_path.replace(".ieq", ".poi")]

    try:
        # Run the valid command
        print(f"Running: {' '.join(valid_command)}")
        subprocess.run(valid_command, check=True)

        # Run the xporta command
        print(f"Running: {' '.join(xporta_command)}")
        subprocess.run(xporta_command, check=True)

        # Copy the last line of the .ieq file into the .poi.ieq file
        with open(ieq_file_path, "r") as ieq_file:
            last_line = ieq_file.readlines()[-1].strip()

        poi_ieq_file_path = ieq_file_path.replace(".ieq", ".poi.ieq")
        with open(poi_ieq_file_path, "a") as poi_ieq_file:
            poi_ieq_file.write(last_line + "\n")

    except subprocess.CalledProcessError as e:
        print(f"An error occurred while running the command: {e}")


