"""
Laboratorio - Manipulación de Datos usando Pandas
-----------------------------------------------------------------------------------------

Este archivo contiene las preguntas que se van a realizar en el laboratorio.

Utilice los archivos `tbl0.tsv`, `tbl1.tsv` y `tbl2.tsv`, para resolver las preguntas.

"""
import pandas as pd

tbl0 = pd.read_csv("tbl0.tsv", sep="\t")
tbl1 = pd.read_csv("tbl1.tsv", sep="\t")
tbl2 = pd.read_csv("tbl2.tsv", sep="\t")


def pregunta_01():
    return len(tbl0)


def pregunta_02():
    return len(tbl0.columns)


def pregunta_03():
    return tbl0["_c1"].value_counts().sort_index()


def pregunta_04():
    return tbl0.groupby("_c1").mean()["_c2"]


def pregunta_05():
    return tbl0.groupby("_c1").max()["_c2"]


def pregunta_06():
    return sorted([x.upper() for x in set(tbl1["_c4"].values)])


def pregunta_07():
    return tbl0.groupby("_c1").sum()["_c2"]


def pregunta_08():
    tablaNueva = tbl0.copy()
    tablaNueva["suma"] = tbl0["_c0"] + tbl0["_c2"]
    return tablaNueva


def pregunta_09():
    tablaNueva = tbl0.copy()
    tablaNueva["year"] = [x.split("-")[0] for x in tbl0["_c3"]]
    return tablaNueva


def pregunta_10():
    tablaNueva = tbl0[["_c1","_c2"]].copy().set_index("_c2").groupby("_c1")
    proc = {g:":".join(sorted([str(x) for x in c])) for g,c in tablaNueva.groups.items()}
    return pd.DataFrame({"_c1":proc.keys(), "_c2":proc.values()}).set_index("_c1")


def pregunta_11():
    tablaNueva = tbl1.copy().set_index("_c4").groupby("_c0")
    proc = {g:",".join(sorted([str(x) for x in c])) for g,c in tablaNueva.groups.items()}
    pd.DataFrame({"_c0":proc.keys(), "_c4":proc.values()})
    return


def pregunta_12():
    tablaNueva = tbl2.copy()
    tablaNueva["_c5"] = tablaNueva["_c5a"] + ":" + [str(x) for x in tablaNueva["_c5b"]]
    tb = tablaNueva.drop(["_c5a","_c5b"], axis=1).set_index("_c5").groupby("_c0")
    proc = {g:",".join(sorted([str(x) for x in c])) for g,c in tb.groups.items()}
    return pd.DataFrame({"_c0":proc.keys(), "_c5":proc.values()})


def pregunta_13():
    tb0 = tbl0.copy()
    tb2 = tbl2.copy()
    return pd.merge(tb2, tb0).drop(["_c0","_c2"], axis=1).groupby("_c1").sum().squeeze()