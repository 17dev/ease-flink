# mylibrary/udf_utils.py

```python
from pyflink.table.udf import ScalarFunction, TableFunction, AggregateFunction

def udf_scalar(func):
    """
    Decorator for creating a scalar UDF.
    """
    class ScalarUDF(ScalarFunction):
        def eval(self, *args):
            return func(*args)
    return ScalarUDF()

def udf_table(func):
    """
    Decorator for creating a table UDF.
    """
    class TableUDF(TableFunction):
        def eval(self, *args):
            yield from func(*args)
    return TableUDF()

def udf_aggregate(func):
    """
    Decorator for creating an aggregate UDF.
    """
    class AggregateUDF(AggregateFunction):
        def create_accumulator(self):
            return func.create_accumulator()

        def accumulate(self, accumulator, *args):
            return func.accumulate(accumulator, *args)

        def retract(self, accumulator, *args):
            return func.retract(accumulator, *args)

        def merge(self, accumulator, accumulators):
            return func.merge(accumulator, accumulators)

        def get_value(self, accumulator):
            return func.get_value(accumulator)

        def create_accumulator(self):
            return func.create_accumulator()

        def accumulate(self, accumulator, *args):
            return func.accumulate(accumulator, *args)

        def retract(self, accumulator, *args):
            return func.retract(accumulator, *args)

        def merge(self, accumulator, accumulators):
            return func.merge(accumulator, accumulators)

        def get_value(self, accumulator):
            return func.get_value(accumulator)

        def get_result_type(self):
            return func.get_result_type()

    return AggregateUDF()
```