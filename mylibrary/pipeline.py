import pyflink_utils

class Pipeline:
    def __init__(self, name):
        self.name = name
        self.source = None
        self.transforms = []
        self.sink = None

    def source(self, source_func):
        self.source = source_func

    def transform(self, transform_func):
        self.transforms.append(transform_func)

    def sink(self, sink_func):
        self.sink = sink_func

    def execute(self):
        env = pyflink_utils.get_execution_environment()
        table_env = pyflink_utils.get_table_environment(env)

        source_table = self.source(env, table_env)

        for transform_func in self.transforms:
            source_table = transform_func(source_table)

        self.sink(source_table)

        env.execute(self.name)