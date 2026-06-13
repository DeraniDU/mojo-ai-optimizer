from std.python import PythonObject
from std.python.bindings import PythonModuleBuilder
from std.os import abort


@export
def PyInit_heavy_ops() -> PythonObject:
    try:
        var module = PythonModuleBuilder("heavy_ops")
        module.def_function[heavy_compute_mojo](
            "heavy_compute_mojo",
            docstring="Heavy repeated AI-style calculation in Mojo"
        )
        return module.finalize()
    except e:
        abort(String("Error creating Mojo module:", e))


def heavy_compute_mojo(iterations_obj: PythonObject) raises -> PythonObject:
    var iterations = Int(py=iterations_obj)
    var total: Float64 = 0.0

    for i in range(iterations):
        var x = Float64(i % 1000) * 0.001

        var score = (
            x * 0.9
            + (x + 1.0) * 0.035
            + (x + 2.0) * 0.045
            + (x + 3.0) * 0.04
            + (x + 4.0) * 0.035
            - 1.0
        )

        if score >= 0.0:
            total += score
        else:
            total -= score

    return PythonObject(total)
