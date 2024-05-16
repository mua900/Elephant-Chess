import traceback


class PrintProblem(Exception):
    def __init__(self, problem_type, message):
        caller = traceback.extract_stack()[-2]
        filename = caller.filename
        line = caller.lineno
        full_message = f"{problem_type}: {message} (File: {filename}, Line: {line})"
        super().__init__(full_message)
