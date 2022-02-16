from pymol import cmd


def coloraf(selection="all"):

    """
    AUTHOR
    Christian Balbin

    DESCRIPTION
    Colors Alphafold structures by pLDDT

    USAGE
    coloraf sele

    PARAMETERS

    sele (string)
    The name of the selection/object to color by pLDDT. Default: all
    """

    cmd.color("blue", f"({selection}) and b > 90")
    cmd.color("cyan", f"({selection}) and b < 90 and b > 70")
    cmd.color("yellow", f"({selection}) and b < 70 and b > 50")
    cmd.color("orange", f"({selection}) and b < 50")


cmd.extend("coloraf", coloraf)
cmd.auto_arg[0]["coloraf"] = [cmd.object_sc, "object", ""]
