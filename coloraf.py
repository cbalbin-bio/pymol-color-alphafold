from pymol import cmd


def coloraf(protein):

    """
    AUTHOR
    Christian Balbin

    DESCRIPTION
    Colors Alphafold structures by pLDDT

    USAGE
    coloraf protein

    PARAMETERS

    protein (string)
    The name of the selection/object to color by pLDDT
    """

    cmd.color("blue", f"m. {protein} and b > 90")
    cmd.color("cyan", f"m. {protein} and b < 90 and b > 70")
    cmd.color("yellow", f"m. {protein} and b < 70 and b > 50")
    cmd.color("orange", f"m. {protein} and b < 50")


cmd.extend("coloraf", coloraf)
cmd.auto_arg[0]["coloraf"] = [cmd.object_sc, "object", ""]
