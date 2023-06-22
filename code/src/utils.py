import logging


def error(msg):
    logging.error(msg)
    raise RuntimeError(msg)


def pipeline_to_name(pipeline):
    return "-".join([p[0] for p in pipeline.steps])
