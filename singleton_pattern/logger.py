def write_log(filename, level, msg):
    with open(filename, "a") as log_file:
        log_file.write("[{0}] {1}\n".format(level, msg))


def critical(msg):
    write_log("CRITICAL", msg)


def error(msg):
    write_log("ERROR", msg)


def warn(msg):
    write_log("WARN", msg)


def info(msg):
    write_log("INFO", msg)


def debug(msg):
    write_log("DEBUG", msg)

