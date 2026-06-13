from std.python import PythonObject
from std.python.bindings import PythonModuleBuilder
from std.os import abort


@export
def PyInit_score_ops() -> PythonObject:
    try:
        var module = PythonModuleBuilder("score_ops")
        module.def_function[batch_predict_count_mojo](
            "batch_predict_count_mojo",
            docstring="Optimized Mojo prediction calculation"
        )
        return module.finalize()
    except e:
        abort(String("Error creating Mojo module:", e))


def batch_predict_count_mojo(records: PythonObject) raises -> PythonObject:
    var pass_count: Int = 0
    var total = len(records)

    var w1: Float64 = 0.9
    var w2: Float64 = 0.035
    var w3: Float64 = 0.045
    var w4: Float64 = 0.04
    var w5: Float64 = 0.035
    var bias: Float64 = -8.0

    for i in range(total):
        var row = records[i]

        var study_hours = Float64(py=row[0])
        var attendance = Float64(py=row[1])
        var past_marks = Float64(py=row[2])
        var assignment_marks = Float64(py=row[3])
        var quiz_marks = Float64(py=row[4])

        var score = (
            study_hours * w1
            + attendance * w2
            + past_marks * w3
            + assignment_marks * w4
            + quiz_marks * w5
            + bias
        )

        if score >= 0:
            pass_count += 1

    return PythonObject(pass_count)