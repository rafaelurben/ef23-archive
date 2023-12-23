import os
import os.path
import json


def clearTraces(tracespath=os.getenv('TRACES_PATH', os.getcwd())):
    if tracespath is None:
        raise EnvironmentError("TRACES_PATH not set")

    files = os.listdir(tracespath)
    tracefiles = [f for f in files if f.startswith("traces") and f.endswith(".json")]
    for t in tracefiles:
        os.remove(tracespath + "/" + t)


def saveTraces(cars, gen_or_name=0, tracespath=os.getenv('TRACES_PATH', os.getcwd())):
    if tracespath is None:
        raise EnvironmentError("TRACES_PATH not set")

    traces = []
    for car in cars:
        traces.append(car.traces)
    f = open(tracespath + "/traces"+str(gen_or_name)+".json", "w")
    json.dump(traces, f)
    f.close()
